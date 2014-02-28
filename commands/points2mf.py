import random
import re


class FIP:

    def __init__(self):
        self.content = ''

    def write(self, string):
        if not string:
            return
        self.content += string

    def getcontents(self):
        return self.content


def iterate(objlist):
    # collect all pairs so that master appeared in pair once with one master
    # so that in list should not exist pairs [A,B] and [B,A]
    for i in range(len(objlist) - 1):
        for j in range(i + 1, len(objlist)):
            yield objlist[i], objlist[j]


def getcoords_zeile(point, glyphletter):
    znamel = re.match('z(\d+)l', point['preset']['pointname'])
    znamer = re.match('z(\d+)r', point['preset']['pointname'])
    zeile = None
    if znamel and point['preset']['pointname'] == znamel.group(0):
        zeile = "{A}px{index}l := {xvalue}u ; {A}py{index}l := {yvalue}u ;"
        zeile = zeile.format(index=znamel.group(1), A=glyphletter,
                             xvalue='%.2f' % (point['coords']['x'] / 100.),
                             yvalue='%.2f' % (point['coords']['y'] / 100.))

    if znamer and point['preset']['pointname'] == znamer.group(0):
        zeile = "{A}px{index}r := {xvalue}u ; {A}py{index}r := {yvalue}u ;"
        zeile = zeile.format(index=znamer.group(1), A=glyphletter,
                             xvalue='%.2f' % (point['coords']['x'] / 100.),
                             yvalue='%.2f' % (point['coords']['y'] / 100.))
    return zeile


class DifferentZPointError(Exception):
    pass


cachekoef = {}


def getcoefficient(left, right):
    axis = ''.join([left['alias'], right['alias']])
    if axis in cachekoef:
        return cachekoef[axis]
    cachekoef[axis] = random.choice([0, 1])
    return cachekoef[axis]


metapolationcache = {}


def getmetapolation(left, right):
    axis = ''.join([left['alias'], right['alias']])
    if axis in metapolationcache:
        return metapolationcache[axis]
    metapolationcache[axis] = random.random()
    return metapolationcache[axis]


def points2mf(glyphname, *masters):
    """ Save current points to mf file

        master is an instance of models.Master
        glyph is an instance of models.Glyph
    """
    import time

    starttime = time.time()

    if len(masters) < 1:
        return ''

    primarymaster = masters[0]

    fip = FIP()

    fip.write("% File parsed with Metapolator %\n")
    fip.write("% box dimension definition %\n")

    fip.write("\n")

    formulas = "{k} * ({A} + {M} * ({B} - {A}))"
    ar = []  # array for definition of formulas

    divider = 0

    for left, right in iterate(masters):
        leftglyph = left['glyphs'][glyphname]
        rightglyph = right['glyphs'][glyphname]

        koef = getcoefficient(left, right)
        divider += koef
        metapolation = getmetapolation(left, right)

        p = formulas.format(A='%.2f' % (leftglyph['advanceWidth'] / 100.),
                            B='%.2f' % (rightglyph['advanceWidth'] / 100.),
                            k=koef,
                            M=metapolation)
        ar.append(p)

    if not divider:
        divider = 1

    glyph = primarymaster['glyphs'][glyphname]

    str_ = 'beginfontchar({glyph}, ({p}) / {divider}, 0, 0)'
    fip.write(str_.format(glyph=int(glyph['name']) + 1,
                          p='+'.join(ar), divider=divider))
    fip.write('\n')
    fip.write("""% z points""")

    mean = ['13','14','26','29','65','67','69','77','78','79','82','83','85','86','87','88','90','94','95','12','27','63','71','80','81','89','2','7','11','28','30','62','64','66','68','70','72','73','75','76','84','4','8','9','15','59','60','61','74','91','92','93']
#des = ['12','27','63','71','80','81','89']
#asc = ['2','7','11','28','30','62','64','66','68','70','72','73','75','76','84']
    cap = ['1','3','5','6','10','16','17','18','19','20','21','22','23','24','25','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58']
