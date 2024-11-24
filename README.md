## 一、下载postgresql
+ windows教程：<https://www.runoob.com/postgresql/windows-install-postgresql.html>
+ Mac OS教程：<https://www.runoob.com/postgresql/mac-install-postgresql.html
+ Linux教程：<https://www.runoob.com/postgresql/linux-install-postgresql.html>

## 二、配置数据库
在SQL Shell（psql）中运行.\labdb.sql中的所有SQL语句，创建一个labdata数据库。

## 三、安装python
安装好后将python加入环境变量（Python目录和Scripts目录都加入环境变量）。
也可以使用虚拟环境：
1.创建虚拟环境：
``` bash
python -m venv venv
```
2.激活虚拟环境
+ windows:
  ```bash
  venv\Scripts\activate
  ```
+ macOS/Linux:
  ```bash
  source venv/bin/activate
  ```
3.退出虚拟环境
```bash
deactivate
```
激活虚拟环境后如图：

![image](https://github.com/user-attachments/assets/4e40be9a-f39d-44de-8320-732e70cd44d1)

注意最前面的(venv)，这个是你创建的虚拟环境的名称，一会代码一定要在这个虚拟幻境里跑，要不然就白配置了
然后输入pip install -r requirements.txt回车，安装相关依赖。

## 三、配置connector.py
在connector.py中配置对应的用户名（默认postgres）、用户密码、数据库名称（sql脚本中创建的数据库名称:labdata）、数据库主机地址（默认localhost）、数据库端口（默认5432）。

## 四、运行程序
切换到项目所在目录下，进入虚拟环境，运行 python main.py即可

## 文件注释
1. database目录下：
+ connector.py：定义了一个Connector类，用于使用psycopg2库管理到PostgreSQL数据库的连接。
2. function目录下：
+ functions.py：包含一组用于管理数据库中的论文、图书、读者和日志的函数。
table目录下：
+ books_info.py：定义了一个图形用户界面（GUI），用于管理books表中的图书信息。
+ logs_info.py：定义了一个图形用户界面（GUI），用于管理logs表中的图书信息。
+ readers_info.py：定义了一个图形用户界面（GUI），用于管理readers表中的图书信息。
+ theses_info.py：定义了一个图形用户界面（GUI），用于管理theses表中的图书信息。
+ user_info.py：。。。
3. ui目录下：
+ admin_ui.py：为管理面板定义了一个图形用户界面，允许管理员管理系统的各个方面，如图书、论文、阅读器和日志。
+ guest_ui.py：为游客定义的界面。
+ user_ui.py：为一般用户定义的界面。
+ main_window.py：主界面。
4. labdb.sql脚本文件，用于创建labdata数据库。
