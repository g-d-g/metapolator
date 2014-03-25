---
layout: layout
---

Metapolator Manual
============================

_Metapolator is constantly changing, the interface is tentative and we recognise there are inefficiencies. This is up to date as of 16 Feb 2014_

## Table of Contents

- Introduction
  - <a href="#metafont">Metafont</a>
  - <a href="#metapolator">Metapolator</a>
- <a href="#ufo">UFO Preparation</a>
- <a href="#starting">Starting Metapolator</a>
- <a href="#interface">The Editor</a>
- <a href="#global">Global Parameters</a>
- <a href="#local">Local Parameters</a>
- <a href="#zpoint">Z-Point Functions</a>

## Introduction

This short guide is provided as guide to using Metapolator to design typeface families. To understand how to use Metapolator, read it all. We assume you know canonical type design concepts like optical correction. If you flunked out of high school math class, we don't yet provide a visual way to edit simple arithmetic and algebra equations, so you might want to mark your calendar to check back in 6 months.

Let's meta-design!

<h2 id="introduction">Introduction</h2>

<h3 id="metafont">Metafont</h3>

<blockquote>Unlike more common outline font formats (such as TrueType or PostScript Type 1), a Metafont font is primarily made up of strokes with finite-width 'pens', along with filled regions. Thus, rather than describing the outline of the glyph directly, a Metafont file describes the pen paths.</blockquote>
– from Wikipedia

<img src="images/a.png" alt="'a' glyph" /><br/>
– *Lowercase 'a' as constructed by Metafont*

The numerical points denote the 'pen positions' (also known as 'z-points') of a stroke. The z-points are where Metafont functions are applied – see <a href="#zpoint">z-point Functions</a>. The 'l' and 'r' points define the thickness (known as 'pen widths') – and angle of each 'pen position'. Together, the 'pen positions' define a pen path (or 'penstroke') – the black line.

<h3 id="metapolator">Metapolator</h3>

Metapolator converts outline fonts to Metafonts by parsing the point coordinates from xml and calculating the 'pen positions' and 'pen widths'. To do so, Metapolator requires specially prepared UFO files.

See <a href="ufo.html">UFO Preparation</a> for further instructions on how to prepare outlines – especially for <a href="zpoint.html#stemcutter">stemcuts</a> and <a href="zpoint.html#inktrap_l">inktraps</a>.

Metapolator uses two font 'masters' – FontA and FontB – to interpolate between and generate fonts. FontA and FontB may have different Pen positions (as in the position of the points in the UFO files) and different <a href="local.html">Local Parameters</a>. Metapolator can also interpolate between different <a href="zpoint.html">z-point Functions</a> for:

<ul>
 - dir
 - dir2
 - angle
 - penwidth
 - tension
 - tensionand
 - superright
 - superleft



<img src="images/a.gif" alt="Metapolation of 'a'" /><br/>
*Metapolation between FontA and FontB*

<h2>Starting Metapolator<a id="starting"></a></h2>

<hr />

The first screen is the 'Settings' screen.<br/>
<img src="images/settings.gif" alt="Settings" /><br/>
1. Click the Project Number you wish to work on.<br/>
2. Enter the Project Name, FontA and FontB if not already filled in.<br/>
3. Select the glyph you wish to edit.<br/>
4. 'Edit' to go to the Editor.

If you are starting a new project, you may wish to edit the <a href="global.html">Global</a> and <a href="local.html">Local Parameters</a> first.

<h1>UFO Preparation</h1>

<ol>
 - Prepare outlines
 - Label z-points
 - Rename glyphs and .glif files
</ol>


<h2>1. Preparing outlines</h2>

Metapolator requires UFOs where shapes are broken up into constituent parts or 'strokes'.<br/>
<img src="images/outlines.png" alt="Outlines" />

Almost all glyphs contain composite shapes which will require splitting up into seperate 'strokes'. Here are some examples:<br/>
<img src="images/ufo/n.png" alt="n" /><br/>
<img src="images/ufo/n2.png" alt="n" /><br/>
<img src="images/ufo/n3.png" alt="n" /><br/>
<img src="images/ufo/n_.png" alt="N" /><br/>
<img src="images/ufo/b_.png" alt="B" />

<h3>Stemcut<a id="stemcut"></a></h3>

