-- 创建数据库 labdata
CREATE DATABASE labdata;

-- 切换到数据库 labdata
\c labdata;

-- === 1. 用户表 ===
-- 用户表：存储管理员和一般用户的信息
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,                -- 用户ID
    username VARCHAR(50) NOT NULL UNIQUE,      -- 用户名
    password VARCHAR(100) NOT NULL,            -- 密码（需要加密存储）
    role VARCHAR(20) NOT NULL CHECK (role IN ('admin', 'reader')) -- 用户角色：管理员或一般用户
);

-- === 2. 论文表 ===
-- 论文表：存储论文信息，支持公开与否
CREATE TABLE theses (
    thesis_id SERIAL PRIMARY KEY,              -- 论文ID
    title VARCHAR(100) NOT NULL,               -- 论文标题
    author VARCHAR(50),                        -- 作者
    download_count INT DEFAULT 0,              -- 下载次数
    doi VARCHAR(100) UNIQUE                    -- DOI，确保唯一性
);

-- === 3. 图书表 ===
-- 图书表：存储图书信息，支持借阅管理
CREATE TABLE books (
    book_id SERIAL PRIMARY KEY,                -- 图书ID
    title VARCHAR(100) NOT NULL,               -- 书名
    author VARCHAR(50),                        -- 作者
    publisher VARCHAR(100),                    -- 出版社
    publication_date DATE,                     -- 出版日期
    stock INT NOT NULL CHECK (stock >= 0)      -- 库存
);

-- === 4. 借阅记录表 ===
-- 借阅记录表：存储图书借阅和归还的日志
CREATE TABLE borrow_logs (
    log_id SERIAL PRIMARY KEY,                 -- 日志ID
    user_id INT NOT NULL REFERENCES users(user_id) ON DELETE CASCADE, -- 借阅人ID
    book_id INT NOT NULL REFERENCES books(book_id) ON DELETE CASCADE  -- 图书ID
);

-- === 5. 读者表 ===
-- 读者表：存储读者信息
CREATE TABLE readers (
    reader_id SERIAL PRIMARY KEY,              -- 读者ID
    name VARCHAR(100) NOT NULL,                -- 姓名
    email VARCHAR(100) NOT NULL UNIQUE,        -- 邮箱
    phone VARCHAR(20)                          -- 电话
);

-- === 6. 信息统计视图 ===
-- 图书数量统计
CREATE OR REPLACE VIEW book_statistics AS
SELECT 
    COUNT(*) AS total_books,
    SUM(stock) AS total_stock
FROM books;

-- 论文数量统计
CREATE OR REPLACE VIEW thesis_statistics AS
SELECT 
    COUNT(*) AS total_theses,
    SUM(download_count) AS total_downloads
FROM theses;

-- 借阅日志统计
CREATE OR REPLACE VIEW borrow_statistics AS
SELECT 
    COUNT(*) AS total_borrows
FROM borrow_logs;

-- === 7. 权限控制 ===
-- 游客查询公开资源
-- 游客查询公开论文
CREATE OR REPLACE VIEW guest_visible_theses AS
SELECT thesis_id, title, author, download_count
FROM theses;

-- 游客查询公开图书
CREATE OR REPLACE VIEW guest_visible_books AS
SELECT book_id, title, author, publisher, publication_date
FROM books;

-- === 8. 触发器 ===
-- 自动更新论文下载次数
CREATE OR REPLACE FUNCTION update_thesis_download_count()
RETURNS TRIGGER AS $$
BEGIN
    UPDATE theses SET download_count = download_count + 1 WHERE thesis_id = NEW.thesis_id;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- === 9. 下载日志表 ===
-- 记录论文下载日志
CREATE TABLE download_logs (
    log_id SERIAL PRIMARY KEY,                 -- 下载日志ID
    user_id INT REFERENCES users(user_id) ON DELETE CASCADE, -- 下载人ID
    thesis_id INT NOT NULL REFERENCES theses(thesis_id) ON DELETE CASCADE -- 论文ID
);

CREATE TRIGGER trigger_update_thesis_download
AFTER INSERT ON download_logs
FOR EACH ROW
EXECUTE FUNCTION update_thesis_download_count();