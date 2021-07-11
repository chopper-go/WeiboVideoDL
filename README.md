# WeiboVideoDL
下载微博视频，默认最高画质

【使用说明】

1.必须先修改cookie，才能使用。如果是会员cookie，可下载4K。

     cookie固定，不需要每次使用时修改。

2.使用前打开main.py，修改参数
~~~
spath=r'E:\小米牙啃小树枝'            #视频保存路径+文件名
url = 'https://weibo.com/3222817584/KohjcjTEI'          #微博链接
cookie="SINAGLOBAL=..."      #会员cookie
vpath=r'c:\temp\v.mp4'       #临时视频路径
apath=r'c:\temp\a.mp4'       #临时音频路径
ffpath=r'C:\ffmpeg\bin\ffmpeg.exe'   #ffmpeg本机路径
~~~

## cookie获取方式
1. 浏览器打开 https://weibo.com/3222817584/KohjcjTEI ，登录微博账号
2. 按F12 打开开发人员工具，搜索框输入dash，刷新网页
3. 选中左侧第一条，右侧找到cookie，复制整段（SINAGLOBAL=.....%7D）

![image](https://github.com/chopper-go/WeiboVideoDL/blob/main/image/wb.jpg)