An extra z-point pair is required preceding/following (depending on ordering) the z-point where a stemcut will be applied.
<img src="images/ufo/nextra.png" alt="N Stemcut" /><br/>
*An 'n' before and after adding an extra point pair for stemcuts*<br/>
&nbsp;<br/>
&nbsp;<br/>
<img src="images/ufo/nstemcut.gif" alt="N Stemcut" /><br/>
*An 'n' with a <a href="stemcut.html">stemcut</a> and <a href="stemshift.html">stemshift</a> applied to the top z-point. The example on the right also has a down function at the 2nd point to create a smooth transition*

<h3>Inktrap<a id="inktrap"></a></h3>

An inktrap is similar to a stemcut as they also requre an extra z-point.

The z-point pair should be parallel to the other z-point pairs; in this case the points are horizontal.

<img src="images/ufo/v_stemcut.gif" alt="V Inktrap" />

<h2>2. Labelling z-points</h2>

<img src="images/ufo/tfilled.png" alt="'t' glyph" /><br/>
Currently every on-curve point needs to be manually labelled in consecutive pairs in the 'z–l' and 'z–r' format; for example, z1l, z1r, z2l, z2r, and so. Each pair creates a z-point. This is the order in which a stroke will be rendered. A new stroke in the same glyph continues the numbering rather than starting from z1 again.

<img src="images/ufo/labelling.gif" alt="Labelling z-points" /><br/>
1. Click a blank point.<br/>
2. Enter the point name.<br/>
3. Save

Take care to keep the l and r sides consistent with the direction which the pen is travelling – a useful metaphor is to imagine the pen as a car: a sudden reversal in the left and right side probably means disaster!<br/>
<img src="images/ufo/tflipped.png" alt="Wrong labels" />

<h2>3. Renaming glyphs and .glif files</h2>

Due to restrictions within Metafont, the .glif filenames and 'glyph name' (an xml tag within the .glif file) must be renamed according to the numeric filenames set out in <a href="glyphnames.txt">glyphnames.txt</a> (also found in the local folder of Metaplator).

*Currently this process is done manually but we would like to automate this in the near future*

<h3>Rename .glif files</h3>

The .glif files are found inside the .ufo/glyphs/ folder. To access, right click on the ufo and 'Show Packaged Contents'.

<h3>Rename 'glyph name'</h3>

A .glif file is an xml file that describes the glyph. The <code>&lt;glyph format="1" name="a"&gt;</code> tag must be changed so that it corresponds to the numeric value; for example <code>&lt;glyph format="1" name="65"&gt;</code>


<h1>Global Parameters</h1>

Excluding metapolation, these parameters correspond to the values in the original UFO font. The input type is a floating point.

<table>
<thead>
<tr>
<th align="left">Parameter </th>
<th align="left"> Description</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">**metapolation**<a id="metapolation"></a> </td>
<td align="left"> The amount of interpolation between FontA and FontB. 0 reads only FontA while 1 reads only FontB; 0.5 is halfway between FontA and FontB and so on.</td>
</tr>
<tr>
<td align="left">**fontsize**<a id="fontsize"></a> </td>
<td align="left"> The 'Units Per EM' divided by 100.</td>
</tr>
<tr>
<td align="left">**mean**<a id="mean"></a> </td>
<td align="left"> The x-height divided by 100.</td>
</tr>
<tr>
<td align="left">**cap**<a id="cap"></a>  </td>
<td align="left"> The cap-height divided by 100.</td>
</tr>
<tr>
<td align="left">**asc**<a id="asc"></a>  </td>
<td align="left">  The ascender height divided by 100.</td>
</tr>
<tr>
<td align="left">**desc**<a id="desc"></a> </td>
<td align="left"> The descender depth divided by 100.</td>
</tr>
<tr>
<td align="left">**box**<a id="box"></a>  </td>
<td align="left"> The total height from either the cap- or ascender height (whichever is higher) to the descender depth, divided by 100. *Currently not in use.*</td>
</tr>
</tbody>
</table>


The Global Parameters page:<br/>
<img src="images/global.png" alt="" />

*Global 1 and Global 2 are the parameter sets currently available, click either to set and edit*


<h1>Local Parameters</h1>

Metapolator uses the Local Parameters at FontA and FontB for interpolation. The input type is a floating point.

