from GENERATOR import *
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
from gtts import gTTS
from googletrans import Translator
from multiprocessing import Pool, Process
from ffmpy import FFmpeg
import time, random, asyncio, timeit, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, urllib, urllib.parse, ast, pytz, wikipedia, pafy, youtube_dl, atexit

print ("\n\n ---  WELCOME TO RFU SEKAWAN  ---\n")

#cl = RIDEN()
cl = RIDEN(authTokenRFU="")
cl.log("YOUR TOKEN : {}".format(str(cl.authToken)))
channel = RIDENChannel(cl,cl.server.CHANNEL_ID['LINE_TIMELINE'])
cl.log("CHANNEL TOKEN : " + str(channel.getChannelResult()))

#riden1 = RIDEN()
#riden1 = RIDEN(authTokenRFU="")
#riden1.log("YOUR TOKEN : {}".format(str(riden1.authToken)))
#channel = RIDENChannel(riden1,riden1.server.CHANNEL_ID['LINE_TIMELINE'])
#riden1.log("CHANNEL TOKEN : " + str(channel.getChannelResult()))

#riden2 = RIDEN()
#riden2 = RIDEN(authTokenRFU="")
#riden2.log("YOUR TOKEN : {}".format(str(riden2.authToken)))
#channel = RIDENChannel(riden2,riden2.server.CHANNEL_ID['LINE_TIMELINE'])
#riden2.log("CHANNEL TOKEN : " + str(channel.getChannelResult()))

#riden3 = RIDEN()
#riden3 = RIDEN(authTokenRFU="")
#riden3.log("YOUR TOKEN : {}".format(str(riden3.authToken)))
#channel = RIDENChannel(riden3,riden3.server.CHANNEL_ID['LINE_TIMELINE'])
#riden3.log("CHANNEL TOKEN : " + str(channel.getChannelResult()))

#riden4 = RIDEN()
#riden4 = RIDEN(authTokenRFU="")
#riden4.log("YOUR TOKEN : {}".format(str(riden4.authToken)))
#channel = RIDENChannel(riden4,riden4.server.CHANNEL_ID['LINE_TIMELINE'])
#riden4.log("CHANNEL TOKEN : " + str(channel.getChannelResult()))

#riden5 = RIDEN()
#riden5 = RIDEN(authTokenRFU="")
#riden5.log("YOUR TOKEN : {}".format(str(riden5.authToken)))
#channel = RIDENChannel(riden5,riden5.server.CHANNEL_ID['LINE_TIMELINE'])
#riden5.log("CHANNEL TOKEN : " + str(channel.getChannelResult()))








print ("LOGIN SUCCESS RFU")

clProfile = cl.getProfile()
clSettings = cl.getSettings()
RIDEN = RIDENPoll(cl)

Rfu = [cl]
mid = cl.profile.mid
#JSMID1 = riden1.profile.mid
#JSMID2 = riden2.profile.mid
#JSMID3 = riden3.profile.mid
#JSMID4 = riden4.profile.mid
#JSMID5 = riden5.profile.mid
RfuBot=[mid]
Owner=["u26972c2269790de24fb84d70ffc5ab5a","ubd78f3da598d3c32e075e062e88545ec","ucfcc82770cad3aa009cae7ee481694a3","u618e665a49782092b069e137b6805a13","uefa598a4ced54efbc01e8c5e14cb4b31","ue481781d7679bbc2c64443e2786cacf7","u5e70a42cadedfb605b0cf402702d9f58"]
RfuSekawan = RfuBot + Rfu + Owner

contact = cl.getProfile()
backup = cl.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

Squad = {
    "UnsendPesan":False,
    "SpamInvite":False,
    "Contact":False,
    "GName":"",
    "AutoRespon":False,
    "KickRespon":False,
    "KillOn":False,
    "KickOn":False,
    "Upfoto":False,
    "UpfotoBot":False,
    "UpfotoGroup":False,
    "Steal":False,
    "Invite":False,
    "Copy":False,
    "autoAdd":True,
    "PesanAdd":"SELFBOT BY.SAI",
    "ContactAdd":{},
    "autoBlock":False,
    "autoJoin":True,
    "AutojoinTicket":False,
    "AutoReject":False,
    "autoRead":False,
    "IDSticker":False,
    "Timeline":False,
    "Welcome":False,
    "BackupBot":True,
    "WcText": "",
    "Leave":False,
    "WvText": "",
    "Mic":False,
    "MicDel":False,
    "Adminadd":False,
    "AdminDel":False,
    "Gift":False,
    "readMember":{},
    "readPoint":{},
    "readTime":{},
    "ROM":{},
    "Blacklist":{},
    "Ban":False,
    "Unban":False,
    "AddMention":True,
    "Admin": {
        "ubd78f3da598d3c32e075e062e88545ec":True,  #TARO MID ADMIN NYA DISINI
        "u26972c2269790de24fb84d70ffc5ab5a":True
    },
}

Mozilla = {
    "userAgent": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0"
    ],
    "mimic": {
        "copy": False,
        "conpp": False,
        "status": False,
        "target": {}
    }
}

setTime = {}
setTime = Squad['readTime']
mulai = time.time() 
msg_dict = {}

ProfileMe = {
    "displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}
ProfileMe["displayName"] = clProfile.displayName
ProfileMe["statusMessage"] = clProfile.statusMessage
ProfileMe["pictureStatus"] = clProfile.pictureStatus

RfuProtect = {
    'protect':True,
    'linkprotect':True,
    'inviteprotect':True,
    'cancelprotect':True,
    'ProtectCancelled':True,
}

RfuCctv={
    "Point1":{},
    "Point2":{},
    "Point3":{},
    "Point4":{},
    "Point5":{}
}

Help ="""
       SELFBOT BY.SAI

me  คอนแท็คบอท
clone @  ก็อปปี้
comeback   คืนร่าง
Kickall   สั่งลบห้อง
responsename   เช้คบอท
leaveall grup   ออกทุกห้อง
Spam on    เปิดระบบรันข้อความ
Contact ban   เช็คแบน แบบคอนแทค
gcreator   เช็คแอดจิงและสำรองของห้อง
invite gcreator   เชิญแอดห้องเข้า
Cekmid:    เช็คmid
Memberlist   รายชื่อสมาชิก
Blocklist   รายชื่อบล้อค
Friendlist mid   midเพิ่อน
Grup id  เช็คไอดีห้อง
mid @  เอาmidเพื่อน
lurking reset   รีรายชื่อ
lurking read    รายชื่ออ่าน
/ti/g/   ตั๋วเชิญ
runtime   เช้คเวลาการล็อคอิน
remove pesan   ลบข้อความ
restart   รีบูทระบบ
kick @   สั่งเตะ
my grup   เช็คชื่อกลุ่ม
rejectall grup   ปฏิเสธกลุ่มเชิญ
mimiclist   เช็ครายชื่อเลียนแบบ
my picture   เช็ครูป
my video   เช้ครูปวิดีโอ
my cover   เช็คปก
topnews  เช้คข่าว
Idline:   เปลี่ยนไอดีไลนื
kalender  ปฏิทิน


            คำสั่งคลิ้ก
guard  สั่งบอทเข้า
riden bye  สั่งบอทออก
my bot   ดูคอนแทคบอท
1grup   ดูชื่อห้องในคลิ้ก
2grup   ดูชื่อห้องในคลิ้ก
3grup   ดูชื่อห้องในคลิ้ก
4grup   ดูชื่อห้องในคลิ้ก
5grup   ดูชื่อห้องในคลิ้ก
bot logout   สั่งบอทออกจากระบบการล็อคอินเซล


    คำสั่งมัลติ
gambar:  รูป
my name  เช็คชื่อ
my bio   เช็คตัส
youtube:    ค้นหายูทูป
Broadcast: ประกาศกลุ่ม
Contactbc: ประกาศแชท
@#   สั่งแท็ก


            คำสั่งตั้งข้อความ
changewelcome:   เปลี่ยนข้อความต้อนรับ
changeleave:    เปลี่ยนข้อความออกจากแชทรวม
changename:    เปลี่ยนชื่อไลน์มีแค่คนล็อคสั่งได้
changebio:     เปลี่ยนตัสไลน์มีแค่คนล็อคสั่งได้
changenameall:      เปลี่ยนชื่อไลน์มีแค่คนล็อคสั่งได้ทั้งหมด
changebioall:      เปลี่ยนตัสไลน์มีแค่คนล็อคสั่งได้คลิ้ก


          คำสั่งของแอดมิน
adminadd @   ตั้งแอดมิน
admindell @   ลบแอนมิน
my team  เช็คแอด
Ban:on   ลงแบนคอนแทค
Unban:on   ลงขาวคอนแทค
Banlock @  บล็อค++แบน
banlist   เช็คแบน
link off   ปิดลิ้งค์
link on  เปิดลิ้งค์
gurl   ขอลิ้งค์ห้อง
status   เช็คตั้งค่า


           คำสั่งแปลภาษา
indonesian:    แปลอินโดนีเซีย
jawa:      แปลอินโดนีเซีย
english:      แปลอังกฤษ
japan:     แปลญี่ปุ่น
korea:    แปลเกาหลี
thailand:    แปลไทย
arab:    แปลอาหรับ
malaysia:   แปลมาเลเซีย
Data birth:
urban: 
Sslink: 
maps: 
cekcuaca: 
jadwalshalat:


           คำสั่งเปิดระบบต่างๆ
Allprotect on   เปิดระบบกันทั้งหมด
Allprotect off   ปิดระบบกันทั้งหมด
Backup on    เปิดการสำรองข้อมูลของบอท
Backup off    ปิดการสำรองข้อมูลบอท
Unsend on   เปิดระบบดึงข้อความยกเลิกมา
Unsend off   เปิดระบบดึงข้อความยกเลิกมา
Changepp on   ปิดระบบเช็คภาพ
Changepp off   ปิดระบบเช็คภาพ
Changeppbot on   เปิดระบบเช็คภาพคลิ้ก
Changeppbot off   ปิดระบบเช็คภาพคลิ้ก
Cfotogrup on   เปิดระบบล็อครูป
Cfotogrup off   ปิดระบบล้อครูป
Timeline on   เช็คโพสเปิด
Timeline off   เช็คโพสปิด
Autojoin on  เปิดการเข้ารวมออโต้
Autojoin off   ปิดการเข้ารวมออโต้
Autoreject on  เปิดระบบปฏิเสธกลุ่มเชิญออโต้
Autoreject off   ปิดระบบปฏิเสธกลุ่มเชิญออโต้
Admin:add-on   เปิดระบบแอดมิน
Admin:add-off   เปิดระบบแอดมิน
Gift:on   เปิดระบบส่งของขวัญ
Gift:off   ปิดระบบส่งของขวัญ
Spaminvite on   เปิดระบบรันห้อง
Spaminvite off   ปิดระบบรันห้อง
Auto jointicket on  เปิดการเข้าโดยตั๋วเชิญ
Auto jointicket off   ปิดการเข้าโดยตั๋วเชิญ
Copy on   เปิดระบบก็อปปี้
Copy off    ปิดระบบก็อปปี้
Steal on   เปิดการขโมยข้อมูล&กอปปี้
Steal off   ปิดการขโมยข้อมุล฿กอปปี้
Contact on  เปิดเช็คคอนแทค
Contact off   ปิดเช็คคอนแทค
Invite on    เปิดเชิญโดยคอนแทค
Invite off   ปิดเชิญโดยคอนแทค
kill on   สั่งเตะโดยคอนแทคเปิด
kill off    สั่งเตะโดยคอนแทคปิด
Mic:add-on    เพิ่มเลียน
Mic:del-on    ลบเลียนแบบ
mimic on   เปิดการเลียนแบบ
mimic off   ปิดการเลียนแบบ
Leave on   กันแชทรวมเปิด
Leave off   กันแชทรวมปิด
sider on   เปิดระบบอ่านออโต้
sider off   ปิดระบบอ่านออโต้
lurking on   เปิดระบบอ่าน
lurking off   ปิดระบบอ่าน
Welcome on   เปิดระบบต้อนรับ
Welcome off   ปิดระบบต้อนรับ
Kick on   เปิดระบบลบห้อง
Kick off   ปิดระบบลบห้อง
sai on  เปิดระบบหมด
sai off  ปิดระบบหมด

      Bots version Lv.2.5.2 \n Latest Update \n 26/07/2018 18:35:24

""""________________________"

#------------------------------------------------ SCRIP DEF ----------------------------------------------------------#

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours,24)
    month, days = divmod(days,30)
    year, month = divmod(month,12)
    century, year = divmod(year,100)
    return '\n%02d ศตวรรษ\n%02d ปี\n%02d เดือน\n%02d วัน\n%02d ชั่วโมง\n%02d นาที\n%02d วินาที' % (century, year, month, days, hours, mins, secs)

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def RIDEN_FAST_USER(fast):
    global time
    global ast
    global groupParam
    try:
        if fast.type == 0:
            return
        if fast.type == 5:
            if Squad["autoAdd"] == True:
                if (Squad["PesanAdd"] in [""," ","\n",None]):
                    pass
                else:
                    Squad["ContactAdd"][fast.param2] = True
                    usr = cl.getContact(op.param2)
                    cl.sendMessage(fast.param1, "สวัสดี {} " + str(Squad["PesanAdd"]).format(usr.displayName))
                    cl.sendMessage(fast.param1, None, contentMetadata={'mid':mid}, contentType=13)

        if fast.type == 5:
            if Squad['autoBlock'] == True:
                try:
                    usr = cl.getContact(op.param2)
                    cl.sendMessage(fast.param1, "Haii {} Sorry Auto Block SELFBOT BY.SAI, SELFBOT BY.SAI".format(usr.displayName))
                    cl.talk.blockContact(0, fast.param1)
                    Squad["Blacklist"][fast.param2] = True
                except Exception as e:
                	cl.log("[SEND_MESSAGE] ERROR : " + str(e))

#--------------------------------------------- PARAM SCRIP AUTO JOIN BOT & AUTO REJECT ------------------------------------------------#

        if fast.type == 13:
            if mid in fast.param3:
              if Squad['autoJoin'] == True:
                if fast.param2 in RfuSekawan and fast.param2 in Squad["Admin"]:
                    cl.acceptGroupInvitation(fast.param1)
                    print ("ANDA JOIN DI GRUP")
            if JSMID1 in fast.param3:
              if Squad['autoJoin'] == True:
                if fast.param2 in RfuSekawan and fast.param2 in Squad["Admin"]:
                    riden1.acceptGroupInvitation(fast.param1)
                    print ("BOT 1 JOIN GRUP")
            if JSMID2 in fast.param3:
              if Squad['autoJoin'] == True:
                if fast.param2 in RfuSekawan and fast.param2 in Squad["Admin"]:
                    riden2.acceptGroupInvitation(fast.param1)
                    print ("BOT 2 JOIN GRUP")
            if JSMID3 in fast.param3:
              if Squad['autoJoin'] == True:
                if fast.param2 in RfuSekawan and fast.param2 in Squad["Admin"]:
                    riden3.acceptGroupInvitation(fast.param1)
                    print ("BOT 3 JOIN GRUP")
                    pass
            if JSMID4 in fast.param3:
              if Squad['autoJoin'] == True:
                if fast.param2 in RfuSekawan and fast.param2 in Squad["Admin"]:
                    riden4.acceptGroupInvitation(fast.param1)
                    print ("BOT 4 JOIN GRUP")
            if JSMID5 in fast.param3:
              if Squad['autoJoin'] == True:
                if fast.param2 in RfuSekawan and fast.param2 in Squad["Admin"]:
                    riden5.acceptGroupInvitation(fast.param1)
                    print ("BOT 5 JOIN GRUP")
                    pass

        if fast.type == 13:
            if mid in fast.param3:
              if Squad['AutoReject'] == True:
                if fast.param2 not in RfuSekawan and fast.param2 not in Owner and fast.param2 not in Squad["Admin"]:
                    gid = cl.getGroupIdsInvited()
                    for i in gid:
                        cl.rejectGroupInvitation(i)
            if JSMID1 in fast.param3:
              if Squad["AutoReject"] == True:
                if fast.param2 not in RfuSekawan and fast.param2 not in Owner and fast.param2 not in Squad["Admin"]:
                    gid = riden1.getGroupIdsInvited()
                    for i in gid:
                        riden1.rejectGroupInvitation(i)
            if JSMID2 in fast.param3:
              if Squad["AutoReject"] == True:
                if fast.param2 not in RfuSekawan and fast.param2 not in Owner and fast.param2 not in Squad["Admin"]:
                    gid = riden2.getGroupIdsInvited()
                    for i in gid:
                        riden2.rejectGroupInvitation(i)
            if JSMID3 in fast.param3:
              if Squad["AutoReject"] == True:
                if fast.param2 not in RfuSekawan and fast.param2 not in Owner and fast.param2 not in Squad["Admin"]:
                    gid = riden3.getGroupIdsInvited()
                    for i in gid:
                        riden3.rejectGroupInvitation(i)
                        pass
            if JSMID4 in fast.param3:
              if Squad["AutoReject"] == True:
                if fast.param2 not in RfuSekawan and fast.param2 not in Owner and fast.param2 not in Squad["Admin"]:
                    gid = riden4.getGroupIdsInvited()
                    for i in gid:
                        riden2.rejectGroupInvitation(i)
            if JSMID5 in fast.param3:
              if Squad["AutoReject"] == True:
                if fast.param2 not in RfuSekawan and fast.param2 not in Owner and fast.param2 not in Squad["Admin"]:
                    gid = riden5.getGroupIdsInvited()
                    for i in gid:
                        riden3.rejectGroupInvitation(i)
                        pass

