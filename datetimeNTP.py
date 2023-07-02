import random
import ntplib  #导入用于与NTP服务器进行通信的库
from datetime import datetime,timezone,timedelta  #导入用于处理日期和时间的库和用于处理时间间隔的库
def get_ntp_time_china():  #定义一个函数来获取NTP时间，并将其转换为东八区时间
    ntp_servers = ['ntp.aliyun.com','time.cloud.tencent.com','cn.ntp.org.cn','ntp.ntsc.ac.cn']  #NTP服务器列表
    selecte_server = random.choice(ntp_servers)  #随机选择一个NTP服务器
    c = ntplib.NTPClient()  #创建一个NTPClient对象，用于与NTP服务器建立连接
    response = c.request(selecte_server)  #使用随机选择的服务器进行请求
    offset = response.offset  #获取NTP服务器与UTC时间的偏移量
    ntp_time = datetime.fromtimestamp(response.tx_time - offset, timezone.utc)  #将NTP时间转换为datetime对象
    ntp_time = ntp_time.astimezone(timezone(timedelta(hours=8)))  #将NTP时间转换为东八区时间
    weekday_cn = {'0': '日', '1': '一', '2': '二', '3': '三', '4': '四', '5': '五', '6': '六'}#将十进制的星期与中文对照
    weekday = weekday_cn.get(ntp_time.strftime('%w'))  #获取本地十进制星期时间
    return ntp_time.strftime('%Y年%m月%d日 星期') + weekday + ntp_time.strftime(' %H:%M:%S'),selecte_server  #对输出的内容进行格式化，并添加上中文的星期
# 获取NTP时间并打印
datetimeNTP,NTPserver = get_ntp_time_china()  # 调用函数获取NTP时间
print('NTP服务器','[',NTPserver,']')
print(datetimeNTP)
