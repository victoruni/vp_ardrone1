#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Запуск программы julius (распознование речи) 
# входящие данные - микрофон
# перенаправление вывода результатов в скрипт ros_ardrone1_julius_to_text.py
#

import roslib; roslib.load_manifest('vp_ardrone1') 
import rospy
from std_msgs.msg import String
import os
import subprocess

def run():
  rospy.set_param("ardrone1_name",1);
  rospy.set_param("ardrone1_do",[0,0]);
  rospy.set_param("ardrone1_digit",[[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]]);
   
  while not rospy.is_shutdown():
     a = os.system('padsp julius -quiet -input mic -C julian.jconf 2>/dev/null | ./ros_ardrone1_julius_to_text.py')
     rospy.sleep(1.0)

if __name__ == '__main__':
       try:
           run()
       except rospy.ROSInterruptException: pass
       except KeyboardInterrupt:
		sys.exit(1)
   

