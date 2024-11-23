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