#box = ['4','8','9','15','59','60','61','74','91','92','93']

    ggroup=""
    gggroup =""

    if glyph['name'] in mean:
        ggroup = 'xheight'
        gggroup = 'mean'

    if glyph['name'] in cap:
        ggroup = 'capital'
        gggroup = 'cap'

    inattr=0
    ivn = 0
    strz = ""
    zzn = []
    startp = []
    startpval = []

    pointshifted= []
    pointshiftedval= []

    pointshiftedy = []
    pointshiftedyval = []

    overx = []
    overxval = []

    overbase = []
    overbaseval = []

    overcap = []
    overcapval = []

    inktrap_l = []
    inktrap_lval = []

    inktrap_r = []
    inktrap_rval = []

    stemshift = []
    stemshiftval = []

    ascpoint = []
    ascpointval = []

    descpoint = []
    descpointval = []

    i = 1

# search for parameters

    for item in masters[0]['glyphs'][glyphname]['points']:
        znamer = re.match('z(\d+)r', item['preset'].get('pointname'))
        znamel = re.match('z(\d+)l', item['preset'].get('pointname'))
        zname = re.match('z(\d+)l', item['preset'].get('pointname'))

        x = item['coords']['x']
        y = item['coords']['y']

        im = item['preset'].get('pointname')

        ipointshifted = item['preset'].get('pointshifted')
 #       ipointshiftedy = item['preset'].get('pointshiftedy')
        istartp = item['preset'].get('startp')
        ioverx = item['preset'].get('overx')
        ioverbase = item['preset'].get('overbase')
        iovercap = item['preset'].get('overcap')
        # iinktrap_l = item['preset'].get('inktrap_l')
        # iinktrap_r = item['preset'].get('inktrap_r')
        # istemshift = item['preset'].get('stemshift')
        # iascpoint = item['preset'].get('ascpoint')
        # idescpoint = item['preset'].get('descpoint')

        if znamel and im == znamel.group(0):
            zzn.append(i)

        # do not delete that lines while you are sure
#       if im == znamel or im == znamer:

            if istartp is not None:
                istartpval = item['preset'].get('startp')
                startp.append("startp")
                startpval.append(istartpval)

            if ipointshifted is not None:
                ipointshiftedval = item['preset'].get('pointshifted')
                pointshifted.append("shifted")
                pointshiftedval.append(ipointshiftedval)
            else:
                pointshifted.append("")
                pointshiftedval.append(0)

#       if ipointshiftedy is not None:
#           ipointshiftedyval = item['preset'].get('pointshiftedy')
#           pointshiftedy.append("shifted")
#           pointshiftedyval.append(ipointshiftedyval)

            if ioverx is not None:
                ioverxval = item['preset'].get('overx')
                overx.append("shifted")
                overxval.append(ioverxval)

            if ioverx is not None:
                ioverxval = item['preset'].get('overx')
                overx.append("shifted")
                overxval.append(ioverxval)

            if ioverbase is not None:
                ioverbaseval = item['preset'].get('overbase')
                overbase.append("shifted")
                overbaseval.append(ioverbaseval)

            if iovercap is not None:
                iovercapval = item['preset'].get('overcap')
                overcap.append("shifted")
                overcapval.append(iovercapval)

            # if iinktrap_l is not None:
            #     iinktrap_lval = item['preset'].get('inktrap_l')
            #     inktrap_l.append("inktrapcut")
            #     inktrap_lval.append(iinktrap_lval)
            # else:
            #     inktrap_l.append("")
            #     inktrap_lval.append(0)

            # if iinktrap_r is not None:
            #     iinktrap_rval = item['preset'].get('inktrap_r')
            #     inktrap_r.append("inktrapcut")
            #     inktrap_rval.append(iinktrap_rval)
            # else:
            #     inktrap_r.append("")
            #     inktrap_rval.append(0)

            # if istemshift is not None:
            #     istemshiftval = item['preset'].get('stemshift')
            #     stemshift.append("stemshift")
            #     stemshiftval.append(istemshiftval)
            # else:
            #     stemshift.append("")
            #     stemshiftval.append(0)

            # if iascpoint is not None:
            #     iascpointval = item['preset'].get('ascpoint')
            #     ascpoint.append("ascpoint")
            #     ascpointval.append(iascpointval)
            # else:
            #     ascpoint.append("")
            #     ascpointval.append(0)

            # if idescpoint is not None:
            #     idescpointval = item['preset'].get('descpoint')
            #     descpoint.append("descpoint")
            #     descpointval.append(idescpointval)
            # else:
            #     descpoint.append('')
            #     descpointval.append(0)

            i += 1