#------------------- ( 1 ) ------------------------- PEMBATAS SCRIP SIDER & WC LV ------------------------------------------------#

        elif fast.type == 55:
            try:
                if RfuCctv['Point1'][fast.param1]==True:
                    if fast.param1 in RfuCctv['Point2']:  
                        Name = cl.getContact(fast.param2).displayName
                        if Name in RfuCctv['Point3'][fast.param1]:
                            pass
                        else:
                            RfuCctv['Point3'][fast.param1] += "\n~" + Name
                            if " " in Name:
                                nick = Name.split(' ')
                                if len(nick) == 2:
                                    cl.mentionWithRFU(fast.param1,fast.param2," \n","" + "\n มีแอบอ่านออกมาเถอะ" )
                                else:
                                    cl.mentionWithRFU(fast.param1,fast.param2," \n","" + "\n มีแอบอ่านออกมาเถอะ" )
                            else:
                                cl.mentionWithRFU(fast.param1,fast.param2," \n","" + "\n มีแอบอ่านออกมาเถอะ" )
                    else:
                        pass
                else:
                    pass
            except:
                pass

        if fast.type == 55:
            try:
                if fast.param1 in Squad['readPoint']:
                    if fast.param2 in Squad['readMember'][fast.param1]:
                        pass
                    else:
                        Squad['readMember'][fast.param1] += fast.param2
                    Squad['ROM'][fast.param1][fast.param2] = fast.param2
                else:
                   pass
            except:
                pass   

        if fast.type == 17:
            if Squad["Welcome"] == True:
                if fast.param2 not in Rfu:
                    ginfo = cl.getGroup(fast.param1)
                    cl.mentionWithRFU(fast.param1,fast.param2," สวัสดี","" + "\n " + str(Squad['WcText']))
                    cl.sendMessage(fast.param1, None, contentMetadata={'mid':fast.param2}, contentType=13)
                    print ("MEMBER HAS JOIN THE GROUP")

        if fast.type == 15:
            if Squad["Leave"] == True:
                if fast.param2 not in Rfu:
                    ginfo = cl.getGroup(fast.param1)
                    cl.mentionWithRFU(fast.param1,fast.param2,"","" + "\n " + str(Squad['LvText']))
                    cl.sendMessage(fast.param1, None, contentMetadata={'mid':fast.param2}, contentType=13)
                    print ("MEMBER HAS LEFT THE GROUP")

#--------------------------------------------- PARAM SCRIP FOR BACKUP BOT ------------------------------------------------#

        if fast.type == 19:
          if Squad["BackupBot"] == True:
            if mid in fast.param3:
              if fast.param2 in RfuBot:
                if fast.param2 not in RfuSekawan and fast.param2 not in Owner and fast.param2 not in Squad["Admin"]:
                    pass
                else:
                    Squad["Blacklist"][fast.param2] = True
                    f=codecs.open('st2__b.json','w','utf-8')
                    json.dump(Squad, f, sort_keys=True, indent=4,ensure_ascii=False)
                    try:
                        riden1.findAndAddContactsByMid(fast.param3)
                        riden1.kickoutFromGroup(fast.param1,[fast.param2])
                        riden1.inviteIntoGroup(fast.param1,[fast.param3])
                        cl.acceptGroupInvitation(fast.param1)
                    except:
                        try:
                            riden2.findAndAddContactsByMid(fast.param3)
                            riden2.kickoutFromGroup(fast.param1,[fast.param2])
                            riden2.inviteIntoGroup(fast.param1,[fast.param3])
                            cl.acceptGroupInvitation(fast.param1)
                        except:
                            try:
                                riden3.findAndAddContactsByMid(fast.param3)
                                riden3.kickoutFromGroup(fast.param1,[fast.param2])
                                riden3.inviteIntoGroup(fast.param1,[fast.param3])
                                cl.acceptGroupInvitation(fast.param1)
                            except:
                                try:
                                    riden4.findAndAddContactsByMid(fast.param3)
                                    riden4.kickoutFromGroup(fast.param1,[fast.param2])
                                    riden4.inviteIntoGroup(fast.param1,[fast.param3])
                                    cl.acceptGroupInvitation(fast.param1)
                                except:
                                    try:
                                        riden5.findAndAddContactsByMid(fast.param3)
                                        riden5.kickoutFromGroup(fast.param1,[fast.param2])
                                        riden5.inviteIntoGroup(fast.param1,[fast.param3])
                                        cl.acceptGroupInvitation(fast.param1)
                                    except:
                                        try:
                                            x = riden1.getGroup(fast.param1)
                                            x.preventedJoinByTicket = False
                                            riden1.updateGroup(x)
                                            Riden = riden1.reissueGroupTicket(fast.param1)
                                            cl.acceptGroupInvitationByTicket(fast.param1,Riden)
                                            riden1.acceptGroupInvitationByTicket(fast.param1,Riden)
                                            riden2.acceptGroupInvitationByTicket(fast.param1,Riden)
                                            riden3.acceptGroupInvitationByTicket(fast.param1,Riden)
                                            riden4.acceptGroupInvitationByTicket(fast.param1,Riden)
                                            riden5.acceptGroupInvitationByTicket(fast.param1,Riden)
                                            x = cl.getGroup(fast.param1)
                                            x.preventedJoinByTicket = True
                                            cl.updateGroup(x)
                                            riden1.kickoutFromGroup(fast.param1,[fast.param2])
                                            Riden = cl.reissueGroupTicket(fast.param1)
                                        except:
                                            pass
                        return
            
            if JSMID1 in fast.param3:
              if fast.param2 in RfuBot:
                if fast.param2 not in RfuSekawan and fast.param2 not in Owner and fast.param2 not in Squad["Admin"]:
                    pass
                else:
                    Squad["Blacklist"][fast.param2] = True
                    f=codecs.open('st2__b.json','w','utf-8')
                    json.dump(Squad, f, sort_keys=True, indent=4,ensure_ascii=False)
                    try:
                        riden2.findAndAddContactsByMid(fast.param3)
                        riden2.kickoutFromGroup(fast.param1,[fast.param2])
                        riden2.inviteIntoGroup(fast.param1,[fast.param3])
                        riden1.acceptGroupInvitation(fast.param1)
                    except:
                        try:
                            riden3.findAndAddContactsByMid(fast.param3)
                            riden3.kickoutFromGroup(fast.param1,[fast.param2])
                            riden3.inviteIntoGroup(fast.param1,[fast.param3])
                            riden1.acceptGroupInvitation(fast.param1)
                        except:
                            try:
                                cl.findAndAddContactsByMid(fast.param3)
                                cl.kickoutFromGroup(fast.param1,[fast.param2])
                                cl.inviteIntoGroup(fast.param1,[fast.param3])
                                riden1.acceptGroupInvitation(fast.param1)
                            except:
                                try:
                                    x = riden2.getGroup(fast.param1)
                                    x.preventedJoinByTicket = False
                                    riden2.updateGroup(x)
                                    Riden = riden2.reissueGroupTicket(fast.param1)
                                    riden1.acceptGroupInvitationByTicket(fast.param1,Riden)
                                    x = riden1.getGroup(fast.param1)
                                    x.preventedJoinByTicket = True
                                    riden1.updateGroup(x)
                                    riden2.kickoutFromGroup(fast.param1,[fast.param2])
                                    Ticket = riden1.reissueGroupTicket(fast.param1)
                                except:
                                    pass
                return

            if JSMID2 in fast.param3:
              if fast.param2 in RfuBot:
                if fast.param2 not in RfuSekawan and fast.param2 not in Owner and fast.param2 not in Squad["Admin"]:
                    pass
                else:
                    Squad["Blacklist"][fast.param2] = True
                    f=codecs.open('st2__b.json','w','utf-8')
                    json.dump(Squad, f, sort_keys=True, indent=4,ensure_ascii=False)
                    try:
                        cl.findAndAddContactsByMid(fast.param3)
                        cl.kickoutFromGroup(fast.param1,[fast.param2])
                        cl.inviteIntoGroup(fast.param1,[fast.param3])
                        riden2.acceptGroupInvitation(fast.param1)
                    except:
                        try:
                            riden1.findAndAddContactsByMid(fast.param3)
                            riden1.kickoutFromGroup(fast.param1,[fast.param2])
                            riden1.inviteIntoGroup(fast.param1,[fast.param3])
                            riden2.acceptGroupInvitation(fast.param1)
                        except:
                            try:
                                riden3.findAndAddContactsByMid(fast.param3)
                                riden3.kickoutFromGroup(fast.param1,[fast.param2])
                                riden3.inviteIntoGroup(fast.param1,[fast.param3])
                                riden2.acceptGroupInvitation(fast.param1)
                            except:
                                try:
                                    x = cl.getGroup(fast.param1)
                                    x.preventedJoinByTicket = False
                                    cl.updateGroup(x)
                                    Riden = cl.reissueGroupTicket(fast.param1)
                                    riden2.acceptGroupInvitationByTicket(fast.param1,Riden)
                                    x = riden2.getGroup(fast.param1)
                                    x.preventedJoinByTicket = True
                                    riden2.updateGroup(x)
                                    riden3.kickoutFromGroup(fast.param1,[fast.param2])
                                    Ticket = riden2.reissueGroupTicket(fast.param1)
                                except:
                                    pass
                return

            if JSMID3 in fast.param3:
              if fast.param2 in RfuBot:
                if fast.param2 not in RfuSekawan and fast.param2 not in Owner and fast.param2 not in Squad["Admin"]:
                    pass
                else:
                    Squad["Blacklist"][fast.param2] = True
                    f=codecs.open('st2__b.json','w','utf-8')
                    json.dump(Squad, f, sort_keys=True, indent=4,ensure_ascii=False)
                    try:
                        cl.findAndAddContactsByMid(fast.param3)
                        cl.kickoutFromGroup(fast.param1,[fast.param2])
                        cl.inviteIntoGroup(fast.param1,[fast.param3])
                        riden3.acceptGroupInvitation(fast.param1)
                    except:
                        try:
                            riden1.findAndAddContactsByMid(fast.param3)
                            riden1.kickoutFromGroup(fast.param1,[fast.param2])
                            riden1.inviteIntoGroup(fast.param1,[fast.param3])
                            riden3.acceptGroupInvitation(fast.param1)
                        except:
                            try:
                                riden2.findAndAddContactsByMid(fast.param3)
                                riden2.kickoutFromGroup(fast.param1,[fast.param2])
                                riden2.inviteIntoGroup(fast.param1,[fast.param3])
                                riden3.acceptGroupInvitation(fast.param1)
                            except:
                                try:
                                    x = cl.getGroup(fast.param1)
                                    x.preventedJoinByTicket = False
                                    cl.updateGroup(x)
                                    Riden = cl.reissueGroupTicket(fast.param1)
                                    riden3.acceptGroupInvitationByTicket(fast.param1,Riden)
                                    x = riden3.getGroup(fast.param1)
                                    x.preventedJoinByTicket = True
                                    riden2.updateGroup(x)
                                    cl.kickoutFromGroup(fast.param1,[fast.param2])
                                    Ticket = riden3.reissueGroupTicket(fast.param1)
                                except:
                                    pass
                return

            if JSMID4 in fast.param3:
              if fast.param2 in RfuBot:
                if fast.param2 not in RfuSekawan and fast.param2 not in Owner and fast.param2 not in Squad["Admin"]:
                    pass
                else:
                    Squad["Blacklist"][fast.param2] = True
                    f=codecs.open('st2__b.json','w','utf-8')
                    json.dump(Squad, f, sort_keys=True, indent=4,ensure_ascii=False)
                    try:
                        cl.findAndAddContactsByMid(fast.param3)
                        cl.kickoutFromGroup(fast.param1,[fast.param2])
                        cl.inviteIntoGroup(fast.param1,[fast.param3])
                        riden3.acceptGroupInvitation(fast.param1)
                    except:
                        try:
                            riden5.findAndAddContactsByMid(fast.param3)
                            riden5.kickoutFromGroup(fast.param1,[fast.param2])
                            riden5.inviteIntoGroup(fast.param1,[fast.param3])
                            riden4.acceptGroupInvitation(fast.param1)
                        except:
                            try:
                                riden5.findAndAddContactsByMid(fast.param3)
                                riden5.kickoutFromGroup(fast.param1,[fast.param2])
                                riden5.inviteIntoGroup(fast.param1,[fast.param3])
                                riden4.acceptGroupInvitation(fast.param1)
                            except:
                                try:
                                    x = cl.getGroup(fast.param1)
                                    x.preventedJoinByTicket = False
                                    cl.updateGroup(x)
                                    Riden = cl.reissueGroupTicket(fast.param1)
                                    riden4.acceptGroupInvitationByTicket(fast.param1,Riden)
                                    x = riden4.getGroup(fast.param1)
                                    x.preventedJoinByTicket = True
                                    riden5.updateGroup(x)
                                    riden2.kickoutFromGroup(fast.param1,[fast.param2])
                                    Ticket = riden4.reissueGroupTicket(fast.param1)
                                except:
                                    pass
                return

            if JSMID5 in fast.param3:
              if fast.param2 in RfuBot:
                if fast.param2 not in RfuSekawan and fast.param2 not in Owner and fast.param2 not in Squad["Admin"]:
                    pass
                else:
                    Squad["Blacklist"][fast.param2] = True
                    f=codecs.open('st2__b.json','w','utf-8')
                    json.dump(Squad, f, sort_keys=True, indent=4,ensure_ascii=False)
                    try:
                        cl.findAndAddContactsByMid(fast.param3)
                        cl.kickoutFromGroup(fast.param1,[fast.param2])
                        cl.inviteIntoGroup(fast.param1,[fast.param3])
                        riden3.acceptGroupInvitation(fast.param1)
                    except:
                        try:
                            riden4.findAndAddContactsByMid(fast.param3)
                            riden4.kickoutFromGroup(fast.param1,[fast.param2])
                            riden4.inviteIntoGroup(fast.param1,[fast.param3])
                            riden5.acceptGroupInvitation(fast.param1)
                        except:
                            try:
                                riden4.findAndAddContactsByMid(fast.param3)
                                riden4.kickoutFromGroup(fast.param1,[fast.param2])
                                riden4.inviteIntoGroup(fast.param1,[fast.param3])
                                riden5.acceptGroupInvitation(fast.param1)
                            except:
                                try:
                                    x = cl.getGroup(fast.param1)
                                    x.preventedJoinByTicket = False
                                    cl.updateGroup(x)
                                    Riden = cl.reissueGroupTicket(fast.param1)
                                    riden5.acceptGroupInvitationByTicket(fast.param1,Riden)
                                    x = riden5.getGroup(fast.param1)
                                    x.preventedJoinByTicket = True
                                    riden4.updateGroup(x)
                                    cl.kickoutFromGroup(fast.param1,[fast.param2])
                                    Ticket = riden5.reissueGroupTicket(fast.param1)
                                except:
                                    pass
                return
        if fast.type == 13:
          if fast.param3 in Squad["Blacklist"]: # AUTO KICK JIKA YG DI BLACKLIST MASUK
            if fast.param2 not in RfuSekawan and fast.param2 not in Owner and fast.param2 not in Squad["Admin"]:
                random.choice(Rfu).cancelGroupInvitation(fast.param1,[fast.param3])
                random.choice(Rfu).kickoutFromGroup(fast.param1,[fast.param2])
                random.choice(Rfu).kickoutFromGroup(fast.param1,[fast.param3])
                G = random.choice(Rfu).getGroup(fast.param1)
                G.preventedJoinByTicket = True
                random.choice(Rfu).updateGroup(G)
                random.choice(Rfu).sendMessage(fast.param1, None, contentMetadata={'mid': fast.param2}, contentType=13)
                random.choice(Rfu).sendMessage(fast.param1, "ผู้ใช้รายนี้อยู่ในบัญชีดำ, โปรดล้างบัญชีดำก่อน\n")

