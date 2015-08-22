import os
find = "<html><script language=\"JavaScript\">window.open(\"readme.eml\", null,\"resizable=no,top=6000,left=6000\")</script></html>" # the string which is to be replaced with
replaceWith = "" # found string which is to be replaced with
from os.path import expanduser
home = expanduser("~")
for dname, dirs, files in os.walk(home):
    for fname in files:
        fpath = os.path.join(dname, fname)
        if(fname is "readme.eml")
            os.remove(fpath);           # remove "readme.eml" file
        elif(fname.endswith(".html") or fname.endswith(".html"))        # if file is html document
            with open(fpath) as f:
                s = f.read()
            s = s.replace(find, replaceWith)
            with open(fpath, "w") as f:
                f.write(s)

