
#coding:utf-8  
      
from wxpy import *  

import cv2  
import os
def face(name):  
    print '正在处理'  
  
    face_cascade = cv2.CascadeClassifier('/home/wlw/learn_project/haarcascade_frontalface_alt.xml')  
    count = 0  
    img = cv2.imread(name)  
    print name
    
    try: 
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)  
        for (x,y,w,h) in faces:  
            count+=1  
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),4)  
            font = cv2.FONT_HERSHEY_SIMPLEX  
  
            roi_gray = gray[y:y+h/2, x:x+w]  
            roi_color = img[y:y+h/2, x:x+w]  
  
  
        cv2.imwrite("face_detected_1.jpg", img)     #保存已经生成好的图片  
        print count  
        return count  
    except:
        print "图片非法"              


#face("/home/wlw/learn_project/180523-160456.gif")   
bot = Bot()   
#扫二维码登录微信       
friend = bot.friends().search(u'幸运的北极熊')[0]       
friend.send(u"你好！!")  
friend.send(u"给我发带人脸的表情包！")
      
# #查到好好友列表的某个好友并向他发送消息       
# print "end"  

# @bot.register()  
# def reply_msg(msg):  
#     msg.reply(u'你好！!')  
# embed()  



@bot.register(Friend,PICTURE)  
def face_msg(msg):  
    image_name = msg.file_name  
    friend = msg.chat  
    print msg.chat  
    print '接收图片'  
    # face(image_name)  
    msg.get_file('' + msg.file_name)  
    count = face(image_name) 
    try: 
        if count==0:  
            msg.reply(u'未检测到人脸')  
        else:  
            msg.reply_image("face_detected_1.jpg")  
            msg.reply(u"检测到%d张人脸"%count)  
        os.remove(image_name)  
        os.remove("face_detected_1.jpg")
    except:
          msg.reply(u"图片非法，无法检测")
      
embed()