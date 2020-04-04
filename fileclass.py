import os
import shutil
import argparse
import lgger as lgg
import timeit

parser = argparse.ArgumentParser(description='fileclass --sdir gitrepo')
parser.add_argument('--sdir', type=str, default=".",   help='source directory',required=False)

args = parser.parse_args()


def get_files(base_dir):
    for entry in os.scandir(base_dir):
        if entry.is_file():
            yield entry
        elif entry.is_dir():
            yield from get_files(entry.path)
        else:
            print(f"Neither a file, nor a dir: {entry.path}")

def buildExtDicts(sdir):
    dicts = {}
    for entry in get_files(sdir):
        if entry.is_dir():
            print(f"dir:{entry.path}")
        elif entry.is_file():
            print(f"file:{entry.path}")
           
    return 

sdir = args.sdir

lgg.info(f"FileClassing {sdir}",lgg.cY)

start = timeit.timeit()
buildExtDicts(sdir)
# (ovfiles,ovbytes) = copyFromTo(sdir,ddir,execute)
elap = timeit.timeit()-start 

#exword = "" if execute else "Would have "
#lgg.info(f"{exword} Overwritten files:{ovfiles}/{tfiles}  overwritenbytes:{ovbytes} secs:{round(elap,3)} ",lgg.cY)
lgg.info(f"file class done - secs:{round(elap,3)} ",lgg.cY)