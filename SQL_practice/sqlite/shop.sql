-- 商品库存练习：请先用 SQLite: Use Database 选择 shop.db。
-- 表名：products，共 20 条虚构商品数据，仅用于 SQL 练习。
-- id：商品编号（整数）。
-- name：商品名称（文本）；“笔记本”属于文具，是纸质笔记本。
-- category：商品分类（电子产品、文具、图书、日用品）。
-- price：单价（元），包含小数。
-- stock：库存数量（件）；0 表示缺货。
-- country：产地国家。

-- 先运行这条查询，熟悉数据。
SELECT * FROM products;

-- 接下来自己写查询；逐条选中，使用 SQLite: Run Selected Query 运行。
-- 1. 只显示商品名称和单价。
SELECT name, price FROM products;

-- 2. 列出所有不重复的商品分类。
SELECT DISTINCT category FROM products;

-- 3. 统计产地国家一共有多少种。
SELECT COUNT(DISTINCT country) FROM products;

-- 4. 查询单价大于或等于 100 元的商品。
SELECT * FROM products
WHERE price >= 100;

-- 5. 查询库存为 0 的商品。
SELECT * FROM products
WHERE stock = 0;

-- 6. 查询分类为“图书”的商品，只显示名称和单价。
SELECT name, price FROM products
WHERE category = '图书';

-- 7. 按单价从高到低显示所有商品。
SELECT * FROM products
ORDER BY price DESC;

-- 8. 先按分类升序，同一分类内再按单价降序排列。
SELECT * FROM products
ORDER BY category, price DESC;
