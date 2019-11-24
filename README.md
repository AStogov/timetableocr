# Time Table OCR
This is an ocr application to analysis school's timetable.

[Click here](http://oken.club:81/upload) to see how this application works (badly). (Attention: Django debug mode is on)

Note: You should add your own tencent cloud api certification to [main.py](https://github.com/AStogov/timetableocr/blob/master/app/main.py) in line 10.



# 课表识别程序

这是一个简易的课表识别(OCR实现)程序，能识别<del>具有高识别度的</del>课表。

[点击这里](http://oken.club:81/upload)来使用实例 (注意: Django开启了调试模式，任何错误信息都会被输出)

注意：你需要先配置位于app文件夹下的[main.py](https://github.com/AStogov/timetableocr/blob/master/app/main.py)文件，在第10行添加自己的腾讯云api密钥。



## 如何获得一份可以识别的课表

1. 在微信公众号：武汉理工教务处中，截取课程表。
   <br /><img src="https://github.com/AStogov/timetableocr/blob/master/1.PNG" width="40%" alt=""/>
2. 裁剪课表到仅保留课表内容。
   <br /><img src="https://github.com/AStogov/timetableocr/blob/master/2.PNG" width="40%" alt=""/>
3. 使用图片编辑程序调整鲜明度为100，对比度为-100，清晰度为100。
   <br /><img src="https://github.com/AStogov/timetableocr/blob/master/3.PNG" width="40%" alt=""/>
4. 上传文件到[此处](http://oken.club:81/upload)