<table>
<thead>
<tr>
<th align="left">Parameter </th>
<th align="left"> Description</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">**px**<a id="px"></a> </td>
<td align="left"> Extra 'pen width', default is 0. Adding px increases the weight of the font – which will usually require compensations and adjustments in the z-point Functions, such as 'pen width', 'over' and 'pen'/'pointshifting'.</td>
</tr>
<tr>
<td align="left">**width**<a id="width"></a>  </td>
<td align="left"> The width of the typeface, default is 1.</td>
</tr>
<tr>
<td align="left">**space**<a id="space"></a> </td>
<td align="left"> Spacing adjustment. Default is 0. Positive value increases spacing; negative value decreases spacing.</td>
</tr>
<tr>
<td align="left">**xheight**<a id="height"></a> </td>
<td align="left"> The x-height. If the value given here is the equal to mean in Global Parameters, then no x-height adjustment is made.</td>
</tr>
<tr>
<td align="left">**capital**<a id="capital"></a>  </td>
<td align="left"> The cap-height. If the value given here is the equal to cap in Global Parameters, then no cap-height adjustment is made.</td>
</tr>
<tr>
<td align="left">**boxheight**<a id="boxheight"></a> </td>
<td align="left"> The total height between cap- or ascender height . If the value given here is the equal to box in Global Parameters, then no total height adjustment is made.</td>
</tr>
<tr>
<td align="left">**ascender**<a id="ascender"></a> </td>
<td align="left"> The ascender height. If the value given here is the equal to asc in Global Parameters, then no ascender height adjustment is made.</td>
</tr>
<tr>
<td align="left">**descender**<a id="descender"></a> </td>
<td align="left"> The descender height. If the value given here is the equal to desc in Global Parameters, then no descender height adjustment is made.</td>
</tr>
<tr>
<td align="left">**inktrap**<a id="inktrap"></a>  </td>
<td align="left"> The size of inktraps when an <a href="zpoint.html#inktrap_l">inktrap_l</a> or <a href="zpoint.html#inktrap_r">inktrap_r</a> function is applied to a point.</td>
</tr>
<tr>
<td align="left">**stemcut**<a id="stemcut"></a>  </td>
<td align="left"> The size of stem cuts when a <a href="local.html#stemcut">stemcut</a> function is applied to a point.</td>
</tr>
<tr>
<td align="left">**skeleton**<a id="skeleton"></a> </td>
<td align="left"> The amount of reduction towards or addition away from the monolinear skeleton. Default is 0. -1 gives you an almost razor-thin skeleton.
    The skeleton parameter is useful when you want to remove contrast.<br/>
    <img src="images/oskeleton.gif" alt="Contrast to no-contrast" />

    Subsquently, px can be added to create a monolinear typeface.<br/>
    <img src="images/obold.gif" alt="Weight on top of contrast" />
    
</tr>
<tr>
<td align="left">**superness**<a id="superness"></a> </td>
<td align="left"> The round/squareness of a superquarter – when using a superleft or superright z-point function.</td>
</tr>
<tr>
<td align="left">**over**<a id="over"></a> </td>
<td align="left"> The amount of overshoot. 0.1 would be equivalent to 10 units in a UFO file.</td>
</tr>
</tbody>
</table>


The Local Parameters page:<br/>
<img src="images/localparam.gif" alt="" />


<h1>Z-point Functions</h1>

These are the Metafont functions that are applied to individual z-points. This is how lettershapes are sculpted. Examples can be found by clicking the function names in the table.

In most functions there is no difference between applying a function to z-l or z-r, the calculation is made either by taking a pair in account or using the center point; for example, an inktrap_l can be similarly applied either to a z3l or z3r. Common sense should apply on which functions will be in conflict; for example, a leftp can not be used on the same point with a rightp. Exceptions are point-coordinate related functions, like penshifted, pointshifted and all overshoot functions.

<h4>Important</h4>

Most of the z-point functions only need to be applied to FontA. The following functions can take a different value in FontB (by specifying it again on the same point) to interpolate between. In the current version a value in FonatA AND FontB is mandatory.

<ul>
 - <a href="#dir">dir</a>
 - <a href="#dir2">dir2</a>
 - <a href="#angle">angle</a>
 - <a href="#penwidth">penwidth</a>
 - <a href="#tension">tension</a>
 - <a href="#tensionand">tensionand</a>
 - <a href="#superright">superright</a>
 - <a href="#superright">superleft</a>



