#!/usr/bin/env python

import time
from subprocess import call

go_time = time.strftime("%Y-%m-%d_%H")

dir_path = "/data/backup"

def db_backup(user,pwd,host,db):
    
    call("/data/mongodb/bin/mongodump -u {} -p {} -h {} -d {} --excludCollection=likereviews --gzip --archive={}/faster-without-likereviews{}.gz".format(user,pwd,host,db,dir_path,go_time), shell=True)
    call("/data/mongodb/bin/mongodump -u {} -p {} -h {} -d {} -c likereviews -o {}/likereviews-{}".format(user,pwd,host,db,dir_path,go_time), shell=True)

if __name__ == '__main__':
    
    db_backup("root","dxhy","10.10.8.12:27017","faster")
