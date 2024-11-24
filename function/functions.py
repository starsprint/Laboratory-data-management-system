import psycopg2
from psycopg2 import sql
from database.connector import Connector


# 管理论文
def add_thesis(title, author, doi):
    """管理员：添加论文"""
    connection = Connector.get_connection()
    cursor = connection.cursor()
    try:
        query = """
            INSERT INTO theses (title, author, download_count, doi)
            VALUES (%s, %s, 0, %s)
        """
        cursor.execute(query, (title, author, doi))
        connection.commit()
    except Exception as e:
        print(f"Error adding thesis: {e}")
    finally:
        cursor.close()


def edit_thesis(title, author=None, doi=None):
    """管理员：编辑论文"""
    connection = Connector.get_connection()
    cursor = connection.cursor()
    try:
        updates = []
        values = []
        if author:
            updates.append("author = %s")
            values.append(author)
        if doi:
            updates.append("doi = %s")
            values.append(doi)
        values.append(title)

        query = f"""
            UPDATE theses
            SET {", ".join(updates)}
            WHERE title = %s
        """
        cursor.execute(query, tuple(values))
        connection.commit()
    except Exception as e:
        print(f"Error editing thesis: {e}")
    finally:
        cursor.close()


def delete_thesis(title):
    """管理员：删除论文"""
    connection = Connector.get_connection()
    cursor = connection.cursor()
    try:
        query = "DELETE FROM theses WHERE title = %s" 
        cursor.execute(query, (title,))
        connection.commit()
    except Exception as e:
        print(f"Error deleting thesis: {e}")
    finally:
        cursor.close()


def query_thesis(title):
    """管理员：通过论文标题查询单个论文"""
    connection = Connector.get_connection()
    cursor = connection.cursor()
    try:
        query = "SELECT title, author, download_count, doi FROM theses WHERE title = %s"
        cursor.execute(query, (title,))
        return cursor.fetchone()
    except Exception as e:
        print(f"Error querying thesis: {e}")
    finally:
        cursor.close()

def query_theses():
    """管理员：查询所有论文"""
    connection = Connector.get_connection()
    cursor = connection.cursor()
    try:
        query = "SELECT title, author, download_count, doi FROM theses"
        cursor.execute(query)
        return cursor.fetchall()
    except Exception as e:
        print(f"Error querying theses: {e}")
    finally:
        cursor.close()

