################spid_for_tieba#########
################author:chinxue#########
######################log##############
#V1.0：2020-2-8：新增查找目录下文件数量功能，只需要更改设置核心网址
import requests as r
from bs4 import BeautifulSoup
from urllib import parse
import os
from selenium import webdriver
import time
import random
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#6已经下载过的数量
img_cnt=0   ##设置当前页已经下载的图片数量
p_cnt=len(os.listdir("H:\\mod_spid\\tiebapage"))     ##设置文件夹图片计数
#1设置网址
base_url='http://tieba.baidu.com/'
###############核心网址###############
in_ldr='http://tieba.baidu.com/p/6479373918'
###################
child_page_url='http://tieba.baidu.com/photo/p?kw=%E5%AD%99%E5%85%81%E7%8F%A0&ie=utf-8&flux=1&tid='
child_page_add_url='&pn=1&fp=2&see_lz=1'
#2设置存储根目录
save_root_dir='H:\\mod_spid'
##父特性选择a的href值，需要具体调整
fg_first_section='div'
fg_first_key='id'
fg_first_value='pagelet_frs-list/pagelet/thread_list'
#4设置子特征值在select(child_section)
child_section='img.BDE_Image'
#5设置子终源在img.attrs.get(child_src)
child_src='src'
#7浏览器设置
chrome_options=webdriver.ChromeOptions()
#chrome_options.add_argument("--window-size=1920,1080")
#chrome_options.add_argument("--start-maximized")
#chrome_options.add_argument('--headless')
chrome_options.add_argument('-disable-gpu')
chrome_options.add_argument("--window-size=50,50")
chrome_options.binary_location='C:\\Users\\Administrator.USER-20190912HP\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe'
chrome_options.add_argument("--no-sandbox")
#capa = DesiredCapabilities.CHROME
#capa["pageLoadStrategy"] = "none"
##其他变量声明，不需要改
series_url_lists=[]
pic_url_lists=[]
save_dir=[]

####查找子页面img并解密            
def fetch_all_series_pic(url):
    print(url)
    resp=r.get(url).text
    if resp is not None:
        bs=BeautifulSoup(resp,'lxml')
        imgs=bs.select(child_section)
        print('****The page has %d img' %len(imgs))
        for img in imgs:
            s=img.get('src').split('/')[-1][:-4]
            pic_url=(child_page_url+str(url.split('/')[-1])+'&pic_id='+s+child_page_add_url)
            pic_url_lists.append(pic_url)
    print('>>current col img time is :',time.ctime())
####得到大图地址       
def get_big_pic(url):
    #prw=webdriver.Chrome(desired_capabilities=capa,options=chrome_options)
    try:
        prw=webdriver.Chrome(options=chrome_options)
        prw.set_page_load_timeout(20)
        try:
            prw.get(url)
            #time.sleep(random.randint(2,5))
            resp=prw.page_source
            prw.quit()
        except:
            resp=None
            print('get none')
    except:
        resp=None
        print('prw is err')
    if resp is not None:
        bs=BeautifulSoup(resp,'html.parser')
        pics=bs.select('img.image_original_original')
        for pic in pics:
            download_pic(pic.attrs.get('src'))
    else:
        print('get false')

def download_pic(url):
    global p_cnt
    try:
        pic_name=str(p_cnt+1)+url.split('/')[-1][-4:]
        print("**download:"+pic_name)
        img_resp=r.get(url).content
        with open(os.path.join(save_dir,pic_name),'wb+')as f:
            f.write(img_resp)
            p_cnt+=1
    except Exception as reason:
        print('write file err')

def add_ldr(ldr):
    global new_ldr
    new_text=[]
    f=open("ldr.txt")
    old_text=f.readlines()
    f.close()
    for i in old_text:
        new_text.append(i.strip())
    #print(new_text)
    if ldr in new_text:
        print('Sorry,the link has been down.')
        new_ldr=None
    else:
        new_ldr=ldr

if __name__=='__main__':
#    global p_cnt
#    p_cnt=1
    new_ldr=None
    print('**mission start:',time.ctime())
####建立目录
    save_dir=os.path.join(save_root_dir,'tiebapage')
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
####爬取子页加密图片地址
    add_ldr(in_ldr)
    if new_ldr!=None:
        fetch_all_series_pic(new_ldr)
    ####解析真实大图地址
        for pic_url in pic_url_lists[img_cnt:]:
            get_big_pic(pic_url)            ####获得图片
        print("****mission.complate:", time.ctime())
        f = open("ldr.txt","a+")
        f.write(new_ldr+"\n")
        f.close()
    else:
        print("exit")
