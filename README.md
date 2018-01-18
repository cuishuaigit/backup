# backup
This script for mongodb  backup and delete old file.

you can modify the time  "nt" and "dt" to  your platform so that you can use yourself policy to ensure how long time the file to state on.

you can use jenkins pipeline make a plan to run this script.

1、create a pipeline task in jenkins

pipeline{
   agent{ label 'db1'}
   stages{
      stage('drop old file'){
         steps{
	   dir('/data/scripts'){
	     sh 'python rm_backup.py'
	   }
	 }
      }
   }
}


2、you must create a schedule
 
 Build periodically
 50  23  *  *  *


