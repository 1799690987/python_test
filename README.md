# <no value>
pip freeze > requirements.txt
## 本地开发

### 创建虚拟环境

~~~~sh
$ python3 -m venv venv
~~~~

### 激活虚拟环境

~~~~sh
$ source venv/bin/activate
~~~~

如果你是使用 VSCode 或者 PyCharm 等 IDE 进行开发的，则需要在选择解释器（Interpreter）的时候，选择 venv/bin/python 这个解释器，否则代码补全和跳转的功能会不正常。

### 安装依赖

首先参考 https://python.byted.org/pip-setup.html 设置 pip 私有源，如果已经设置过，则可以跳过此步。

~~~~sh
$ pip install -r requirements.txt
~~~~

### 启动项目

~~~~sh
$ ./bootstrap.sh
~~~~

或者直接执行

~~~~sh
$ python server.py
~~~~

## 常见问题

### ConnectionRefusedError: [Errno 61] Connection refused

如果在 macOS 系统中进行开发，访问远端服务（数据库、下游服务）时需要通过 consul 来进行服务发现，但是 macOS 上没有公司内的服务发现系统，因此连接会失败。

这时可以设置 CONSUL_HTTP_HOST 环境变量来指定使用远端的 consul 来做服务发现。比如：

~~~~sh
$ export CONSUL_HTTP_HOST=10.6.131.78
~~~~

目前推荐使用你的 devbox 上的 consul 来给本地开发环境提供服务发现功能。

## 更多

- [Euler 文档](https://python.byted.org/library/euler/index.html)








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