#   nnz = 0
#   for zitem in zzn :
#     nnz = nnz +1

    zzn.sort()
    semi = ";"
    close = ")"

    mffunc = '{k} * ({A} + {m} * ({B} - {A}))'

    for i in range(len(zzn)):
        zitem = i + 1

        #   zitemb = zzn[i]
        #   zitemc = zzn[i-1]
        zeile = ''

        ar = {'x': [], 'y': []}
        divider = 0

        for left, right in iterate(masters):
            leftpoint = left['glyphs'][glyphname]['points'][i]['coords']
            rightpoint = right['glyphs'][glyphname]['points'][i]['coords']
            koef = getcoefficient(left, right)
            metapolation = getmetapolation(left, right)
            divider += koef

            f = mffunc.format(k=koef, m=metapolation, A=leftpoint['x'],
                              B=rightpoint['x'])
            ar['x'].append(f)

            f = mffunc.format(k=koef, m=metapolation, A=leftpoint['y'],
                              B=rightpoint['y'])
            ar['y'].append(f)

        if not divider:
            divider = 1

        zeile = 'z{i} = ( (({fx}) / {d}), (({fy}) / {d}) );'
        zeile = zeile.format(fx='+'.join(ar['x']), fy='+'.join(ar['y']),
                             d=divider, i=zitem)



        ## default string

        # mABx = "1 * (Apx{i}l + 1 * (Bpx{i}l - Apx{i}l))".format(i=zitem)
        # mACx = "1 * (Apx{i}l + 0 * (Cpx{i}l - Apx{i}l))".format(i=zitem)
        # mBCx = "0 * (Bpx{i}l + 0 * (Cpx{i}l - Bpx{i}l))".format(i=zitem)
        # mCDx = "0 * (Cpx{i}l + 0 * (Dpx{i}l - Cpx{i}l))".format(i=zitem)
        # mBDx = "0 * (Bpx{i}l + 0 * (Dpx{i}l - Bpx{i}l))".format(i=zitem)
        # mADx = "0 * (Apx{i}l + 0 * (Dpx{i}l - Apx{i}l))".format(i=zitem)

        # mABy = "1 * (Apy{i}l + 1 * (Bpy{i}l - Apy{i}l))".format(i=zitem)
        # mACy = "1 * (Apy{i}l + 0 * (Cpy{i}l - Apy{i}l))".format(i=zitem)
        # mBCy = "0 * (Bpy{i}l + 0 * (Cpy{i}l - Bpy{i}l))".format(i=zitem)
        # mCDy = "0 * (Cpy{i}l + 0 * (Dpy{i}l - Cpy{i}l))".format(i=zitem)
        # mBDy = "0 * (Bpy{i}l + 0 * (Dpy{i}l - Bpy{i}l))".format(i=zitem)
        # mADy = "0 * (Apy{i}l + 0 * (Dpy{i}l - Apy{i}l))".format(i=zitem)

        # zeile = "z{i} = (({ABx} + {ACx} + {BCx} + {CDx} + {BDx} + {ADx}) / 2, ({ABy} + {ACy} + {BCy} + {CDy} + {BDy} + {ADy}) / 2);"
        # zeile = zeile.format(ABx=mABx, ACx=mACx, BCx=mBCx,
        #                      CDx=mCDx, BDx=mBDx, ADx=mADx,
        #                      ABy=mABy, ACy=mACy, BCy=mBCy,
        #                      CDy=mCDy, BDy=mBDy, ADy=mADy,
        #                      i=zitem)

        fip.write("\n")
        fip.write(zeile)

