#!/usr/bin/env python
# -*-encoding: utf-8 -*-

import  os
import time

cur_time = time.time()
st = cur_time - cur_time%86400 + time.timezone

dir_path = "/data/backup"

#删除
def drop_file(file_dir):
    for filename in os.listdir(file_dir):
        if os.path.isfile(file_dir + "/" +filename):
            ft = os.stat(file_dir + "/" +filename)
            lt = int(ft.st_mtime)
            nt = cur_time - 3600*2
            dt = st - 86400*2
            
            #delete  file  by hour in today
            if st < lt < nt:
                try:
                    os.remove(file_dir + "/" + filename)
                    time.sleep(3)
                    print ("Deleted success" + file_dir + "/" + filename)
                except (SyntaxError,IOError) as e:
                    print (e)
            #delete file by day
            if lt < dt:
                try:
                    os.remove(file_dir + "/" + filename)
                    time.sleep(3)
                    print ("Deleted success" + file_dir + "/" + filename)
                except (SyntaxError,IOError) as e:
                    print (e)
if __name__ == '__main__':
   
    drop_file(dir_path)
    
