#!/usr/bin/env Python3
# -*- encoding:utf-8 *-*
from urllib import request
import re   #使用正则表达式
import io
import os
import sys
import ssl
import urllib.request

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

def getResponse(url):
    #url请求对象 Request是一个类
    url_request = request.Request(url)
    #print("Request对象的方法是：",url_request.get_method())
    
    #上下文使用的对象，包含一系列方法
    #url_response = request.urlopen(url) #打开一个url或者一个Request对象
    url_response = request.urlopen(url_request)
    '''
       geturl()：返回 full_url地址
         info(): 返回页面的元(Html的meta标签)信息
         <meta>：可提供有关页面的元信息（meta-information），比如针对搜索引擎和更新频度的描述和关键词。
      getcode(): 返回响应的HTTP状态代码 
      100-199 用于指定客户端应相应的某些动作。
      200-299 用于表示请求成功。      ------>  200
      300-399 用于已经移动的文件并且常被包含在定位头信息中指定新的地址信息。
      400-499 用于指出客户端的错误。  ------>  404
      500-599 用于支持服务器错误。 
         read(): 读取网页内容，注意解码方式(避免中文和utf-8之间转化出现乱码)
    '''
    # print("urlresponse=")
    # print(url_response)
    return url_response   #返回这个对象


def getJpg(data):
    jpglist = re.findall(r'src="http.+?.jpg"',data)
    return  jpglist

def datacutup(data):
	data=(str(data)).replace("\n","")
	data=(str(data)).replace("\t","")
	data=(str(data)).replace("\r","")
	data=(str(data)).replace(" ","")
	data=(str(data)).replace(" ","")
	data=(str(data)).replace(u'\u3000',u'')
	data=(str(data)).replace("\[","")
	return data

def gettitle(data):
	re_title_rule=r'<title>(.*?)-故宫博物院</title>'
	tm=re.findall(re_title_rule, data)
	return tm[0]

def getimg(data):
	re_img_rule=r'<imgtilegenerator="0"(.*?)/>'
	return re.findall(re_img_rule, data)

def getinfo(data):
	re_info_rule=r'<BR>(.*?)</p>'
	tm=re.findall(re_info_rule, data)
	tm=str(tm)
	tm=re.sub(r'<.*?>',"",tm)
	tm=re.sub(r'TAG.*',"",tm)
	tm=re.sub(" ","",tm)
	return str(tm)


def downLoad(jpgUrl,n,name):
    picname=name+str(n)
    try:
        request.urlretrieve(jpgUrl,'%s.jpg'  %picname)   
    except Exception as e:
        print(e)
    finally:
        print('图片%s下载操作完成' % n)


def main():
	ssl._create_default_https_context = ssl._create_unverified_context
	start_num=559
	maxnum=100
	pathroot=os.getcwd()  

	i=0
	while i<maxnum:		
		#go back to the root directory
		os.chdir(pathroot)

		#make next url
		i+=1
		url="https://www.dpm.org.cn/collection/ceramic/227"+str(start_num+i)+".html"
		http_response = getResponse(url) 

		#get web data
		data=http_response.read().decode('utf-8')
		data=datacutup(data)	

		#get title, img, info	
		title=str(i)+gettitle(data)
		jpgarray=getimg(data)
		infomation=getinfo(data)

		#create a new file
		dirname=pathroot+"//"+str(title)
		print(dirname)
		if os.path.exists(dirname) is False :
			os.mkdir(dirname)
		os.chdir(dirname)
		f = open(title+".txt",'w',encoding='utf-8') # 写模式
		f.write(infomation)

		#download picture
		global n
		n=1
		for item in jpgarray:
			jpg_download=re.findall(r'src="(.*?)"',item)
			print(jpg_download[0])
			downLoad(jpg_download[0],n,title)
			n=n+1

if __name__ == "__main__":
    main()