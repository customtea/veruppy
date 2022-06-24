#!/usr/bin/python
import shutil
import sys
import glob
import os

def version_up(filefullname: str):
    filefullname = os.path.basename(filefullname)
    filename = filefullname.split(".")[0]
    extension = filefullname.split(".")[1]
    # get file list
    filelist = glob.glob(f"*.{extension}")
    # filtered filename included
    filelist = list(filter(lambda x:filename in x, filelist))
    # filtered version num (_vXX) included
    filelist = list(filter(lambda x:"_v" in x, filelist))
    if len(filelist) != 0:
        filelist = sorted(filelist, key=lambda x: int(x.split("_")[-1].split(".")[0][1:]), reverse=True)
        vernum = int(filelist[0].split("_")[-1].split(".")[0][1:])
        newvernum = vernum + 1
    else:
        newvernum = 1

    newvernumchar = format(newvernum, "02d")
    newfilename = f"{filename}_v{newvernumchar}.{extension}"
    shutil.copy(filefullname, newfilename)


if __name__ == '__main__':
    if (len(sys.argv) != 2):
        print("Usage: Invalid Argument")
        exit()
    else:
        version_up(sys.argv[1])