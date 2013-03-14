#!/usr/bin/env python
#-*-coding:utf-8 -*-

# 
#  Слушатель ros_ardrone1_sub_voice
#  чтение сообщений из темы ardrone1_textspeech (строка голосовой команды)
#  и отправка команд и установка параметров
#  для управления ardrone 2.0
#


import roslib; roslib.load_manifest('vp_ardrone1')
import rospy
import subprocess
import shlex

from ardrone_autonomy.msg import *
from ardrone_autonomy.srv import *
from std_msgs.msg import String
from std_msgs.msg import Empty
from geometry_msgs.msg import Twist

arr_commands=[["DRONE","ROBERT"],
              ["HI","BUY","THANKS"],
              ["ON","OFF","FORWARD","BACK","LEFT","RIGHT","TURN","UP","DOWN","HANG","BASE"],
              ["ZERO","ONE","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE"],
              ["FAST","SLOW"]]
ok_=["11000","01000",
     "10100","10110","10101",
     "10101","10001"]              

def controller(data):

    if(data.data>0):
      str = data.data
    arr_str=str.split();
    # разбор предложения
    str1="";str2="";
    for ind,frazes in enumerate(arr_commands):
      for fraza in frazes:
        if result.count(element)>0:
          pub.publish(element)
          index=ind+1
 

     if(str ==" "):  # взлет
       pub1=rospy.Publisher('ardrone/takeoff', Empty)
       pub1.publish()
       # параметры
     elif(str ==" "):  # посадка
       pub2=rospy.Publisher('ardrone/land', Empty)
       pub2.publish()
     elif(str ==" "):  # посадка
       pub3=rospy.Publisher('ardrone/cmd_vel', Twist)
       pub3.publish()




    print str
    rospy.loginfo(str)
    pub.publish(String(cmd))
      pub.publish(String(str))
      if index==1:    # взлет
       pub1.publish()
      elif index==2:    # посадка
       pub2.publish()
      elif index==3:    # стоять
       twist.linear.x=0.
       twist.linear.y=0.
       twist.linear.z=0.
       twist.angular.z=0.
       rospy.set_param("vp_ardrone_geometry",[0.,0.,0.,0.,0.,0.])
       pub3.publish(twist)
      elif index==4:    # назад
       pserv=rospy.get_param("vp_ardrone_geometry")
       twist.linear.x=max(min(pserv[0],0.)-0.2,-1.)
       pserv[0]=twist.linear.x
       rospy.set_param("vp_ardrone_geometry",pserv)
       pub3.publish(twist)
      elif index==5:    # вперед
       pserv=rospy.get_param("vp_ardrone_geometry")
       twist.linear.x=min(max(pserv[0],0.)+0.2,1.)
       pserv[0]=twist.linear.x
       rospy.set_param("vp_ardrone_geometry",pserv)
       pub3.publish(twist)
      elif index==6:    # влево
       pserv=rospy.get_param("vp_ardrone_geometry")
       twist.linear.y=min(max(pserv[1],0.)+0.2,1.)
       pserv[1]=twist.linear.y
       rospy.set_param("vp_ardrone_geometry",pserv)
       pub3.publish(twist)
      elif index==7:    # вправо
       pserv=rospy.get_param("vp_ardrone_geometry")
       twist.linear.y=max(min(pserv[1],0.)-0.2,-1.)
       pserv[1]=twist.linear.y
       rospy.set_param("vp_ardrone_geometry",pserv)
       pub3.publish(twist)
      elif index==8:    # вверх
       pserv=rospy.get_param("vp_ardrone_geometry")
       twist.linear.z=min(max(pserv[2],0.)+0.2,1.)
       pserv[2]=twist.linear.z
       rospy.set_param("vp_ardrone_geometry",pserv)
       pub3.publish(twist)
      elif index==9:    # вниз
       pserv=rospy.get_param("vp_ardrone_geometry")
       twist.linear.z=max(min(pserv[2],0.)-0.2,-1.)
       pserv[2]=twist.linear.z
       rospy.set_param("vp_ardrone_geometry",pserv)
       pub3.publish(twist)
      elif index==10:    # кружиться влево
       pserv=rospy.get_param("vp_ardrone_geometry")
       twist.angular.z=max(min(pserv[5],0.)-0.2,-1.)
       pserv[5]=twist.angular.z
       rospy.set_param("vp_ardrone_geometry",pserv)
       pub3.publish(twist)
      elif index==11:    # кружиться вправо
       pserv=rospy.get_param("vp_ardrone_geometry")
       twist.angular.z=min(max(pserv[5],0.)+0.2,1.)
       pserv[5]=twist.angular.z
       rospy.set_param("vp_ardrone_geometry",pserv)
       pub3.publish(twist)
      elif index==12:    # быстрее
       pserv=rospy.get_param("vp_ardrone_geometry")
       if pserv[0]>0:
         twist.linear.x=min(pserv[0]+0.2,1.)
       elif pserv[0]<0:
         twist.linear.x=max(pserv[0]-0.2,-1.)
       else:
         pass
       if pserv[1]>0:
         twist.linear.y=min(pserv[1]+0.2,1.)
       elif pserv[1]<0:
         twist.linear.y=max(pserv[1]-0.2,-1.)
       else:
         pass
       if pserv[2]>0:
         twist.linear.z=min(pserv[2]+0.2,1.)
       elif pserv[2]<0:
         twist.linear.z=max(pserv[2]-0.2,-1.)
       else:
         pass
       if pserv[5]>0:
         twist.angular.z=min(pserv[5]+0.2,1.)
       elif pserv[5]<0:
         twist.angular.z=max(pserv[5]-0.2,-1.)
       else:
         pass
       pserv[0]=twist.linear.x
       pserv[1]=twist.linear.y
       pserv[2]=twist.linear.z
       pserv[5]=twist.angular.z
       rospy.set_param("vp_ardrone_geometry",pserv)
       pub3.publish(twist)
      elif index==13:    # медленнее
       pserv=rospy.get_param("vp_ardrone_geometry")
       if pserv[0]>0:
         twist.linear.x=pserv[0]-0.2
       elif pserv[0]<0:
         twist.linear.x=pserv[0]+0.2
       else:
         pass
       if pserv[1]>0:
         twist.linear.y=pserv[1]-0.2
       elif pserv[1]<0:
         twist.linear.y=pserv[1]+0.2
       else:
         pass
       if pserv[2]>0:
         twist.linear.z=pserv[2]-0.2
       elif pserv[2]<0:
         twist.linear.z=pserv[2]+0.2
       else:
         pass
       if pserv[5]>0:
         twist.angular.z=pserv[5]-0.2
       elif pserv[5]<0:
         twist.angular.z=pserv[5]+0.2
       else:
         pass
       pserv[0]=twist.linear.x
       pserv[1]=twist.linear.y
       pserv[2]=twist.linear.z
       pserv[5]=twist.angular.z
       rospy.set_param("vp_ardrone_geometry",pserv)
       pub3.publish(twist)
      else:
        print "no!!!"
      
def listener():
   pub = rospy.Publisher('ardrone1_move', String)
   rospy.init_node('ros_ardrone1_sub_voice')
   sub = rospy.Subscriber("ardrone1_textspeech",String,controller)
   rospy.spin()
 
if __name__ == '__main__':
   listener()
   
