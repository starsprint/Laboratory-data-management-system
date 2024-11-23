import psycopg2
from psycopg2 import sql
from PySide6.QtWidgets import QMessageBox


class Connector:
    __connection = None
    __cursor = None

    def __init__(self):
        self.__userName = 'postgres'       # 数据库用户名
        self.__password = '123456'        # 用户密码
        self.__databaseName = 'labdata'   # 数据库名称
        self.__host = 'localhost'         # 数据库主机地址
        self.__port = 5432                # 数据库端口
        try:
            # 初始化数据库连接
            Connector.__connection = psycopg2.connect(
                host=self.__host,
                user=self.__userName,
                password=self.__password,
                dbname=self.__databaseName,
                port=self.__port
            )
            Connector.__cursor = Connector.__connection.cursor()
        except Exception as e:
            # 如果连接失败，弹出错误提示框
            QMessageBox.critical(None, '数据库连接错误',
                                 f'无法连接到数据库，请检查用户名、密码、主机地址和端口是否正确。\n错误信息：{e}')

    @staticmethod
    def get_cursor():
        """获取游标对象"""
        if Connector.__cursor is None or Connector.__connection is None:
            Connector()
        return Connector.__cursor

    @staticmethod
    def get_connection():
        """获取数据库连接对象"""
        if Connector.__connection is None:
            Connector()
        return Connector.__connection

    @staticmethod
    def close_connection():
        """关闭数据库连接"""
        if Connector.__cursor is not None:
            Connector.__cursor.close()
        if Connector.__connection is not None:
            Connector.__connection.close()
        Connector.__connection = None
        Connector.__cursor = None
