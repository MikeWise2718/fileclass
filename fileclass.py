import os
import shutil
import argparse
import lgger as lgg
import timeit


class FileClass:
    parser = argparse.ArgumentParser(description='fileclass --sdir gitrepo')
    parser.add_argument('--sdir', type=str, default=".",   help='source directory',required=False)

    args = parser.parse_args()

    extDicts = {}

    ignoreDirList = (".git","Library")
    classDicts = {"lfs":(".obj",".tiff")}

    def getClass(self,ext):
        for key in self.classDicts.keys():
            if ext in self.classDicts[key]:
                return key
        return "rest"


    def digestEntry(self, entry:os.DirEntry ):
        _,ext = os.path.splitext(entry.name)
        if ext=="":
            print(entry.path)
        if not ext in self.extDicts:
            self.extDicts[ext] = { "num":0, "bytes":0 }
        extdict = self.extDicts[ext]
        extdict["num"] += 1
        extdict["bytes"] += entry.stat().st_size


    def isToBeIgnored(self,entry:os.DirEntry):
        if not entry.is_dir():
            return False
        if entry.name in self.ignoreDirList:
            lgg.info(f"  Ignoring {entry.name}",lgg.cR)
            return True
        return False


    def getFiles(self,base_dir):
        for entry in os.scandir(base_dir):
            if entry.is_file():
                yield entry
            elif entry.is_dir():
                print(entry.name)
                if not self.isToBeIgnored(entry):
                    yield from self.getFiles(entry.path)
            else:
                print(f"Neither a file, nor a dir: {entry.path}")


    def buildExtDicts(self,sdir):
        lgg.info(f"buildExtDicts",lgg.cW)          
        self.extDicts = {}
        for entry in self.getFiles(sdir):
            if entry.is_dir():
                lgg.info(f"  dir:{entry.path}",lgg.cB)
            elif entry.is_file():
                # lgg.info(f"  file:{entry.path}",lgg.cC)
                self.digestEntry(entry)
        return 

    def dumpExtDicts(self):
        lgg.info(f"dumpExtDicts",lgg.cW)  
        nfiles = 0
        nbytes = 0        
        for key in self.extDicts.keys():
            exd = self.extDicts[key]
            nfilesext = exd["num"]
            nbytesext = exd["bytes"]
            cls = self.getClass(key)
            nfiles += nfilesext
            nbytes += nbytesext
            mbytes = round(nbytesext/1e6,3)
            lgg.info(f"  {key:>8} {cls:>6} - num:{nfilesext:>4}  bytes:{nbytesext:>8}   mb:{mbytes:>6}",lgg.cW)
        mbytes = round(nbytes / 1e6,3)
        lgg.info(f"totals - files{nfiles} bytes:{nbytes} mb:{mbytes}",lgg.cW)

    def main(self):
        sdir = self.args.sdir

        lgg.info(f"FileClassing {sdir}",lgg.cY)

        stime = timeit.time.time()
        self.buildExtDicts(sdir)
        self.dumpExtDicts()

        # (ovfiles,ovbytes) = copyFromTo(sdir,ddir,execute)
        elap = timeit.time.time()-stime 

        #exword = "" if execute else "Would have "
        #lgg.info(f"{exword} Overwritten files:{ovfiles}/{tfiles}  overwritenbytes:{ovbytes} secs:{round(elap,3)} ",lgg.cY)
        lgg.info(f"file class done - secs:{round(elap,3)} ",lgg.cY)

if __name__ == "__main__":
    fc = FileClass()
    fc.main()
