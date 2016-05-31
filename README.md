# watermark
===========
This is my graduation project. I want to build a web site ,it's can register user and manager user. 
also it's have personal space. If you register the website you can upload your image for watermark.
and then, you can pick one algorithm to go. If you need to extract the watermark from the target 
image you are welcome to extract by this site! So it's should be a good place to protect your own
intellectual property right! It's use many many third party lib! For Example: `matplotlib`,`numpy`
and `Pillow`, etc!

Configure the operating system environment
------------------------------------------

####Update source for ubuntu & update software
```shell
sudo apt-get update
sudo apt-get upgrade
```
####Install Mysql
```shell
sudo apt-get install mysql-server
sudo apt-get install mysql-client
```
####Install Pip
```shell
sudo apt-get install python-dev
sudo apt-get install build-essential
sudo apt-get install python-pip
```
And we can also use curl and python to download and install Pip.
```shell
curl "https://bootstrap.pypa.io/get_pip.py" -o "get_pip.py"
python get-pip.py
```
####Install SqlAlchemy & Mysql
```shell
sudo apt-get install python-all-dev
sudo apt-get install python-mysqldb
sudo apt-get install libmysqlclient-dev
```
Because, I am going to use sqlalchemy to connect the database. so 
I want will need the `mysql-python` for me.
####Install virtualenv by pip & create a virtual env for test!
```shell
pip install virtualenv
virtualenv sqlalchemyEnv
cd sqlalchemyEnv
mkdir src
cd src
pip install mysql-python
pip install sqlalchemy
```
####Install erlang & rabbitmq
```shell
sudo apt-get install erlang
sudo apt-get install rabbitmq-server
```
Because ,I will use the celery so the default AMQP is my first choose!
so I install it on my machine! if you like to use another you can try it!
```shell
sudo rabbitmq-server start
```
Now,You rabbitmq server should work! if no! try to fix ! google is your good friend!
Installation Dependent package
#### Install numpy & scipy
```shell
sudo apt-get install python-numpy
sudo apt-get install python-scipy
```
#### Install matplotlib
```shell
sudo apt-get install libpng-dev
```
Get the freetype source and make it install by hand
```shell
wget http://download.savannah.gnu.org/releases/freetype/freetype-2.4.10.tar.gz
tar zxvf freetype-2.4.10.tar.gz
cd freetype-2.4.10/
./configure
make
sudo make install
```
After install success and then you can install the matplotlib
```shell
sudo pip install matplotlib
```

Install the watermark requirement
------------------------------
Before you install the requirement ,you should install the something!
```shell
sudo apt-get install libjpeg8-dev
sudo ln -s /usr/lib/x86_64-linux-gnu/libjpeg.so /usr/lib
sudo apt-get install build-essential autoconf libtool pkg-config python-opengl python-imaging python-pyrex python-pyside.qtopengl idle-python2.7 qt4-dev-tools qt4-designer libqtgui4 libqtcore4 libqt4-xml libqt4-test libqt4-script libqt4-network libqt4-dbus python-qt4 python-qt4-gl libgle3 python-dev
sudo apt-get install python-pil
```
Now, time to install it!
```shell
    pip install -r requirements.txt
```
I find get some error! said i install `cffi` error! and i try the below
command , and fix it!
```shell
sudo apt-get remove build-essential libffi-dev python-dev
sudo apt-get install build-essential libffi-dev python-dev
sudo apt-get remove python-pycparser
sudo apt-get install python-pycparser
```
Also, when i install the `pyopenssl` ,it is get me a error!
```shell
sudo apt-get install libssl-dev`
```
If you install crypt failure,try the below command!
```shell
sudo apt-get install build-essential libssl-dev libffi-dev python-dev
```
Create a database for watermark
-------------------------------
```shell
mysql -uroot -p
create database sqlalchemy
```

Test the watermark with celery
------------------------------
```shell
celery worker -l info --beat
```
Warning don't run this on root!

