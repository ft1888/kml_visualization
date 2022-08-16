# coding:utf-8
import os
import sys
import requests
from pykml import parser
from pykml.factory import nsmap

from PyQt5.QtGui import QPixmap, QKeySequence, QImage
from PyQt5.QtWidgets import QApplication, QGraphicsScene, QGraphicsPixmapItem, QFileDialog, QMainWindow, \
    QShortcut
from animal import Ui_kml_animal
import xlwt
import xlrd
import csv
import time


class MyMainForm(QMainWindow, Ui_kml_animal):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        QShortcut(QKeySequence("Up"), self, self.openPrevImg)
        QShortcut(QKeySequence("Down"), self, self.openNextImg)

        self.readkml.clicked.connect(self.openDirDialog)
        self.nextpage.clicked.connect(self.openNextImg)
        self.prepage.clicked.connect(self.openPrevImg)
        self.starttime.clicked.connect(self.Start)
        self.endtime.clicked.connect(self.End)
        self.record.clicked.connect(self.RecordActivity)
        self.exportcsv.clicked.connect(self.Csv_Export)
        # self.initialize.clicked.connect(self.initialization)

        self.radioButton_1.clicked.connect(self.rb1)
        self.radioButton_2.clicked.connect(self.rb2)
        self.radioButton_3.clicked.connect(self.rb3)
        self.radioButton_4.clicked.connect(self.rb4)
        self.radioButton_5.clicked.connect(self.rb5)
        self.radioButton_6.clicked.connect(self.rb6)
        self.radioButton_7.clicked.connect(self.rb7)
        self.radioButton_8.clicked.connect(self.rb8)
        self.radioButton_9.clicked.connect(self.rb9)
        self.radioButton_11.clicked.connect(self.rb11)
        self.radioButton_12.clicked.connect(self.rb12)

        self.cwd = os.getcwd()  # 获取当前程序文件位置
        self.srcpath = ''
        self.file_index = 0
        self.src = []
        self.lng = []
        self.lat = []
        self.alt = []
        self.time = []
        self.info = []
        self.name = []
        self.image = QPixmap()
        self.activity = ''
        self.visitorid = ''
        self.record_index = 1
        self.start_index = 1
        self.end_index = 1
        self.info_record = xlwt.Workbook(encoding='utf-8', style_compression=0)  # 新建一个excel
        self.sheet = self.info_record.add_sheet('sheet1')  # 新建一个sheet
        self.detect = []  # 检查是安卓文件还是苹果文件
        self.start = ''  # 记录开始时间
        self.end = ''  # 记录结束时间

    # def wheelEvent(self, event):
    #     self.information.clear()
    #     delta = event.angleDelta()
    #     oriention = delta.y() / 8
    #     if oriention < 0:
    #         self.file_index += 1
    #         if self.file_index >= len(self.src):
    #             self.file_index = len(self.src) - 1
    #         if self.file_index == len(self.src) - 1:
    #             self.information.setText('\n\n\n\n这是最后一张图片了，辛苦您啦！')
    #
    #         if len(self.src) <= 0 or self.file_index >= len(self.src):
    #             return
    #         url = self.src[self.file_index]
    #         res = requests.get(url)
    #         img = QImage.fromData(res.content)  # 加载网络图片
    #         self.image = QPixmap.fromImage(img)
    #         self.LoadPic()
    #         self.information.setText(
    #             '时间：' + self.time[self.file_index] + '\n经度：' + self.lng[self.file_index] + '\n纬度：' + self.lat[
    #                 self.file_index] + '\n海拔：' + self.alt[self.file_index])
    #         self.picname.setText(self.name[self.file_index])
    #
    #
    #     else:
    #         self.file_index -= 1
    #         if self.file_index < 0:
    #             self.file_index = 0
    #
    #         if len(self.src) <= 0 or self.file_index >= len(self.src):
    #             return
    #         url = self.src[self.file_index]
    #         res = requests.get(url)
    #         img = QImage.fromData(res.content)  # 加载网络图片
    #         self.image = QPixmap.fromImage(img)
    #         self.LoadPic()
    #         self.information.setText(
    #             '时间：' + self.time[self.file_index] + '\n经度：' + self.lng[self.file_index] + '\n纬度：' + self.lat[
    #                 self.file_index] + '\n海拔：' + self.alt[self.file_index])
    #         self.picname.setText(self.name[self.file_index])

    def openDirDialog(self):
        self.initialization()
        dirpath, filetype = QFileDialog.getOpenFileName(self,
                                                        "选取文件",
                                                        self.cwd, "kml文件(*.kml)")  # 起始路径

        if dirpath == "":
            print("\n取消选择")
            return

        self.srcpath = dirpath

        self.visitornumber.setText(os.path.basename(dirpath).split('.')[0])  # 标记最后一级路径名称,显示游客编号
        self.visitorid = os.path.basename(dirpath).split('.')[0]

        for snippet in self.an_or_mac(dirpath):  # 判断是安卓文件还是苹果文件
            self.detect.append(snippet)

        if self.detect:
            for filename in self.scanAllInfo_Android(dirpath):
                self.src.append(filename[0])  # 获取图片url
                self.time.append(filename[2])  # 获取时间
                self.name.append(filename[1])  # 获取名称
                self.lng.append(filename[3])  # 获取经度
                self.lat.append(filename[4])  # 获取纬度
                self.alt.append(filename[5])  # 获取海拔
        else:
            for filename in self.scanAllInfo(dirpath):  # 初始信息获取
                self.info.append(filename[0])  # 获取info
                self.time.append(filename[2])  # 获取时间
                self.name.append(filename[1])  # 获取名称
                self.lng.append(filename[3])  # 获取经度
                self.lat.append(filename[4])  # 获取纬度
                self.alt.append(filename[5])  # 获取海拔

            for filename in self.find_src(self.info):  # 获取图片url
                self.src.append(filename)
        if not self.src:
            self.feedback.setText('未解析到图像信息，3秒后退出程序')
            time.sleep(3)
            return

        # for filename in self.find_time(self.info):  # 获取时间
        #     self.time.append(filename)
        # print(self.src)
        url = self.src[self.file_index]
        res = requests.get(url)
        img = QImage.fromData(res.content)  # 加载网络图片
        self.image = QPixmap.fromImage(img)
        self.LoadPic()

        self.information.setText(
            '时间：' + self.time[self.file_index] + '\n经度：' + self.lng[self.file_index] + '\n纬度：' + self.lat[
                self.file_index] + '\n海拔：' + self.alt[self.file_index])

        self.picname.setText(self.name[self.file_index])

        self.sheet.write(0, 0, '游客编号')
        self.sheet.write(0, 1, '活动编号')
        self.sheet.write(0, 2, '活动类型')
        self.sheet.write(0, 3, '活动地点')
        self.sheet.write(0, 4, '开始时间')
        self.sheet.write(0, 5, '结束时间')
        self.sheet.write(0, 6, '经度')
        self.sheet.write(0, 7, '纬度')
        self.sheet.write(0, 8, '海拔')

    def openNextImg(self):
        self.feedback.clear()
        self.file_index += 1
        if self.file_index >= len(self.src):
            self.file_index = len(self.src) - 1
        if self.file_index == len(self.src) - 1:
            self.feedback.setText('这是最后一张图片了，辛苦您啦！')

        if len(self.src) <= 0 or self.file_index >= len(self.src):
            return

        url = self.src[self.file_index]
        res = requests.get(url)
        img = QImage.fromData(res.content)  # 加载网络图片
        self.image = QPixmap.fromImage(img)
        self.LoadPic()
        self.information.setText(
            '时间：' + self.time[self.file_index] + '\n经度：' + self.lng[self.file_index] + '\n纬度：' + self.lat[
                self.file_index] + '\n海拔：' + self.alt[self.file_index])
        self.picname.setText(self.name[self.file_index])

    def openPrevImg(self):
        self.file_index -= 1
        if self.file_index < 0:
            self.file_index = 0

        if len(self.src) <= 0 or self.file_index >= len(self.src):
            return
        url = self.src[self.file_index]
        res = requests.get(url)
        img = QImage.fromData(res.content)  # 加载网络图片
        self.image = QPixmap.fromImage(img)
        self.LoadPic()
        self.information.setText(
            '时间：' + self.time[self.file_index] + '\n经度：' + self.lng[self.file_index] + '\n纬度：' + self.lat[
                self.file_index] + '\n海拔：' + self.alt[self.file_index])
        self.picname.setText(self.name[self.file_index])
        self.feedback.clear()

    def an_or_mac(self, folderpath):
        detect = []
        with open(folderpath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines:
                if 'snippet' in line:
                    detect.append('snippet')
                else:
                    pass
        return detect

    def LoadPic(self):
        self.graphicsView.scene = QGraphicsScene()  # 创建一个图片元素的对象
        item = QGraphicsPixmapItem(self.image)  # 创建一个变量用于承载加载后的图片
        self.graphicsView.scene.addItem(item)  # 将加载后的图片传递给scene对象
        self.graphicsView.setScene(self.graphicsView.scene)
        self.graphicsView.fitInView(QGraphicsPixmapItem(QPixmap(self.image)))  # 图像自适应大小

    def Start(self):
        self.start_index = self.file_index
        self.information_s.setText(
            '开始时间：' + self.time[self.start_index] + '\n活动类型：' + self.activity + '\n活动地点：' + self.activityplace.text())
        self.start = self.time[self.start_index]

    def End(self):
        self.end_index = self.file_index
        self.information_e.setText(
            '结束时间：' + self.time[self.end_index])
        self.end = self.time[self.end_index]

    def RecordActivity(self):
        if self.activity and self.activityplace.text() and self.start:
            self.sheet.write(self.record_index, 0, self.visitorid)
            self.sheet.write(self.record_index, 1, self.record_index)
            self.sheet.write(self.record_index, 2, self.activity)
            self.sheet.write(self.record_index, 3, self.activityplace.text())
            self.sheet.write(self.record_index, 4, self.start)
            self.sheet.write(self.record_index, 5, self.end)
            self.sheet.write(self.record_index, 6, self.lng[self.start_index])
            self.sheet.write(self.record_index, 7, self.lat[self.start_index])
            self.sheet.write(self.record_index, 8, self.alt[self.start_index])
            self.feedback.setText(
                '该条活动记录成功！活动信息如下：' + '\n活动类型：' + self.activity + '\n活动地点：' + self.activityplace.text() + '\n开始时间：' +
                self.start + '\n结束时间：' + self.end + '\n经度：' + self.lng[
                    self.start_index] + '\n纬度：' + self.lat[self.start_index] + '\n海拔：' + self.alt[self.start_index])
            self.record_index += 1
            self.activityplace.clear()  # 清空输入框
            self.information_e.clear()
            self.information_s.clear()

            self.radioButton_10.setChecked(True)
            self.activity = ''
            self.start = ''
            self.end = ''
        elif self.activity and self.activityplace.text() and bool(self.start) == False:
            self.sheet.write(self.record_index, 0, self.visitorid)
            self.sheet.write(self.record_index, 1, self.record_index)
            self.sheet.write(self.record_index, 2, self.activity)
            self.sheet.write(self.record_index, 3, self.activityplace.text())
            self.sheet.write(self.record_index, 4, self.start)
            self.sheet.write(self.record_index, 5, self.end)
            self.feedback.setText(
                '该条活动记录成功！活动信息如下：' + '\n活动类型：' + self.activity + '\n活动地点：' + self.activityplace.text() + '\n开始时间：' +
                self.start + '\n结束时间：' + self.end + '\n经度：' + '\n纬度：' + '\n海拔：')
            self.record_index += 1
            self.activityplace.clear()  # 清空输入框
            self.information_e.clear()
            self.information_s.clear()

            self.radioButton_10.setChecked(True)
            self.activity = ''
            self.start = ''
            self.end = ''

        else:
            self.feedback.setText('该条活动信息尚未完善，请检查')

    def Csv_Export(self):
        savepath, filetype = QFileDialog.getSaveFileName(self,
                                                         "文件保存",
                                                         self.cwd, "csv文件(*.csv)")  # 起始路径

        if savepath == "":
            self.feedback.setText('文件未保存')
            # print("\n取消选择")
            return
        xlspath = os.path.dirname(savepath) + '/' + os.path.basename(savepath).split('.')[0] + '.xls'
        self.info_record.save(xlspath)
        # data = pd.read_excel(xlspath, 'sheet1', index_col=0)
        # data.to_csv(savepath, encoding='utf_8_sig')
        self.xls_to_csv(xlspath, savepath)
        os.remove(xlspath)
        self.feedback.setText('文件保存成功！保存路径为:' + '\n' + savepath)

    def initialization(self):
        self.graphicsView.scene = QGraphicsScene()
        self.graphicsView.setScene(self.graphicsView.scene)
        self.graphicsView.scene.clear()
        # self.visitornumber.clear()
        self.activityplace.clear()
        self.information.clear()
        self.information_s.clear()
        self.information_e.clear()
        self.feedback.clear()
        self.srcpath = ''
        self.file_index = 0
        self.src = []
        self.lng = []
        self.lat = []
        self.alt = []
        self.time = []
        self.name = []
        self.info = []
        self.image = QPixmap()
        self.activity = ''
        self.visitorid = ''
        self.record_index = 1
        self.start_index = 1
        self.end_index = 1
        self.info_record = xlwt.Workbook(encoding='utf-8', style_compression=0)  # 新建一个excel
        self.sheet = self.info_record.add_sheet('sheet1')  # 新建一个sheet
        self.detect = []
        self.start = ''
        self.end = ''

    def xls_to_csv(self, xlspath, savepath):
        workbook = xlrd.open_workbook(xlspath)
        table = workbook.sheet_by_index(0)
        with open(savepath, 'w', encoding='utf_8_sig', newline='') as f:
            write = csv.writer(f)
            for row_num in range(table.nrows):
                row_value = table.row_values(row_num)
                write.writerow(row_value)

    def rb1(self):
        self.activity = '入园'
        self.endtime.setEnabled(False)

    def rb2(self):
        self.activity = '参观'
        self.endtime.setEnabled(True)

    def rb3(self):
        self.activity = '游乐'
        self.endtime.setEnabled(True)

    def rb4(self):
        self.activity = '休息'
        self.endtime.setEnabled(True)

    def rb5(self):
        self.activity = '就餐'
        self.endtime.setEnabled(True)

    def rb6(self):
        self.activity = '如厕'
        self.endtime.setEnabled(False)

    def rb7(self):
        self.activity = '其他服务'
        self.endtime.setEnabled(False)

    def rb8(self):
        self.activity = '寻路'
        self.endtime.setEnabled(False)

    def rb9(self):
        self.activity = '离园'
        self.endtime.setEnabled(False)

    def rb11(self):
        self.activity = '上车'
        self.endtime.setEnabled(False)

    def rb12(self):
        self.activity = '下车'
        self.endtime.setEnabled(False)

    def scanAllInfo(self, folderPath):
        info = []
        name = []
        time = []
        lng = []
        lat = []
        alt = []
        store = []
        namespace = {"ns": nsmap[None]}
        with open(folderPath, 'r', encoding='utf-8') as f:
            root = parser.parse(f).getroot()
            pms = root.xpath(".//ns:Placemark", namespaces=namespace)  # 精确查找
        for i in range(len(pms) - 1):
            try:
                if 'src' in pms[i].description.text:
                    info.append(pms[i].description.text)
                    try:
                        name.append(pms[i].name.text)
                    except:
                        name.append('该图片没有名称')
                    try:
                        lng.append(str(pms[i].ExtendedData.Data[4].value))
                    except:
                        lng.append('无经度信息')
                    try:
                        lat.append(str(pms[i].ExtendedData.Data[5].value))
                    except:
                        lat.append('无纬度信息')
                    try:
                        alt.append(str(pms[i].ExtendedData.Data[6].value))
                    except:
                        alt.append('无海拔信息')
                    try:
                        time.append(self.time_convert(str(pms[i].ExtendedData.Data[9].value)[:10]))
                    except:
                        time.append('无时间信息')
            except:
                print('存在异常')

        for i in range(len(info)):
            store.append([info[i], name[i], time[i], lng[i], lat[i], alt[i]])
        # store.sort(key=itemgetter(0))  # 按照第一项进行排序
        return store

    def scanAllInfo_Android(self, folderPath):
        info = []
        name = []
        time = []
        lng = []
        lat = []
        alt = []
        store = []
        namespace = {"ns": nsmap[None]}
        with open(folderPath, 'r', encoding='utf-8') as t:
            lines = t.readlines()
            for line in lines:
                try:
                    if 'src' in line:
                        info.append(line.split('src')[1].split('"')[:][1])
                except:
                    info.append('无图片链接')
        t.close()

        with open(folderPath, 'r', encoding='utf-8') as f:
            root = parser.parse(f).getroot()
            pms = root.xpath(".//ns:Placemark", namespaces=namespace)  # 精确查找

        for i in range(2, len(pms) - 1):
            try:
                if pms[i].name.text:
                    name.append(pms[i].name.text)
                else:
                    name.append('该图片没有名称')
            except:
                name.append('该图片没有名称')
            try:
                time.append(self.time_convert(str(pms[i].ExtendedData.Data[3].value)[:10]))
            except:
                time.append('无时间信息')
            try:
                lng.append(str(pms[i].Point.coordinates).split(',')[0])
            except:
                lng.append('无经度信息')
            try:
                lat.append(str(pms[i].Point.coordinates).split(',')[1])
            except:
                lat.append('无纬度信息')
            try:
                alt.append(str(pms[i].Point.coordinates).split(',')[2])
            except:
                alt.append('无海拔信息')

        for i in range(len(info)):
            store.append([info[i], name[i], time[i], lng[i], lat[i], alt[i]])
        # store.sort(key=itemgetter(0))  # 按照第一项进行排序
        return store

    def find_src(self, list):  # 提取图片链接
        src = []
        for i, file in enumerate(list):
            src.append(file.split('src')[1].split('"')[:][1])
        return src

    def find_lng(self, list):  # 经度
        lng = []
        for i, file in enumerate(list):
            lng.append(file.split('</br>')[1].split('</div>')[0].replace('<div>经度：', ''))
        return lng

    def find_lat(self, list):  # 纬度
        lat = []
        for i, file in enumerate(list):
            lat.append(file.split('</br>')[1].split('</div>')[1].replace('<div>纬度：', ''))
        return lat

    def find_alt(self, list):  # 海拔
        alt = []
        for i, file in enumerate(list):
            alt.append(file.split('</br>')[1].split('</div>')[2].replace('<div>海拔：', ''))
        return alt

    def find_time(self, list):  # 时间
        time = []
        for i, file in enumerate(list):
            time.append(file.split('</br>')[1].split('</div>')[3].replace('<div>时间：', ''))
        return time

    def find_timepro(self, list):  # 时间比较
        time_t = []
        for i, file in enumerate(list):
            time_t.append(int(file.split(' ')[1].split(':')[0]) * 60 + int(file.split(' ')[1].split(':')[1]) + int(
                file.split(' ')[1].split(':')[2]) / 60)
        return time_t

    def time_convert(self, str):
        time_local = time.localtime(int(str))
        pub_time = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
        return pub_time


if __name__ == "__main__":
    # QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    ITN = MyMainForm()
    ITN.show()
    sys.exit(app.exec_())
