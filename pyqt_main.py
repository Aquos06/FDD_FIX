import sys
from PyQt5.QtWidgets import *  # 引入PyQt相關類別
from PyQt5.QtGui import *
from PyQt5.QtCore import *
# from pyqtgraph.graphicsItems import *
import pyqtgraph as pg
import math
from pyqt_ui import *  # 導入窗口介面
import numpy as np
from PIL import Image  # pillow
import os
import json
import cv2
import qdarkstyle
import time 

from utility import toLog

class roiwidge(QWidget):  # 介面布局自動縮放
    def __init__(self,parent=None):
        super(roiwidge, self).__init__(parent)
        self.ui = Ui_Form(self)

        self.ui.graphicsView.mouseReleaseEvent = self.gpmouseReleaseEvent
        self.ui.graphicsView.mousePressEvent = self.gpmousePressEvent
        # 清除界面所有ROI
        self.ui.ClearROIButton.clicked.connect(self.ClearAllROI)
        # draw ROI finish
        self.ui.confirmROIButton.clicked.connect(self.confirmROI)

        self.bgrColor = [(255,0,0),(0,255,0),(0,255,255),(203,192,255)]
        self.penColor = ['b', 'g', 'y', 'm']
        self.totname = 1 

        self.ui.PPE_ROI.setEnabled(False)
        self.ui.Person_ROI.setEnabled(False)

        # for save draw roi pos
        self.ROI_view = {}
        self.lastPoint = QPoint()
        self.endPoint = QPoint()
        self.points = []  # 僅多邊形使用
        self.name = []
        self.rect_draw_count = 0
        self.tmp_multi = []
        
        self.qssStyle = '''
                    QHeaderView
                    {
                        background:transparent;
                    }
                    QHeaderView::section
                    {
                        font-size:20px;
                        font-family:"Microsoft JhengHei";
                        color:#FFFFFF;
                        background:#60669B;
                        border:none;
                        text-align:left;
                        margin-left:0px;
                        padding-left:0px;
                    }
                    QTableWidget
                    {
                        background:#FFFFFF;
                        border:none;
                        font-size:20px;
                        font-family:"Microsoft JhengHei";
                        color:#666666;
                    }
                    QTableWidget::item
                    {
                        font-size:20px;
                        font-family:"Microsoft JhengHei";
                        border-bottom:1px solid #EEF1F7 ;
                    }
                    
                    QTableWidget::item::selected
                    {
                        color:red;
                        background:#EFF4FF;
                    }
                    QScrollBar::handle:vertical
                    {
                        background: rgba(255,255,255,20%);
                        border: 0px solid grey;
                        border-radius:3px;
                        width: 8px;
                    }
                    QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical
                    {
                        background:rgba(255,255,255,10%);
                    }
                    QScollBar::add-line:vertical, QScrollBar::sub-line:vertical
                    {
                        background:transparent;
                    }
                    
                   QPushButton:hover{text-align : center;
                               background-color : #4277BD;
                               font : 20px \"Microsoft JhengHei\";
                               color:rgb(255, 255, 255);}
                   QPushButton{text-align : center;
                               background-color : #499DD0;
                               font : 20px \"Microsoft JhengHei\";
                               padding: none;
                               color:rgb(255, 255, 255);}
                   QCheckBox {font : 20px \"Microsoft JhengHei\";
                        color: white;
                    }
                   QCheckBox:hover {color:#f00;}
                   
                   QComboBox {
                       font : 18px \"Microsoft JhengHei\";
                       color:white;
                       padding: 1px 15px 1px 3px;
                       border:2px solid #4277BD;
                       border-radius:5px 5px 0px 0px;
                   }
                   QComboBox::drop-down {
                       subcontrol-origin: padding;
                       subcontrol-position: top right;
                       width: 15px;
                       color:white;
                       border:none;
                   }
                   QComboBox::down-arrow,QDateEdit::down-arrow {
                       top: 0px;
                       left: -10px;
                       image: url(icon/down-arrow.png);
                       width:20px;
                       height:20px;
                   }
                   QComboBox:on { 
                           padding-top: 3px;
                           padding-left: 4px;
                   }
                   QComboBox::down-arrow:on { 
                       top: 1px;
                       left: -7px;
                   }
                   '''
        self.setStyleSheet(self.qssStyle)
        self.openJson()

    def setChannel(self, channel):
        
        if channel == 0 :
            self.fname = 'channel1.jpg'
            self.channel = 'Camera1'
            self.imgPerson = cv2.imread('./ROI/Camera1/person.jpg')
            self.imgPPE = cv2.imread('./ROI/Camera1/PPE.jpg')
            self.imgFall = cv2.imread('./ROI/Camera1/fall_down.jpg')
            self.config = 'channel1'
        
        elif channel == 1:
            self.fname = 'channel2.jpg'
            self.channel = 'Camera2'
            self.imgPerson = cv2.imread('./ROI/Camera2/person.jpg')
            self.imgPPE = cv2.imread('./ROI/Camera2/PPE.jpg')
            self.imgFall = cv2.imread('./ROI/Camera2/fall_down.jpg')
            self.config = 'channel2'

        elif channel == 2:
            self.fname = 'channel3.jpg'
            self.channel = 'Camera3'
            self.imgPerson = cv2.imread('./ROI/Camera3/person.jpg')
            self.imgPPE = cv2.imread('./ROI/Camera3/PPE.jpg')
            self.imgFall = cv2.imread('./ROI/Camera3/fall_down.jpg')
            self.config = 'channel3'
        
        else: 
            self.fname = 'channel4.jpg'
            self.channel = 'Camera4'
            self.imgPerson = cv2.imread('./ROI/Camera4/person.jpg')
            self.imgPPE = cv2.imread('./ROI/Camera4/PPE.jpg')
            self.imgFall = cv2.imread('./ROI/Camera4/fall_down.jpg')
            self.config = 'channel4'
        
        self.scene = QGraphicsScene(0, 0, self.ui.ROILabel.width(), self.ui.ROILabel.height())

        self.ui.graphicsView.setScene(self.scene)
        self.ui.graphicsView.setStyleSheet("background:transparent") 

    def openJson(self):
        data = open('output/loggin.json')
        self.ROI_logging = json.load(data)
        data.close()

    #  滑鼠控制事件 : 滑鼠點擊
    def gpmousePressEvent(self, event):
        # 按下鼠標左鍵
        # print(1)
        if event.buttons() == QtCore.Qt.LeftButton:
            # 獲取座標位址 (QpointF.x,QpointF.y)
            point = self.ui.graphicsView.mapToScene(event.pos())
            # pyqt的ui介面如果選擇畫多邊形 ROI
            if self.ui.comboBox.currentText() == 'draw MultiRect ROI':
                self.points.append(point)
                self.test(points=self.points)
            # 若不是，記錄每次點擊的座標位址
            elif self.ui.comboBox.currentText() == 'draw Rect ROI':
                self.lastPoint = point

        elif event.buttons() == QtCore.Qt.RightButton and len(self.scene.items()) > 0:
            QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
            if self.ui.comboBox.currentText() == 'draw MultiRect ROI' :
                self.scene.removeItem(self.tmp_multi[-1])
                del self.tmp_multi[-1]
                del self.points[-1]

                if len(self.tmp_multi) == 0:
                    self.points = []

            elif self.ui.comboBox.currentText() == 'draw Rect ROI':
                if len(self.name) != self.rect_draw_count:
                    self.scene.removeItem(self.scene.items()[1])
                    self.rect_draw_count -= 1
            # self.ui.graphicsView.setScene(self.scene)
            QtWidgets.QApplication.restoreOverrideCursor()
        event.accept()
    # 當滑鼠點擊放開時
    def gpmouseReleaseEvent(self, event):
        if event.button() == 1 :
            QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
            point = self.ui.graphicsView.mapToScene(event.pos())
            self.endPoint = point
            (x, y, w, h) = self.caculat_Rec(self.lastPoint, self.endPoint)
            self.test((x, y), (w, h))
            QtWidgets.QApplication.restoreOverrideCursor()

    # 計算矩形ROI的原點和長寬
    def caculat_Rec(self, pos1, pos2):
        x1 = pos1.x()
        x2 = pos2.x()
        y1 = pos1.y()
        y2 = pos2.y()

        if x1 >= x2:
            x = x2
        else:
            x = x1
        if y1 >= y2:
            y = y2
        else:
            y = y1
        h = abs(y1 - y2)
        w = abs(x1 - x2)
        return x, y, w, h

    def xyxy2xywh(self,x1,y1,x2,y2):
        if x1 >= x2:
            x = x2
        else:
            x = x1
        if y1 >= y2:
            y = y2
        else:
            y = y1
        h = abs(y1 - y2)
        w = abs(x1 - x2)
        return x, y, w, h

    # ROI : pos(x,y) , size(w,h), points : for MultiRectROI
    def test(self, pos=(0, 0), size=(0, 0), points=list(), confirm = False, shape = None, color = None, name = None, flag = False):
        
        # 當上次畫完矩陣未儲存，自動刪除紀錄
        if len(self.name)!=self.rect_draw_count and len(points) <= 1:
            f = open('output/loggin.json','r')
            data = json.load(f)
            f.close()
            self.scene.clear()
            self.ROI_view.clear()
            self.rect_draw_count -= 1
            for i in data[self.channel]['fall down']:
                if i.split("_")[0] == 'Rect':
                    x,y,w,h = self.xyxy2xywh(data[self.channel]['fall down'][i]['coor'][0],data[self.channel]['fall down'][i]['coor'][1],data[self.channel]['fall down'][i]['coor'][2], data[self.channel]['fall down'][i]['coor'][3])
                    self.test((x,y),(w,h),shape = 'Rect',color = int(data[self.channel]['fall down'][i]['color']), name = i, flag = True)
                else:
                    self.test(points = data[self.channel]['fall down'][i]['coor'], color = int(data[self.channel]['fall down'][i]['color']),flag = True, name = i,shape = 'Multi')
        # 如果使用者想畫矩形 ROI
        #always go to this if. 
        elif (self.ui.comboBox.currentText() == 'draw Rect ROI' and flag == False) or (shape == 'Rect' and flag == True):
            if shape != 'Rect':
                frame = pg.RectROI(pos, size, pen=pg.mkPen(self.penColor[len(self.name)%4], width=4))
                self.scene.addItem(frame)
                self.points.clear()
                self.rect_draw_count += 1
            else:
                frame = pg.RectROI(pos, size, pen=pg.mkPen(self.penColor[color], width = 4))
                self.scene.addItem(frame)
                self.ROI_view[name]=[frame]
                myFont = QtGui.QFont("Microsoft JhengHei", 15, 1000 , italic=False)
                self.text = self.scene.addText(name, myFont)
                self.text.setPos(pos[0], pos[1] - 30)
                self.ROI_view[name].append(self.scene.items()[-1])
                
        # 如果使用者想畫多邊形 ROI
        elif (flag == False and self.ui.comboBox.currentText() == 'draw MultiRect ROI' and pos == (0, 0) and size == (0, 0)) or (shape == 'Multi' and flag == True):
            if shape != 'Multi':
                if len(points)> 1:
                    Pointed = [points[-2],points[-1]]
                else: 
                    Pointed = points
                if confirm:
                    frame = pg.PolyLineROI(Pointed, pen=pg.mkPen(self.penColor[len(self.name)%4-1], width = 4))
                else:
                    frame = pg.PolyLineROI(Pointed, pen=pg.mkPen(self.penColor[len(self.name)%4], width=4))
                self.scene.addItem(frame)
                self.tmp_multi.append(frame)
            else:
                for i in range(len(points)):
                    points[i][0] = points[i][0] * self.ui.graphicsView.width() / self.imgPerson.shape[1]
                    points[i][1] = points[i][1] * self.ui.graphicsView.height() / self.imgPerson.shape[0]
                points.append(points[0])
                frame = pg.PolyLineROI(points, pen = pg.mkPen(self.penColor[color], width = 4))
                self.scene.addItem(frame)
                self.ROI_view[name]= [frame]
                myFont = QtGui.QFont("Microsoft JhengHei", 15, 1000 , italic=False)
                self.text = self.scene.addText(name, myFont)
                self.text.setPos(points[0][0], points[0][1] - 30)
                self.ROI_view[name].append(self.scene.items()[-1])

    def clearJson(self):
        f = open('output/loggin.json', 'r')
        data = json.load(f)
        f.close()

        newData = {
            "person": {},
            "PPE" : {},
            "fall down": {},
            "maximum": {},
            "minimum": {}
        }

        data[self.channel] = newData
        f = open('output/loggin.json', 'w')
        json.dump(data,f,indent=2)
        f.close()

        f = open('output/loggin.json', 'r')
        self.ROI_logging = json.load(f)
        f.close()

    def clearIMG(self):
        blank = cv2.imread('./ROI/Camera1/blank.jpg')

        if self.channel == 'Camera1':
            cv2.imwrite('./ROI/Camera1/PPE.jpg', blank)
            cv2.imwrite('./ROI/Camera1/Person.jpg', blank)
            cv2.imwrite('./ROI/Camera1/fall_down.jpg', blank)

            self.imgFall = cv2.imread('./ROI/Camera1/fall_down.jpg')
            self.imgPPE = cv2.imread('./ROI/Camera1/PPE.jpg')
            self.imgPerson = cv2.imread('./ROI/Camera1/Person.jpg')
        elif self.channel == 'Camera2':
            cv2.imwrite('./ROI/Camera2/PPE.jpg', blank)
            cv2.imwrite('./ROI/Camera2/Person.jpg', blank)
            cv2.imwrite('./ROI/Camera2/fall_down.jpg', blank)

            self.imgFall = cv2.imread('./ROI/Camera2/fall_down.jpg')
            self.imgPPE = cv2.imread('./ROI/Camera2/PPE.jpg')
            self.imgPerson = cv2.imread('./ROI/Camera2/Person.jpg')
        elif self.channel == 'Camera3':
            cv2.imwrite('./ROI/Camera3/PPE.jpg', blank)
            cv2.imwrite('./ROI/Camera3/Person.jpg', blank)
            cv2.imwrite('./ROI/Camera3/fall_down.jpg', blank)

            self.imgFall = cv2.imread('./ROI/Camera3/fall_down.jpg')
            self.imgPPE = cv2.imread('./ROI/Camera3/PPE.jpg')
            self.imgPerson = cv2.imread('./ROI/Camera3/Person.jpg')
        else:
            cv2.imwrite('./ROI/Camera4/PPE.jpg', blank)
            cv2.imwrite('./ROI/Camera4/Person.jpg', blank)
            cv2.imwrite('./ROI/Camera4/fall_down.jpg', blank)

            self.imgFall = cv2.imread('./ROI/Camera4/fall_down.jpg')
            self.imgPPE = cv2.imread('./ROI/Camera4/PPE.jpg')
            self.imgPerson = cv2.imread('./ROI/Camera4/Person.jpg')

    def ClearAllROI(self):
        QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
        self.ui.tableWidget.clearContents()    # 清空頁面暫存
        self.ui.tableWidget.setRowCount(0)
        self.points.clear()
        self.name.clear()
        self.clearJson() #need to change
        self.clearIMG() #need to change
        self.ROI_view.clear()
        self.rect_draw_count=0
        self.totname = 1
        toLog(f"ROI {self.channel} Updated")
        self.scene.clear()
        self.changeAIConf()
        QtWidgets.QApplication.restoreOverrideCursor()

    # ROI位址紀錄 pos : 矩形: [top_x, top_y , bottom_x, bottom_y]
    def ROI_pos_logging(self, pos):
        self.save_file = 'output/'

        data = {
            self.name[-1] : {
                "coor": pos,
                'enable': True,
                "color": ((len(self.name))%4-1)
            }
        }
        if self.ui.detect_size.currentText() == 'draw minimum':
            self.ROI_logging[str(self.channel)]['minimum'].update(data)
        elif self.ui.detect_size.currentText() == 'draw maximum':
            self.ROI_logging[str(self.channel)]['maximum'].udpate(data)
        else:
            if self.ui.Person_ROI.isChecked():
                self.ROI_logging[str(self.channel)]['person'].update(data)

                if self.name[-1].split("_")[0] == 'Rect':
                    self.imgPerson = cv2.rectangle(self.imgPerson,(int(pos[0]/self.ui.graphicsView.width()*self.imgPerson.shape[1]), int(pos[1]/self.ui.graphicsView.height()*self.imgPerson.shape[0])), (int(pos[2]/self.ui.graphicsView.width()*self.imgPerson.shape[1]), int(pos[3]/self.ui.graphicsView.height()*self.imgPerson.shape[0])), (255,0,0), -1)
                else:
                    for i in len(pos):
                        pos[i][0] = int(pos[i][0]/self.ui.graphicsView.width()*self.imgPerson.shape[1])
                        pos[i][1] = int(pos[i][1]/self.ui.graphicsView.height()*self.imgPerson.shape[0])
                        pos = np.array([pos])
                    self.imgPerson = cv2.fillPoly(self.imgPerson, [pos], color = self.bgrColor[len(self.name)%4-1])
                if self.channel == 'Camera1':
                    cv2.imwrite('./ROI/Camera1/person.jpg', self.imgPerson)
                elif self.channel == 'Camera2':
                    cv2.imwrite('./ROI/Camera2/person.jpg', self.imgPerson)
                elif self.channel == 'Camera3':
                    cv2.imwrite('./ROI/Camera3/person.jpg', self.imgPerson)
                else:
                    cv2.imwrite('./ROI/Camera4/person.jpg', self.imgPerson)

            if self.ui.PPE_ROI.isChecked():
                self.ROI_logging[str(self.channel)]['PPE'].update(data)
                if self.name[-1].split("_")[0] == 'Rect':
                    self.imgPPE = cv2.rectangle(self.imgPPE, (int(pos[0]/self.ui.graphicsView.width()*self.imgPerson.shape[1]), pos[1]/int(self.ui.graphicsView.height()*self.imgPerson.shape[0])), (int(pos[2]/self.ui.graphicsView.width()*self.imgPerson.shape[1]), int(pos[3]/self.ui.graphicsView.height()*self.imgPerson.shape[0])), (255,0,0), -1)
                else:
                    for i in pos:
                        i[0] = int(i[0]/self.ui.graphicsView.width()*self.imgPerson.shape[1])
                        i[1] = int(i[1]/self.ui.graphicsView.height()*self.imgPerson.shape[0])
                    pos = np.array([pos])
                    self.imgPPE = cv2.fillPoly(self.imgPPE, [pos], color = (255,0,0))
                if self.channel == 'Camera1':
                    cv2.imwrite('./ROI/Camera1/PPE.jpg', self.imgPPE)
                elif self.channel == 'Camera2':
                    cv2.imwrite('./ROI/Camera2/PPE.jpg', self.imgPPE)
                elif self.channel == 'Camera3':
                    cv2.imwrite('./ROI/Camera3/PPE.jpg', self.imgPPE)
                else:
                    cv2.imwrite('./ROI/Camera4/PPE.jpg', self.imgPPE)
                    
            if self.ui.Falldown_ROI.isChecked():
                self.ROI_logging[str(self.channel)]['fall down'].update(data)
                if self.name[-1].split("_")[0] == 'Rect':
                    self.imgFall = cv2.rectangle(self.imgFall, (int(pos[0]/self.ui.graphicsView.width()*self.imgPerson.shape[1]), int(pos[1]/self.ui.graphicsView.height()*self.imgPerson.shape[0])), (int(pos[2]/self.ui.graphicsView.width()*self.imgPerson.shape[1]), int(pos[3]/self.ui.graphicsView.height()*self.imgPerson.shape[0])), color = self.bgrColor[len(self.name)%4-1], thickness = -1)
                else :
                    for i in pos:
                        i[0] = int(i[0]/self.ui.graphicsView.width()*self.imgPerson.shape[1])
                        i[1] = int(i[1]/self.ui.graphicsView.height()*self.imgPerson.shape[0])
                    pos = np.array([pos])
                    self.imgFall = cv2.fillPoly(self.imgFall, [pos], color = self.bgrColor[len(self.name)%4-1])

                if self.channel == 'Camera1':
                    cv2.imwrite('./ROI/Camera1/fall_down.jpg', self.imgFall)
                elif self.channel == 'Camera2':
                    cv2.imwrite('./ROI/Camera2/fall_down.jpg', self.imgFall)
                elif self.channel == 'Camera3':
                    cv2.imwrite('./ROI/Camera3/fall_down.jpg', self.imgFall)
                else:
                    cv2.imwrite('./ROI/Camera4/fall_down.jpg', self.imgFall)

        toLog(f"ROI {self.channel} Updated")
        try:
            f = open('output/loggin.json', 'w')
            json.dump(self.ROI_logging, f, indent=2)
            f.close()

            f = open('json/AiSettings.json', 'r')
            data = json.load(f)
            f.close()

            data[self.channel]['change'] = True

            f = open('json/AiSettings.json', 'w')
            json.dump(data,f,indent=2)
            f.close()

        except:
            print('Failed to save ROI...')

        self.points.clear()
    # ROI name record
    def Roiname_record(self):
        if self.ui.comboBox.currentText() == 'draw Rect ROI':
            self.name.append(f'Rect_{self.totname}')
            self.totname += 1
        elif self.ui.comboBox.currentText() == 'draw MultiRect ROI':
            self.name.append(f'MultiRect_{self.totname}')
            self.totname += 1

    def confirmROI(self):
        QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
        # font format
        myFont = QtGui.QFont("Microsoft JhengHei", 15, 1000 , italic=False)
        if len(self.scene.items()) == 0:
            QtWidgets.QApplication.restoreOverrideCursor()
            return
        # 矩形確認儲存
        self.Roiname_record()

        if self.ui.comboBox.currentText() == 'draw Rect ROI':
            x1 = self.lastPoint.x()
            x2 = self.endPoint.x()
            y1 = self.lastPoint.y()
            y2 = self.endPoint.y()
            self.ROI_view[self.name[-1]]=[self.scene.items()[1]]
            self.ROI_pos_logging([int(x1), int(y1), int(x2), int(y2)])
            # display text of roi name
            self.text = self.scene.addText(self.name[-1], myFont)
            self.text.setPos(x1, y1 - 30)
            self.ROI_view[self.name[-1]].append(self.scene.items()[-(len(self.name))])
        # 多邊形確認儲存
        elif self.ui.comboBox.currentText() == 'draw MultiRect ROI':
            # 多邊形ROI位址紀錄
            point = list()
            for i in self.points:
                point.append([int(i.x()), int(i.y())])
            # 將結尾與開頭座標連結
            draw = point.copy()
            draw.append(point[0])
            self.rect_draw_count += 1
            self.test(points=draw,confirm=True)
            # display set
            self.ROI_view[self.name[-1]]=self.tmp_multi
            # display text of roi name
            self.text = self.scene.addText(self.name[-1], myFont)
            self.text.setPos(int(point[0][0]), int(point[0][1]) - 45)
            self.ROI_view[self.name[-1]].append(self.scene.items()[-(len(self.name))])
            # init logging for roi pos
            self.tmp_multi = list()
            del draw
            # json file logging
            self.ROI_pos_logging(point)
        # form
        self.ROI_form()
        QtWidgets.QApplication.restoreOverrideCursor()

    def checkEnable(self):
        QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
        button = self.sender()
        if button.isChecked():
            row = self.ui.tableWidget.indexAt(button.parent().pos()).row()
            # 取得該列roi名稱
            title = self.ui.tableWidget.item(row, 0).text()

            for i in self.ROI_logging[self.channel]:
                if title in list(self.ROI_logging[self.channel][i]):
                    self.ROI_logging[self.channel][i][title]['enable'] = True

            f = open('./output/loggin.json','w')
            json.dump(self.ROI_logging,f,indent=2)
            f.close()
        else:
            row = self.ui.tableWidget.indexAt(button.parent().pos()).row()
            # 取得該列roi名稱
            title = self.ui.tableWidget.item(row, 0).text()

            for i in self.ROI_logging[self.channel]:
                if title in list(self.ROI_logging[self.channel][i]):
                    self.ROI_logging[self.channel][i][title]['enable'] = False

            f = open('./output/loggin.json','w')
            json.dump(self.ROI_logging,f,indent=2)
            f.close()

        self.redraw()
        QtWidgets.QApplication.restoreOverrideCursor()

    def redraw(self):
        blank = cv2.imread('./ROI/Camera1/blank.jpg')
        for coor in self.ROI_logging[self.channel]['fall down']:
            if coor.split('_')[0] == 'Rect' and self.ROI_logging[self.channel]['fall down'][coor]['enable'] == True:
                blank =cv2.rectangle(blank, (int(self.ROI_logging[self.channel]['fall down'][coor]['coor'][0]/self.ui.graphicsView.width()*self.imgPerson.shape[1]), int(self.ROI_logging[self.channel]['fall down'][coor]['coor'][1]/self.ui.graphicsView.height()*self.imgPerson.shape[0])), (int(self.ROI_logging[self.channel]['fall down'][coor]['coor'][2]/self.ui.graphicsView.width()*self.imgPerson.shape[1]), int(self.ROI_logging[self.channel]['fall down'][coor]['coor'][3]/self.ui.graphicsView.height()*self.imgPerson.shape[0])), color = self.bgrColor[int(self.ROI_logging[self.channel]['fall down'][coor]['color'])], thickness =-1)
            else:
                if self.ROI_logging[self.channel]['fall down'][coor]['enable'] == True:
                    coordinate = np.array(self.ROI_logging[self.channel]['fall down'][coor]['coor'])
                    blank = cv2.fillPoly(blank, [coordinate], color = self.bgrColor[int(self.ROI_logging[self.channel]['fall down'][coor]['color'])])

        self.imgFall = blank
        if self.channel == 'Camera1':
            cv2.imwrite('./ROI/Camera1/fall_down.jpg', blank)
        elif self.channel == 'Camera2':
            cv2.imwrite('./ROI/Camera2/fall_down.jpg', blank)
        elif self.channel == 'Camera3':
            cv2.imwrite('./ROI/Camera3/fall_down.jpg', blank)
        else:
            cv2.imwrite('./ROI/Camera4/fall_down.jpg', blank)

        f = open('json/AiSettings.json', 'r')
        data = json.load(f)
        f.close()

        data[self.channel]['change'] = True

        toLog(f"ROI {self.channel} Updated")

        f = open('json/AiSettings.json', 'w')
        json.dump(data,f,indent=2)
        f.close()

    # 右側欄位紀錄
    ## 可刪除指定ROI
    def ROI_form(self):
        a = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.setRowCount(a + 1)
        self.ui.tableWidget.setItem(a, 0, QTableWidgetItem(self.name[-1]))
        # delete specific roi
        widget = QtWidgets.QWidget()
        hLayout = QtWidgets.QHBoxLayout()

        self.delete_specific = QPushButton('delete')
        self.delete_specific.setStyleSheet(self.qssStyle)
        self.delete_specific.setMinimumHeight(50)
        self.delete_specific.clicked.connect(self.del_specific_roi)
        self.delete_specific.setMinimumHeight(1)
        hLayout.addWidget(self.delete_specific)
        widget.setLayout(hLayout)
        self.ui.tableWidget.setCellWidget(a, 1, widget)
        self.ui.tableWidget.setRowHeight(a,50)

        widgetEnable = QtWidgets.QWidget()
        layout = QtWidgets.QHBoxLayout()

        self.enable = QtWidgets.QCheckBox()
        self.enable.setChecked(True)
        self.enable.setStyleSheet("""
                    QCheckBox::indicator{
                        background-color:red;
                        
                    }
                    QCheckBox::indicator:checked{
                        background-color:green;
                    }
                    QCheckBox{
                        color:white
                    }
        """)
        self.enable.clicked.connect(self.checkEnable)
        self.enable.setMinimumHeight(1)
        layout.addWidget(self.enable)
        widgetEnable.setLayout(layout)
        
        self.ui.tableWidget.setCellWidget(a,2,widgetEnable)

        self.changeAIConf()
    
    def changeAIConf(self):
        f = open('./json/AiSettings.json', 'r')
        data = json.load(f)
        f.close()

        data[self.channel]['change'] = True

        f = open('./json/AiSettings.json', 'w')
        json.dump(data,f,indent=2)
        f.close()

    def del_specific_roi(self):
        QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
        button = self.sender()
        if button:
            # 確認當前位址 - 列
            row = self.ui.tableWidget.indexAt(button.parent().pos()).row()
            # 取得該列roi名稱
            title = self.ui.tableWidget.item(row, 0).text()
            # 刪除表單列資料
            self.ui.tableWidget.removeRow(row)
            # 刪除該roi相關紀錄
            for i in self.ROI_logging[self.channel]:
                if title in list(self.ROI_logging[self.channel][i]):
                    del self.ROI_logging[self.channel][i][title]
                    blank = cv2.imread('./ROI/Camera1/blank.jpg')
                    for coor in self.ROI_logging[self.channel][i]:
                        if coor.split('_')[0] == 'Rect' and self.ROI_logging[self.channel][i][coor]['enable'] == True:
                            blank =cv2.rectangle(blank, (int(self.ROI_logging[self.channel][i][coor]['coor'][0]/self.ui.graphicsView.width()*self.imgPerson.shape[1]), int(self.ROI_logging[self.channel][i][coor]['coor'][1]/self.ui.graphicsView.height()*self.imgPerson.shape[0])), (int(self.ROI_logging[self.channel][i][coor]['coor'][2]/self.ui.graphicsView.width()*self.imgPerson.shape[1]), int(self.ROI_logging[self.channel][i][coor]['coor'][3]/self.ui.graphicsView.height()*self.imgPerson.shape[0])), color = self.bgrColor[int(self.ROI_logging[self.channel][i][coor]['color'])], thickness =-1)
                        else:
                            if self.ROI_logging[self.channel][i][coor]['enable'] == True:
                                coordinate = np.array([self.ROI_logging[self.channel][i][coor]['coor']])
                                blank = cv2.fillPoly(blank, [coordinate], color = self.bgrColor[int(self.ROI_logging[self.channel][i][coor]['color'])])

                    if i == 'Person':
                        self.imgPerson = blank
                        if self.channel == 'Camera1':
                            cv2.imwrite('./ROI/Camera1/person.jpg', blank)
                        elif self.channel == 'Camera2':
                            cv2.imwrite('./ROI/Camera2/person.jpg', blank)
                        elif self.channel == 'Camera3':
                            cv2.imwrite('./ROI/Camera3/person.jpg', blank)
                        else:
                            cv2.imwrite('./ROI/Camera4/Person.jpg', blank)
                    elif i == 'PPE':
                        self.imgPPE = blank
                        if self.channel == 'Camera1':
                            cv2.imwrite('./ROI/Camera1/PPE.jpg', blank)
                        elif self.channel == 'Camera2':
                            cv2.imwrite('./ROI/Camera2/PPE.jpg', blank)
                        elif self.channel == 'Camera3':
                            cv2.imwrite('./ROI/Camera3/PPE.jpg', blank)
                        else:
                            cv2.imwrite('./ROI/Camera4/PPE.jpg', blank) 
                    else:
                        self.imgFall = blank
                        if self.channel == 'Camera1':
                            cv2.imwrite('./ROI/Camera1/fall_down.jpg', blank)
                        elif self.channel == 'Camera2':
                            cv2.imwrite('./ROI/Camera2/fall_down.jpg', blank)
                        elif self.channel == 'Camera3':
                            cv2.imwrite('./ROI/Camera3/fall_down.jpg', blank)
                        else:
                            cv2.imwrite('./ROI/Camera4/fall_down.jpg', blank)

            # del display roi
            if 'Rect_' in title:
                for i in self.ROI_view[title]:
                    self.scene.removeItem(i)
                self.rect_draw_count -= 1
            else:
                for i in self.ROI_view[title]:
                    self.scene.removeItem(i)
            del self.ROI_view[title]
            self.name.remove(title)
            
            if len(self.name) == 0:
                self.totname = 1
                self.ClearAllROI()

            # self.ui.graphicsView.setScene(self.scene)
            self.tmp_multi = []
            self.changeAIConf()
            data1 = open('output/loggin.json', 'w')
            json.dump(self.ROI_logging, data1, indent=2)
            data1.close()
            toLog(f"Camera {self.channel} Updated")

        QtWidgets.QApplication.restoreOverrideCursor()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

    myWin = roiwidge()
    myWin.setChannel(0)
    myWin.show()
    sys.exit(app.exec_())