# coding:utf-8
import os
import sys

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtGui import QPixmap, QTextCursor, QKeySequence, QPainter
from PyQt5.QtWidgets import QApplication, QWidget, QGraphicsScene, QGraphicsPixmapItem, QFileDialog, QMainWindow, \
    QShortcut
from assist import Ui_Form
import shutil
from natsort import ns, natsorted


class MyMainForm(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        QShortcut(QKeySequence("Enter"), self, self.CopytoFound)  # 设置快捷键Enter
        QShortcut(QKeySequence("Up"), self, self.openPrevImg)
        QShortcut(QKeySequence("Down"), self, self.openNextImg)
        QShortcut(QKeySequence("Escape"), self, self.CancelCopy)

        self.btnOpenDir.clicked.connect(self.openDirDialog)
        self.btnNext.clicked.connect(self.openNextImg)
        self.btnPrev.clicked.connect(self.openPrevImg)
        self.btnStart.clicked.connect(self.openStartImg)
        self.btnEnd.clicked.connect(self.openEndImg)
        self.btnPrev10.clicked.connect(self.openPrevImg_10)
        self.btnNext10.clicked.connect(self.openNextImg_10)

        self.copybj1.clicked.connect(self.copymarkpic1)
        self.copybj2.clicked.connect(self.copymarkpic2)
        self.copybj3.clicked.connect(self.copymarkpic3)

        self.markyuantu1.clicked.connect(self.mkyuantu1)
        self.markyuantu2.clicked.connect(self.mkyuantu2)
        self.markyuantu3.clicked.connect(self.mkyuantu3)

        self.copyFound.clicked.connect(self.CopytoFound)
        self.copytofound1.clicked.connect(self.CopytoFound1)
        self.copytofound2.clicked.connect(self.CopytoFound2)
        self.copytofound3.clicked.connect(self.CopytoFound3)
        self.copytofound4.clicked.connect(self.CopytoFound4)
        self.copytofound5.clicked.connect(self.CopytoFound5)
        self.copytofound6.clicked.connect(self.CopytoFound6)

        self.CancelcopyFound.clicked.connect(self.CancelCopy)
        self.Cancelcopytofound1.clicked.connect(self.CancelCopy1)
        self.Cancelcopytofound2.clicked.connect(self.CancelCopy2)
        self.Cancelcopytofound3.clicked.connect(self.CancelCopy3)

        self.batu_pro.clicked.connect(self.ProBatu)

        self.pic_clear.clicked.connect(self.Clear_Graphic)  # 初始化
        self.btnNextDir.clicked.connect(self.OpenNextDir)  # 载入下一个文件夹

        self.cwd = os.getcwd()  # 获取当前程序文件位置
        self.imageList = []  # 源图完整路径列表
        self.imageName = []  # 源图名称列表
        self.imagebatu = []  # 靶图列表

        self.file_index = 0  # 文件索引
        self.mark_index1 = 0
        self.mark_index2 = 0
        self.mark_index3 = 0
        self.image = QPixmap()
        self.srcpath = ''
        self.dirindex = 0

    def wheelEvent(self, event):
        self.textFound.clear()
        delta = event.angleDelta()
        oriention = delta.y() / 8
        if oriention < 0:
            self.file_index += 1
            if self.file_index >= len(self.imageList):
                self.file_index = len(self.imageList) - 1
            if self.file_index == len(self.imageList) - 1:
                self.textFound.setText('\n已经是最后一张了，辛苦您啦！')

            if len(self.imageList) <= 0 or self.file_index >= len(self.imageList):
                return
            cur_path = self.imageList[self.file_index]
            self.image.load(cur_path)
            self.Loadyuantu()
            self.yuantutext.setText(
                self.imageName[self.file_index] + '  (' + str((self.file_index + 1)) + '/' + str(
                    len(self.imageList)) + ')')


        else:
            self.file_index -= 1
            if self.file_index < 0:
                self.file_index = 0

            if len(self.imageList) <= 0 or self.file_index >= len(self.imageList):
                return
            cur_path = self.imageList[self.file_index]
            self.image.load(cur_path)
            self.Loadyuantu()
            self.yuantutext.setText(
                self.imageName[self.file_index] + '  (' + str((self.file_index + 1)) + '/' + str(
                    len(self.imageList)) + ')')

    def Clear_Graphic(self):
        # 文件索引累加 1
        # self.image = QPixmap()
        self.textFound.clear()
        self.yuantutext.clear()
        self.graphicsView_batu.scene.clear()
        self.graphicsView_yuantu.scene.clear()

        self.graphicsView_batu_2.scene = QGraphicsScene()
        self.graphicsView_batu_2.setScene(self.graphicsView_batu_2.scene)
        self.graphicsView_batu_2.scene.clear()

        self.graphicsView_batu_3.scene = QGraphicsScene()
        self.graphicsView_batu_3.setScene(self.graphicsView_batu_3.scene)
        self.graphicsView_batu_3.scene.clear()

        self.graphicsView_batu_4.scene = QGraphicsScene()
        self.graphicsView_batu_4.setScene(self.graphicsView_batu_4.scene)
        self.graphicsView_batu_4.scene.clear()

        self.cwd = os.getcwd()  # 获取当前程序文件位置
        self.imageList = []  # 源图完整路径列表
        self.imageName = []  # 源图名称列表
        self.imagebatu = []  # 靶图列表

        self.file_index = 0  # 文件索引
        self.mark_index1 = 0
        self.mark_index2 = 0
        self.mark_index3 = 0
        self.image = QPixmap()
        # self.srcpath = ''

    def OpenNextDir(self):
        self.Clear_Graphic()  # 初始化
        dir_list = []
        list = os.listdir(self.cwd)
        for file in natsorted(list, alg=ns.PATH):
            list_path = os.path.join(self.cwd, file)
            dir_list.append(list_path)  # 返回自然排序的文件列表
        print(dir_list)
        print(self.srcpath)
        src_path = str(self.srcpath)
        i = 0
        while len(dir_list) > 0:
            if os.path.samefile(dir_list[i], src_path):  # 判断路径是否相同
                self.dirindex = i
                break
            else:
                i += 1
            if i >= len(dir_list) - 1:
                break

        self.dirindex += 1
        if self.dirindex >= len(dir_list) - 1:
            self.textFound.setText('\n已经是最后一个文件夹了，辛苦您啦！')
            self.dirindex = len(dir_list) - 1

        dirpath = dir_list[self.dirindex]  # 获取下一个文件的路径
        self.markcurdir.setText('当前文件夹：' + os.path.basename(dirpath))

        self.srcpath = dirpath
        for filename in self.scanAllImagesName(dirpath + '/' + 'detect'):  # 获取所有源图名称
            self.imageName.append(filename)

        for filename in self.scanAllImages(dirpath + '/' + 'detect'):  # 获取所有源图完整路径
            self.imageList.append(filename)

        self.image.load(self.imageList[self.file_index])
        self.Loadyuantu()

        for filename in self.scanAllImages(dirpath + '/' + 'pic_dst'):
            self.imagebatu.append(filename)

        self.image.load(self.imagebatu[self.file_index])
        self.Loadbatu()
        # self.yuantutext.setText(self.imageName[self.file_index])
        self.yuantutext.setText(
            self.imageName[self.file_index] + '  (' + str((self.file_index + 1)) + '/' + str(len(self.imageList)) + ')')

    def openDirDialog(self):
        dirpath = QFileDialog.getExistingDirectory(self,
                                                   "选取文件夹",
                                                   self.cwd)  # 起始路径

        if dirpath == "":
            print("\n取消选择")
            return

        self.srcpath = dirpath

        self.markcurdir.setText('当前文件夹：' + os.path.basename(dirpath))  # 标记最后一级路径名称
        for filename in self.scanAllImagesName(dirpath + '/' + 'detect'):  # 获取所有源图名称
            self.imageName.append(filename)

        for filename in self.scanAllImages(dirpath + '/' + 'detect'):  # 获取所有源图完整路径
            self.imageList.append(filename)

        self.image.load(self.imageList[self.file_index])
        self.Loadyuantu()

        for filename in self.scanAllImages(dirpath + '/' + 'pic_dst'):
            self.imagebatu.append(filename)

        self.image.load(self.imagebatu[self.file_index])
        self.Loadbatu()
        # self.yuantutext.setText(self.imageName[self.file_index])
        self.yuantutext.setText(
            self.imageName[self.file_index] + '  (' + str((self.file_index + 1)) + '/' + str(len(self.imageList)) + ')')

    def scanAllImages(self, folderPath):
        images = []
        for root, dirs, files in os.walk(folderPath):
            for file in files:
                relativePath = os.path.join(root, file)
                images.append(relativePath)
        images.sort(key=lambda x: x.lower())
        return images

    def scanAllDirs_name(self, folderPath):  # 文件名对应序号
        dirs_name = {}
        dirs = []
        for file in os.listdir(folderPath):
            if os.path.isdir(os.path.join(folderPath, file)):
                dirs.append(os.path.join(folderPath, file))
        for i, file in enumerate(dirs):
            dirs_name[file] = i
        return dirs_name

    def scanAllDirs_num(self, folderPath):  # 文件序号对应文件名
        dirs_num = {}
        dirs = []
        for file in os.listdir(folderPath):
            if os.path.isdir(os.path.join(folderPath, file)):
                dirs.append(os.path.join(folderPath, file))
        for i, file in enumerate(dirs):
            dirs_num[i] = file
        return dirs_num

    def scanAllImagesName(self, folderPath):
        imagesname = []
        for root, dirs, files in os.walk(folderPath):
            for file in files:
                imagesname.append(file)
        imagesname.sort(key=lambda x: x.lower())
        return imagesname

    '''def ChoiceImage(self):
        self.image = QPixmap()
        path = QFileDialog.getOpenFileName(self, "选取文件", "C:/Users/HP/Desktop/", "(*.png);(*.jpg)")[0]
        # print(path)
        self.image.load(path)
        self.LoadImage()'''

    def openNextImg(self):
        # 文件索引累加 1
        # self.image = QPixmap()
        self.textFound.clear()
        self.file_index += 1
        if self.file_index >= len(self.imageList):
            self.file_index = len(self.imageList) - 1

        if self.file_index == len(self.imageList) - 1:
            self.textFound.setText('\n已经是最后一张了，辛苦您啦！')

        if len(self.imageList) <= 0 or self.file_index >= len(self.imageList):
            return

        cur_path = self.imageList[self.file_index]
        self.image.load(cur_path)
        self.Loadyuantu()
        self.yuantutext.setText(
            self.imageName[self.file_index] + '  (' + str((self.file_index + 1)) + '/' + str(len(self.imageList)) + ')')

    def openNextImg_10(self):
        # 文件索引累加 1
        # self.image = QPixmap()
        self.textFound.clear()
        self.file_index += 10
        if self.file_index >= len(self.imageList):
            self.file_index = len(self.imageList) - 1

        if self.file_index == len(self.imageList) - 1:
            self.textFound.setText('\n已经是最后一张了，辛苦您啦！')

        if len(self.imageList) <= 0 or self.file_index >= len(self.imageList):
            return

        cur_path = self.imageList[self.file_index]
        self.image.load(cur_path)
        self.Loadyuantu()
        self.yuantutext.setText(
            self.imageName[self.file_index] + '  (' + str((self.file_index + 1)) + '/' + str(len(self.imageList)) + ')')

    def openPrevImg(self):
        # 文件索引减 1
        # self.image = QPixmap()
        self.textFound.clear()
        self.file_index -= 1
        if self.file_index < 0:
            self.file_index = 0

        if len(self.imageList) <= 0 or self.file_index >= len(self.imageList):
            return

        # 当前路径
        cur_path = self.imageList[self.file_index]
        self.image.load(cur_path)
        self.Loadyuantu()
        self.yuantutext.setText(
            self.imageName[self.file_index] + '  (' + str((self.file_index + 1)) + '/' + str(len(self.imageList)) + ')')

    def openPrevImg_10(self):
        # 文件索引减 1
        # self.image = QPixmap()
        self.textFound.clear()
        self.file_index -= 10
        if self.file_index < 0:
            self.file_index = 0

        if len(self.imageList) <= 0 or self.file_index >= len(self.imageList):
            return

        # 当前路径
        cur_path = self.imageList[self.file_index]
        self.image.load(cur_path)
        self.Loadyuantu()
        self.yuantutext.setText(
            self.imageName[self.file_index] + '  (' + str((self.file_index + 1)) + '/' + str(len(self.imageList)) + ')')

    def openStartImg(self):
        # 文件索引减 1
        # self.image = QPixmap()
        self.file_index = 0

        # 当前路径
        cur_path = self.imageList[self.file_index]
        self.image.load(cur_path)
        self.Loadyuantu()
        self.yuantutext.setText(
            self.imageName[self.file_index] + '  (' + str((self.file_index + 1)) + '/' + str(len(self.imageList)) + ')')

    def openEndImg(self):
        # 文件索引减 1
        # self.image = QPixmap()
        self.file_index = len(self.imageList) - 1
        # 当前路径
        cur_path = self.imageList[self.file_index]
        self.image.load(cur_path)
        self.Loadyuantu()
        self.yuantutext.setText(
            self.imageName[self.file_index] + '  (' + str((self.file_index + 1)) + '/' + str(len(self.imageList)) + ')')

    def Loadyuantu(self):
        self.graphicsView_yuantu.scene = QGraphicsScene()  # 创建一个图片元素的对象
        item = QGraphicsPixmapItem(self.image)  # 创建一个变量用于承载加载后的图片
        self.graphicsView_yuantu.scene.addItem(item)  # 将加载后的图片传递给scene对象
        self.graphicsView_yuantu.setScene(self.graphicsView_yuantu.scene)

    def Loadbatu(self):
        self.graphicsView_batu.scene = QGraphicsScene()  # 创建一个图片元素的对象
        item = QGraphicsPixmapItem(self.image)  # 创建一个变量用于承载加载后的图片
        self.graphicsView_batu.scene.addItem(item)  # 将加载后的图片传递给scene对象
        self.graphicsView_batu.setScene(self.graphicsView_batu.scene)

    def mkyuantu1(self):
        self.mark_index1 = self.file_index
        cur_path = self.imageList[self.file_index]
        self.image.load(cur_path)
        self.Loadmarkyuantu1()

    def mkyuantu2(self):
        self.mark_index2 = self.file_index
        cur_path = self.imageList[self.file_index]
        self.image.load(cur_path)
        self.Loadmarkyuantu2()

    def mkyuantu3(self):
        self.mark_index3 = self.file_index
        cur_path = self.imageList[self.file_index]
        self.image.load(cur_path)
        self.Loadmarkyuantu3()

    def Loadmarkyuantu1(self):
        self.graphicsView_batu_2.scene = QGraphicsScene()  # 创建一个图片元素的对象
        item = QGraphicsPixmapItem(self.image)  # 创建一个变量用于承载加载后的图片
        self.graphicsView_batu_2.scene.addItem(item)  # 将加载后的图片传递给scene对象
        self.graphicsView_batu_2.setScene(self.graphicsView_batu_2.scene)

    def Loadmarkyuantu2(self):
        self.graphicsView_batu_3.scene = QGraphicsScene()  # 创建一个图片元素的对象
        item = QGraphicsPixmapItem(self.image)  # 创建一个变量用于承载加载后的图片
        self.graphicsView_batu_3.scene.addItem(item)  # 将加载后的图片传递给scene对象
        self.graphicsView_batu_3.setScene(self.graphicsView_batu_3.scene)

    def Loadmarkyuantu3(self):
        self.graphicsView_batu_4.scene = QGraphicsScene()  # 创建一个图片元素的对象
        item = QGraphicsPixmapItem(self.image)  # 创建一个变量用于承载加载后的图片
        self.graphicsView_batu_4.scene.addItem(item)  # 将加载后的图片传递给scene对象
        self.graphicsView_batu_4.setScene(self.graphicsView_batu_4.scene)

    def CopytoFound(self):
        src = self.imageList[self.file_index]
        found_path = self.srcpath + '/' + 'found'
        dst = os.path.join(found_path, self.imageName[self.file_index])
        shutil.copy(src, dst)
        self.textFound.setText(self.imageName[self.file_index] + '  ' + '是你小子！')

    def CancelCopy(self):
        found_path = self.srcpath + '/' + 'found'
        dst = os.path.join(found_path, self.imageName[self.file_index])
        if os.path.exists(dst):
            os.remove(dst)
        self.textFound.setText('对不起,  ' + self.imageName[self.file_index] + ',  我认错你了')

    def CopytoFound1(self):
        src = self.imageList[self.file_index]
        found_path = self.srcpath + '/' + 'found1'
        folder = os.path.exists(found_path)
        if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
            os.makedirs(found_path)
        dst = os.path.join(found_path, self.imageName[self.file_index])
        shutil.copy(src, dst)
        self.textFound.setText(self.imageName[self.file_index] + '  ' + '是你小子！')

    def copymarkpic1(self):
        src = self.imageList[self.mark_index1]
        found_path = self.srcpath + '/' + 'found1'
        folder = os.path.exists(found_path)
        if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
            os.makedirs(found_path)
        dst = os.path.join(found_path, self.imageName[self.mark_index1])
        shutil.copy(src, dst)
        self.textFound.setText(self.imageName[self.mark_index1] + '  ' + '是你小子！')

    def CancelCopy1(self):
        found_path = self.srcpath + '/' + 'found1'
        dst = os.path.join(found_path, self.imageName[self.file_index])
        if os.path.exists(dst):
            os.remove(dst)
        self.textFound.setText('对不起,  ' + self.imageName[self.file_index] + ',  我认错你了')

    def CopytoFound2(self):
        src = self.imageList[self.file_index]
        found_path = self.srcpath + '/' + 'found2'
        folder = os.path.exists(found_path)
        if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
            os.makedirs(found_path)
        dst = os.path.join(found_path, self.imageName[self.file_index])
        shutil.copy(src, dst)
        self.textFound.setText(self.imageName[self.file_index] + '  ' + '是你小子！')

    def copymarkpic2(self):
        src = self.imageList[self.mark_index2]
        found_path = self.srcpath + '/' + 'found2'
        folder = os.path.exists(found_path)
        if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
            os.makedirs(found_path)
        dst = os.path.join(found_path, self.imageName[self.mark_index2])
        shutil.copy(src, dst)
        self.textFound.setText(self.imageName[self.mark_index2] + '  ' + '是你小子！')

    def CancelCopy2(self):
        found_path = self.srcpath + '/' + 'found2'
        dst = os.path.join(found_path, self.imageName[self.file_index])
        if os.path.exists(dst):
            os.remove(dst)
        self.textFound.setText('对不起,  ' + self.imageName[self.file_index] + ',  我认错你了')

    def CopytoFound3(self):
        src = self.imageList[self.file_index]
        found_path = self.srcpath + '/' + 'found3'
        folder = os.path.exists(found_path)
        if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
            os.makedirs(found_path)
        dst = os.path.join(found_path, self.imageName[self.file_index])
        shutil.copy(src, dst)
        self.textFound.setText(self.imageName[self.file_index] + '  ' + '是你小子！')

    def CopytoFound4(self):
        src = self.imageList[self.file_index]
        found_path = self.srcpath + '/' + 'found4'
        folder = os.path.exists(found_path)
        if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
            os.makedirs(found_path)
        dst = os.path.join(found_path, self.imageName[self.file_index])
        shutil.copy(src, dst)
        self.textFound.setText(self.imageName[self.file_index] + '  ' + '是你小子！')

    def CopytoFound5(self):
        src = self.imageList[self.file_index]
        found_path = self.srcpath + '/' + 'found5'
        folder = os.path.exists(found_path)
        if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
            os.makedirs(found_path)
        dst = os.path.join(found_path, self.imageName[self.file_index])
        shutil.copy(src, dst)
        self.textFound.setText(self.imageName[self.file_index] + '  ' + '是你小子！')

    def CopytoFound6(self):
        src = self.imageList[self.file_index]
        found_path = self.srcpath + '/' + 'found6'
        folder = os.path.exists(found_path)
        if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
            os.makedirs(found_path)
        dst = os.path.join(found_path, self.imageName[self.file_index])
        shutil.copy(src, dst)
        self.textFound.setText(self.imageName[self.file_index] + '  ' + '是你小子！')

    def ProBatu(self):
        src = self.imageList[self.file_index]
        batu_path = 'F:/demo_f/probatu'
        name = self.imageName[self.file_index]
        proname = name.replace(name[:3], 'pro')
        dst = os.path.join(batu_path, proname)
        shutil.copy(src, dst)
        self.textFound.setText(proname + '  ' + '新靶图复制成功！')

    def copymarkpic3(self):
        src = self.imageList[self.mark_index3]
        found_path = self.srcpath + '/' + 'found3'
        folder = os.path.exists(found_path)
        if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
            os.makedirs(found_path)
        dst = os.path.join(found_path, self.imageName[self.mark_index3])
        shutil.copy(src, dst)
        self.textFound.setText(self.imageName[self.mark_index3] + '  ' + '是你小子！')

    def CancelCopy3(self):
        found_path = self.srcpath + '/' + 'found3'
        dst = os.path.join(found_path, self.imageName[self.file_index])
        if os.path.exists(dst):
            os.remove(dst)
        self.textFound.setText('对不起,  ' + self.imageName[self.file_index] + ',  我认错你了')

    '''def Text(self):
        cur_name = self.imageName[self.file_index]
        self.textFound.setText(cur_name)'''

    '''def Text(self):
        name = str(self.imageName[self.file_index])
        cursor = self.textFound.textCursor()
        cursor.movePosition(QTextCursor.End)
        self.textFound.append(name)
        self.textFound.setTextCursor(cursor)
        self.textFound.ensureCursorVisible()'''

    '''def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        painter = QPainter(self)
        pixmap = QPixmap("C:/Users/fangtao/Desktop/back.jpg")
        painter.drawPixmap(self.rect(), pixmap)'''


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ITN = MyMainForm()
    ITN.show()
    sys.exit(app.exec_())
