# Cpanorama_Server
#this is panorama img slice api server

该项目使用flask编写，运行flasktest启动。

目前有两个有用的接口。

+/upload

+/deal

/upload接口上传全景图片（一个传参'file'），返回code和name。

/deal接口处理全景图片，两个参数:

+fileName:返回code

+imgName:返回name

