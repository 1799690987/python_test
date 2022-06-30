# python_test
python

###
安装：

安装OpenCV之前需要先安装 numpy, matplotlib。

先安装OpenCV-Python, 由于一些经典的算法被申请了版权，新版本有很大的限制，所以选用3.4.3以下的版本
#### opencv
、、、
pip install opencv-python==3.4.2.17
、、、
#### opencv-contrib
、、、
pip install opencv-contrib-python==3.4.2.17
、、、

#### matplotlib
、、、
pip install matplotlib
pip install matplotlib -i https://pypi.tuna.tsinghua.edu.cn/simple
、、、

####  numpy
'''
pip install numpy -i https://pypi.tuna.tsinghua.edu.cn/simple
'''

#### imutils简介

imutils是Adrian Rosebrock开发的一个python工具包，它整合了opencv、numpy和matplotlib的相关操作，主要是用来进行图形图像的处理，如图像的平移、旋转、缩放、骨架提取、显示等等，后期又加入了针对视频的处理，如摄像头、本地文件等。imutils同时支持python2和python3。
安装imutils
pip install imutils

#### pytesseract
pip install pytesseract

tesseract dm2.jpeg stdout

如果按照失败：
cd /usr/local/Homebrew/Library/Taps/homebrew/
rm -rf homebrew-core
git clone https://github.com/Homebrew/homebrew-core.git