#---------------------------------- SCRIP PROTECT GRUP -------------------------------------#

        if fast.type == 19:
            if fast.param2 not in RfuSekawan and fast.param2 not in Owner and fast.param2 not in Squad["Admin"]:
                if fast.param2 in RfuBot:
                    pass
                elif RfuProtect["protect"] == True:
                    random.choice(Rfu).kickoutFromGroup(fast.param1,[fast.param2])
                    cl.findAndAddContactsByMid(fast.param3)
                    cl.inviteIntoGroup(fast.param1,[fast.param3])
                    Squad["Blacklist"][fast.param2] = True
                    random.choice(Rfu).sendMessage(fast.param1, None, contentMetadata={'mid': fast.param2}, contentType=13)
                    random.choice(Rfu).sendMessage(fast.param1, "guard")

        if fast.type == 11:
            if fast.param2 not in RfuSekawan and fast.param2 not in Owner and fast.param2 not in Squad["Admin"]:
                if fast.param2 in RfuBot:
                    pass
                elif RfuProtect["linkprotect"] == True:
                    Squad["Blacklist"][fast.param2] = True
                    G = random.choice(Rfu).getGroup(fast.param1)
                    G.preventedJoinByTicket = True
                    random.choice(Rfu).updateGroup(G)
                    random.choice(Rfu).kickoutFromGroup(fast.param1,[fast.param2])
                    Squad["Blacklist"][fast.param2] = True

        if fast.type == 13:
          if fast.param2 not in RfuSekawan and fast.param2 not in Owner and fast.param2 not in Squad["Admin"]:
            if fast.param2 in RfuBot:
                pass
            elif RfuProtect["inviteprotect"] == True:
                Squad["Blacklist"][fast.param2] = True
                random.choice(Rfu).cancelGroupInvitation(fast.param1,[fast.param3])
                random.choice(Rfu).kickoutFromGroup(fast.param1,[fast.param2])
                random.choice(Rfu).kickoutFromGroup(fast.param1,[fast.param3])
                random.choice(Rfu).sendMessage(fast.param1, None, contentMetadata={'mid': fast.param2}, contentType=13)
                random.choice(Rfu).sendMessage(fast.param1, "ระบบป้องกันการเชิญสมาชิก \n คอนแทตต่อไปนี้ ติดบัญชีดำของระบบบอท (*-_-)/")
                G = random.choice(Rfu).getGroup(fast.param1)
                G.preventedJoinByTicket = True
                random.choice(Rfu).updateGroup(G)
                if fast.param2 not in RfuSekawan and fast.param2 not in Owner and fast.param2 not in Squad["Admin"]:
                    if fast.param2 in RfuBot:
                        pass
                    elif RfuProtect["inviteprotect"] == True:
                        Squad["Blacklist"][fast.param2] = True
                        random.choice(Rfu).cancelGroupInvitation(fast.param1,[fast.param3])
                        random.choice(Rfu).kickoutFromGroup(fast.param1,[fast.param2])
                        random.choice(Rfu).kickoutFromGroup(fast.param1,[fast.param3])
                        random.choice(Rfu).sendMessage(fast.param1, None, contentMetadata={'mid': fast.param2}, contentType=13)
                        random.choice(Rfu).sendMessage(fast.param1, "ระบบป้องกันการเชิญสมาชิก \n คอนแทตต่อไปนี้ ติดบัญชีดำของระบบบอท (*-_-)/")
                        G = random.choice(Rfu).getGroup(fast.param1)
                        G.preventedJoinByTicket = True
                        random.choice(Rfu).updateGroup(G)
                        if fast.param2 not in RfuSekawan and fast.param2 not in Owner and fast.param2 not in Squad["Admin"]:
                            if fast.param2 in RfuBot:
                                pass
                            elif RfuProtect["cancelprotect"] == True:
                                Squad["Blacklist"][fast.param2] = True
                                random.choice(Rfu).cancelGroupInvitation(fast.param1,[fast.param3])
                                random.choice(Rfu).kickoutFromGroup(fast.param1,[fast.param3])
                                random.choice(Rfu).sendMessage(fast.param1, None, contentMetadata={'mid': fast.param2}, contentType=13)
                                random.choice(Rfu).sendMessage(fast.param1, "ระบบป้องกันการยกเลิกสมาชิก \n คอนแทตต่อไปนี้ ติดบัญชีดำของระบบบอท (*-_-)/")
                                G = random.choice(Rfu).getGroup(fast.param1)
                                G.preventedJoinByTicket = True
                                random.choice(Rfu).updateGroup(G)

        if fast.type == 32:
            if fast.param2 not in RfuSekawan and fast.param2 not in Owner and fast.param2 not in Squad["Admin"]:
                if fast.param2 in RfuBot:
                    pass
                elif RfuProtect["ProtectCancelled"] == True:
                    random.choice(Rfu).kickoutFromGroup(fast.param1,[fast.param2])
                    cl.findAndAddContactsByMid(fast.param3)
                    cl.inviteIntoGroup(fast.param1,[fast.param3])
                    Squad["Blacklist"][fast.param2] = True
                    random.choice(Rfu).sendMessage(fast.param1, None, contentMetadata={'mid': fast.param2}, contentType=13)
                    random.choice(Rfu).sendMessage(fast.param1, "ระบบป้องกันการยกเลิกสมาชิก \n คอนแทตต่อไปนี้ ติดบัญชีดำของระบบบอท (*-_-)/")

        if fast.type == 19:
            if fast.param3 in Squad["Admin"]:        # JIKA ADMIN KE KICK
              if fast.param2 not in RfuSekawan and fast.param2 not in Owner and fast.param2 not in Squad["Admin"]:
                  random.choice(Rfu).kickoutFromGroup(fast.param1,[fast.param2])
                  riden1.findAndAddContactsByMid(fast.param3)
                  riden1.inviteIntoGroup(fast.param1,[fast.param3])
                  G = random.choice(Rfu).getGroup(fast.param1)
                  G.preventedJoinByTicket = True
                  random.choice(Rfu).updateGroup(G)
                  Squad["Blacklist"][fast.param2] = True
                  riden1.sendMessage(fast.param1, None, contentMetadata={'mid': fast.param2}, contentType=13)
                  riden1.sendMessage(fast.param1, "คอนแทคต่อไปนี้ติดบัญชีดำของระบบบอท (*-_-)/")

        if fast.type == 13:
          if fast.param2 and fast.param3 in Squad["Blacklist"]: # AUTO KICK JIKA YG DI BLACKLIST MASUK
            if fast.param2 not in RfuSekawan and fast.param2 not in Owner and fast.param2 not in Squad["Admin"]:
                random.choice(Rfu).cancelGroupInvitation(fast.param1,[fast.param3])
                random.choice(Rfu).kickoutFromGroup(fast.param1,[fast.param2])
                random.choice(Rfu).kickoutFromGroup(fast.param1,[fast.param3])
                G = random.choice(Rfu).getGroup(fast.param1)
                G.preventedJoinByTicket = True
                random.choice(Rfu).updateGroup(G)
                random.choice(Rfu).sendMessage(fast.param1, None, contentMetadata={'mid': fast.param2}, contentType=13)
                random.choice(Rfu).sendMessage(fast.param1, "User Added Blacklist, Please to Unfollow blacklist first.\n")

        if fast.type == 17:
          if fast.param2 not in RfuSekawan and fast.param2 not in Owner and fast.param2 not in Squad["Admin"]:
            if fast.param2 in Squad["Blacklist"]: # AUTO KICK JIKA YG DI BLACKLIST MASUK
                random.choice(Rfu).kickoutFromGroup(fast.param1,[fast.param2])
                G = random.choice(Rfu).getGroup(fast.param1)
                G.preventedJoinByTicket = True
                random.choice(Rfu).updateGroup(G)
                Squad["Blacklist"][op.param2] = True
                random.choice(Rfu).sendMessage(fast.param1, None, contentMetadata={'mid': fast.param2}, contentType=13)
                random.choice(Rfu).sendMessage(fast.param1, "User Added Blacklist, Please to Unfollow blacklist first.\n")

        if fast.type == 55:
          if fast.param2 not in RfuSekawan and fast.param2 not in Owner and fast.param2 not in Squad["Admin"]:
            if fast.param2 in Squad["Blacklist"]: # AUTO KICK JIKA YG DI BLACKLIST MASUK
                random.choice(Rfu).kickoutFromGroup(fast.param1,[fast.param2])
                G = random.choice(Rfu).getGroup(fast.param1)
                G.preventedJoinByTicket = True
                random.choice(Rfu).updateGroup(G)
                Squad["Blacklist"][op.param2] = True
                random.choice(Rfu).sendMessage(fast.param1, None, contentMetadata={'mid': fast.param2}, contentType=13)
                random.choice(Rfu).sendMessage(fast.param1, "User Added Blacklist, Please to Unfollow blacklist first.\n")

        if fast.type == 46:
            if fast.param2 in RfuBot:
                cl.removeAllMessages()
                riden1.removeAllMessages()
                riden2.removeAllMessages()
                riden3.removeAllMessages()
                riden4.removeAllMessages()
                riden5.removeAllMessages()