<table>
<thead>
<tr>
<th align="left">Function </th>
<th align="left"> Input </th>
<th align="left"> Description</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">**startp**<a id="start"></a> </td>
<td align="left"> 0 or 1 </td>
<td align="left"> Starts a new penstroke. Z1 will always require a startp – otherwise Metafont will return an error.
    
    <img src="http://24.media.tumblr.com/20f71b21bb37b49c9f3096091c52ef52/tumblr_mprytrSzNm1svhn7so1_500.png" alt="" /><br/>
    'g' glyph as a single penstroke.

    <img src="images/startp/e_.gif" alt="" /><br/>
    'E' glyph being formed with the addition of startp commands then penshifted commands.

    <img src="images/startp/equals.gif" alt="" /><br/>
    '=' glyph before and after applying a startp to the second stroke.
    
    </td>
</tr>
<tr>
<td align="left">**doubledash**<a id="doubledash"></a> </td>
<td align="left"> 0 or 1 </td>
<td align="left"> Creates a straight line to the next z-point (z+1). This is required because Metafont's default mode of drawing is to connect points with curves.
    
    <h1>doubledash and tripledash</h1>

    <img src="images/dash/n.gif" alt="" />
    An <a href="inktrap.html">inktrap_l</a> has been applied but the penstroke is not straight due to the nature of Metafont's default curve drawing. So a doubledash is added to straighten the stroke.<br/>
    &nbsp;<br/>
    &nbsp;

    <img src="images/dash/n-dashes.gif" alt="" />
    The difference between doubledash and tripledash.
    
    </td>
</tr>
<tr>
<td align="left">**<a href="dash.html">tripledash</a>**<a id="tripledash"></a> </td>
<td align="left"> 0 or 1 </td>
<td align="left"> Creates a straight line which blends smoothly into the next z+1. The angle of the tangent at z+1 will be equal to the angle between z and z+1.</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td align="left">**superleft**<a id="superleft"></a> </td>
<td align="left"> Float </td>
<td align="left"> Creates a left quarter of a <a href="http://en.wikipedia.org/wiki/Superellipse">superellipse</a>. Superquarters are not as flexible as ordinary curves – direction and tension commands are not applicable and pointshifting is difficult to tame with superquarters. However, <a href="http://metaflop.com/img/helloworld/bespoke-helloworld-01-it.png">interesting results</a> are possible.</td>
</tr>
<tr>
<td align="left">**superright**<a id="superright"></a> </td>
<td align="left"> Float </td>
<td align="left"> Creates a right quarter of a <a href="http://en.wikipedia.org/wiki/Superellipse">superellipse</a>. See above.</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>

    <img src="images/dir/arightp.gif" alt="" /><br/>
    'a', before and after a rightp function is applied to z2.  <br/>
    &nbsp;<br/>
    <img src="images/dir/adownp.png" alt="" /><br/>
    Downp function.<br/>
    &nbsp;<br/>
    <img src="images/dir/aupp.png" alt="" /><br/>
    Upp function.<br/>
    &nbsp;<br/>
    <img src="images/dir/adir.gif" alt="" /><br/>
    Dir function in counterclockwise increments of 45°. Note how the curve between z2 and z3 is very much affected by the direction at z1, this is because there is no function on z2 that constrains the direction or tension in anyway.

    <h1>leftp2, rightp2, downp2, upp2, dir2</h1>

    <img src="images/dir2/adir2.gif" alt="" /><br/>
    Dir2 function in counterclockwise increments of 45°. Dir2 is applied on z7 to change the angle on the final z-point in the penstroke – at z8.

