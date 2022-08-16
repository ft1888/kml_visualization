import time
import datetime
import pytz
a='zhengque'
if bool(a)==True:
    print('测试成功')
else:
    print('测试失败')


# src=[]
# with open('anjie.kml', 'r', encoding='utf-8') as f:
#     lines = f.readlines()
#     # for line in lines:
#     #     if 'snippet' in line:
#     #         print('安卓文件')
#     #     else:
#     #         pass
#     for line in lines:
#         try:
#             if 'src' in line:
#                 #print(line.split('"')[3])
#                 src.append(line.split('"')[3])
#         except:
#             print('检索失败')
#
# print(src)
# tz = pytz.timezone('Asia/Shanghai')  # 东八区
# timestamp=1646385428
#
# t = datetime.datetime.fromtimestamp(int(timestamp), pytz.timezone('Asia/Shanghai')).strftime('%Y-%m-%d %H:%M:%S')
#
# print(t)
#
# time_local = time.localtime(int(timestamp))  # 注意：这里的整数不能超过11位数
#
# pub_date = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
# pub_time = time.strftime("%H:%M:%S", time_local)
#
# print(pub_time)
# print(pub_date)
