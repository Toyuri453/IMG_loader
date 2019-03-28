
from queue import Queue
import os

import time
import threading
import urllib.request
import urllib.error
import datetime
import sys
sys.path.append(".")


dirname = os.getcwd()
print_lock = threading.Lock()
data_q = Queue()
SAVELINK = False
DEBUG = True

MaxThread = 40

def mkdir(path):
    tmppath = os.getcwd()+"\\"+path
    try:
        os.makedirs(tmppath)

    except:
        pass
    return tmppath

def main():
    #socket.setdefaulttimeout(10)
    if(sys.version_info.major != 3):
        print("This script only works for python3")
        return

    start = time.time()
    try:
        print("download chara")
        charadl.main()
    except:
        pass

    try:
        print("download background")
        bgdl.main()
    except:
        pass

    try:
        print("download class/job")
        classdl.main()
    except:
        pass

    try:
        print("download summon stone")
        summondl.main()
    except:
        pass

    try:
        print("download weapon")
        weapondl.main()
    except:
        pass

    print("entire job took:", time.time()-start)



if __name__ == '__main__':
  main()
  os.system("pause")

