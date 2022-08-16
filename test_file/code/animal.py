# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'animal.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication


class Ui_kml_animal(object):
    def setupUi(self, kml_animal):
        # 获取显示器分辨率
        self.desktop = QApplication.desktop()
        self.screenRect = self.desktop.screenGeometry()
        self.screenheight = self.screenRect.height()
        self.screenwidth = self.screenRect.width()
        a = self.screenheight / 1080
        b = self.screenwidth / 1920

        kml_animal.setObjectName("kml_animal")
        kml_animal.resize(1297*b, 979*a)
        self.graphicsView = QtWidgets.QGraphicsView(kml_animal)
        self.graphicsView.setGeometry(QtCore.QRect(600*a, 60*a, 681*b, 831*b))
        self.graphicsView.setObjectName("graphicsView")
        self.readkml = QtWidgets.QPushButton(kml_animal)
        self.readkml.setGeometry(QtCore.QRect(10*a, 10*a, 301*b, 61*b))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(14)
        self.readkml.setFont(font)
        self.readkml.setObjectName("readkml")
        self.label = QtWidgets.QLabel(kml_animal)
        self.label.setGeometry(QtCore.QRect(20*a, 100*a, 101*b, 31*b))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(kml_animal)
        self.label_2.setGeometry(QtCore.QRect(20*a, 180*a, 101*b, 31*b))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(kml_animal)
        self.label_3.setGeometry(QtCore.QRect(20*a, 280*a, 101*b, 31*b))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.record = QtWidgets.QPushButton(kml_animal)
        self.record.setGeometry(QtCore.QRect(10*a, 910*a, 231*b, 51*b))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(14)
        self.record.setFont(font)
        self.record.setObjectName("record")
        self.exportcsv = QtWidgets.QPushButton(kml_animal)
        self.exportcsv.setGeometry(QtCore.QRect(320*a, 910*a, 231*b, 51*b))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(14)
        self.exportcsv.setFont(font)
        self.exportcsv.setObjectName("exportcsv")
        self.prepage = QtWidgets.QPushButton(kml_animal)
        self.prepage.setGeometry(QtCore.QRect(610*a, 910*a, 271*b, 51*b))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(15)
        self.prepage.setFont(font)
        self.prepage.setObjectName("prepage")
        self.nextpage = QtWidgets.QPushButton(kml_animal)
        self.nextpage.setGeometry(QtCore.QRect(1000*a, 910*a, 271*b, 51*b))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(15)
        self.nextpage.setFont(font)
        self.nextpage.setObjectName("nextpage")
        self.visitornumber = QtWidgets.QTextBrowser(kml_animal)
        self.visitornumber.setGeometry(QtCore.QRect(160*a, 100*a, 401*b, 41*b))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.visitornumber.setFont(font)
        self.visitornumber.setObjectName("visitornumber")
        self.radioButton_1 = QtWidgets.QRadioButton(kml_animal)
        self.radioButton_1.setGeometry(QtCore.QRect(150*a, 160*a, 115*b, 19*b))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(12)
        self.radioButton_1.setFont(font)
        self.radioButton_1.setObjectName("radioButton_1")
        self.radioButton_2 = QtWidgets.QRadioButton(kml_animal)
        self.radioButton_2.setGeometry(QtCore.QRect(260*a, 160*a, 115*b, 19*b))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(12)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.information = QtWidgets.QTextBrowser(kml_animal)
        self.information.setGeometry(QtCore.QRect(160*a, 340*a, 391*b, 151*b))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.information.setFont(font)
        self.information.setObjectName("information")
        self.starttime = QtWidgets.QPushButton(kml_animal)
        self.starttime.setGeometry(QtCore.QRect(10*a, 530*a, 121*b, 51*b))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(14)
        self.starttime.setFont(font)
        self.starttime.setObjectName("starttime")
        self.endtime = QtWidgets.QPushButton(kml_animal)
        self.endtime.setGeometry(QtCore.QRect(10*a, 610*a, 121*b, 51*b))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(14)
        self.endtime.setFont(font)
        self.endtime.setObjectName("endtime")
        self.label_4 = QtWidgets.QLabel(kml_animal)
        self.label_4.setGeometry(QtCore.QRect(10*a, 390*a, 141*b, 41*b))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.information_s = QtWidgets.QTextBrowser(kml_animal)
        self.information_s.setGeometry(QtCore.QRect(160*a, 510*a, 391*b, 81*b))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.information_s.setFont(font)
        self.information_s.setObjectName("information_s")
        self.radioButton_3 = QtWidgets.QRadioButton(kml_animal)
        self.radioButton_3.setGeometry(QtCore.QRect(370*a, 160*a, 115*b, 19*b))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(12)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(kml_animal)
        self.radioButton_4.setGeometry(QtCore.QRect(480*a, 160*a, 81*b, 19*b))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(12)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_5 = QtWidgets.QRadioButton(kml_animal)
        self.radioButton_5.setGeometry(QtCore.QRect(150*a, 200*a, 81*b, 19*b))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(12)
        self.radioButton_5.setFont(font)
        self.radioButton_5.setObjectName("radioButton_5")
        self.radioButton_6 = QtWidgets.QRadioButton(kml_animal)
        self.radioButton_6.setGeometry(QtCore.QRect(150*a, 240*a, 81*b, 19*b))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(12)
        self.radioButton_6.setFont(font)
        self.radioButton_6.setObjectName("radioButton_6")
        self.radioButton_7 = QtWidgets.QRadioButton(kml_animal)
        self.radioButton_7.setGeometry(QtCore.QRect(370*a, 240*a, 111*b, 19*b))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(12)
        self.radioButton_7.setFont(font)
        self.radioButton_7.setObjectName("radioButton_7")
        self.radioButton_8 = QtWidgets.QRadioButton(kml_animal)
        self.radioButton_8.setGeometry(QtCore.QRect(480*a, 200*a, 91*b, 19*b))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(12)
        self.radioButton_8.setFont(font)
        self.radioButton_8.setObjectName("radioButton_8")
        self.radioButton_9 = QtWidgets.QRadioButton(kml_animal)
        self.radioButton_9.setGeometry(QtCore.QRect(260*a, 240*a, 91*b, 19*b))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(12)
        self.radioButton_9.setFont(font)
        self.radioButton_9.setObjectName("radioButton_9")
        self.activityplace = QtWidgets.QLineEdit(kml_animal)
        self.activityplace.setGeometry(QtCore.QRect(160*a, 280*a, 391*b, 41*b))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.activityplace.setFont(font)
        self.activityplace.setObjectName("activityplace")
        self.information_e = QtWidgets.QTextBrowser(kml_animal)
        self.information_e.setGeometry(QtCore.QRect(160*a, 610*a, 391*b, 61*b))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.information_e.setFont(font)
        self.information_e.setObjectName("information_e")
        self.label_5 = QtWidgets.QLabel(kml_animal)
        self.label_5.setGeometry(QtCore.QRect(600*a, 20*a, 101*b, 31*b))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.picname = QtWidgets.QTextBrowser(kml_animal)
        self.picname.setGeometry(QtCore.QRect(710*a, 20*a, 571*b, 31*b))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.picname.setFont(font)
        self.picname.setObjectName("picname")
        self.radioButton_10 = QtWidgets.QRadioButton(kml_animal)
        self.radioButton_10.setGeometry(QtCore.QRect(520*a, 240*a, 91*b, 19*b))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(12)
        self.radioButton_10.setFont(font)
        self.radioButton_10.setObjectName("radioButton_10")
        self.radioButton_10.setVisible(False)
        self.label_6 = QtWidgets.QLabel(kml_animal)
        self.label_6.setGeometry(QtCore.QRect(20*a, 760*a, 111*b, 41*b))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.feedback = QtWidgets.QTextBrowser(kml_animal)
        self.feedback.setGeometry(QtCore.QRect(160*a, 690*a, 391*b, 201*b))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.feedback.setFont(font)
        self.feedback.setObjectName("feedback")
        self.radioButton_11 = QtWidgets.QRadioButton(kml_animal)
        self.radioButton_11.setGeometry(QtCore.QRect(260*a, 200*a, 91*b, 19*b))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(12)
        self.radioButton_11.setFont(font)
        self.radioButton_11.setObjectName("radioButton_11")
        self.radioButton_12 = QtWidgets.QRadioButton(kml_animal)
        self.radioButton_12.setGeometry(QtCore.QRect(370*a, 200*a, 91*b, 19*b))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(12)
        self.radioButton_12.setFont(font)
        self.radioButton_12.setObjectName("radioButton_12")

        self.retranslateUi(kml_animal)
        QtCore.QMetaObject.connectSlotsByName(kml_animal)

    def retranslateUi(self, kml_animal):
        _translate = QtCore.QCoreApplication.translate
        kml_animal.setWindowTitle(_translate("kml_animal", "kml_animal"))
        self.readkml.setText(_translate("kml_animal", "读取kml文件"))
        self.label.setText(_translate("kml_animal", "游客编号"))
        self.label_2.setText(_translate("kml_animal", "活动类型"))
        self.label_3.setText(_translate("kml_animal", "活动地点"))
        self.record.setText(_translate("kml_animal", "记录活动"))
        self.exportcsv.setText(_translate("kml_animal", "导出csv文件"))
        self.prepage.setText(_translate("kml_animal", "上一张(↑)"))
        self.nextpage.setText(_translate("kml_animal", "下一张(↓)"))
        self.radioButton_1.setText(_translate("kml_animal", "入园"))
        self.radioButton_2.setText(_translate("kml_animal", "参观"))
        self.starttime.setText(_translate("kml_animal", "开始时间"))
        self.endtime.setText(_translate("kml_animal", "结束时间"))
        self.label_4.setText(_translate("kml_animal", "当前图片信息"))
        self.radioButton_3.setText(_translate("kml_animal", "游乐"))
        self.radioButton_4.setText(_translate("kml_animal", "休息"))
        self.radioButton_5.setText(_translate("kml_animal", "就餐"))
        self.radioButton_6.setText(_translate("kml_animal", "如厕"))
        self.radioButton_7.setText(_translate("kml_animal", "其他服务"))
        self.radioButton_8.setText(_translate("kml_animal", "寻路"))
        self.radioButton_9.setText(_translate("kml_animal", "离园"))
        self.label_5.setText(_translate("kml_animal", "照片名称"))
        self.radioButton_10.setText(_translate("kml_animal", "不显示"))
        self.label_6.setText(_translate("kml_animal", "信息反馈"))
        self.radioButton_11.setText(_translate("kml_animal", "上车"))
        self.radioButton_12.setText(_translate("kml_animal", "下车"))
