import os,sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog
from Ui_widget import Ui_AreYouSmling
from Mydataset import get_test_data_loader
from PIL import Image,ImageQt

import torchvision.transforms as transforms
import torch
import numpy as np
from ResNet18 import ResNet18
from Predict import predict
import matplotlib.pyplot as plt

CLASSES=['飞机','汽车','鸟','猫','鹿','狗','青蛙','马','船','卡车']
class mywindow(QtWidgets.QWidget,Ui_AreYouSmling):
    def __init__(self):
        super(mywindow,self).__init__()
        self.cwd=os.getcwd()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.read_dataset)
        self.pushButton_2.clicked.connect(self.read_file)
        self.pushButton_3.clicked.connect(self.predict)
    def read_file(self):
        self.label_2.setText(" ")
        self.label_3.setText(" ")
        file,filetype=QFileDialog.getOpenFileName(self,'open image',self.cwd,"*.JPG,*.JPEG,*.png,*.jpg,ALL Files(*)")
        if not file=='':
            self.image=Image.open(file)
            jpg = QtGui.QPixmap(file).scaled(self.label.width(), self.label.height())
            self.label.setPixmap(jpg)

    def read_dataset(self):
        self.label_2.setText(" ")
        batch=get_test_data_loader(1)
        image,label=next(iter(batch))
        self.image=image #将tensor传走
        self.label_3.setText(CLASSES[label])
        image=image.squeeze(dim=0)
        std=[0.2023, 0.1994, 0.2010]
        mean=[0.4914, 0.4822, 0.4465]
        image[0]=image[0]*std[0]+mean[0]
        image[1]=image[1]*std[1]+mean[1]
        image[2]=image[2]*std[2]+mean[2]
        unloader=transforms.ToPILImage()
        image=unloader(image)
        pixmap=ImageQt.toqpixmap(image)
        jpg=QtGui.QPixmap(pixmap).scaled(self.label.width(),self.label.height())
        self.label.setPixmap(jpg)
    
       
    def predict(self):
        #先将图片转为PIL形式
        
        image=self.image
        pred=predict(image)
        self.label_4.setText('Predicting')
        #pred=predict(image)
        self.label_4.setText('Predicted')
        self.label_2.setText(CLASSES[pred])


if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    myshow=mywindow()
    myshow.show()
    sys.exit(app.exec_())