
#coding:utf-8  
      
from wxpy import *  
      
bot = Bot()   
#扫二维码登录微信       
friend = bot.friends().search(u'幸运的北极熊')[0]       
friend.send(u"你好！!")  
      
#查到好好友列表的某个好友并向他发送消息       
print "end"  

@bot.register()  
def reply_msg(msg):  
    msg.reply(u'你好！!')  
embed()  