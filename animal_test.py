from pykml import parser
from pykml.factory import nsmap
from lxml import html
from operator import itemgetter


def find_src(str):  # 提取图片链接
    return str.split(' ')[6].split('"')[:][1]


def find_lng(str):  # 经度
    return str.split('</br>')[1].split('</div>')[0].replace('<div>经度：', '')


def find_lat(str):  # 纬度
    return str.split('</br>')[1].split('</div>')[1].replace('<div>纬度：', '')


def find_alt(str):  # 海拔
    return str.split('</br>')[1].split('</div>')[2].replace('<div>海拔：', '')


def find_time(str):  # 时间
    return str.split('</br>')[1].split('</div>')[3].replace('<div>时间：', '')


def find_timepro(str):  # 时间比较
    return int(str.split(' ')[1].split(':')[0]) * 60 + int(str.split(' ')[1].split(':')[1]) + int(
        str.split(' ')[1].split(':')[2]) / 60


namespace = {"ns": nsmap[None]}

with open('test_li.kml', 'r', encoding='utf-8') as f:
    # doc = parser.parse(f)
    # print(type(doc))
    root = parser.parse(f).getroot()

    pms = root.xpath(".//ns:Placemark[.//ns:description]", namespaces=namespace)  # 精确查找
    pmn = root.xpath(".//ns:Placemark[.//ns:name]", namespaces=namespace)
    pma = root.findall(".//ns:Placemark", namespaces=namespace)
    place = root.xpath(".//ns:Placemark", namespaces=namespace)
    root1 = root.xpath(".//ns:Placemark[.//ns:ExtendedData]", namespaces=namespace)

for pm in pms:
    if 'src' in pm.description.text:
        #print(find_src(pm.description.text))
        print(pm.description.text.split('src')[1].split('"')[:][1])
# for pm in pma:
    # print(pm.Point.coordinates.text)
     #print(pm.name.text)
    # print(pm.TimeStamp.when)
    # try:
    #     print(pm.description)
    # except:
    #     try:
    #         print(pm.name.text)
    #     except:
    #         print('无描述信息')

# for i in range(2, len(pma) - 1):
#     try:
#         if pma[i].name.text:
#             print(pma[i].name.text)
#         else:
#             print('该图片没有名称')
#     except:
#         print('该图片没有名称')
#     print(str(pma[i].Point.coordinates).split(',')[0])
#     print(pma[i].ExtendedData.Data[3].value)



# for pm in pms:
#     print(pm.a.text)


info = []
name = []

 # for pm in root1:
 #     print(pm.value.text)

# for i in range(len(place) - 1):
#     try:
#         # print(place[i].name)
#         if 'src' in place[i].description.text:
#             info.append(place[i].description.text)
#             try:
#                 name.append(str(place[i].ExtendedData.Data[9].value)[:10])
#                 # for pms in place[i].ExtendedData.Data:
#                 #     print(pms[9].value)
#             except:
#                 name.append('该图片没有名称')
#     except:
#         print('存在异常')
# print(info)
# print(name)


# time_t = []
# for filename in info:
#     time_t.append(find_time(filename))
# print(time_t)
#
# time_c=[]
# for filename in time_t:
#     time_c.append(find_timepro(filename))
# print(time_c)
# # print(pms)
# pms = root.findall(".//ns:Placemark", namespaces=namespace)



# for pm in pmn:
#     print(pm.name)

# for pm in root.iterchildren():
#     if hasattr(pm, 'Placemark'):
#         print(pm.Placemark.description)