</tr>
<tr>
<td align="left">**<a href="dir.html">leftp</a>**<a id="leftp"></a> </td>
<td align="left"> 0 or 1 </td>
<td align="left"> Direction at z will be leftwards.</td>
</tr>
<tr>
<td align="left">**<a href="dir.html">rightp</a>**<a id="rightp"></a> </td>
<td align="left"> 0 or 1 </td>
<td align="left"> As above but rightwards.</td>
</tr>
<tr>
<td align="left">**<a href="dir.html">downp</a>**<a id="downp"></a> </td>
<td align="left"> 0 or 1 </td>
<td align="left"> As above but downwards.</td>
</tr>
<tr>
<td align="left">**<a href="dir.html">upp</a>**<a id="upp"></a> </td>
<td align="left"> 0 or 1 </td>
<td align="left"> As above but upwards.</td>
</tr>
<tr>
<td align="left">**<a href="dir.html">dir</a>**<a id="dir"></a> </td>
<td align="left"> Foat </td>
<td align="left"> As above but at the specified. Metafont angles are measured in degrees counterclockwise from a horizontal rightward line. See <a href="images/clock.png" target="_blank">Metafont&nbsp;clock</a>.</td>
</tr>
<tr>
<td align="left">**<a href="dir2.html">leftp2</a>**<a id="leftp2"></a> </td>
<td align="left"> 0 or 1 </td>
<td align="left"> Direction going into z+1 will be leftwards. **Important:** direction commands (leftp, rightp, downp, upp, dir)  can not be used on the last z point as it reqiures a z+1 point. Direction2 commands (lefpt2, rightp2, downp2, upp2, dir2) are used on the z-point before the final one in a penstroke to specify the terminatng direction. For example, if z8 is the last z-point in a penstroke, leftp2 would be applied to z7 to create a leftwards travelling ending at z8.</td>
</tr>
<tr>
<td align="left">**<a href="dir2.html">rightp2</a>**<a id="rightp2"></a> </td>
<td align="left"> 0 or 1 </td>
<td align="left"> Similar to leftp2 but rightwards.</td>
</tr>
<tr>
<td align="left">**<a href="dir2.html">downp2</a>**<a id="downp2"></a> </td>
<td align="left"> 0 or 1 </td>
<td align="left"> Similar to leftp2 but downwards.</td>
</tr>
<tr>
<td align="left">**<a href="dir2.html">upp2</a>**<a id="upp2"></a> </td>
<td align="left"> 0 or 1 </td>
<td align="left"> Similar to leftp2 but upwards.</td>
</tr>
<tr>
<td align="left">**<a href="dir2.html">dir2</a>**<a id="dir2"></a> </td>
<td align="left"> Float </td>
<td align="left"> Similar to leftp2 but at the <a href="images/clock.png" target="_blank">angle</a> specified.</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td align="left">**<a href="tension.html">tension</a>**<a id="tension"></a> </td>
<td align="left"> 3 digit integer </td>
<td align="left"> Specifies the 'tension' of a curve. All curves have a default tension of 100. 075–400 is the allowed range. Higher values creates a straighter line (400 usually produces a straight line), while a decrease is looser.</td>
</tr>
<tr>
<td align="left">**<a href="tension.html#and">tensionand</a>**<a id="tensionand"></a> </td>
<td align="left"> 6 digit integer </td>
<td align="left"> Asymmetrical tension setting, the first 3 digit specifies the first half of a curve, while the next 3 specifies the second half.</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td align="left">**cycle**<a id="cycle"></a> </td>
<td align="left"> 0 or 1 </td>
<td align="left"> Specified on the last z-point in a penstroke to create a stroke loop. Used in glyphs such as 'o' to create a circle.
    
    A cycle command turns a penstroke into a closed loop. For example an 'o' without a cycle looks like this:<br/>
    <img src="images/cycle/oopen.png" alt="" />
    &nbsp;<br/>
    Once a cycle function is applied to z4, the loop is closed:<br/>
    <img src="images/cycle/oclosed.png" alt="" />
    
    </td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td align="left">**<a href="penshifted.html">penshifted</a>**<a id="penshifted"></a> </td>
