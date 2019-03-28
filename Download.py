
from queue import Queue
import os

import time
import threading
import urllib.request
import urllib.error
import datetime
import sys

dirname = os.getcwd()
print_lock = threading.Lock()
data_q = Queue()
SAVELINK = False
DEBUG = False

def saveImg(url,dir):
        imgName = url.split('/')[-1]
        #dir = dirname+"\\"+groupdir[imgData.groupid]
        print("downloading:"+imgName)
        try:
            headers = {
                "User-Agent": "Firefox/47.0",
            }
            request = urllib.request.Request(url=url, headers=headers)
            response = urllib.request.urlopen(request)
            img = response.read()

            if(os.path.isfile(dir + "\\" + ) == False):
                with open(dir+"\\"+,'wb') as file:
                    file.write(img)
            else:
                pass
            return True
        except OSError as err:
            print("not exist!")
            with open(dir+.txt","a",encoding='utf-8') as errfile:
                errstr = "error:"+ url +" not exist\n"
                if(DEBUG):
                    errstr += "  err " + str(format(err)) + "\n"
                errfile.write(errstr)
            pass
            return False

def main():
    print("hello")


if __name__ == '__main__':
  main()
  os.system("pause")

