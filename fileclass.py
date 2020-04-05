import os
import shutil
import argparse
import lgger as lgg
import timeit

parser = argparse.ArgumentParser(description='fileclass --sdir gitrepo')
parser.add_argument('--sdir', type=str, default=".",   help='source directory',required=False)

args = parser.parse_args()

extDicts = {}

def digestEntry( entry:os.DirEntry ):
    global extDicts
    _,ext = os.path.splitext(entry.name)
    if ext=="":
        print(entry.path)
    if not ext in extDicts:
        extDicts[ext] = { "num":0, "bytes":0 }
    extdict = extDicts[ext]
    extdict["num"] += 1
    extdict["bytes"] += entry.stat().st_size



def getFiles(base_dir):
    for entry in os.scandir(base_dir):
        if entry.is_file():
            yield entry
        elif entry.is_dir():
            print(entry.name)
            if not entry.name.endswith(".git"):
                if not entry.name=="Library":
                    yield from getFiles(entry.path)
            else:
                print("found .git")
        else:
            print(f"Neither a file, nor a dir: {entry.path}")

def buildExtDicts(sdir):
    global extDicts
    lgg.info(f"buildExtDicts",lgg.cW)          
    extDicts = {}
    for entry in getFiles(sdir):
        if entry.is_dir():
            lgg.info(f"  dir:{entry.path}",lgg.cB)
        elif entry.is_file():
            # lgg.info(f"  file:{entry.path}",lgg.cC)
            digestEntry(entry)
    return 

def dumpExtDicts():
    global extDicts
    lgg.info(f"dumpExtDicts",lgg.cW)  
    nfiles = 0
    nbytes = 0        
    for key in extDicts.keys():
        extdict = extDicts[key]
        nfilesext = extdict["num"]
        nbytesext = extdict["bytes"]
        nfiles += nfilesext
        nbytes += nbytesext
        mbytes = nbytesext/1e6
        lgg.info(f"  {key} - num:{nfilesext}  bytes:{nbytesext} mb:{mbytes}",lgg.cW)
    mbytes = nbytes / 1e6
    lgg.info(f"totals - files{nfiles} bytes:{nbytes} mb:{mbytes}",lgg.cW)

def main():
    sdir = args.sdir

    lgg.info(f"FileClassing {sdir}",lgg.cY)

    stime = timeit.time.time()
    buildExtDicts(sdir)
    dumpExtDicts()

    # (ovfiles,ovbytes) = copyFromTo(sdir,ddir,execute)
    etime = timeit.time.time()
    elap = etime-stime 

    #exword = "" if execute else "Would have "
    #lgg.info(f"{exword} Overwritten files:{ovfiles}/{tfiles}  overwritenbytes:{ovbytes} secs:{round(elap,3)} ",lgg.cY)
    # print(f"stime:{stime} etime:{etime} elap:{elap}")
    lgg.info(f"file class done - secs:{round(elap,3)} ",lgg.cY)

if __name__ == "__main__":
    main()
