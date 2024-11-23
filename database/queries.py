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


def edit_thesis(thesis_id, title=None, author=None, doi=None):
    """管理员：编辑论文"""
    connection = Connector.get_connection()
    cursor = connection.cursor()
    try:
        updates = []
        values = []
        if title:
            updates.append("title = %s")
            values.append(title)
        if author:
            updates.append("author = %s")
            values.append(author)
        if doi:
            updates.append("doi = %s")
            values.append(doi)
        values.append(thesis_id)

        query = f"""
            UPDATE theses
            SET {", ".join(updates)}
            WHERE thesis_id = %s
        """
        cursor.execute(query, tuple(values))
        connection.commit()
    except Exception as e:
        print(f"Error editing thesis: {e}")
    finally:
        cursor.close()


def delete_thesis(thesis_id):
    """管理员：删除论文"""
    connection = Connector.get_connection()
    cursor = connection.cursor()
    try:
        query = "DELETE FROM theses WHERE thesis_id = %s" 
        cursor.execute(query, (thesis_id,))
        connection.commit()
    except Exception as e:
        print(f"Error deleting thesis: {e}")
    finally:
        cursor.close()


def query_theses():
    """管理员：查询所有论文"""
    connection = Connector.get_connection()
    cursor = connection.cursor()
    try:
        query = "SELECT thesis_id, title, author, doi FROM theses"
        cursor.execute(query)
        results = cursor.fetchall()
        print(results)
        return results
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


def edit_book(book_id, title=None, author=None, publisher=None, publication_date=None, stock=None):
    """管理员：编辑图书"""
    connection = Connector.get_connection()
    cursor = connection.cursor()
    try:
        updates = []
        values = []
        if title:
            updates.append("title = %s")
            values.append(title)
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
        values.append(book_id)

        query = f"""
            UPDATE books
            SET {", ".join(updates)}
            WHERE book_id = %s  
        """
        cursor.execute(query, tuple(values))
        connection.commit()
    except Exception as e:
        print(f"Error editing book: {e}")
    finally:
        cursor.close()


def delete_book(book_id):
    """管理员：删除图书"""
    connection = Connector.get_connection()
    cursor = connection.cursor()
    try:
        query = "DELETE FROM books WHERE book_id = %s"  
        cursor.execute(query, (book_id,))
        connection.commit()
    except Exception as e:
        print(f"Error deleting book: {e}")
    finally:
        cursor.close()


def query_books():
    """管理员：查询所有图书"""
    connection = Connector.get_connection()
    cursor = connection.cursor()
    try:
        query = "SELECT * FROM books"
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


def edit_reader(reader_id, name=None, email=None, phone=None):
    """管理员：编辑读者"""
    connection = Connector.get_connection()
    cursor = connection.cursor()
    try:
        updates = []
        values = []
        if name:
            updates.append("name = %s")
            values.append(name)
        if email:
            updates.append("email = %s")
            values.append(email)
        if phone:
            updates.append("phone = %s")
            values.append(phone)
        values.append(reader_id)

        query = f"""
            UPDATE readers
            SET {", ".join(updates)}
            WHERE reader_id = %s  
        """
        cursor.execute(query, tuple(values))
        connection.commit()
    except Exception as e:
        print(f"Error editing reader: {e}")
    finally:
        cursor.close()


def delete_reader(reader_id):
    """管理员：删除读者"""
    connection = Connector.get_connection()
    cursor = connection.cursor()
    try:
        query = "DELETE FROM readers WHERE reader_id = %s"  
        cursor.execute(query, (reader_id,))
        connection.commit()
    except Exception as e:
        print(f"Error deleting reader: {e}")
    finally:
        cursor.close()


def query_readers():
    """管理员：查询所有读者"""
    connection = Connector.get_connection()
    cursor = connection.cursor()
    try:
        query = "SELECT * FROM readers"
        cursor.execute(query)
        return cursor.fetchall()
    except Exception as e:
        print(f"Error querying readers: {e}")
    finally:
        cursor.close()


# 管理借阅
def delete_log(log_id):
    """管理员：删除借阅日志"""
    connection = Connector.get_connection()
    cursor = connection.cursor()
    try:
        query = "DELETE FROM borrow_logs WHERE log_id = %s" 
        cursor.execute(query, (log_id,))
        connection.commit()
    except Exception as e:
        print(f"Error deleting log: {e}")
    finally:
        cursor.close()


def query_logs():
    """管理员：查询所有借阅日志"""
    connection = Connector.get_connection()
    cursor = connection.cursor()
    try:
        query = "SELECT * FROM borrow_logs"
        cursor.execute(query)
        return cursor.fetchall()
    except Exception as e:
        print(f"Error querying logs: {e}")
    finally:
        cursor.close()


# 信息统计
def get_statistics():
    """管理员：获取统计信息"""
    connection = Connector.get_connection()
    cursor = connection.cursor()
    try:
        query = """
            SELECT
                (SELECT COUNT(*) FROM books) AS book_count,
                (SELECT COUNT(*) FROM theses) AS thesis_count,
                (SELECT SUM(borrow_count) FROM books) AS book_borrows,
                (SELECT SUM(download_count) FROM theses) AS thesis_downloads
        """
        cursor.execute(query)
        return cursor.fetchone()
    except Exception as e:
        print(f"Error getting statistics: {e}")
    finally:
        cursor.close()

# 用户功能

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

def borrow_book(user_id, book_id):
    """用户：借阅图书"""
    connection = Connector.get_connection()
    cursor = connection.cursor()
    try:
        # Verify user exists
        cursor.execute("SELECT 1 FROM users WHERE user_id = %s", (user_id,))
        if cursor.fetchone() is None:
            print(f"User ID {user_id} does not exist.")
            return
        # Check if the book is available
        cursor.execute("SELECT stock FROM books WHERE book_id = %s", (book_id,))
        stock = cursor.fetchone()[0]
        if stock > 0:
            # Update the stock
            cursor.execute("UPDATE books SET stock = stock - 1 WHERE book_id = %s", (book_id,))
            # Log the borrowing
            cursor.execute("INSERT INTO borrow_logs (user_id, book_id) VALUES (%s, %s)", (user_id, book_id))
            connection.commit()
        else:
            print("Book is not available for borrowing.")
    except Exception as e:
        print(f"Error borrowing book: {e}")
    finally:
        cursor.close()

def return_book(user_id, book_id):
    """用户：归还图书"""
    connection = Connector.get_connection()
    cursor = connection.cursor()
    try:
        # Update the stock
        cursor.execute("UPDATE books SET stock = stock + 1 WHERE id = %s", (book_id,))
        # Log the return
        cursor.execute("DELETE FROM borrow_logs WHERE user_id = %s AND book_id = %s", (user_id, book_id))
        connection.commit()
    except Exception as e:
        print(f"Error returning book: {e}")
    finally:
        cursor.close()

def user_exists(user_id):
    connection = Connector.get_connection()  # Assuming Connector is your database connection manager
    cursor = connection.cursor()
    try:
        # Execute a query to check if the user exists
        cursor.execute("SELECT 1 FROM users WHERE user_id = %s", (user_id,))
        # Fetch one result; if it exists, the user exists
        return cursor.fetchone() is not None
    except Exception as e:
        print(f"Error checking user existence: {e}")
        return False
    finally:
        cursor.close()
