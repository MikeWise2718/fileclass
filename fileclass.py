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
    clsDicts = {}

    ignoreDirList = (".git","Library")
    classExtLists = {"lfs":(".obj",".tiff")}

    def getClass(self,ext):
        for key in self.classExtLists.keys():
            if ext in self.classExtLists[key]:
                return key
        return "rest"

    def getLongestExtKeyLength(self):
        mxkeylen = 0
        for key in self.extDicts:
            if len(key)>mxkeylen:
                mxkeylen = len(key)
        return mxkeylen

    def digestEntry(self, entry:os.DirEntry ):
        _,ext = os.path.splitext(entry.name)
        if not ext in self.extDicts:
            self.extDicts[ext] = { "num":0, "bytes":0,"maxbytes":0,"maxname":"" }
        exd = self.extDicts[ext]
        exd["num"] += 1
        esize = entry.stat().st_size
        exd["bytes"] += esize
        if esize>exd["maxbytes"]:
            exd["maxbytes"] = esize
            exd["maxname"] = entry.path
        if esize>10e6:
            emb = round(esize/1e6,3)
            lgg.info(f"    big file: {emb} mb - {entry.path}")


    def isToBeIgnored(self,entry:os.DirEntry):
        if not entry.is_dir():
            return False
        if entry.name in self.ignoreDirList:
            lgg.info(f"    Ignoring {entry.name}",lgg.cR)
            return True
        return False


    def getFiles(self,base_dir):
        for entry in os.scandir(base_dir):
            if entry.is_file():
                yield entry
            elif entry.is_dir():
                lgg.info(f"    Directory {entry.name}",lgg.cC)
                if not self.isToBeIgnored(entry):
                    yield from self.getFiles(entry.path)
            else:
                print(f"Neither a file, nor a dir: {entry.path}")


    def buildExtDicts(self,sdir):
        lgg.info(f"  buildExtDicts dir:{sdir}",lgg.cP)          
        self.extDicts = {}
        for entry in self.getFiles(sdir):
            if entry.is_dir():
                lgg.info(f"    dir:{entry.path}",lgg.cB)
            elif entry.is_file():
                # lgg.info(f"  file:{entry.path}",lgg.cC)
                self.digestEntry(entry)
        return 


    def dumpExtDicts(self):
        lgg.info(f"  dumpExtDicts",lgg.cP)  
        nfiles = 0
        nbytes = 0        
        mxkeylen = self.getLongestExtKeyLength()
        for extkey in self.extDicts.keys():
            exd = self.extDicts[extkey]
            nfilesext = exd["num"]
            nbytesext = exd["bytes"]
            maxbytesext = exd["maxbytes"]
            avgbytesext = round(maxbytesext/nfilesext,0)
            cls = self.getClass(extkey)
            nfiles += nfilesext
            nbytes += nbytesext
            mbytes = round(nbytesext/1e6,3)
            extkeypad = extkey.rjust(mxkeylen)
            lgg.info(f"  {extkeypad} {cls:>6} - num:{nfilesext:>4}  sizecls-max:{maxbytesext:>10} avg:{avgbytesext:>10}  tot-mb:{mbytes:>6}",lgg.cB)
        mbytes = round(nbytes / 1e6,3)
        lgg.info(f"totals - files{nfiles} bytes:{nbytes} mb:{mbytes}",lgg.cB)

    def buildClsDicts(self):
        lgg.info(f"  buildClsDicts",lgg.cP)          
        self.clsDicts = {}
        for extkey in self.extDicts.keys():
            exd = self.extDicts[extkey]
            clskey = self.getClass(extkey)
            if not clskey in self.clsDicts:
                self.clsDicts[clskey] = { "num":0, "bytes":0 }
            cld = self.clsDicts[clskey]
            cld["num"] += exd["num"]
            cld["bytes"] += exd["bytes"]

    def dumpClsDicts(self):
        lgg.info(f"  dumpClsDicts",lgg.cP)  
        nfiles = 0
        nbytes = 0        
        for clskey in self.clsDicts.keys():
            cld = self.clsDicts[clskey]
            nfilescls = cld["num"]
            nbytescls = cld["bytes"]
            nfiles += nfilescls
            nbytes += nbytescls
            mbytes = round(nbytescls/1e6,3)
            lgg.info(f"  {clskey:>6} - num:{nfilescls:>4}    tot-mb:{mbytes:>6}",lgg.cG)            
        mbytes = round(nbytes / 1e6,3)
        lgg.info(f"totals - files{nfiles} bytes:{nbytes} mb:{mbytes}",lgg.cG)

    def main(self):
        sdir = self.args.sdir

        lgg.info(f"FileClassing {sdir}",lgg.cY)

        stime = timeit.time.time()
        self.buildExtDicts(sdir)
        self.dumpExtDicts()
        self.buildClsDicts()
        self.dumpClsDicts()

        # (ovfiles,ovbytes) = copyFromTo(sdir,ddir,execute)
        elap = timeit.time.time()-stime 

        #exword = "" if execute else "Would have "
        #lgg.info(f"{exword} Overwritten files:{ovfiles}/{tfiles}  overwritenbytes:{ovbytes} secs:{round(elap,3)} ",lgg.cY)
        lgg.info(f"file class done - secs:{round(elap,3)} ",lgg.cY)

if __name__ == "__main__":
    fc = FileClass()
    fc.main()