#------------------- ( 2 ) ------------------------- PEMBATAS SCRIP ------------------------------------------------#

        if fast.type == 26:
            msg = fast.message
            text = msg.text
            rfuText = msg.text
            msg_id = msg.id
            kirim = msg.to           
            user = msg._from
            if msg.toType == 0 or msg.toType == 2:
                if msg.toType == 0:
                    to = kirim
                elif msg.toType == 2:
                    to = kirim
                if msg.contentType == 0:
                    if Squad["autoRead"] == True:
                        cl.sendChatChecked(kirim, msg_id)
                        riden1.sendChatChecked(kirim, msg_id)
                        riden2.sendChatChecked(kirim, msg_id)
                        riden3.sendChatChecked(kirim, msg_id)
                        riden4.sendChatChecked(kirim, msg_id)
                        riden5.sendChatChecked(kirim, msg_id)
                    if kirim in Squad["readPoint"]:
                        if user not in Squad["ROM"][kirim]:
                            Squad["ROM"][kirim][user] = True
                    if user in Mozilla["mimic"]["target"] and Mozilla["mimic"]["status"] == True and Mozilla["mimic"]["target"][user] == True:
                        text = msg.text
                        if text is not None:
                            cl.sendMessage(kirim,text)
                    if Squad["UnsendPesan"] == True:
                        msg = fast.message
                        if msg.toType == 0:
                            cl.log(" {} - {} ".format(str(user), str(rfuText)))
                        else:
                            cl.log(" {} - {} ".format(str(kirim), str(rfuText)))
                            msg_dict[msg.id] = {"rider": rfuText, "pelaku": user, "createdTime": msg.createdTime, "contentType": msg.contentType, "contentMetadata": msg.contentMetadata}
                    if Squad["Timeline"] == True:
                       if msg.contentType == 16:
                            ret_ = "Info Postingan\n"
                            if msg.contentMetadata["serviceType"] == "GB":
                                contact = cl.getContact(user)
                                auth = "\n Penulis : {}".format(str(contact.displayName))
                            else:
                                auth = "\n Penulis : {}".format(str(contact.displayName))
                                ret_ += auth
                            if "stickerId" in msg.contentMetadata:
                                stck = "\n Stiker : https://line.me/R/shop/detail/{}".format(str(msg.contentMetadata["packageId"]))
                                ret_ += stck
                            if "mediaOid" in msg.contentMetadata:
                                object_ = msg.contentMetadata["mediaOid"].replace("svc=myhome|sid=h|","")
                                if msg.contentMetadata["mediaType"] == "V":
                                    if msg.contentMetadata["serviceType"] == "GB":
                                        ourl = "\n Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                        murl = "\n Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(msg.contentMetadata["mediaOid"]))
                                    else:
                                        ourl = "\n Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                        murl = "\n Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(object_))
                                    ret_ += murl
                                else:
                                    if msg.contentMetadata["serviceType"] == "GB":
                                        ourl = "\n Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                    else:
                                        ourl = "\n Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                ret_ += ourl
                            if "text" in msg.contentMetadata:
                                dia = cl.getContact(user)
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan = 'Pengirim: '
                                xteam = str(dia.displayName)
                                pesan = ''
                                pesan2 = pesan+"@ARDIAN_GANTENG\n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':dia.mid}
                                zx2.append(zx)
                                kata = "\n Tulisan : {}".format(str(msg.contentMetadata["text"]))
                                purl = "\n Post URL : {}".format(str(msg.contentMetadata["postEndUrl"]).replace("line://","https://line.me/R/"))
                                ret_ += purl
                                ret_ += kata
                                zxc += pesan2
                                pesan = xpesan + zxc + ret_ + ""
                                cl.sendMessage(kirim, pesan, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)

        if fast.type == 65:
          if Squad['UnsendPesan'] == True:
              try:
                  you = fast.param1
                  msg.id = fast.param2
                  user = msg._from
                  if msg.id in msg_dict:
                    if msg_dict[msg.id]["pelaku"]:
                        pelaku = cl.getContact(msg_dict[msg.id]["pelaku"])
                        nama = pelaku.displayName
                        dia = "Detect Pesan Terhapus\n"
                        dia += "\n1. Name : " + nama
                        dia += "\n2. Taken : {}".format(str(msg_dict[msg.id]["createdTime"]))
                        dia += "\n3. Pesannya : {}".format(str(msg_dict[msg.id]["rider"]))
                        cl.mentionWithRFU(you,user," Nah","\n\n" +str(dia))
              except:
                  cl.sendMessage(you, "Return")

        if fast.type in [25,26]:
            msg = fast.message
            user = msg._from
            kirim = msg.to
            if msg.contentType == 7:
                if Squad['IDSticker'] == True:
                    stk_id = msg.contentMetadata['STKID']
                    stk_ver = msg.contentMetadata['STKVER']
                    pkg_id = msg.contentMetadata['STKPKGID']
                    filler = "STICKER CHECKS\nSTKID : %s\nSTKPKGID : %s\nSTKVER : %s\n\nTHIS IS LINK\n\nline://shop/detail/%s" % (stk_id,pkg_id,stk_ver,pkg_id)
                    cl.mentionWithRFU(kirim,user,"My Code Sticker\n","" + "\n\n" + str(filler))
                else:
                    pass

        if fast.type == 25 or fast.type == 26:
            msg = fast.message
            user = msg._from
            kirim = msg.to
            if msg.contentType == 1:
              if Squad['Upfoto'] == True:
                if user in Owner:
                    path = cl.downloadObjectMsg(msg.id)
                    cl.updateProfilePicture(path)
                    cl.mentionWithRFU(kirim,user," Update Picture Success ","")
                    Squad['Upfoto'] = False

        if fast.type == 25 or fast.type == 26:
            msg = fast.message
            user = msg._from
            kirim = msg.to
            if msg.contentType == 1:
              if Squad['UpfotoBot'] == True:
                if user in RfuSekawan or user in Squad["Admin"]:
                    path1 = riden1.downloadObjectMsg(msg.id)
                    path2 = riden2.downloadObjectMsg(msg.id)
                    path3 = riden3.downloadObjectMsg(msg.id)
                    path4 = riden4.downloadObjectMsg(msg.id)
                    path5 = riden5.downloadObjectMsg(msg.id)
                    riden1.updateProfilePicture(path1)
                    riden2.updateProfilePicture(path2)
                    riden3.updateProfilePicture(path3)
                    riden1.mentionWithRFU(kirim,user," Update Picture Success ","")
                    riden2.mentionWithRFU(kirim,user," Update Picture Success ","")
                    riden3.mentionWithRFU(kirim,user," Update Picture Success ","")
                    riden4.mentionWithRFU(kirim,user," Update Picture Success ","")
                    riden5.mentionWithRFU(kirim,user," Update Picture Success ","")
                    Squad['UpfotoBot'] = False

        if fast.type == 25 or fast.type == 26:
            msg = fast.message
            user = msg._from
            kirim = msg.to
            if msg.contentType == 1:
              if Squad['UpfotoGroup'] == True:
                if user in RfuSekawan or user in Squad["Admin"]:
                    path = cl.downloadObjectMsg(msg.id)
                    cl.updateGroupPicture(kirim, path)
                    cl.mentionWithRFU(kirim,user," Update Picture Grup Success ","")
                    Squad['UpfotoGroup'] = False

        if fast.type in [25,26]:
          if Squad['Contact'] == True:
              msg = fast.message
              user = msg._from
              kirim = msg.to
              if msg.contentType == 13:
                if 'displayName' in msg.contentMetadata:
                    contact = cl.getContact(msg.contentMetadata["mid"])
                    try:
                        cover = cl.getProfileCoverURL(user)
                    except:
                        cover = ""
                    cl.sendMessage(kirim,"Nama:\n" + msg.contentMetadata["displayName"] + "\n\nMid:\n" + msg.contentMetadata["mid"] + "\n\nBio:\n" + contact.statusMessage + "\n\nPicture URL:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\nCover URL:\n" + str(cover))
                else:
                    contact = cl.getContact(msg.contentMetadata["mid"])
                    try:
                        cover = cl.getProfileCoverURL(user)
                    except:
                        cover = ""
                    cl.sendText(kirim,"Nama:\n" + contact.displayName + "\n\nMid:\n" + msg.contentMetadata["mid"] + "\n\nBio:\n" + contact.statusMessage + "\n\nPicture URL\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\nCover URL:\n" + str(cover))

        if fast.type == 25 or fast.type == 26:
            msg = fast.message
            user = msg._from
            kirim = msg.to
            if msg.contentType == 13:
                try:
                    if user in RfuSekawan or user in Squad["Admin"]:
                      if Squad["Ban"] == True:
                        if msg.contentMetadata["mid"] in Squad["Blacklist"]:
                            name = msg.contentMetadata["displayName"]
                            cl.sendMessage(kirim, name + str(" อยู่ในรายการบัญชีดำแล้ว"))
                            Squad['Ban'] = False
                        else:
                            Squad["Blacklist"][msg.contentMetadata["mid"]] = True
                            name = msg.contentMetadata["displayName"]
                            cl.sendMessage(kirim, name + str(" ได้เพิ่มลงบัญชีดำ"))
                            Squad['Ban'] = False
                      if Squad["Unban"] == True:
                        if msg.contentMetadata["mid"] in Squad["Blacklist"]:
                            del Squad["Blacklist"][msg.contentMetadata["mid"]]
                            name = msg.contentMetadata["displayName"]
                            cl.sendMessage(kirim, name + str(" อยู่ในรายการบัญชีขาวแล้ว"))
                            Squad['Unban'] = False
                        else:
                            name = msg.contentMetadata["displayName"]
                            cl.sendMessage(kirim, name + str(" ไม่มีอะไรในบัญชีดำ"))
                            Squad['Unban'] = False
                      if Squad["Adminadd"] == True:
                        if msg.contentMetadata["mid"] in Squad["Admin"]:
                            name = msg.contentMetadata["displayName"]
                            cl.sendMessage(kirim, name + str(" อยู่ในรายการผู้ดูแล"))
                            Squad['Adminadd'] = False
                        else:
                            Squad["Admin"][msg.contentMetadata["mid"]] = True
                            name = msg.contentMetadata["displayName"]
                            cl.sendMessage(kirim, name + str(" เพิ่มในผู้ดูแล"))
                            Squad['Adminadd'] = False
                      if Squad["AdminDel"] == True:
                        if msg.contentMetadata["mid"] in Squad["Admin"]:
                            del Squad["Admin"][msg.contentMetadata["mid"]]
                            name = msg.contentMetadata["displayName"]
                            cl.sendMessage(kirim, name + str("  ทำสำเร็จในการลบผู้ดูแลระบบ"))
                            Squad['AdminDel'] = False
                        else:
                            name = msg.contentMetadata["displayName"]
                            cl.sendMessage(kirim, name + str(" ได้ลบผู้นี้ออกจากผู้ดูแลระบบ"))
                            Squad['AdminDel'] = False
                except Exception as error:
                    cl.sendText(kirim, str(error))

        if fast.type == 25 or fast.type == 26:
          if Squad['Invite'] == True:
            msg = fast.message
            user = msg._from
            kirim = msg.to
            if msg.contentType == 13:
                if user in RfuSekawan or user in Squad["Admin"]:
                    _name = msg.contentMetadata["displayName"]
                    invite = msg.contentMetadata["mid"]
                    groups = cl.getGroup(kirim)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            cl.sendText(msg.to, _name + " อยู่ในกลุ่มนี้แล้ว")
                        else:
                            targets.append(invite)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                cl.findAndAddContactsByMid(target)
                                cl.inviteIntoGroup(kirim,[target])
                                cl.sendText(kirim,"Invite " + _name + "\nสำเร็จ")
                                Squad['Invite'] = False
                                break
                            except:             
                                 cl.sendText(kirim, 'Contact error')
                                 Squad['Invite'] = False
                                 break

        if fast.type == 25 or fast.type == 26:
          if Squad['Steal'] == True:
            msg = fast.message
            user = msg._from
            kirim = msg.to
            if msg.contentType == 13:
                if user in RfuSekawan or user in Squad["Admin"]:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = cl.getGroup(kirim)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            print ("[Target] Stealed")
                            break             
                        else:
                            targets.append(copy)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                contact = cl.getContact(target)
                                cl.sendText(kirim,"Nama :\n" + msg.contentMetadata["displayName"] + "\n\nBio :\n" + contact.statusMessage+ "\n\nMid :\n" + msg.contentMetadata["mid"] + "\n\nSteal Succes..")
                                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                cl.sendImageWithURL(kirim,image)
                                cover = cl.getProfileCoverURL(target)
                                cl.sendImageWithURL(kirim, cover)
                                Squad['Steal'] = False
                                break                     
                            except:             
                                 cl.sendText(kirim, 'Contact error')
                                 Squad['Steal'] = False
                                 break

        if fast.type == 25 or fast.type == 26:
          if Squad['KillOn'] == True:
            msg = fast.message
            user = msg._from
            kirim = msg.to
            if msg.contentType == 13:
                if user in RfuSekawan or user in Squad["Admin"]:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = cl.getGroup(kirim)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            print ("[Target] Kick Via Contact")
                            break             
                        else:
                            targets.append(copy)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            if target not in RfuSekawan:
                                try:
                                    cl.kickoutFromGroup(kirim,[target])
                                    Squad['KillOn'] = False
                                    break
                                except:             
                                     cl.sendText(kirim, 'ไม่พบเป้าหมาย')
                                     Squad['KillOn'] = False
                                     break

        if fast.type == 25 or fast.type == 26:
          if Squad['Gift'] == True:
            msg = fast.message
            user = msg._from
            kirim = msg.to
            if msg.contentType == 13:
                if user in RfuSekawan or user in Squad["Admin"]:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = cl.getGroup(kirim)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            print ("[Target] Send Gift")
                            break             
                        else:
                            targets.append(copy)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                cl.sendMessage(target, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58','PRDTYPE': 'THEME','MSGTPL': '12'}, contentType = 9)
                                riden1.sendMessage(target, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58','PRDTYPE': 'THEME','MSGTPL': '12'}, contentType = 9)
                                riden2.sendMessage(target, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58','PRDTYPE': 'THEME','MSGTPL': '12'}, contentType = 9)
                                riden3.sendMessage(target, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58','PRDTYPE': 'THEME','MSGTPL': '12'}, contentType = 9)
                                riden4.sendMessage(target, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58','PRDTYPE': 'THEME','MSGTPL': '12'}, contentType = 9)
                                riden5.sendMessage(target, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58','PRDTYPE': 'THEME','MSGTPL': '12'}, contentType = 9)
                                Squad['Gift'] = False
                                break
                            except:             
                                 cl.sendText(kirim, 'Target Error')
                                 Squad['Gift'] = False
                                 break

        if fast.type == 25 or fast.type == 26:
          if Squad["Mic"] == True:
            msg = fast.message
            user = msg._from
            kirim = msg.to
            if msg.contentType == 13:
                if user in RfuSekawan or user in Squad["Admin"]:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = cl.getGroup(kirim)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            print ("[Target] Mimic Add")
                            break             
                        else:
                            targets.append(copy)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                Mozilla["mimic"]["target"][target] = True
                                cl.sendText(kirim,"เพิ่มเป้าหมายแล้ว")
                                Squas['Mic'] = False
                                break
                            except:             
                                 cl.sendText(kirim, 'โปรดกลับมาและส่งติดต่ออีกครั้ง \ n เราจะโหลดโปรแกรมอีกครั้ง')
                                 break

        if fast.type == 25 or fast.type == 26:
          if Squad["MicDel"] == True:
            msg = fast.message
            user = msg._from
            kirim = msg.to
            if msg.contentType == 13:
                if user in RfuSekawan or user in Squad["Admin"]:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = cl.getGroup(kirim)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            print ("[Target] Mimic Add")
                            break             
                        else:
                            targets.append(copy)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                del Mozilla["mimic"]["target"][target]
                                cl.sendText(kirim,"Target is Dellete!")
                                Squad['MicDel'] = False
                                break
                            except:             
                                 cl.sendText(kirim, 'โปรดกลับมาและส่งติดต่ออีกครั้ง \ n เราจะโหลดโปรแกรมอีกครั้ง')
                                 break

        if fast.type == 25 or fast.type == 26:
          if Squad['Copy'] == True:
            msg = fast.message
            user = msg._from
            kirim = msg.to
            if msg.contentType == 13:
                if user in RfuSekawan or user in Squad["Admin"]:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = cl.getGroup(kirim)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            print ("[Target] Stealed")
                            break             
                        else:
                            targets.append(copy)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                cl.cloneContactProfile(target)
                                cl.sendText(kirim, "คัดลอกสำเร็จ")
                                Squad['Copy'] = False
                                break
                            except:             
                                 cl.sendText(kirim, "เออเล่อ")
                                 Squad['Copy'] = False
                                 break
                                 
                                 
#======= AUTO TAG & CHAT BATAS SCRIP ========
        if fast.type == 26:
            msg = fast.message
            user = msg._from
            kirim = msg.to
            if msg.contentType == 0 and user not in mid and msg.toType == 2:
                if "MENTION" in msg.contentMetadata.keys() != None:
                    if Squad['AutoRespon'] == True:
                        contact = cl.getContact(user)
                        cName = contact.displayName
                        balas = [cName + "\n" + str(Squad['MentionText'])]
                        ret_ = "" + random.choice(balas)
                        name = re.findall(r'@(\w+)', msg.text)
                        mention = ast.literal_eval(msg.contentMetadata["MENTION"])
                        mentionees = mention['MENTIONEES']
                        for mention in mentionees:
                              if mention['M'] in mid:
                                  cl.mentionWithRFU(kirim,user,"","" +str(ret_))
                                  break

        if fast.type == 26:
            msg = fast.message
            user = msg._from
            kirim = msg.to
            if msg.contentType == 0 and user not in RfuSekawan or user not in Squad["Admin"]:
                if "MENTION" in msg.contentMetadata.keys() != None:
                    if Squad['KickRespon'] == True:
                        contact = cl.getContact(user)
                        cName = contact.displayName
                        balas = [cName + "ขอบคุณที่แท็คเรียกข้า","ขอบคุณสำหรับการแท็ค"]
                        ret_ = "" + random.choice(balas)
                        name = re.findall(r'@(\w+)', msg.text)
                        mention = ast.literal_eval(msg.contentMetadata["MENTION"])
                        mentionees = mention['MENTIONEES']
                        for mention in mentionees:
                              if mention['M'] in mid:
                                  cl.mentionWithRFU(kirim,user,"","" +str(ret_))
                                  cl.kickoutFromGroup(kirim,[user])
                                  break

        if fast.type == 25 or fast.type == 26:
          if Squad['SpamInvite'] == True:
            msg = fast.message
            user = msg._from
            kirim = msg.to
            if msg.contentType == 13:
                if user in RfuSekawan or user in Squad["Admin"]:
                    korban = msg.contentMetadata["displayName"]
                    invite = msg.contentMetadata["mid"]
                    groups = cl.getGroup(kirim)
                    pending = groups.invitee
                    targets = []
                    for x in groups.members:
                        if korban in x.displayName:
                            cl.sendText(kirim, korban + " อยู่ในกลุ่มนี้แล้ว")
                        else:
                            targets.append(invite)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                cl.findAndAddContactsByMid(target)
                                riden1.findAndAddContactsByMid(target)
                                riden2.findAndAddContactsByMid(target)
                                riden3.findAndAddContactsByMid(target)
                                cl.createGroup("Fuck",[target]) # KALAU MAU BUAT BANYAK SILAHKAN TAMBAHIN SESUKA KALIAN :>
                                cl.createGroup("Fuck",[target]) # HANYA SPAM VIA CONTACT
                                cl.createGroup("Fuck",[target])
                                riden1.createGroup("Fuck",[target])
                                riden1.createGroup("Fuck",[target])
                                riden1.createGroup("Fuck",[target])
                                riden2.createGroup("Fuck",[target])
                                riden2.createGroup("Fuck",[target])
                                riden2.createGroup("Fuck",[target])
                                riden3.createGroup("Fuck",[target])
                                riden3.createGroup("Fuck",[target])
                                riden3.createGroup("Fuck",[target])
                                riden4.createGroup("Fuck",[target])
                                riden4.createGroup("Fuck",[target])
                                riden4.createGroup("Fuck",[target])
                                riden5.createGroup("Fuck",[target])
                                riden5.createGroup("Fuck",[target])
                                riden5.createGroup("Fuck",[target])
                                cl.sendText(kirim,"การเชิญ  " + korban + "\nเรียบร้อย")
                                Squad['SpamInvite'] = False
                            except:             
                                 cl.sendText(kirim, 'เออเล่อ')
                                 Squad['SpamInvite'] = False
                                 break


#------------------- ( 3 ) ------------------------- PEMBATAS SCRIP ------------------------------------------------#

        if fast.type == 25 or fast.type == 26:
            msg = fast.message
            text = msg.text
            rfuText = msg.text
            msg_id = msg.id
            kirim = msg.to           
            user = msg._from
            if msg.toType == 0 or msg.toType == 2:
                if msg.toType == 0:
                    to = kirim
                elif msg.toType == 2:
                    to = kirim
                if msg.contentType == 0:
                    if Squad["autoRead"] == True:
                        cl.sendChatChecked(0, msg_id)

                    elif rfuText is None:
                        return
                    else:               
                        if rfuText.lower() == 'กระบวนการปรับเปลี่ยน':
                            cl.sendMessage(0, user)

                        elif rfuText.lower() == "me":
                            if user in RfuSekawan or user in Squad["Admin"]:
                                cl.sendMessage(kirim, None, contentMetadata={'mid': mid}, contentType=13)
                                cl.mentionWithRFU(kirim,mid," ","")

                        elif rfuText.lower() == "help":
                            if user in RfuSekawan or user in Squad["Admin"]:
                                 cl.sendMessage(kirim, str(Help))

                        elif rfuText.lower() == "speed":
                            if user in RfuSekawan or user in Squad["Admin"]:
                                no = time.time()
                                cl.sendText("ubd78f3da598d3c32e075e062e88545ec", ' ')
                                elapsed_time = time.time() - no
                                cl.sendText(kirim, "%s" % (elapsed_time))
                                no1 = time.time()
                                riden1.sendText("ubd78f3da598d3c32e075e062e88545ec", ' ')
                                elapsed_time = time.time() - no1
                                riden1.sendText(kirim, "%s" % (elapsed_time))
                                no2 = time.time()
                                riden2.sendText("ubd78f3da598d3c32e075e062e88545ec", ' ')
                                elapsed_time = time.time() - no2
                                riden2.sendText(kirim, "%s" % (elapsed_time))
                                no3 = time.time()
                                riden3.sendText("ubd78f3da598d3c32e075e062e88545ec", ' ')
                                elapsed_time = time.time() - no3
                                riden3.sendText(kirim, "%s" % (elapsed_time))
                                no4 = time.time()
                                riden4.sendText("ubd78f3da598d3c32e075e062e88545ec", ' ')
                                elapsed_time = time.time() - no4
                                riden4.sendText(kirim, "%s" % (elapsed_time))
                                no5 = time.time()
                                riden5.sendText("ubd78f3da598d3c32e075e062e88545ec", ' ')
                                elapsed_time = time.time() - no5
                                riden5.sendText(kirim, "%s" % (elapsed_time))

                        elif rfuText.lower() == "responsename":
                            if user in RfuSekawan or user in Squad["Admin"]:
                                team1 = cl.getContact(mid).displayName
                                team2 = riden1.getContact(JSMID1).displayName
                                team3 = riden2.getContact(JSMID2).displayName
                                team4 = riden3.getContact(JSMID3).displayName
                                team5 = riden4.getContact(JSMID4).displayName
                                team6 = riden5.getContact(JSMID5).displayName
                                owner = "ubd78f3da598d3c32e075e062e88545ec"
                                cl.mentionWithRFU(kirim,owner," Ready On ","" + str(" ("+team1+")"))
                                riden1.mentionWithRFU(kirim,owner," Ready On ","" + str(" ("+team2+")"))
                                riden2.mentionWithRFU(kirim,owner," Ready On ","" + str(" ("+team3+")"))
                                riden3.mentionWithRFU(kirim,owner," Ready On ","" + str(" ("+team4+")"))
                                riden4.mentionWithRFU(kirim,owner," Ready On ","" + str(" ("+team5+")"))
                                riden5.mentionWithRFU(kirim,owner," Ready On ","" + str(" ("+team6+")"))

                        elif rfuText.lower() == "my bot":
                            if user in RfuSekawan or user in Squad["Admin"]:
                               cl.sendMessage(kirim, None, contentMetadata={'mid': mid}, contentType=13)
                               cl.sendMessage(kirim, None, contentMetadata={'mid': JSMID1}, contentType=13)
                               cl.sendMessage(kirim, None, contentMetadata={'mid': JSMID2}, contentType=13)
                               cl.sendMessage(kirim, None, contentMetadata={'mid': JSMID3}, contentType=13)
                               cl.sendMessage(kirim, None, contentMetadata={'mid': JSMID4}, contentType=13)
                               cl.sendMessage(kirim, None, contentMetadata={'mid': JSMID5}, contentType=13)

                        elif rfuText.lower() == "my team":
                            if user in RfuSekawan or user in Squad["Admin"]:
                                rfu = ""
                                sekawan = ""
                                wa = 0
                                wi = 0
                                for m_id in Owner:
                                    wa = wa + 1
                                    end = '\n'
                                    rfu += str(wa) + ". " +cl.getContact(m_id).displayName + "\n"
                                for m_id in Squad["Admin"]:
                                    wi = wi + 1
                                    end = '\n'
                                    sekawan += str(wi) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendText(kirim,"SELFBOT BY.SAI\n\nOwner:\n"+rfu+"\nAdmin:\n"+sekawan+"\n( %s ) " %(str(len(Owner)+len(Squad["Admin"]))))                                

                        elif rfuText.lower() == "guard":
                            if user in RfuSekawan or user in Squad["Admin"]:
                                X = cl.getGroup(kirim)
                                X.preventedJoinByTicket = False
                                cl.updateGroup(X)
                                invsend = 0
                                Riden = cl.reissueGroupTicket(kirim)
                                riden1.acceptGroupInvitationByTicket(kirim,Riden)
                                riden2.acceptGroupInvitationByTicket(kirim,Riden)
                                riden3.acceptGroupInvitationByTicket(kirim,Riden)
                                riden4.acceptGroupInvitationByTicket(kirim,Riden)
                                riden5.acceptGroupInvitationByTicket(kirim,Riden)
                                X = cl.getGroup(kirim)
                                X.preventedJoinByTicket = True
                                cl.updateGroup(X)
                                X.preventedJoinByTicket(X)
                                cl.updateGroup(X)

                        elif rfuText.lower() == "riden bye":
                            if user in RfuSekawan or user in Squad["Admin"]:
                                ginfo = cl.getGroup(kirim)
                                owner = "ubd78f3da598d3c32e075e062e88545ec"
                                riden1.mentionWithRFU(kirim,owner," ไปละนะ ","\n Good Bye" + str(" ("+ginfo.name+")"))
                                riden5.leaveGroup(kirim)
                                riden4.leaveGroup(kirim)
                                riden3.leaveGroup(kirim)
                                riden2.leaveGroup(kirim)
                                riden1.leaveGroup(kirim)
#                                cl.leaveGroup(kirim)

                        elif rfuText.lower() == "leaveall grup":
                            if user in RfuSekawan or user in Squad["Admin"]:
                                gid = cl.getGroupIdsJoined()
                                gid = riden1.getGroupIdsJoined()
                                gid = riden2.getGroupIdsJoined()
                                gid = riden3.getGroupIdsJoined()
                                gid = riden4.getGroupIdsJoined()
                                gid = riden5.getGroupIdsJoined()
                                for i in gid:
                                    cl.leaveGroup(i)
                                    riden1.leaveGroup(i)
                                    riden2.leaveGroup(i)
                                    riden3.leaveGroup(i)
                                    riden4.leaveGroup(i)
                                    riden5.leaveGroup(i)
                                    print ("Kicker Leave All group")

                        elif rfuText in ["Kick on"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad["KickOn"] = True
                                cl.sendText(kirim,"Status:\n{''cancel'':0,''kick'':1}")
                        elif rfuText in ["Kick off"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad["KickOn"] = False
                                cl.sendText(kirim,"Status:\n{''cancel'':0,''kick'':0}")

                        elif "Kickall" in rfuText:
                            if user in RfuSekawan or user in Squad["Admin"]:
                              if msg.toType == 2:
                                if Squad["KickOn"]:
                                    _name = msg.text.replace("Kickall","")
                                    gs = cl.getGroup(kirim)
                                    targets = []
                                    for g in gs.members:
                                        if _name in g.displayName:
                                            targets.append(g.mid)
                                    if targets == []:
                                        cl.sendText(kirim,"Target Not found.")
                                    else:
                                        for target in targets:
                                          if target not in RfuSekawan and target not in Squad["Admin"]:
                                            try:
                                                klist=[cl,riden1,riden2,riden3]
                                                kicker=random.choice(klist)
                                                kicker.kickoutFromGroup(kirim,[target])
                                                print (kirim,[g.mid])
                                            except Exception as error:
                                                cl.sendText(kirim, str(error))

                        elif "Spam " in rfuText:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                txt = rfuText.split(" ")
                                jmlh = int(txt[2])
                                teks = rfuText.replace("Spam "+str(txt[1])+" "+str(jmlh)+" ","")
                                tulisan = jmlh * (teks+"\n")
                                if txt[1] == "on":
                                    if jmlh <= 500:
                                       for x in range(jmlh):
                                           cl.sendText(kirim, teks)
                                    else:
                                       cl.sendText(kirim, "ได้แค่500ข้อความ")
                                elif txt[1] == "off":
                                    if jmlh <= 500:
                                        cl.sendText(kirim, tulisan)
                                    else:
                                        cl.sendText(kirim, "ได้แค่500ข้อความ")

                        elif "Cekmid: " in rfuText:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                ardian = rfuText.replace("Cekmid: ","")
                                cl.sendMessage(kirim, None, contentMetadata={'mid': ardian}, contentType=13)
                                contact = cl.getContact(ardian)
                                ganteng = cl.getProfileCoverURL(ardian)
                                path = str(ganteng)
                                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                try:
                                    cl.sendText(kirim,"Nama :\n" + contact.displayName + "\n\nBio :\n" + contact.statusMessage)
                                    cl.sendText(kirim,"Profile Picture " + contact.displayName)
                                    cl.sendImageWithURL(kirim,image)
                                    cl.sendText(kirim,"Cover Picture " + contact.displayName)
                                    cl.sendImageWithURL(kirim,path)
                                except:
                                    pass

                        elif ("Banlock " in rfuText):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"][0]["M"]
                                targets = []
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                for target in targets:
                                    try:
                                        Squad["Blacklist"][target] = True
                                        cl.sendText(kirim,"Succes Banned ")
                                    except:
                                        pass

                        elif rfuText.lower() == "banlist":
                            if user in RfuSekawan or user in Squad["Admin"]:
                                if Squad["Blacklist"] == {}:
                                    cl.sendText(kirim,"ไม่มีบัญชีดำ")
                                else:
                                    mc = "Daftar Blacklist "
                                    num=1
                                    ragets = cl.getContacts(Squad["Blacklist"])
                                    for mi_d in ragets:
                                        mc+="\n%i. %s" % (num, mi_d.displayName)
                                        num=(num+1)
                                    mc+="\n\n รวม %i บัญชีดำ " % len(ragets)
                                    cl.sendText(kirim, mc)

                        elif rfuText in ["Contact ban"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                              if Squad["Blacklist"] == {}:
                                  cl.sendText(kirim,"ไม่มีคอนแทคในบัญชีดำของระบบอท")
                              else:
                                  cl.sendText(kirim,"คอนแทคคนที่ติดบัญชีดำของระบบอท")
                                  h = ""
                                  for i in Squad["Blacklist"]:
                                      h = cl.getContact(i)
                                      cl.sendMessage(kirim, None, contentMetadata={'mid': i}, contentType=13)

                        elif rfuText in ["Clear ban"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad["Blacklist"] = {}
                                cl.sendText(kirim,"ได้ทำการล้างบัญชีดำเรียบร้อยแล้ว")
                                print ("Clear Ban")

                        elif rfuText in ["Ban:on"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad["Ban"] = True
                                cl.sendText(kirim,"กรุณาลงคอนแทคคนที่จะบัญชีดำครับ")
                        elif rfuText in ["Unban:on"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad["Unban"] = True
                                cl.sendText(kirim,"กรุณาลงคอนแทคคนที่จะบัญชีดำครับ")

                        elif rfuText.lower() == 'link on':
                            if user in RfuSekawan or user in Squad["Admin"]:
                                if msg.toType == 2:
                                    group = cl.getGroup(kirim)
                                    group.preventedJoinByTicket = False
                                    cl.updateGroup(group)

                        elif rfuText.lower() == 'link off':
                            if user in RfuSekawan or user in Squad["Admin"]:
                                if msg.toType == 2:
                                    group = cl.getGroup(kirim)
                                    group.preventedJoinByTicket = True
                                    cl.updateGroup(group)

                        elif rfuText.lower() == 'gurl':
                          if user in RfuSekawan or user in Squad["Admin"]:
                            if msg.toType == 2:
                                grup = cl.getGroup(kirim)
                                if grup.preventedJoinByTicket == False:
                                    set = cl.reissueGroupTicket(kirim)
                                    cl.sendMessage(kirim, "ลิ้งค์นี้คือลิ้งค์กลุ่มของคุณ \n \nhttps://line.me/R/ti/g/{}".format(str(set)))
                                else:
                                    cl.sendMessage(kirim, "พิมพ์ link on เพือเปิดลิ้งค์ห้อง")

                        elif rfuText.lower() == 'gcreator':
                            if user in RfuSekawan or user in Squad["Admin"]:
                                try:
                                    group = cl.getGroup(kirim)
                                    GS = group.creator.mid
                                    cl.sendMessage(kirim, None, contentMetadata={'mid': GS}, contentType=13)
                                    cl.mentionWithRFU(kirim,GS,"คนนี้คือคนสร้างห้อง ","")
                                    contact = cl.getContact(GS.mid)
                                except:
                                    W = group.members[0].mid
                                    cl.sendMessage(kirim, None, contentMetadata={'mid': W}, contentType=13)
                                    cl.mentionWithRFU(kirim,W,"คนนี้คือคนสร้างห้อง ","")

                        elif "invite gcreator" == rfuText:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                try:
                                    group = cl.getGroup(kirim)
                                    GS = group.creator.mid
                                    cl.sendMessage(kirim, None, contentMetadata={'mid': GS}, contentType=13)
                                    cl.mentionWithRFU(kirim,GS,"คนนี้คือคนสร้างห้อง ","")
                                    cl.findAndAddContactsByMid(GS)
                                    cl.inviteIntoGroup(kirim,[GS])
                                    cl.mentionWithRFU(kirim,user,"เชิญคนสร้างกลุ่ม ","")
                                    contact = cl.getContact(GS.mid)
                                except:
                                    W = group.members[0].mid
                                    cl.sendMessage(kirim, None, contentMetadata={'mid': W}, contentType=13)
                                    cl.mentionWithRFU(kirim,W,"คนนี้คือคนสร้างห้อง  ","")
                                    cl.findAndAddContactsByMid(W)
                                    cl.inviteIntoGroup(kirim,[W])
                                    cl.mentionWithRFU(kirim,user,"เชิญคนสร้างกลุ่ม ","")

                        elif rfuText.lower() == 'ginfo':
                            if user in RfuSekawan or user in Squad["Admin"]:
                                group = cl.getGroup(kirim)
                                try:
                                    gCreator = group.creator.displayName
                                except:
                                    gCreator = "Tidak ditemukan"
                                if group.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(group.invitee))
                                if group.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(line.reissueGroupTicket(group.id)))
                                cuki = "INFO GRUP"
                                cuki += "\nNama Group : {}".format(str(group.name))
                                cuki += "\nID Group :\n? {}".format(group.id)
                                cuki += "\nPembuat : {}".format(str(gCreator))
                                cuki += "\nJumlah Member : {}".format(str(len(group.members)))
                                cuki += "\nJumlah Pending : {}".format(gPending)
                                cuki += "\nGroup Qr : {}".format(gQr)
                                cuki += "\nGroup Ticket : {}".format(gTicket)
                                cl.sendMessage(kirim, str(cuki))

                        elif rfuText in ["Memberlist"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                kontak = cl.getGroup(kirim)
                                group = kontak.members
                                num=1
                                msgs="รายชื่อสมาชิกทั้งหมด\n"
                                for ids in group:
                                    msgs+="\n%i. %s" % (num, ids.displayName)
                                    num=(num+1)
                                msgs+="\n\nจำนวน  ( %i )  คน" % len(group)
                                cl.sendText(kirim, msgs)

                        elif rfuText in ["Blocklist"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                blockedlist = cl.getBlockedContactIds()
                                kontak = cl.getContacts(blockedlist)
                                num=1
                                msgs="รายการ การบล็อคสมาชิก\n"
                                for ids in kontak:
                                    msgs+="\n%i. %s" % (num, ids.displayName)
                                    num=(num+1)
                                msgs+="\n\nจำนวน  %i  คน" % len(kontak)
                                cl.sendText(kirim, msgs)

                        elif rfuText in ["Friendlist mid"]: 
                            if user in RfuSekawan or user in Squad["Admin"]:
                                gruplist = cl.getAllContactIds()
                                kontak = cl.getContacts(gruplist)
                                num=1
                                msgs="รายการ MID เพื่อนของเรา\n"
                                for ids in kontak:
                                    msgs+="\n%i. %s" % (num, ids.mid)
                                    num=(num+1)
                                msgs+="\n\nจำนวน  %i คน" % len(kontak)
                                cl.sendText(kirim, msgs)

                        elif "Grup id" in rfuText:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                saya = rfuText.replace('Grup id','')
                                gid = cl.getGroup(kirim)
                                cl.sendText(kirim, "ID Grup : \n" + gid.id + "\nName Grup : \n" + str(gid.name))

                        elif 'mid ' in rfuText.lower():
                          if user in RfuSekawan or user in Squad["Admin"]:
                              try:
                                  key = eval(msg.contentMetadata["MENTION"])
                                  u = key["MENTIONEES"][0]["M"]
                                  cmid = cl.getContact(u).mid
                                  cl.sendText(kirim, str(cmid))
                              except Exception as e:
                                  cl.sendText(kirim, str(e))

                        elif "Profile" in rfuText:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                key = eval(msg.contentMetadata["MENTION"])
                                key1 = key["MENTIONEES"][0]["M"]
                                contact = cl.getContact(key1)
                                cover = cl.getProfileCoverURL(key1)
                                path = str(cover)
                                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                try:
                                    cl.sendText(kirim,"ชื่อ \n" + contact.displayName + "\n\nตัส \n" + contact.statusMessage)
                                    cl.sendImageWithURL(kirim,image)
                                    cl.sendImageWithURL(kirim,path)
                                except Exception as error:
                                    cl.sendMessage(kirim, str(error))

                        elif rfuText.lower() == 'lurking on':
                            if user in RfuSekawan or user in Squad["Admin"]:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                if kirim in Squad['readPoint']:
                                        try:
                                            del Squad['readPoint'][kirim]
                                            del Squad['readMember'][kirim]
                                            del Squad['readTime'][kirim]
                                        except:
                                            pass
                                        Squad['readPoint'][kirim] = msg.id
                                        Squad['readMember'][kirim] = ""
                                        Squad['readTime'][kirim] = datetime.now().strftime('%H:%M:%S')
                                        Squad['ROM'][kirim] = {}
                                        with open('sider.json', 'w') as fp:
                                            json.dump(Squad, fp, sort_keys=True, indent=4)
                                            cl.sendMessage(kirim,"Lurking already on")
                                else:
                                    try:
                                        del read['readPoint'][kirim]
                                        del read['readMember'][kirim]
                                        del read['readTime'][kirim]
                                    except:
                                        pass
                                    Squad['readPoint'][kirim] = msg.id
                                    Squad['readMember'][kirim] = ""
                                    Squad['readTime'][kirim] = datetime.now().strftime('%H:%M:%S')
                                    Squad['ROM'][kirim] = {}
                                    with open('sider.json', 'w') as fp:
                                        json.dump(Squad, fp, sort_keys=True, indent=4)
                                        cl.sendMessage(kirim, "Set reading point:\n" + readTime)
                                        
                        elif rfuText.lower() == 'lurking off':
                            if user in RfuSekawan or user in Squad["Admin"]:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                if kirim not in Squad['readPoint']:
                                    cl.sendMessage(kirim,"Lurking already off..")
                                else:
                                    try:
                                            del Squad['readPoint'][kirim]
                                            del Squad['readMember'][kirim]
                                            del Squad['readTime'][kirim]
                                    except:
                                          pass
                                    cl.sendMessage(kirim, "Delete reading point:\n" + readTime)
                
                        elif rfuText.lower() == 'lurking reset':
                            if user in RfuSekawan or user in Squad["Admin"]:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                if kirim in Squad["readPoint"]:
                                    try:
                                        Squad["readPoint"][kirim] = True
                                        Squad["readMember"][kirim] = {}
                                        Squad["readTime"][kirim] = readTime
                                        Squad["ROM"][kirim] = {}
                                    except:
                                        pass
                                    cl.sendMessage(kirim, "Reset reading point:\n" + readTime)
                                else:
                                    cl.sendMessage(kirim, "Lurking on dulu kaka..")
                                    
                        elif rfuText.lower() == 'lurking read':
                            if user in RfuSekawan or user in Squad["Admin"]:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                if kirim in Squad['readPoint']:
                                    if Squad["ROM"][kirim].items() == []:
                                        cl.sendMessage(kirim,"[ Reader ]:\nNone")
                                    else:
                                        chiya = []
                                        for rom in Squad["ROM"][kirim].items():
                                            chiya.append(rom[1])
                                        cmem = cl.getContacts(chiya) 
                                        zx = ""
                                        zxc = ""
                                        zx2 = []
                                        xpesan = 'Pembaca Pesan:\n'
                                    for x in range(len(cmem)):
                                        xname = str(cmem[x].displayName)
                                        pesan = ''
                                        pesan2 = pesan+"@ARDIAN_GANTENG\n"
                                        xlen = str(len(zxc)+len(xpesan))
                                        xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                        zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                                        zx2.append(zx)
                                        zxc += pesan2
                                    text = xpesan+ zxc + "\nLurking time: \n" + readTime
                                    try:
                                        cl.sendMessage(kirim, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                    except Exception as error:
                                        print (error)
                                    pass
                                else:
                                    cl.sendMessage(kirim,"Lurking on dulu kaka ??")

                        elif rfuText.lower() == 'sider on':
                            if user in RfuSekawan or user in Squad["Admin"]:
                                try:
                                    del RfuCctv['Point2'][kirim]
                                    del RfuCctv['Point3'][kirim]
                                    del RfuCctv['Point1'][kirim]
                                except:
                                    pass
                                RfuCctv['Point2'][kirim] = msg.id
                                RfuCctv['Point3'][kirim] = ""
                                RfuCctv['Point1'][kirim]=True
                                cl.sendText(kirim,"Sider Set to On..")

                        elif rfuText.lower() == 'sider off':
                            if user in RfuSekawan or user in Squad["Admin"]:
                                if kirim in RfuCctv['Point2']:
                                    RfuCctv['Point1'][kirim]=False
                                    cl.sendText(kirim, RfuCctv['Point3'][kirim])
                                else:
                                    cl.sendText(kirim, "Off not Going")


                        elif text.lower() == '@#':
                            if user in RfuSekawan or user in Squad["Admin"]:
                                group = cl.getGroup(msg.to)
                                nama = [contact.mid for contact in group.members]
                                k = len(nama)//20
                                for a in range(k+1):
                                    txt = u''
                                    s=0
                                    b=[]
                                    for i in group.members[a*20 : (a+1)*20]:
                                        b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                                        s += 7
                                        txt += u'@Alin \n'
                                    cl.sendMessage(to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                                    cl.sendMessage(to, "จำนวน {}  คน".format(str(len(nama))))
                        elif rfuText in ["Welcome on"]:
                          if user in RfuSekawan or user in Squad["Admin"]:
                            if user in RfuSekawan:
                                Squad['Welcome'] = True
                                cl.sendText(kirim,"เปิดระบบทักทายเรียบร้อย")
                        elif rfuText in ["Welcome off"]:
                          if user in RfuSekawan or user in Squad["Admin"]:
                            if user in RfuSekawan:
                                Squad['Welcome'] = False
                                cl.sendText(kirim,"ปิดระบบทักทายเรียบร้อย")

                        elif "changewelcome: " in rfuText.lower():
                            if user in RfuSekawan or user in Squad["Admin"]:
                                teks = rfuText.split(": ")
                                data = rfuText.replace(teks[0] + ": ","")
                                try:
                                    Squad["WcText"] = data
                                    cl.sendText(kirim,"ข้อความการทักทายคนเข้ากลุ่ม ดังนี้\n" +str("(" +data+ ")"))
                                except:
                                    cl.sendText(kirim,"Name Error")

                        elif rfuText in ["Leave on"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad['Leave'] = True
                                cl.sendText(kirim,"เปิดป้องกันการดึงแชทรวม")
                        elif rfuText in ["Leave off"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad['Leave'] = False
                                cl.sendText(kirim,"ปิดป้องกันการดึงแชทรวม")

                        elif "changeleave: " in rfuText.lower():
                            if user in RfuSekawan or user in Squad["Admin"]:
                                teks = rfuText.split(": ")
                                data = rfuText.replace(teks[0] + ": ","")
                                try:
                                    Squad["LvText"] = data
                                    cl.sendText(kirim,"ข้อความทักทายคนดึงแชทรวม ดังนี้ \n" +str("(" +data+ ")"))
                                except:
                                    cl.sendText(kirim,"Name Error")

                        elif rfuText.lower() == "runtime":
                            if user in RfuSekawan or user in Squad["Admin"]:
                                eltime = time.time() - mulai                                
                                opn = " "+waktu(eltime)
                                cl.sendText(kirim,"การทำงานของเซลบอท \n" + opn + "\n SELFBOT BY.SAI")                

                        elif "Broadcast: " in rfuText:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                bc = msg.text.replace("Broadcast: ","")
                                gid = cl.getGroupIdsJoined()
                                owner = "u26972c2269790de24fb84d70ffc5ab5a"
                                for i in gid:
                                    cl.mentionWithRFU(i,owner," ","\n" + str(" ("+bc+")"))

                        elif "Contactbc: " in rfuText:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                bc = msg.text.replace("Contactbc: ","")
                                gid = cl.getAllContactIds()
                                owner = "u26972c2269790de24fb84d70ffc5ab5a"
                                for i in gid:
                                    cl.mentionWithRFU(i,owner," ","\n" + str(" ("+bc+")"))

                        elif "adminadd " in rfuText.lower():
                            if user in RfuSekawan:
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"][0]["M"]
                                targets = []
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                for target in targets:
                                    if target in Squad["Admin"]:
                                        cl.sendText(kirim, "รายชื่อนี้เป็นผู้ดูแลระบบแล้ว")
                                    else:
                                        try:
                                            Squad["Admin"][target] = True
                                            cl.sendText(kirim, "ลงทะเบียนเพื่อ Admin ")
                                        except Exception as e:
                                            cl.sendText(kirim, str(error))

                        elif "admindell " in rfuText.lower():
                            if user in Owner:
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"][0]["M"]
                                targets = []
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                for target in targets:
                                    if target not in Squad["Admin"]:
                                        cl.sendText(kirim, "ไม่ได้ลงทะเบียนใน Admin")
                                    else:
                                        try:
                                            del Squad["Admin"][target]
                                            cl.sendText(kirim, "ลบแล้วส่งผลให้ผู้ดูแลระบบ")
                                        except Exception as e:
                                            cl.sendText(kirim, str(error))

                        elif "changename: " in rfuText.lower():
                            if user in RfuSekawan:
                                name = rfuText.split(": ")
                                change = rfuText.replace(name[0] + ": ","")
                                cll = cl.getProfile()
                                cll.displayName = change
                                cl.updateProfile(cll)
                                owner = "u26972c2269790de24fb84d70ffc5ab5a"
                                cl.mentionWithRFU(kirim,owner," อัปเดตชื่อ ","\n คือชื่อ  " + str(change))

                        elif "changebio: " in rfuText.lower():
                            if user in RfuSekawan:
                                proses = rfuText.split(": ")
                                teks = rfuText.replace(proses[0] + ": ","")
                                no1 = cl.getProfile()
                                no1.statusMessage = teks
                                cl.updateProfile(no1)
                                cl.sendText(kirim,"อัปเดตตัส  คือ  " + teks)

                        elif "changenameall: " in rfuText.lower():
                            if user in RfuSekawan:
                                name = rfuText.split(": ")
                                change = rfuText.replace(name[0] + ": ","")
                                cll = cl.getProfile()
                                cll1 = riden1.getProfile()
                                cll2 = riden2.getProfile()
                                cll3 = riden3.getProfile()
                                cll.displayName = change
                                cll1.displayName = change
                                cll2.displayName = change
                                cll3.displayName = change
                                cll4.displayName = change
                                cll5.displayName = change
                                cl.updateProfile(cll)
                                riden1.updateProfile(cll1)
                                riden2.updateProfile(cll2)
                                riden3.updateProfile(cll3)
                                cl.mentionWithRFU(kirim,user," ปรับปรุงชื่อความสำเร็จ ","\ n เปลี่ยนเป็น " + str(change))
                                riden1.mentionWithRFU(kirim,user," ปรับปรุงชื่อความสำเร็จ ","\ n เปลี่ยนเป็น " + str(change))
                                riden2.mentionWithRFU(kirim,user," ปรับปรุงชื่อความสำเร็จ ","\ n เปลี่ยนเป็น " + str(change))
                                riden3.mentionWithRFU(kirim,user," ปรับปรุงชื่อความสำเร็จ ","\ n เปลี่ยนเป็น " + str(change))
                                riden4.mentionWithRFU(kirim,user," ปรับปรุงชื่อความสำเร็จ ","\ n เปลี่ยนเป็น " + str(change))
                                riden5.mentionWithRFU(kirim,user," ปรับปรุงชื่อความสำเร็จ ","\ n เปลี่ยนเป็น " + str(change))

                        elif "changebioall: " in rfuText.lower():
                            if user in RfuSekawan:
                                proses = rfuText.split(": ")
                                teks = rfuText.replace(proses[0] + ": ","")
                                no = cl.getProfile()
                                no1 = riden1.getProfile()
                                no2 = riden2.getProfile()
                                no3 = riden3.getProfile()
                                no4 = riden4.getProfile()
                                no5 = riden5.getProfile()
                                no.statusMessage = teks
                                no1.statusMessage = teks
                                no2.statusMessage = teks
                                no3.statusMessage = teks
                                no4.statusMessage = teks
                                no5.statusMessage = teks
                                cl.updateProfile(no)
                                riden1.updateProfile(no1)
                                riden2.updateProfile(no2)
                                riden3.updateProfile(no3)
                                riden4.updateProfile(no4)
                                riden5.updateProfile(no5)
                                cl.sendText(kirim,"ปรับปรุงตัส เป็น  " + teks)
                                riden1.sendText(kirim,"ปรับปรุงตัส เป็น  " + teks)
                                riden2.sendText(kirim,"ปรับปรุงตัส เป็น  " + teks)
                                riden3.sendText(kirim,"ปรับปรุงตัส เป็น  " + teks)
                                riden4.sendText(kirim,"ปรับปรุงตัส เป็น  " + teks)
                                riden5.sendText(kirim,"ปรับปรุงตัส เป็น  " + teks)

                        elif rfuText.lower() == "remove pesan":
                            if user in RfuSekawan or user in Squad["Admin"]:
                                try:
                                    cl.removeAllMessages(fast.param2)
                                    riden1.removeAllMessages(fast.param2)
                                    riden2.removeAllMessages(fast.param2)
                                    riden3.removeAllMessages(fast.param2)
                                    riden4.removeAllMessages(fast.param2)
                                    riden5.removeAllMessages(fast.param2)
                                    ginfo = cl.getGroup(kirim)
                                    owner = "u26972c2269790de24fb84d70ffc5ab5a"
                                    cl.mentionWithRFU(kirim,owner," ลบข้อความทั้งหมด ","\n ในกลุ่ม" + str(" ("+ginfo.name+")"))
                                    riden1.mentionWithRFU(kirim,owner," ลบข้อความทั้งหมด ","\n ในกลุ่ม" + str(" ("+ginfo.name+")"))
                                    riden2.mentionWithRFU(kirim,owner," ลบข้อความทั้งหมด ","\n ในกลุ่ม" + str(" ("+ginfo.name+")"))
                                    riden3.mentionWithRFU(kirim,owner," ลบข้อความทั้งหมด ","\n ในกลุ่ม" + str(" ("+ginfo.name+")"))
                                    riden4.mentionWithRFU(kirim,owner," ลบข้อความทั้งหมด ","\n ในกลุ่ม" + str(" ("+ginfo.name+")"))
                                    riden5.mentionWithRFU(kirim,owner," ลบข้อความทั้งหมด ","\n ในกลุ่ม" + str(" ("+ginfo.name+")"))
                                except:
                                    pass

                        elif rfuText.lower() == 'restart':
                            if user in RfuSekawan:
                                cl.sendText(kirim, 'รอการรีระบบการล็อคอิน')
                                print ("Restarting Server")
                                restart_program()

                        elif rfuText.lower() == 'bot logout':
                            if user in RfuSekawan:
                                cl.mentionWithRFU(kirim,user," เราได้ปิดระบบเซลบอททุกอย่างเรียบร้อยแล้ว","")
                                print ("Selfbot Off")
                                exit(1)

                        elif "kick " in rfuText.lower():
                            if user in RfuSekawan or user in Squad["Admin"]:
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"][0]["M"]
                                targets = []
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                for target in targets:
                                    if target in Rfu:
                                        pass
                                    else:
                                        try:
                                            klist=[cl,riden1,riden2,riden3]
                                            kicker=random.choice(klist)
                                            kicker.kickoutFromGroup(kirim,[target])
                                            Squad["Blacklist"][target] = True
                                        except Exception as e:
                                            cl.sendText(kirim, str(error))

                        elif rfuText.lower() == 'my grup':
                            if user in RfuSekawan or user in Squad["Admin"]:
                                groups = cl.groups
                                ret_ = "รายชื่อกลุ่ม"
                                no = 0 + 1
                                for gid in groups:
                                    group = cl.getGroup(gid)
                                    ret_ += "\n\n{}. {} ".format(str(no), str(group.name))
                                    no += 1
                                ret_ += "\n\nจำนวน {} กลุ่ม".format(str(len(groups)))
                                cl.sendText(kirim, str(ret_))

                        elif rfuText.lower() == '1grup':
                            if user in RfuSekawan or user in Squad["Admin"]:
                                groups = riden1.groups
                                ret_ = "GRUP JOIN"
                                no = 0 + 1
                                for gid in groups:
                                    group = riden1.getGroup(gid)
                                    ret_ += "\n\n{}. {} ".format(str(no), str(group.name))
                                    no += 1
                                ret_ += "\n\nTOTAL {} GRUP JOIN".format(str(len(groups)))
                                riden1.sendText(kirim, str(ret_))

                        elif rfuText.lower() == '2grup':
                            if user in RfuSekawan or user in Squad["Admin"]:
                                groups = riden2.groups
                                ret_ = "GRUP JOIN"
                                no = 0 + 1
                                for gid in groups:
                                    group = riden2.getGroup(gid)
                                    ret_ += "\n\n{}. {} ".format(str(no), str(group.name))
                                    no += 1
                                ret_ += "\n\nTOTAL {} GRUP JOIN".format(str(len(groups)))
                                riden2.sendText(kirim, str(ret_))

                        elif rfuText.lower() == '3grup':
                            if user in RfuSekawan or user in Squad["Admin"]:
                                groups = riden3.groups
                                ret_ = "GRUP JOIN"
                                no = 0 + 1
                                for gid in groups:
                                    group = riden3.getGroup(gid)
                                    ret_ += "\n\n{}. {} ".format(str(no), str(group.name))
                                    no += 1
                                ret_ += "\n\nTOTAL {} GRUP JOIN".format(str(len(groups)))
                                riden3.sendText(kirim, str(ret_))

                        elif rfuText.lower() == '4grup':
                            if user in RfuSekawan or user in Squad["Admin"]:
                                groups = riden4.groups
                                ret_ = "GRUP JOIN"
                                no = 0 + 1
                                for gid in groups:
                                    group = riden4.getGroup(gid)
                                    ret_ += "\n\n{}. {} ".format(str(no), str(group.name))
                                    no += 1
                                ret_ += "\n\nTOTAL {} GRUP JOIN".format(str(len(groups)))
                                riden4.sendText(kirim, str(ret_))

                        elif rfuText.lower() == '5grup':
                            if user in RfuSekawan or user in Squad["Admin"]:
                                groups = riden5.groups
                                ret_ = "GRUP JOIN"
                                no = 0 + 1
                                for gid in groups:
                                    group = riden5.getGroup(gid)
                                    ret_ += "\n\n{}. {} ".format(str(no), str(group.name))
                                    no += 1
                                ret_ += "\n\nTOTAL {} GRUP JOIN".format(str(len(groups)))
                                riden5.sendText(kirim, str(ret_))

                        elif rfuText.lower().startswith("rejectall grup"):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                ginvited = cl.getGroupIdsInvited()
                                ginvited = riden1.getGroupIdsInvited()
                                ginvited = riden2.getGroupIdsInvited()
                                ginvited = riden3.getGroupIdsInvited()
                                ginvited = riden4.getGroupIdsInvited()
                                ginvited = riden5.getGroupIdsInvited()
                                if ginvited != [] and ginvited != None:
                                    for gid in ginvited:
                                        cl.rejectGroupInvitation(gid)
                                        riden1.rejectGroupInvitation(gid)
                                        riden2.rejectGroupInvitation(gid)
                                        riden3.rejectGroupInvitation(gid)
                                        riden4.rejectGroupInvitation(gid)
                                        riden5.rejectGroupInvitation(gid)
                                    cl.sendMessage(kirim, "Succes Cancell {} Invite Grup".format(str(len(ginvited))))
                                    riden1.sendMessage(kirim, "Succes Cancell {} Invite Grup".format(str(len(ginvited))))
                                    riden2.sendMessage(kirim, "Succes Cancell {} Invite Grup".format(str(len(ginvited))))
                                    riden3.sendMessage(kirim, "Succes Cancell {} Invite Grup".format(str(len(ginvited))))
                                    riden4.sendMessage(kirim, "Succes Cancell {} Invite Grup".format(str(len(ginvited))))
                                    riden5.sendMessage(kirim, "Succes Cancell {} Invite Grup".format(str(len(ginvited))))
                                else:
                                    cl.sendMessage(kirim, "Nothing Invited")
                                    riden1.sendMessage(kirim, "Nothing Invited")
                                    riden2.sendMessage(kirim, "Nothing Invited")
                                    riden3.sendMessage(kirim, "Nothing Invited")
                                    riden4.sendMessage(kirim, "Nothing Invited")
                                    riden5.sendMessage(kirim, "Nothing Invited")

                        elif rfuText.lower() == 'status':
                            if user in RfuSekawan or user in Squad["Admin"]:
                                try:
                                    hasil = "Status Bot\n"
                                    if Squad["autoAdd"] == True: hasil += "\nAuto Add ( on )"
                                    else: hasil += "\nAuto Add ( off )"
                                    if Squad["autoJoin"] == True: hasil += "\nAuto Join ( on )"
                                    else: hasil += "\nAuto Join ( off )"
                                    if Squad["AutoReject"] == True: hasil += "\nAuto Reject Room ( on )"
                                    else: hasil += "\nAuto Reject Room ( off )"
                                    if Squad["AutojoinTicket"] == True: hasil += "\nAuto Join Ticket ( on )"
                                    else: hasil += "\nAuto Join Ticket ( off )"
                                    if Squad["autoRead"] == True: hasil += "\nAuto Read ( on )"
                                    else: hasil += "\nAuto Read ( off )"
                                    if Squad["AutoRespon"] == True: hasil += "\nDetect Mention ( on )"
                                    else: hasil += "\nDetect Mention ( off )"
                                    if Squad["KickRespon"] == True: hasil += "\nDetect Mention ( on )"
                                    else: hasil += "\nDetect Kick Mention ( off )"
                                    if Squad["Contact"] == True: hasil += "\nCheck Contact ( on )"
                                    else: hasil += "\nCheck Contact ( off )"
                                    if Squad["Timeline"] == True: hasil += "\nCheck Post Timeline ( on )"
                                    else: hasil += "\nCheck Post ( off )"
                                    if Squad["IDSticker"] == True: hasil += "\nCheck Sticker ( on )"
                                    else: hasil += "\nCheck Sticker ( off )"
                                    if Squad["UnsendPesan"] == True: hasil += "\nUnsend Message ( on )"
                                    else: hasil += "\nUnsend Message ( off )"
                                    if RfuProtect["protect"] == True: hasil += "\nProtect Grup ( on )"
                                    else: hasil += "\nProtect Grup ( off )"
                                    if RfuProtect["linkprotect"] == True: hasil += "\nProtect Link Grup ( on )"
                                    else: hasil += "\nProtect Link Grup ( off )"
                                    if RfuProtect["inviteprotect"] == True: hasil += "\nProtect Invite Grup ( on )"
                                    else: hasil += "\nProtect Invite Grup ( off )"
                                    if RfuProtect["cancelprotect"] == True: hasil += "\nProtect Cancel Grup ( on )"
                                    else: hasil += "\nProtect Cancel Grup ( off )"
                                    if RfuProtect["ProtectCancelled"] == True: hasil += "\nProtect Cancel Member ( on )"
                                    else: hasil += "\nProtect Cancel Member ( off )"
                                    if Squad["BackupBot"] == True: hasil += "\nBackup Bot ( on )"
                                    else: hasil += "\nBackup Bot ( off )"
                                    if Squad["KickOn"] == True: hasil += "\nKick All Member ( on )"
                                    else: hasil += "\nKick All Member ( off )"
                                    if Squad["SpamInvite"] == True: hasil += "\nSpam invite via contact ( on )"
                                    else: hasil += "\nSpam invite Via Contact ( off )"
                                    hasil += "\n\nSELFBOT BY.SAI"
                                    cl.sendMessage(kirim, str(hasil))
                                except Exception as error:
                                    cl.sendMessage(kirim, str(error))

                        elif rfuText in ["Allprotect on"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                try:
                                    RfuProtect['protect'] = True
                                    RfuProtect['linkprotect'] = True
                                    RfuProtect['inviteprotect'] = True
                                    RfuProtect['cancelprotect'] = True
                                    RfuProtect['ProtectCancelled'] = True
                                    grup = cl.getGroup(kirim)
                                    cl.sendText(kirim,"ได้ทำการเปิดระบบป้องกันทั้งหมด \n " +str(grup.name))
                                except Exception as e:
                                    cl.sendText(kirim, str(error))
                        elif rfuText in ["Allprotect off"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                try:
                                    RfuProtect['protect'] = False
                                    RfuProtect['linkprotect'] = False
                                    RfuProtect['inviteprotect'] = False
                                    RfuProtect['cancelprotect'] = False
                                    RfuProtect['ProtectCancelled'] = False
                                    grup = cl.getGroup(kirim)
                                    cl.sendText(kirim,"ได้ทำการปิดระบบป้องกันทั้งหมด \n " +str(grup.name))
                                except Exception as e:
                                    cl.sendText(kirim, str(error))

                        elif rfuText in ["Backup on"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad['BackupBot'] = True
                                cl.sendText(kirim,"เปิดระบบสำรองข้อมูลของบอท")
                        elif rfuText in ["Backup off"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad['BackupBot'] = False
                                cl.sendText(kirim,"ปิดระบบสำรองข้อมูลของบอท")

                        elif rfuText in ["Unsend on"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad['UnsendPesan'] = True
                                cl.sendText(kirim,"เปิดระบบเช็คการยกเลิกข้อความ")
                        elif rfuText in ["Unsend off"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad['UnsendPesan'] = False
                                cl.sendText(kirim,"ปิดระบบเช็คการยกเลิกข้อความ")

                        elif rfuText in ["Changepp on"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad['Upfoto'] = True
                                cl.sendText(kirim,"กรุณาส่งรูปภาพ เพือเปลี่ยนรูปภาพโปรไฟล์")
                        elif rfuText in ["Changepp off"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad['Upfoto'] = False
                                cl.sendText(kirim,"ปิดการเปลี่ยนรูปภาพ")

                        elif rfuText in ["Changeppbot on"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad['UpfotoBot'] = True
                                riden1.sendText(kirim,"กรุณาส่งรูปภาพ เพือเปลี่ยนรูปภาพโปรไฟล์คลิ้ก")
                                riden2.sendText(kirim,"กรุณาส่งรูปภาพ เพือเปลี่ยนรูปภาพโปรไฟล์คลิ้ก")
                                riden3.sendText(kirim,"กรุณาส่งรูปภาพ เพือเปลี่ยนรูปภาพโปรไฟล์คลิ้ก")
                                riden4.sendText(kirim,"กรุณาส่งรูปภาพ เพือเปลี่ยนรูปภาพโปรไฟล์คลิ้ก")
                                riden5.sendText(kirim,"กรุณาส่งรูปภาพ เพือเปลี่ยนรูปภาพโปรไฟล์คลิ้ก")
                        elif rfuText in ["Changeppbot off"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad['UpfotoBot'] = False
                                riden1.sendText(kirim,"ปิดการเปลี่ยนรูปภาพ")
                                riden2.sendText(kirim,"ปิดการเปลี่ยนรูปภาพ")
                                riden3.sendText(kirim,"ปิดการเปลี่ยนรูปภาพ")
                                riden2.sendText(kirim,"ปิดการเปลี่ยนรูปภาพ")
                                riden3.sendText(kirim,"ปิดการเปลี่ยนรูปภาพ")

                        elif rfuText in ["Cfotogrup on"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad['UpfotoGrup'] = True
                                cl.sendText(kirim,"ส่งกลุ่มรูปภาพเพื่อเปลี่ยนรูป")
                        elif rfuText in ["Cfotogrup off"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad['UpfotoGrup'] = False
                                cl.sendText(kirim,"ปิดการเปลี่ยนรูปกลุ่ม")

                        elif rfuText in ["Timeline on"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad['Timeline'] = True
                                cl.sendText(kirim,"เปิดระบบเช็คไทม์ไลน์")
                        elif rfuText in ["Timeline off"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad['Timeline'] = False
                                cl.sendText(kirim,"ปิดระบบเช็คไทม์ไลน์")

                        elif rfuText in ["Autojoin on"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad['autoJoin'] = True
                                cl.sendText(kirim,"เปิดการเข้ากลุ่มออโต้")
                        elif rfuText in ["Autojoin off"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad['autoJoin'] = False
                                cl.sendText(kirim,"ปิดการเข้ากลุ่มออโต้")

                        elif rfuText in ["Autoreject on"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad['AutoReject'] = True
                                cl.sendText(msg.to,"ปฏิเสธการตั้งค่าเป็นเปิด")
                        elif rfuText in ["Autoreject off"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad['AutoReject'] = False
                                cl.sendText(msg.to,"ปฏิเสธการตั้งค่าเป็นปิด")

                        elif rfuText in ["Admin:add-on"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad["Adminadd"] = True
                                cl.sendText(kirim,"ส่งข้อมูลติดต่อหรือคอนแท็คเพื่อเพิ่ม Admin")
                        elif rfuText in ["Admin:add-off"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad["Adminadd"] = False
                                cl.sendText(kirim,"ส่งข้อมูลติดต่อหรือคอนแท็คเพื่อปิดการเพิ่ม Admin")

                        elif rfuText in ["Admin:del-on"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad["AdminDel"] = True
                                cl.sendText(kirim,"ส่งข้อมูลติดต่อหรือคอนแท็คเพื่อลบ Admin")
                        elif rfuText in ["Admin:del-off"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad["AdminDel"] = False
                                cl.sendText(kirim,"ส่งข้อมูลติดต่อหรือคอนแท็คเพื่อปิดการลบ Admin")

                        elif rfuText in ["Gift:on"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad["Gift"] = True
                                cl.sendText(kirim,"ส่งข้อมูลติดต่อหรือคอนแท็คเพื่อส่งของขวัญ")
                        elif rfuText in ["Gift:off"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad["Gift"] = False
                                cl.sendText(kirim,"ส่งข้อมูลติดต่อหรือคอนแท็คเพื่อปิดการส่งของขวัญ")

                        elif rfuText in ["Spaminvite on"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad["SpamInvite"] = True
                                cl.sendText(kirim,"ส่งข้อมูลติดต่อหรือคอนแท็คเพื่อรันกลุ่ม")
                        elif rfuText in ["Spaminvite off"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad["Gift"] = False
                                cl.sendText(kirim,"ส่งข้อมูลติดต่อหรือคอนแท็คเพื่อปิดการรันกลุ่ม.")

                        elif rfuText in ["Auto jointicket on"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad["AutojoinTicket"] = True
                                cl.sendText(kirim,"เปิดการเข้ากลุ่มโดยตั๋ว")
                        elif rfuText in ["Auto jointicket off"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad["AutojoinTicket"] = False
                                cl.sendText(kirim,"ปิดการเข้ากลุ่มโดยตั๋ว")
                        elif '/ti/g/' in rfuText.lower():
                            if user in RfuSekawan or user in Squad["Admin"]:
                                link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                links = link_re.findall(msg.text)
                                n_links=[]
                                for l in links:
                                    if l not in n_links:
                                        n_links.append(l)
                                for ticket_id in n_links:
                                    if Squad["AutojoinTicket"] == True:
                                        group=cl.findGroupByTicket(ticket_id)
                                        cl.acceptGroupInvitationByTicket(group.id,ticket_id)
                                        cl.sendText(kirim,"Success Masuk %s" % str(group.name))

                        elif rfuText in ["Copy on"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad['Copy'] = True
                                cl.sendText(kirim,"ส่งผู้ติดต่อหรือคอนแท็คสำหรับคัดลอกผู้ใช้")
                        elif rfuText in ["Copy off"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad['Copy'] = False
                                cl.sendText(kirim,"ส่งผู้ติดต่อหรือคอนแท็คสำหรับคัดลอกผู้ใช้ปิด")

                        elif rfuText.lower().startswith("clone "):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = cl.getContact(ls)
                                        cl.cloneContactProfile(ls)
                                        cl.sendMessage(kirim, "คัดลอกโปรไฟล์เรียบร้อยแล้ว {}".format(contact.displayName))

                        elif rfuText.lower() == 'comeback':
                            if user in RfuSekawan or user in Squad["Admin"]:
                                try:
                                    clProfile.displayName = str(ProfileMe["displayName"])
                                    clProfile.statusMessage = str(ProfileMe["statusMessage"])
                                    clProfile.pictureStatus = str(ProfileMe["pictureStatus"])
                                    cl.updateProfileAttribute(8, clProfile.pictureStatus)
                                    cl.updateProfile(clProfile)
                                    cl.sendMessage(kirim, "กลับไปที่บัญชีของฉันแล้ว")
                                except:
                                    cl.sendMessage(kirim, "เออเล่อ")

                        elif rfuText in ["Steal on"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad['Steal'] = True
                                cl.sendText(kirim,"กรุณาส่งคอนแท็คสำหรับการตรวจสอบข้อมูล")
                        elif rfuText in ["Steal off"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad['Steal'] = False
                                cl.sendText(kirim,"ปิดการตรวจสอบข้อมูล")

                        elif rfuText in ["Contact on"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad['Contact'] = True
                                cl.sendText(kirim,"เปิดการเช็คคอนแท็ค")
                        elif rfuText in ["Contact off"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad['Contact'] = False
                                cl.sendText(kirim,"ปิดการเช็คคอนแท็ค")

                        elif rfuText in ["Invite on"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad['Invite'] = True
                                cl.sendText(kirim,"กรุณาส่งคอนแทคสำหรับการเชิญ")
                        elif rfuText in ["Invite off"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad['Invite'] = False
                                cl.sendText(kirim,"ปิดการเชิญโดยคอนแท็ค")

                        elif rfuText.lower() == 'kill on':
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad["KillOn"] = True
                                cl.sendMessage(kirim, "กรุณาส่งคอนแท็คสำหรับการลบ")
                        elif rfuText.lower() == 'kill off':
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad["KillOn"] = False
                                cl.sendMessage(kirim, "ปิดการลบโดยคอนแท็ค")

                        elif rfuText in ["Mic:add-on"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Target["Mic"] = True
                                cl.sendText(kirim,"กรุณาลงคอนแท็คเพิ่มการ พูดตาม")
                        elif rfuText in ["Mic:del-on"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Target["MicDel"] = True
                                cl.sendText(kirim,"กรุณาลงคอนแท็คลบการ พูดตาม")
                        elif "mimic" in rfuText.lower():
                            if user in RfuSekawan or user in Squad["Admin"]:
                                sep = rfuText.split(" ")
                                mic = rfuText.replace(sep[0] + " ","")
                                if mic == "on":
                                    if Mozilla["mimic"]["status"] == False:
                                        Mozilla["mimic"]["status"] = True
                                        cl.sendText(kirim,"เปิดระบบการพูดตาม")
                                elif mic == "off":
                                    if Mozilla["mimic"]["status"] == True:
                                        Mozilla["mimic"]["status"] = False
                                        cl.sendText(kirim,"ปิดระบบการพูดตาม")

                        elif rfuText.lower() == 'mimiclist':
                            if user in RfuSekawan or user in Squad["Admin"]:
                                if Mozilla["mimic"]["target"] == {}:
                                    cl.sendText(kirim,"รายชื่อการพูดตาม")
                                else:
                                    mc = "Mimic List"
                                    for mi_d in Mozilla["mimic"]["target"]:
                                        mc += "\n? "+cl.getContact(mi_d).displayName
                                    cl.sendText(kirim,mc + "\nเสร็จสิ้น")

                        elif rfuText.lower() == 'sai off':
                            if user in RfuSekawan or user in Squad["Admin"]:
                                try:
                                    Squad['Mic'] = False
                                    Squad['MicDel'] = False
                                    Squad['Gift'] = False
                                    Squad['Steal'] = False
                                    Squad['Invite'] = False
                                    Squad['Contact'] = False
                                    Squad['Copy'] = False
                                    Squad['autoJoin'] = False
                                    Squad['autoAdd'] = False
                                    Squad['AutojoinTicket'] = False
                                    Squad['UnsendPesan'] = False
                                    Squad['AutoReject'] = False
                                    Squad['Timeline'] = False
                                    Squad['Upfoto'] = False
                                    Squad['UpfotoBot'] = False
                                    Squad['UpfotoGrup'] = False
                                    Squad['Adminadd'] = False
                                    Squad['AdminDel'] = False
                                    Squad['Welcome'] = False
                                    Squad['Leave'] = False
                                    Squad['Ban'] = False
                                    Squad['Unban'] = False
                                    Squad['KillOn'] = False
                                    Squad['KickOn'] = False
                                    Squad['SpamInvite'] = False
                                    cl.sendText(kirim,"ปิดระบบทุกอย่าง")
                                except Exception as e:
                                    cl.sendText(kirim, str(error))

                        elif rfuText.lower() == 'sai on':
                            if user in RfuSekawan or user in Squad["Admin"]:
                                try:
                                    Squad['Mic'] = True
                                    Squad['MicDel'] = True
                                    Squad['Gift'] = True
                                    Squad['Steal'] = True
                                    Squad['Invite'] = True
                                    Squad['Contact'] = True
                                    Squad['Copy'] = True
                                    Squad['autoJoin'] = True
                                    Squad['autoAdd'] = True
                                    Squad['AutojoinTicket'] = True
                                    Squad['UnsendPesan'] = True
                                    Squad['AutoReject'] = True
                                    Squad['Timeline'] = True
                                    Squad['Upfoto'] = True
                                    Squad['UpfotoBot'] = True
                                    Squad['UpfotoGrup'] = True
                                    Squad['Adminadd'] = True
                                    Squad['AdminDel'] = True
                                    Squad['Welcome'] = True
                                    Squad['Leave'] = True
                                    Squad['Ban'] = True
                                    Squad['Unban'] = True
                                    Squad['KillOn'] = True
                                    Squad['KickOn'] = True
                                    Squad['SpamInvite'] = True
                                    cl.sendText(kirim,"เปิดระบบทุกอย่าง")
                                except Exception as e:
                                    cl.sendText(kirim, str(error))

                        elif rfuText.lower().startswith("my name"):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                contact = cl.getContact(user)
                                cl.sendMessage(kirim, "ชื่อของคุณ {}".format(contact.displayName))
                        elif rfuText.lower().startswith("my bio"):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                contact = cl.getContact(user)
                                cl.sendMessage(kirim, "ตัสของคุณ \n{}".format(contact.statusMessage))
                        elif rfuText.lower().startswith("my picture"):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                contact = cl.getContact(user)
                                cl.sendImageWithURL(kirim,"http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus))
                        elif rfuText.lower().startswith("my video"):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                contact = cl.getContact(user)
                                cl.sendVideoWithURL(kirim,"http://dl.profile.line-cdn.net/{}/vp".format(contact.pictureStatus))
                        elif rfuText.lower().startswith("my cover"):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                channel = cl.getProfileCoverURL(user)          
                                path = str(channel)
                                cl.sendImageWithURL(kirim, path)

#------------------------------------------ SOCIAL MEDIA ----------------------------------------------------#

                        elif rfuText.lower().startswith("topnews"):
                              if user in RfuSekawan or user in Squad["Admin"]:
                                  rfu=requests.get("https://newsapi.org/v2/top-headlines?country=id&apiKey=1214d6480f6848e18e01ba6985e2008d")
                                  data=rfu.text
                                  data=json.loads(data)
                                  hasil = "Top News\n\n"
                                  hasil += "(1) " + str(data["articles"][0]["title"])                                                        
                                  hasil += "\n     Sumber : " + str(data["articles"][0]["source"]["name"])
                                  hasil += "\n     Penulis : " + str(data["articles"][0]["author"])
                                  hasil += "\n     Link : " + str(data["articles"][0]["url"])
                                  hasil += "\n\n(2) " + str(data["articles"][1]["title"])                                                        
                                  hasil += "\n     Sumber : " + str(data["articles"][1]["source"]["name"])
                                  hasil += "\n     Penulis : " + str(data["articles"][1]["author"])   
                                  hasil += "\n     Link : " + str(data["articles"][1]["url"])
                                  hasil += "\n\n(3) " + str(data["articles"][2]["title"])                                                        
                                  hasil += "\n     Sumber : " + str(data["articles"][2]["source"]["name"])
                                  hasil += "\n     Penulis : " + str(data["articles"][2]["author"])
                                  hasil += "\n     Link : " + str(data["articles"][2]["url"])
                                  hasil += "\n\n(4) " + str(data["articles"][3]["title"])                                                        
                                  hasil += "\n     Sumber : " + str(data["articles"][3]["source"]["name"])
                                  hasil += "\n     Penulis : " + str(data["articles"][3]["author"])
                                  hasil += "\n     Link : " + str(data["articles"][3]["url"])
                                  hasil += "\n\n(5) " + str(data["articles"][4]["title"])                                                        
                                  hasil += "\n     Sumber : " + str(data["articles"][4]["source"]["name"])
                                  hasil += "\n     Penulis : " + str(data["articles"][4]["author"])
                                  hasil += "\n     Link : " + str(data["articles"][4]["url"])
                                  hasil += "\n\n(6) " + str(data["articles"][5]["title"])                                                        
                                  hasil += "\n     Sumber : " + str(data["articles"][5]["source"]["name"])
                                  hasil += "\n     Penulis : " + str(data["articles"][5]["author"])
                                  hasil += "\n     Link : " + str(data["articles"][5]["url"])
                                  path = data["articles"][3]["urlToImage"]
                                  cl.sendText(kirim, str(hasil))
                                  cl.sendImageWithURL(kirim, str(path))

                        elif "Data birth: " in rfuText:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                tanggal = rfuText.replace("Data birth: ","")
                                r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                                data=r.text
                                data=json.loads(data)
                                lahir = data["data"]["lahir"]
                                usia = data["data"]["usia"]
                                ultah = data["data"]["ultah"]
                                zodiak = data["data"]["zodiak"]
                                cl.sendText(kirim," I N F O R M A S I \n"+"Date Of Birth : "+lahir+"\nAge : "+usia+"\nUltah : "+ultah+"\nZodiak : "+zodiak+"\n  I N F O R M A S I ")

                        elif rfuText.lower().startswith("urban: "):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                sep = rfuText.split(" ")
                                judul = rfuText.replace(sep[0] + " ","")
                                url = "http://api.urbandictionary.com/v0/define?term="+str(judul)
                                with requests.session() as s:
                                    s.headers["User-Agent"] = random.choice(Mozilla["userAgent"])
                                    r = s.get(url)
                                    data = r.text
                                    data = json.loads(data)
                                    cu = "Urban Result\n\n"
                                    cu += "\nText: "+ data["tags"][0]
                                    cu += ","+ data["tags"][1]
                                    cu += ","+ data["tags"][2]
                                    cu += ","+ data["tags"][3]
                                    cu += ","+ data["tags"][4]
                                    cu += ","+ data["tags"][5]
                                    cu += ","+ data["tags"][6]
                                    cu += ","+ data["tags"][7]
                                    cu += "\n[1]\nAuthor: "+str(data["list"][0]["author"])+"\n"
                                    cu += "\nWord: "+str(data["list"][0]["word"])+"\n"
                                    cu += "\nLink: "+str(data["list"][0]["permalink"])+"\n"
                                    cu += "\nDefinition: "+str(data["list"][0]["definition"])+"\n"
                                    cu += "\nExample: "+str(data["list"][0]["example"])+"\n"
                                    cl.sendText(kirim, str(cu))

                        elif "Sslink: " in rfuText:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                 website = msg.text.replace("Sslink: ","")
                                 response = requests.get("http://rahandiapi.herokuapp.com/sswebAPI?key=betakey&link="+website+"")
                                 data = response.json()
                                 pictweb = data['result']
                                 cl.sendImageWithURL(kirim, pictweb)

                        elif rfuText.lower().startswith("maps: "):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                location = rfuText.lower().replace("maps: ","")
                                with requests.session() as web:
                                    web.headers["user-agent"] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
                                    rfu = web.get("http://api.corrykalam.net/apiloc.php?lokasi={}".format(urllib.parse.quote(location)))
                                    data = rfu.text
                                    data = json.loads(data)
                                    if data[0] != "" and data[1] != "" and data[2] != "":
                                        link = "https://www.google.co.id/maps/@{},{},15z".format(str(data[1]), str(data[2]))
                                        ret_ = "Check Location\n"
                                        ret_ += "\n Lokasi : " + data[0]
                                        ret_ += "\n Google Maps : " + link
                                        ret_ += "\n\nSearch Location Success"
                                    else:
                                        ret_ = "Searching Location Error or Location Tidak Ditemukan"
                                    cl.sendText(kirim,str(ret_))

                        elif rfuText.lower().startswith("cekcuaca: "):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                weather = rfuText.lower().replace("cekcuaca: ","")
                                with requests.session() as web:
                                    web.headers["user-agent"] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
                                    rfu = web.get("http://api.corrykalam.net/apicuaca.php?kota={}".format(urllib.parse.quote(weather)))
                                    data = rfu.text
                                    data = json.loads(data)
                                    if "result" not in data:
                                        ret_ = "Cheking Weather\n"
                                        ret_ += "\nSuhu : " + data[1].replace("Suhu : ","")
                                        ret_ += "\nLokasi : " + data[0].replace("Temperatur di kota ","")
                                        ret_ += "\nKelembaban : " + data[2].replace("Kelembaban : ","")
                                        ret_ += "\nTekanan Udara : " + data[3].replace("Tekanan udara : ","")
                                        ret_ += "\nKecepatan Angin : " + data[4].replace("Kecepatan angin : ","")
                                        ret_ += "\n\nSearching Weather Success"
                                    else:
                                        ret_ = "Checking Weather Error or Not Found Location"
                                    cl.sendText(kirim, str(ret_))

                        elif rfuText.lower().startswith("jadwalshalat: "):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                shalat = rfuText.lower().replace("jadwalshalat: ","")
                                with requests.session() as web:
                                    web.headers["user-agent"] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
                                    rfu = web.get("http://api.corrykalam.net/apisholat.php?lokasi={}".format(urllib.parse.quote(shalat)))
                                    data = rfu.text
                                    data = json.loads(data)
                                    if data[1] != "Subuh : " and data[2] != "Dzuhur : " and data[3] != "Ashar : " and data[4] != "Maghrib : " and data[5] != "Isha : ":
                                        ret_ = "Jadwal Shalat\n"
                                        ret_ += "\nLocation : " + data[0]
                                        ret_ += "\n " + data[1]
                                        ret_ += "\n " + data[2]
                                        ret_ += "\n " + data[3]
                                        ret_ += "\n " + data[4]
                                        ret_ += "\n " + data[5]
                                        ret_ += "\n\nJadwal Shalat Wilayah"
                                    else:
                                        ret_ = "Jadwa Shalat Wilayah Error or Not Found Location" 
                                    cl.sendText(kirim, str(ret_))

                        elif "Idline: " in rfuText:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                 msgg = rfuText.replace('Idline: ','')
                                 conn = cl.findContactsByUserid(msgg)
                                 if True:
                                    cl.sendText(kirim,"Link User : https://line.me/ti/p/~" + msgg)
                                    cl.sendMessage(kirim, None, contentMetadata={'mid': conn.mid}, contentType=13)
                                    contact = cl.getContact(conn.mid)
                                    cl.sendImageWithURL(kirim,"http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                                    cover = cl.getProfileCoverURL(conn.mid)
                                    cl.sendImageWithURL(kirim, cover)
                                    cl.mentionWithRFU(kirim,conn.mid,"Tag User\n","")

                        elif 'say-id: ' in rfuText.lower():
                            if user in RfuSekawan or user in Squad["Admin"]:
                                try:
                                    isi = rfuText.lower().replace('say-id: ','')
                                    tts = gTTS(text=isi, lang='id', slow=False)
                                    tts.save('temp.mp3')
                                    cl.sendAudio(kirim, 'temp.mp3')
                                except Exception as e:
                                    cl.sendText(kirim, str(e))

                        elif 'say-en: ' in rfuText.lower():
                            if user in RfuSekawan or user in Squad["Admin"]:
                                try:
                                    isi = rfuText.lower().replace('say-en: ','')
                                    tts = gTTS(text=isi, lang='en', slow=False)
                                    tts.save('temp.mp3')
                                    cl.sendAudio(kirim, 'temp.mp3')
                                except Exception as e:
                                    cl.sendText(kirim, str(e))

                        elif 'say-jp: ' in rfuText.lower():
                            if user in RfuSekawan or user in Squad["Admin"]:
                                try:
                                    isi = rfuText.lower().replace('say-jp: ','')
                                    tts = gTTS(text=isi, lang='ja', slow=False)
                                    tts.save('temp.mp3')
                                    cl.sendAudio(kirim, 'temp.mp3')
                                except Exception as e:
                                    cl.sendText(kirim, str(e))

                        elif 'say-ar: ' in rfuText.lower():
                            if user in RfuSekawan or user in Squad["Admin"]:
                                try:
                                    isi = rfuText.lower().replace('say-ar: ','')
                                    tts = gTTS(text=isi, lang='ar', slow=False)
                                    tts.save('temp.mp3')
                                    cl.sendAudio(kirim, 'temp.mp3')
                                except Exception as e:
                                    cl.sendText(kirim, str(e))

                        elif 'say-ko: ' in rfuText.lower():
                            if user in RfuSekawan or user in Squad["Admin"]:
                                try:
                                    isi = rfuText.lower().replace('say-ko: ','')
                                    tts = gTTS(text=isi, lang='ko', slow=False)
                                    tts.save('temp.mp3')
                                    cl.sendAudio(kirim, 'temp.mp3')
                                except Exception as e:
                                    cl.sendText(kirim, str(e))

                        elif 'apakah: ' in rfuText.lower():
                            if user in RfuSekawan or user in Squad["Admin"]:
                                try:
                                    txt = ['iya','tidak','bisa jadi','mungkin saja','tidak mungkin','au ah gelap']
                                    isi = random.choice(txt)
                                    tts = gTTS(text=isi, lang='id', slow=False)
                                    tts.save('temp2.mp3')
                                    cl.sendAudio(kirim, 'temp2.mp3')
                                except Exception as e:
                                    cl.sendText(kirim, str(e))

                        elif 'kapan: ' in rfuText.lower():
                            if user in RfuSekawan or user in Squad["Admin"]:
                                try:
                                    txt = ['kapan kapan','besok','satu abad lagi','Hari ini','Tahun depan','Minggu depan','Bulan depan','Sebentar lagi']
                                    isi = random.choice(txt)
                                    tts = gTTS(text=isi, lang='id', slow=False)
                                    tts.save('temp2.mp3')
                                    cl.sendAudio(kirim, 'temp2.mp3')
                                except Exception as e:
                                    cl.sendText(kirim, str(e))

                        elif "Wikipedia: " in rfuText:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                try:
                                    wiki = rfuText.lower().replace("Wikipedia: ","")
                                    wikipedia.set_lang("id")
                                    pesan="Title ("
                                    pesan+=wikipedia.page(wiki).title
                                    pesan+=")\n\n"
                                    pesan+=wikipedia.summary(wiki, sentences=1)
                                    pesan+="\n"
                                    pesan+=wikipedia.page(wiki).url
                                    cl.sendText(kirim, pesan)
                                except:
                                    try:
                                        pesan="Over Text Limit! Please Click link\n"
                                        pesan+=wikipedia.page(wiki).url
                                        cl.sendText(kirim, pesan)
                                    except Exception as e:
                                        cl.sendText(kirim, str(e))

                        elif rfuText.lower() == 'kalender':
                            if user in RfuSekawan or user in Squad["Admin"]:
                                tz = pytz.timezone("Asia/Makassar")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                cl.sendMessage(kirim, readTime)

                        elif "gambar: " in rfuText.lower():
                            if user in RfuSekawan or user in Squad["Admin"]:
                                try:
                                    query = rfuText.replace("gambar: ", "")
                                    query = query.replace(" ", "+")
                                    gambar = cl.download_image(query)
                                    cl.sendImageWithURL(kirim, gambar)
                                except Exception as e:
                                    cl.sendText(kirim, str(e))                                    

                        elif "youtube: " in rfuText.lower():
                            if user in RfuSekawan or user in Squad["Admin"]:
                                try:
                                    query = rfuText.replace("youtube: ", "")
                                    query = query.replace(" ", "+")
                                    x = cl.youtube(query)
                                    cl.sendText(kirim, x)
                                except Exception as e:
                                    cl.sendText(kirim, str(e))

#--------------------------------- TRANSLATOR -------------------------------------------------#

                        elif rfuText.lower().startswith("indonesian: "):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                sep = rfuText.split(" ")
                                isi = rfuText.replace(sep[0] + " ","")
                                translator = Translator()
                                hasil = translator.translate(isi, dest='id')
                                text = hasil.text
                                cl.sendMessage(kirim, "Translator Indonesian\n\n" + str(text))

                        elif rfuText.lower().startswith("english: "):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                sep = rfuText.split(" ")
                                isi = rfuText.replace(sep[0] + " ","")
                                translator = Translator()
                                hasil = translator.translate(isi, dest='en')
                                text = hasil.text
                                cl.sendMessage(kirim, "Translator English\n\n" + str(text))

                        elif rfuText.lower().startswith("korea: "):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                    sep = rfuText.split(" ")
                                    isi = rfuText.replace(sep[0] + " ","")
                                    translator = Translator()
                                    hasil = translator.translate(isi, dest='ko')
                                    text = hasil.text
                                    cl.sendMessage(kirim, "Translator Korea\n\n" + str(text))

                        elif rfuText.lower().startswith("japan: "):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                sep = rfuText.split(" ")
                                isi = rfuText.replace(sep[0] + " ","")
                                translator = Translator()
                                hasil = translator.translate(isi, dest='ja')
                                text = hasil.text
                                cl.sendMessage(kirim, "Translator Japan\n\n" + str(text))

                        elif rfuText.lower().startswith("thailand: "):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                sep = rfuText.split(" ")
                                isi = rfuText.replace(sep[0] + " ","")
                                translator = Translator()
                                hasil = translator.translate(isi, dest='th')
                                text = hasil.text
                                cl.sendMessage(kirim, "Translator Thailand\n\n" + str(text))

                        elif rfuText.lower().startswith("arab: "):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                sep = rfuText.split(" ")
                                isi = rfuText.replace(sep[0] + " ","")
                                translator = Translator()
                                hasil = translator.translate(isi, dest='ar')
                                text = hasil.text
                                cl.sendMessage(kirim, "Translator Saudi Arabia\n\n" + str(text))

                        elif rfuText.lower().startswith("malaysia: "):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                sep = rfuText.split(" ")
                                isi = rfuText.replace(sep[0] + " ","")
                                translator = Translator()
                                hasil = translator.translate(isi, dest='ms')
                                text = hasil.text
                                cl.sendMessage(kirim, "Translator Malaysia\n\n" + str(text))

                        elif rfuText.lower().startswith("jawa: "):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                sep = rfuText.split(" ")
                                isi = rfuText.replace(sep[0] + " ","")
                                translator = Translator()
                                hasil = translator.translate(isi, dest='jw')
                                text = hasil.text
                                cl.sendMessage(kirim, "Translator Jawa\n\n" + str(text))

    except Exception as error:
        print (error)

#-------------------------------------------- FINNISHING SCRIP ------------------------------------------------#

while True:
    try:
        Operation = RIDEN.singleTrace(count=50)
        if Operation is not None:
            for fast in Operation:
                RIDEN.setRevision(fast.revision)
                thread1 = threading.Thread(target=RIDEN_FAST_USER, args=(fast,))#self.OpInterrupt[fast.type], args=(fast,)
                thread1.start()
                thread1.join()
    except Exception as RIDEN:
        logError(RIDEN)