# reading penstrokes font B

    inattr = 0
    ivn = 0
    stre = " ... "
    strtwo = " .. "
    stline = " -- "
    strz = ""
    zzn = []

    startp = []
    startpval = []

    doubledash = []
    doubledashvalB = []

    tripledash = []
    tripledashvalB = []

    tension = []
    tensionB = []
    tensionvalB = []

    tensionand = []
    tensionandB = []
    tensionandvalB = []
    tensionandval2B = []

    superright = []
    superrightvalB = []

    superleft = []
    superleftvalB = []

    dir = []
    dirB = []
    dirvalB = []

    dir2 = []
    dir2B = []
    dir2valB = []

    leftp = []
    leftpvalB = []

    rightp = []
    rightpvalB = []

    upp = []
    uppvalB = []

    downp = []
    downpvalB = []

    penshifted = []
    penshiftedvalB = []

    i = 1

    for item in glyph['points']:
        znamer = re.match('z(\d+)r', item['preset'].get('pointname'))
        znamel = re.match('z(\d+)l', item['preset'].get('pointname'))
        zname = re.match('z(\d+)l', item['preset'].get('pointname'))

        x = item['coords']['x']
        y = item['coords']['y']

        im = item['preset'].get('pointname')

        idoubledash = item['preset'].get('doubledash')
        itripledash = item['preset'].get('tripledash')
        idir = item['preset'].get('dir')
        idir2 = item['preset'].get('dir2')
        ileftp = item['preset'].get('leftp')
        iupp = item['preset'].get('upp')
        irightp = item['preset'].get('rightp')
        idownp = item['preset'].get('downp')
        # itension = item['preset'].get('tension')
        itensionand = item['preset'].get('tensionand')
        # isuperright = item['preset'].get('superright')
        # isuperleft = item['preset'].get('superleft')
        ipenshifted = item['preset'].get('penshifted')

        if znamel and im == znamel.group(0):
            zzn.append(i)

            if idoubledash is not None:
                idoubledashval = item['preset'].get('doubledash')
                doubledash.append("doubledash")
                doubledashvalB.append(idoubledashval)

            if itripledash is not None:
                itripledashval = item['preset'].get('tripledash')
                tripledash.append(" ---")
                tripledashvalB.append(itripledashval)

            if idir is not None:
                idirval = item['preset'].get('dir')
                dirB.append("dir")
                dirvalB.append(idirval)
            else:
                dirB.append("")
                dirvalB.append(0)

            if idir2 is not None:
                idir2val = item['preset'].get('dir2')
                dir2B.append("dir")
                dir2valB.append(idir2val)

            if iupp is not None:
                iuppval = item['preset'].get('upp')
                upp.append("up")
                uppvalB.append(iuppval)

            if ileftp is not None:
                ileftpval = item['preset'].get('leftp')
                leftp.append("left")
                leftpvalB.append(ileftpval)

            if irightp is not None:
                irightpval = item['preset'].get('rightp')
                rightp.append("right")
                rightpvalB.append(irightpval)

            if idownp is not None:
                idownpval = item['preset'].get('downp')
                downp.append("down")
                downpvalB.append(idownpval)

            # if itension is not None:
            #     itensionval = item['preset'].get('tension')
            #     tensionB.append("tension")
            #     tensionvalB.append(itensionval)

            if itensionand is not None:
                itensionandval = item['preset'].get('tensionand')
                tensionandB.append("tensionand")
                tensionandvalB.append(itensionandval[:3])
                tensionandval2B.append(itensionandval[-3:])
            else:
                tensionandB.append("")
                tensionandvalB.append(0)
                tensionandval2B.append(0)

            # if isuperright is not None:
            #     isuperrightval = item['preset'].get('superright')
            #     superright.append("superright")
            #     superrightvalB.append(isuperrightval)

            # if isuperleft is not None:
            #     isuperleftval = item['preset'].get('superleft')
            #     superleft.append("superleft")
            #     superleftvalB.append(isuperleftval)

            if idir is not None:
                idirval = item['preset'].get('dir')
                dir.append("dir")
                dirvalB.append(idirval)

            if ipenshifted is not None:
                ipenshiftedval = item['preset'].get('penshifted')
                penshifted.append("shifted")
                penshiftedvalB.append(ipenshiftedval)

    # reading font penstrokes Font A

    fip.write("\n")
    fip.write("""% penstrokes""")

    # fip.write("\n")
    # fip.write("""fill""")

    inattr = 0
    ivn = 0
    stre = " ... "
    tripledash = "---"
    strtwo = " .. "
    stline = " -- "
    strz = ""
    zzn = []
    startp = []
    startpval = []

    doubledash = []
    doubledashval = []

    tripledash = []
    tripledashval = []

    tension = []
    tensionval = []

    tensionand = []
    tensionandval = []
    tensionandval2 = []

    superright = []
    superrightval = []

    superleft = []
    superleftval = []

    dir = []
    dirval = []

    leftp = []
    leftpval = []

    rightp = []
    rightpval = []

    upp = []
    uppval = []

    downp = []
    downpval = []

    dir2 = []
    dir2val = []

    leftp2 = []
    leftp2val = []

    rightp2 = []
    rightp2val = []

    upp2 = []
    upp2val = []

    downp2 = []
    downp2val = []

    penshifted = []
    penshiftedval = []

    overx = []
    overxval = []

    overbase = []
    overbaseval = []

    overcap = []
    overcapval = []

    overasc = []
    overascval = []

    overdesc = []
    overdescval = []

    cycle = []
    cycleval = []

    type = []
    typeval = []

    control_out = []
    control_outval = []

    control_in = []
    control_inval = []

    i = 1

    for item in glyph['points']:

        znamer = re.match('z(\d+)r', item['preset'].get('pointname'))
        znamel = re.match('z(\d+)l', item['preset'].get('pointname'))
        zname = re.match('z(\d+)l', item['preset'].get('pointname'))

        x = item['coords']['x']
        y = item['coords']['y']

        im = item['preset'].get('pointname')

        istartp = item['preset'].get('startp')
        idoubledash = item['preset'].get('doubledash')
        itripledash = item['preset'].get('tripledash')
        idir = item['preset'].get('dir')
        idir2 = item['preset'].get('dir2')
        ileftp = item['preset'].get('leftp')
        ileftp2 = item['preset'].get('leftp2')
        iupp = item['preset'].get('upp')
        iupp2 = item['preset'].get('upp2')
        irightp = item['preset'].get('rightp')
        irightp2 = item['preset'].get('rightp2')
        idownp = item['preset'].get('downp')
        idownp2 = item['preset'].get('downp2')
        # itension = item['preset'].get('tension')
        itensionand = item['preset'].get('tensionand')
        # isuperright = item['preset'].get('superright')
        # isuperleft = item['preset'].get('superleft')
        ipenshifted = item['preset'].get('penshifted')
        ioverx = item['preset'].get('overx')
        ioverbase = item['preset'].get('overbase')
        iovercap = item['preset'].get('overcap')
        ioverasc = item['preset'].get('overasc')
        ioverdesc = item['preset'].get('overdesc')
        # icycle = item['preset'].get('cycle')
        itype = item['preset'].get('type')
        icontrol_out = item['preset'].get('control_out')
        icontrol_in = item['preset'].get('control_in')

        if znamel and im == znamel.group(0):
            zzn.append(i)

        # do not delete that lines while you are sure
