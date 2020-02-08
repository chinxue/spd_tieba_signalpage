import os
path='/home/pi/share/tiebapage'
text1="INSERT INTO `dede_addon17` VALUES('"
text2="','1','-17','0','1','0','"
text3="','1580826452','','','192.168.1.9','0','0','0','0','','/uploads/141108/"
text4="');"
f=open("/home/pi/share/dede_addon17_0_e7248237f0876069.txt",'a')
num=len(os.listdir("/var/www/abc/uploads/141108"))
for i in os.listdir(path):
    # print(i)
    text=text1+str(num)+text2+i[:-4]+text3+i+text4+"\n"
    f.write(text)
    num+=1
f.close()
print(num)