<td align="left"> String </td>
<td align="left"> Shifts the point after other transformations have been applied. There is usually no difference between penshifted and pointshifted – it becomes important when using superleft or superright. See <a href="penshifted.html">instructions</a> on how to create 'magnetic' points that attach to other points and more.</td>
</tr>
<tr>
<td align="left">**<a href="pointshifed.html">pointshifted</a>**<a id="pointshifted"></a> </td>
<td align="left"> String </td>
<td align="left"> Shifts the poiint before transformations have been applied.</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td align="left">**<a href="angle.html">angle</a>**<a id="angle"></a> </td>
<td align="left"> '+string' or '‑string' </td>
<td align="left"> Changes the pen angle. Enter equations such as: '+20' or '-30'.</td>
</tr>
<tr>
<td align="left">**<a href="penwidth.html">penwidth</a>**<a id="penwidth"></a> </td>
<td align="left"> Float </td>
<td align="left"> Multiplies the pen width by the value entered. 1 keeps the width, 0.5 is half, 2 is double and so on.</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td align="left">**<a href="over.html">overx</a>**<a id="overx"></a> </td>
<td align="left"> y&thinsp;–&thinsp;l or y&thinsp;–&thinsp;r </td>
<td align="left"> Used to create overshoots by the amount specified in the <a href="local.html#over">over</a> Local Parameter. Enter the the y&thinsp;–&thinsp;l or y&thinsp;–&thinsp;r point (y3l, y4r, and so on) which corresponds to where the overshoot should occur. Overx can also be applied to points adjacent to the overshoot to shift the whole curve instead of one point – this keeps the shape of the curve intact. See <a href="over.html#curve">Overshoot whole curve</a>.</td>
</tr>
<tr>
<td align="left">**<a href="over.html">overbase</a>**<a id="overbase"></a> </td>
<td align="left"> y&thinsp;–&thinsp;l or y&thinsp;–&thinsp;r </td>
<td align="left"> Similar to overx but at the baseline.</td>
</tr>
<tr>
<td align="left">**<a href="over.html">overcap</a>**<a id="overcap"></a> </td>
<td align="left"> y&thinsp;–&thinsp;l or y&thinsp;–&thinsp;r </td>
<td align="left"> Similar to overx but at the cap-height.</td>
</tr>
<tr>
<td align="left">**<a href="over.html">overasc</a>**<a id="overasc"></a> </td>
<td align="left"> y&thinsp;–&thinsp;l or y&thinsp;–&thinsp;r </td>
<td align="left"> Similar to overx but at the ascender.</td>
</tr>
<tr>
<td align="left">**<a href="over.html">overdesc</a>**<a id="overdesc"></a> </td>
<td align="left"> y&thinsp;–&thinsp;l or y&thinsp;–&thinsp;r </td>
<td align="left"> Similar to overx but at the descender.</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td align="left">**ascpoint**<a id="ascpoint"></a> </td>
<td align="left"> y&thinsp;–&thinsp;l or y&thinsp;–&thinsp;r </td>
<td align="left"> Tags a point as part of the ascender to prevent it from being affected by the xheight, capital, or descender parameter. *Currently not in use.*</td>
</tr>
<tr>
<td align="left">**descpoint**<a id="descpoint"></a> </td>
<td align="left"> y&thinsp;–&thinsp;l or y&thinsp;–&thinsp;r </td>
<td align="left"> Tags a point as part of the descender to prevent it from being affected by the xheight, capital, or ascender parameter. *Currently not in use.*</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td align="left">**<a href="stemcut.html">stemcutter</a>**<a id="stemcutter"></a> </td>
<td align="left"> Float </td>
<td align="left"> Used in conjuction with stemshift to create a stem cut. A value of '1' decreases the penwidth by the amount specified in the <a href="local#stemcut">stemcut</a> Local Parameter. The stem will not be straight so a stemshift and <a href="stemcut.html">other corrections</a> are needed. **Important:** The ufo must be prepared with extra z-points, see <a href="ufo.html#stemcut">UFO Preparation</a>.</td>
</tr>
<tr>
<td align="left">**<a href="stemcut.html">stemshift</a>**<a id="stemshift"></a> </td>
<td align="left"> Float </td>
<td align="left"> -1 straightens the left side of the stem, 1 straightens the right side. Other values create non-straight strokes. See <a href="stemcut.html">More</a>. **Important:** The ufo must be prepared with extra z-points, see <a href="ufo.html#stemcut">UFO Preparation</a>.</td>
</tr>
<tr>
<td align="left">**<a href="inktrap.html">inktrap_l</a>**<a id="inktrap_l"></a> </td>
<td align="left"> Float </td>
<td align="left"> Decreases the penwidth by the amount specified in the <a href="local.html#intrap">inktrap</a> Local Parameter and straightens up the stem on the left side of the penstroke. Used in conjuction with inktrap_r on a colliding penstrokes to create a symmetrical inktrap. The difference between inktrap_l/r and stemcutter &amp; stemshift is that the inktrap_l/r function will always create a straight edge, whereas using stemscutter &amp; stemshift can create results like <a href="stemcut.html#notstraight">this</a>. **Important:** The ufo must be prepared with extra z-points, see <a href="ufo.html#inktrap">UFO Preparation</a>.</td>
</tr>
<tr>
<td align="left">**<a href="inktrap.html">inktrap_r</a>**<a id="inktrap_r"></a> </td>
<td align="left"> Float </td>
<td align="left"> As above but on the right side.</td>
</tr>
</tbody>
</table>