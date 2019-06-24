#!/usr/bin/env python
# -*-encoding: utf-8 -*-

import  os
import time

cur_time = time.time()
#获取当天零点的时间戳
st = cur_time - cur_time%86400 + time.timezone

dir_path = "/data/backup"

#删除
def drop_file(file_dir):
    for filename in os.listdir(file_dir):
        if os.path.isfile(file_dir + "/" +filename):
            ft = os.stat(file_dir + "/" +filename)
            lt = int(ft.st_mtime)
            nt = cur_time - 3600*2 #获取当天保留截止的时间戳
            dt = st - 86400*5      #获取保留天数的时间戳
            
            #delete  file  by hour in today
            if st < lt < nt:
                try:
                    os.remove(file_dir + "/" + filename)
                    os.removedirs(file_dir + "/" + filename)
                    time.sleep(3)
                    print ("Deleted success" + file_dir + "/" + filename)
                except (SyntaxError,IOError) as e:
                    print (e)
            #delete file by day
            elif lt < dt:
                try:
                    os.remove(file_dir + "/" + filename)
                    os.removedirs(file_dir + "/" + filename)
                    time.sleep(3)
                    print ("Deleted success" + file_dir + "/" + filename)
                except (SyntaxError,IOError) as e:
                    print (e)
if __name__ == '__main__':
   
    drop_file(dir_path)
    