#        if im == znamel or im == znamer:

            if istartp is not None:
                istartpval = item['preset'].get('startp')
                startp.append("\nfill\n")
                startpval.append(istartpval)
            else:
                startp.append("")
                startpval.append(0)

            # if icycle is not None :
            #     icycleval = item['preset'].get('cycle')
            #     cycle.append("cycle")
            #     cycleval.append(icycleval)
            # else :
            #     cycle.append("")
            #     cycleval.append(0)

            if idoubledash is not None :
                idoubledashval = item['preset'].get('doubledash')
                doubledash.append(" -- ")
                doubledashval.append(idoubledashval)
            else :
                doubledash.append("")
                doubledashval.append(0)

            if itripledash is not None :
                itripledashval = item['preset'].get('tripledash')
                tripledash.append(" ---")
                tripledashval.append(itripledashval)
            else:
                tripledash.append("")
                tripledashval.append(0)

            if idir2 is not None :
                idir2val = item['preset'].get('dir2')
                dir2.append("dir")
                dir2val.append(idir2val)
            else :
                dir2.append("")
                dir2val.append(0)

            if iupp is not None :
                iuppval = item['preset'].get('upp')
                upp.append("{up} ")
                uppval.append(iuppval)
            else :
                upp.append("")
                uppval.append(0)

            if ileftp is not None :
                ileftpval = item['preset'].get('leftp')
                leftp.append("{left} ")
                leftpval.append(ileftpval)
            else:
                leftp.append("")
                leftpval.append(0)

            if irightp is not None :
                irightpval = item['preset'].get('rightp')
                rightp.append("{right} ")
                rightpval.append(irightpval)
            else :
                rightp.append("")
                rightpval.append(0)

            if idownp is not None :
                idownpval = item['preset'].get('downp')
                downp.append(" {down} ")
                downpval.append(idownpval)
            else :
                downp.append("")
                downpval.append(0)

            if idownp2 is not None :
                idownp2val = item['preset'].get('downp2')
                downp2.append(" {down} ")
                downp2val.append(idownp2val)
            else :
                downp2.append("")
                downp2val.append(0)

            if iupp2 is not None :
                iupp2val = item['preset'].get('upp2')
                upp2.append("{up} ")
                upp2val.append(iupp2val)
            else :
                upp2.append("")
                upp2val.append(0)


            if ileftp2 is not None :
                ileftp2val = item['preset'].get('leftp2')
                leftp2.append("{left} ")
                leftp2val.append(ileftp2val)
            else :
                leftp2.append("")
                leftp2val.append(0)

            if irightp2 is not None :
                irightp2val = item['preset'].get('rightp2')
                rightp2.append("{right} ")
                rightp2val.append(irightp2val)
            else :
                rightp2.append("")
                rightp2val.append(0)


            # if itension is not None :
            #     itensionval = item['preset'].get('tension')
            #     tension.append("tension")
            #     tensionval.append(itensionval)
            # else :
            #     tension.append("")
            #     tensionval.append(0)

            if itensionand is not None :
                itensionandval = item['preset'].get('tensionand')
                tensionand.append("tensionand")
                tensionandval.append(itensionandval[:3])
                tensionandval2.append(itensionandval[-3:])
            else :
                tensionand.append("")
                tensionandval.append(0)
                tensionandval2.append(0)


            # if isuperright is not None :
            #     isuperrightval = item['preset'].get('superright')
            #     superright.append("super_qr")
            #     superrightval.append(isuperrightval)
            # else :
            #     superright.append("")
            #     superrightval.append(0)

            # if isuperleft is not None :
            #     isuperleftval = item['preset'].get('superleft')
            #     superleft.append("super_ql")
            #     superleftval.append(isuperleftval)
            # else :
            #     superleft.append("")
            #     superleftval.append(0)

            if idir is not None :
                idirval = item['preset'].get('dir')
                dir.append("dir")
                dirval.append(idirval)
            else :
                dir.append("")
                dirval.append(0)

            if ipenshifted is not None :
                ipenshiftedval = item['preset'].get('penshifted')
                penshifted.append("shifted")
                penshiftedval.append(ipenshiftedval)
            else :
                penshifted.append("")
                penshiftedval.append(0)

            if ioverx is not None :
                ioverxval = item['preset'].get('overx')
                overx.append("shifted")
                overxval.append(ioverxval)
            else :
                overx.append("")
                overxval.append(0)


            if ioverbase is not None :
                ioverbaseval = item['preset'].get('overbase')
                overbase.append("shifted")
                overbaseval.append(ioverbaseval)
            else :
                overbase.append("")
                overbaseval.append(0)


            if iovercap is not None :
                iovercapval = item['preset'].get('overcap')
                overcap.append("shifted")
                overcapval.append(iovercapval)
            else :
                overcap.append("")
                overcapval.append(0)


            if itype is not None :
                itypeval = item['preset'].get('type')
                type.append("type")
                typeval.append(itypeval)
            else :
                type.append("")
                typeval.append(0)


            if icontrol_out is not None :
                icontrol_outval = item['preset'].get('control_out')
                control_out.append("control_out")
                control_outval.append(icontrol_outval)
            else :
                control_out.append("")
                control_outval.append(0)

            if icontrol_in is not None :
                icontrol_inval = item['preset'].get('control_in')
                control_in.append("control_in")
                control_inval.append(icontrol_inval)
            else :
                control_in.append("")
                control_inval.append(0)

            i += 1

    zzn.sort()
    zeile = ""
    semi = ";"

    fip.write('\n')

    for i in range(len(zzn) - 1):
        zitem = zzn[i]
        zeile = str(startp[i]) + "z" + str(zitem)

        if startp[i + 1] == "":

            dash = " -- "

            if type[i+1] != "":
                zeile += dash

            if control_out[i] != "":
                zeile = " .. controls z" + str(zitem) + " and "

            if control_in[i] != "":
                zeile = " z" + str(zitem) + " .. "

        else :
          if control_out[i] != "":
            zeile +=  " .. cycle" + semi + '\n'
          else :
            zeile +=  " .. cycle" + semi + '\n'


        fip.write(zeile)

        zitemb = zzn[i + 1]
        zeile = "z" + str(zitemb)
        i = i + 1

    if len(zzn) >= i:

        fip.write(zeile + " .. cycle" + semi)

    fip.write("\n")
    fip.write("% pen labels\n")
    fip.write("penlabels(range 1 thru 99);\n")
    fip.write("endchar;")

    print time.time() - starttime

    return fip.getcontents()