# 管理图书
def add_book(title, author, publisher, publication_date, stock):
    """管理员：添加图书"""
    connection = Connector.get_connection()
    cursor = connection.cursor()
    try:
        query = """
            INSERT INTO books (title, author, publisher, publication_date, stock)
            VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(query, (title, author, publisher, publication_date, stock))
        connection.commit()
    except Exception as e:
        print(f"Error adding book: {e}")
    finally:
        cursor.close()


def edit_book(title, author=None, publisher=None, publication_date=None, stock=None):
    """管理员：编辑图书"""
    connection = Connector.get_connection()
    cursor = connection.cursor()
    try:
        updates = []
        values = []
        if author:
            updates.append("author = %s")
            values.append(author)
        if publisher:
            updates.append("publisher = %s")
            values.append(publisher)
        if publication_date:
            updates.append("publication_date = %s")
            values.append(publication_date)
        if stock is not None:
            updates.append("stock = %s")
            values.append(stock)
        values.append(title)

        query = f"""
            UPDATE books
            SET {", ".join(updates)}
            WHERE title = %s  
        """
        cursor.execute(query, tuple(values))
        connection.commit()
    except Exception as e:
        print(f"Error editing book: {e}")
    finally:
        cursor.close()


def delete_book(title):
    """管理员：删除图书"""
    connection = Connector.get_connection()
    cursor = connection.cursor()
    try:
        query = "DELETE FROM books WHERE title = %s"  
        cursor.execute(query, (title,))
        connection.commit()
    except Exception as e:
        print(f"Error deleting book: {e}")
    finally:
        cursor.close()


def query_book(title):
    """管理员：通过书名查询单个图书"""
    connection = Connector.get_connection()
    cursor = connection.cursor()
    try:
        query = "SELECT title, author, publisher, publication_date, stock, borrow_count FROM books WHERE title = %s"
        cursor.execute(query, (title,))
        return cursor.fetchone()
    except Exception as e:
        print(f"Error querying book: {e}")
    finally:
        cursor.close()

def query_books():
    """管理员：查询所有图书"""
    connection = Connector.get_connection()
    cursor = connection.cursor()
    try:
        query = "SELECT title, author, publisher, publication_date, stock, borrow_count FROM books"
        cursor.execute(query)
        return cursor.fetchall()
    except Exception as e:
        print(f"Error querying books: {e}")
    finally:
        cursor.close()

# 管理读者
def add_reader(name, email, phone):
    """管理员：添加读者"""
    connection = Connector.get_connection()
    cursor = connection.cursor()
    try:
        query = """
            INSERT INTO readers (name, email, phone)
            VALUES (%s, %s, %s)
        """
        cursor.execute(query, (name, email, phone))
        connection.commit()
    except Exception as e:
        print(f"Error adding reader: {e}")
    finally:
        cursor.close()


def edit_reader(name, email=None, phone=None):
    """管理员：编辑读者"""
    connection = Connector.get_connection()
    cursor = connection.cursor()
    try:
        updates = []
        values = []
        if email:
            updates.append("email = %s")
            values.append(email)
        if phone:
            updates.append("phone = %s")
            values.append(phone)
        values.append(name)

        query = f"""
            UPDATE readers
            SET {", ".join(updates)}
            WHERE name = %s  
        """
        cursor.execute(query, tuple(values))
        connection.commit()
    except Exception as e:
        print(f"Error editing reader: {e}")
    finally:
        cursor.close()


def delete_reader(name):
    """管理员：删除读者"""
    connection = Connector.get_connection()
    cursor = connection.cursor()
    try:
        query = "DELETE FROM readers WHERE name = %s"  
        cursor.execute(query, (name,))
        connection.commit()
    except Exception as e:
        print(f"Error deleting reader: {e}")
    finally:
        cursor.close()


def query_reader(name):
    """管理员：通过姓名查询单个读者"""
    connection = Connector.get_connection()
    cursor = connection.cursor()
    try:
        query = "SELECT name, email, phone FROM readers WHERE name = %s"
        cursor.execute(query, (name,))
        return cursor.fetchone()
    except Exception as e:
        print(f"Error querying reader: {e}")
    finally:
        cursor.close()

def query_readers():
    """管理员：查询所有读者"""
    connection = Connector.get_connection()
    cursor = connection.cursor()
    try:
        query = "SELECT name, email, phone FROM readers"
        cursor.execute(query)
        return cursor.fetchall()
    except Exception as e:
        print(f"Error querying readers: {e}")
    finally:
        cursor.close()

# 管理日志
def query_log(reader_name, book_title):
    """管理员：通过读者姓名和书名查询单个日志"""
    connection = Connector.get_connection()
    cursor = connection.cursor()
    try:
        query = "SELECT reader_name, book_title, time FROM logs WHERE reader_name = %s AND book_title = %s"
        cursor.execute(query, (reader_name, book_title))
        return cursor.fetchone()
    except Exception as e:
        print(f"Error querying log: {e}")
    finally:
        cursor.close()

def query_logs():
    """管理员：查询所有日志"""
    connection = Connector.get_connection()
    cursor = connection.cursor()
    try:
        query = "SELECT reader_name, book_title, time FROM logs"
        cursor.execute(query)
        return cursor.fetchall()
    except Exception as e:
        print(f"Error querying logs: {e}")
    finally:
        cursor.close()


def delete_log(reader_name, book_title):
    """管理员：删除日志"""
    connection = Connector.get_connection()
    cursor = connection.cursor()
    try:
        query = "DELETE FROM logs WHERE reader_name = %s AND book_title = %s"
        cursor.execute(query, (reader_name, book_title))
        connection.commit()
    except Exception as e:
        print(f"Error deleting log: {e}")
    finally:
        cursor.close()


# Upload Thesis
def upload_thesis(title, author, doi):
    """用户：上传论文"""
    connection = Connector.get_connection()
    cursor = connection.cursor()
    try:
        query = """
            INSERT INTO theses (title, author, download_count, doi)
            VALUES (%s, %s, 0, %s)
        """
        cursor.execute(query, (title, author, doi))
        connection.commit()
    except Exception as e:
        print(f"Error uploading thesis: {e}")
    finally:
        cursor.close()

# Download Thesis
def download_thesis(title):
    """用户：下载论文"""
    connection = Connector.get_connection()
    cursor = connection.cursor()
    try:
        query = "UPDATE theses SET download_count = download_count + 1 WHERE title = %s"
        cursor.execute(query, (title,))
        connection.commit()
    except Exception as e:
        print(f"Error downloading thesis: {e}")
    finally:
        cursor.close()

# Borrow Book
def borrow_book(reader_name, book_title):
    """用户：借阅图书"""
    connection = Connector.get_connection()
    cursor = connection.cursor()
    try:
        # Check if the book is available
        query = "SELECT stock FROM books WHERE title = %s"
        cursor.execute(query, (book_title,))
        stock = cursor.fetchone()[0]
        if stock > 0:
            # Update stock and add log entry
            update_query = "UPDATE books SET stock = stock - 1, borrow_count = borrow_count + 1 WHERE title = %s"
            cursor.execute(update_query, (book_title,))
            log_query = "INSERT INTO logs (reader_name, book_title) VALUES (%s, %s)"
            cursor.execute(log_query, (reader_name, book_title))
            connection.commit()
        else:
            print("Book is not available for borrowing.")
    except Exception as e:
        print(f"Error borrowing book: {e}")
    finally:
        cursor.close()

# Return Book
def return_book(reader_name, book_title):
    """用户：归还图书"""
    connection = Connector.get_connection()
    cursor = connection.cursor()
    try:
        # Update stock and remove log entry
        update_query = "UPDATE books SET stock = stock + 1 WHERE title = %s"
        cursor.execute(update_query, (book_title,))
        delete_log_query = "DELETE FROM logs WHERE reader_name = %s AND book_title = %s"
        cursor.execute(delete_log_query, (reader_name, book_title))
        connection.commit()
    except Exception as e:
        print(f"Error returning book: {e}")
    finally:
        cursor.close()

def get_book_statistics():
    """获取图书统计信息"""
    connection = Connector.get_connection()
    cursor = connection.cursor()
    try:
        query = "SELECT total_books, total_stock, total_borrows FROM book_statistics"
        cursor.execute(query)
        return cursor.fetchone()
    except Exception as e:
        print(f"Error getting book statistics: {e}")
    finally:
        cursor.close()

def get_thesis_statistics():
    """获取论文统计信息"""
    connection = Connector.get_connection()
    cursor = connection.cursor()
    try:
        query = "SELECT total_theses, total_downloads FROM thesis_statistics"
        cursor.execute(query)
        return cursor.fetchone()
    except Exception as e:
        print(f"Error getting thesis statistics: {e}")
    finally:
        cursor.close()
