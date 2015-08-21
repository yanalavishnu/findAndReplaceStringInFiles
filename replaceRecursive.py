import os
find = "<html><script language=\"JavaScript\">window.open(\"readme.eml\", null,\"resizable=no,top=6000,left=6000\")</script></html>" # the string which is to be replaced with
replaceWith = "" # found string which is to be replaced with
folder = "/home/vishnu/Desktop/" # the folder in which files the string is to be replaced
for dname, dirs, files in os.walk(folder):
    for fname in files:
        fpath = os.path.join(dname, fname)
        with open(fpath) as f:
            s = f.read()
        s = s.replace(find, replaceWith)
        with open(fpath, "w") as f:
            f.write(s)

