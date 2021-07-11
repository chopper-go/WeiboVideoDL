# coding=utf-8
# 作者【乔巴】： https://github.com/chopper-go

from urllib.parse import unquote_plus
import requests,re
import subprocess 
import os
from urllib import parse


# 根据需求修改参数
spath=r'E:\'  #视频保存路径
url = 'https://weibo.com/3222817584/KohjcjTEI'  #需要下载的微博链接
cookie="SINAGLOBAL=..."  #自己的会员cookie
vpath=r'c:\temp\v.mp4'  #临时文件路径
apath=r'c:\temp\a.mp4'  #临时文件路径
ffpath=r'C:\ffmpeg\bin\ffmpeg.exe'  


head1 = {
        "referer": url,
        "Cookie": cookie,
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
    }

res = requests.get(url,headers=head1)
r = res.content.decode('utf-8','ignore')

# t = r'usercard=\"name=(.*?)<a  suda-uatrack='
# tit = re.findall(t, r)
# title = tit[0]

# mediaID = re.findall(r'dash&type=feedvideo&objectid=(.*?)&keys=', r)  #getdash链接, 1080p+ 关键字
mediaID = re.findall(r'1034-video:(.*?):', r)  # 4k, 1080p
mediaID = unquote_plus(mediaID[0])

try:
    url='https://weibo.com/aj/video/getdashinfo?ajwvr=6&media_ids='+str(mediaID) #实际dash链接
except:
    pass

print(url)

file = requests.get(url,headers=head1).json()

if file['data'] ==[]:  #720p 竖
    v2 = re.findall(r'fluency=(.*?)&', r)#720p 关键字
    # v2 = re.findall(r'&video_src=(.*?)&', r) #720p 竖版，关键字
    v3=unquote_plus(v2[0])
    v3= parse.unquote(v3)
    v3= parse.unquote(v3)
    vlabel =re.findall(r'mp4_(.*?)&', v3)[0]  #分辨率
    savepath =spath+'-['+ vlabel + '][菜包时光机].mp4'
    mp4 = requests.get(v3)  #下载视频
    with open(savepath, 'wb') as f:
        f.write(mp4.content)
        f.close()
    print('下载完成：', savepath)
    quit()


play= file['data']['list'][0]['details']
try:
    v = play[0]['play_info']['url']  #获取视频链接，最高分辨率
except:
    v = play[1]['play_info']['url']    
vlabel =re.findall(r'dash_(.*?)&', v)[0]  #分辨率
vlabel=unquote_plus(vlabel)

a = play[-1]['play_info']['url']  #获取音频链接 
# alabel = play[-1]['play_info']['audio_sample_rate']

mp4 = requests.get(v)  #下载视频
with open(vpath, 'wb') as f:
    f.write(mp4.content)
    f.close()

mp3 = requests.get(a)  #下载音频
with open(apath, 'wb') as f:
    f.write(mp3.content)
    f.close()
# print('下载成功')



if vlabel=='2160p': vlabel='4k'
savepath =spath+'-['+ vlabel + '].mp4'
cmd = ffpath + ' -i '+ vpath + ' -i '+ apath + ' -c:v copy -c:a aac -strict experimental '+ savepath    #合并视频+音频
subprocess.call(cmd, shell=True)
os.remove(vpath)
os.remove(apath)
print('合并完成，保存至'+savepath)
