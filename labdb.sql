-- 创建数据库 labdata
CREATE DATABASE labdata;

-- 切换到数据库 labdata
\c labdata;

-- === 1. 用户表 ===
CREATE TABLE users (
    username VARCHAR(50) PRIMARY KEY,          -- 用户名
    password VARCHAR(100) NOT NULL,            -- 密码（需要加密存储）
    role VARCHAR(20) NOT NULL CHECK (role IN ('admin', 'reader')) -- 用户角色：管理员或一般用户
);

-- === 2. 论文表 ===
CREATE TABLE theses (
    title VARCHAR(100) PRIMARY KEY,            -- 论文标题
    author VARCHAR(50),                        -- 作者
    download_count INT DEFAULT 0,              -- 下载次数
    doi VARCHAR(100) UNIQUE                    -- DOI，确保唯一性
);

-- === 3. 图书表 ===
CREATE TABLE books (
    title VARCHAR(100) PRIMARY KEY,            -- 书名
    author VARCHAR(50),                        -- 作者
    publisher VARCHAR(100),                    -- 出版社
    publication_date DATE,                     -- 出版日期
    stock INT NOT NULL CHECK (stock >= 0),     -- 库存
    borrow_count INT DEFAULT 0                 -- 借阅量
);

-- === 4. 读者表 ===
CREATE TABLE readers (
    name VARCHAR(100) PRIMARY KEY,             -- 姓名
    email VARCHAR(100) NOT NULL UNIQUE,        -- 邮箱
    phone VARCHAR(20)                          -- 电话
);

-- === 5. 日志表 ===
CREATE TABLE logs (
    reader_name VARCHAR(100) NOT NULL REFERENCES readers(name) ON DELETE CASCADE, -- 借阅者姓名
    book_title VARCHAR(100) NOT NULL REFERENCES books(title) ON DELETE CASCADE,   -- 借阅图书名
    time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP                             -- 借阅时间
);

-- === 6. 信息统计视图 ===
-- 图书数量统计
CREATE OR REPLACE VIEW book_statistics AS
SELECT 
    COUNT(*) AS total_books,                   -- 图书总数
    SUM(stock) AS total_stock,                 -- 总库存
    SUM(borrow_count) AS total_borrows         -- 总借阅量
FROM books;

-- 论文数量统计
CREATE OR REPLACE VIEW thesis_statistics AS
SELECT 
    COUNT(*) AS total_theses,                  -- 论文总数
    SUM(download_count) AS total_downloads     -- 总下载量
FROM theses;