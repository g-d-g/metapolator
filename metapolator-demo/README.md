## metapolator-demo, a generated CouchApp

Install with 
    
    couchapp push . http://localhost:5984/metapolator-demo

or (if you have security turned on)

    couchapp push . http://adminname:adminpass@localhost:5984/metapolator-demo
  
Dave Crossland created this app by running

    brew install couchdb;
    ln -sfv /usr/local/opt/couchdb/*.plist ~/Library/LaunchAgents;
    launchctl load ~/Library/LaunchAgents/homebrew.mxcl.couchdb.plist;
    sudo env ARCHFLAGS="-arch i386 -arch x86_64" pip install couchapp;
    couchapp -v generate app metapolator-demo;
    cd metapolator-demo;
    couchapp push . http://localhost:5984/metapolator-demo;
    couchapp autopush . http://localhost:5984/metapolator-demo;
    open http://localhost:5984/metapolator-demo/_design/metapolator-demo/index.html;

## License

GPLv3