# -*-coding:utf-8 -*-
# *-*Author:DreamYee*-*
# Create:2019/09/01 13:31
# File:DemoA.py

# calendar
import calendar
cal = calendar.month(2015,1)
print(cal)

# calendar(year,w = 2, l = 1, c = 6)
year = calendar.calendar(2015)
print(year)

# isleap(year):判断是否为闰年
print(calendar.isleap(2000))

# leapdays(y1,y2):返回在y1,y2两年之间的闰年总数，包括Y1,不包括y2
print(calendar.leapdays(2000,2003))

# month(year,month,w=2,l=1)
print(calendar.month(2015,5))

# monthcalendar(year,month)
print(calendar.monthcalendar(2015,5))

# monthrange(year,month)
print(calendar.monthrange(2015,5))

# weekday(year,month,day)
print(calendar.weekday(2015,5,4))

# time
# time()
import time
print(time.time())
print(time.localtime())

# gmtime()
import time
print(time.gmtime())

# asctime()当前日期时间和星期
print(time.asctime())

h = time.localtime(1000000)
print(h)

# ctime()
print(time.ctime())

# mktime()
lt = time.localtime()
print(lt)

# strftime()
print(time.strftime("%y,%m,%d"))
'''
格式	    含义	         取值范围（格式）
%y	去掉世纪的年份	00-99，如"15"
%Y	完整的年份	如"2015"
%j	指定日期是一年中的第几天	001-366
%m	返回月份	01-12
%b	本地简化月份的名称	简写英文月份
%B	本地完整月份的名称	完整英文月份
%d	该月的第几日	如5月1日返回"01"
%H	该日的第几时（24小时制）	00-23
%l	该日的第几时（12小时制）	01-12
%M	分钟	00-59
%S	秒	00-59
%U	在该年中的第多少星期（以周日为一周起点）	00-53
%W	同上，只不过是以周一为起点	00-53
%w	一星期中的第几天	0-6
%Z	时区	在中国大陆测试，返回CST，即China Standard Time
%x	日期	日/月/年
%X	时间	时:分:秒
%c	详细日期时间	日/月/年 时:分:秒
%%	‘%’字符	‘%’字符
%p	上下午	AM or PM
'''

# strptime()
today = time.strftime("%y,%m,%d")
print(today)
print(time.strptime(today,"%y,%m,%d"))

# datetime
'''
datetime.date：日期类，常用的属性有year/month/day
datetime.time：时间类，常用的有hour/minute/second/microsecond
datetime.datetime：日期时间类
datetime.timedelta：时间间隔，即两个时间点之间的时间长度
datetime.tzinfo：时区类
'''
# date类
import datetime
today = datetime.date.today()
print(today)

# time类
t = datetime.time(1,2,3)
print(t)

# timedelta类
now = datetime.datetime.now()
print(now)
# 对now增加5个小时
b = now+datetime.timedelta(hours=5)
print(b)
c = now+datetime.timedelta(weeks=2)
print(c)
d = c- b
print(d)