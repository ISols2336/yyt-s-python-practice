-- SQLBook: Code
-- Active: 1792068170224@@127.0.0.1@3306@practicedb
-- 今日练习：建库、建表、插入数据，再查询验证。
-- 运行前确认活动连接和当前数据库；连接的备注名不等于当前数据库名。
-- 本文件保留了已执行的 INSERT，练习时逐条运行，不要直接“全部运行”。

-- CREATE DATABASE：创建数据库；IF NOT EXISTS：同名库不存在时才创建。
-- 已存在时跳过创建，保留原库和数据，不会创建第二个同名库。
CREATE DATABASE IF NOT EXISTS practiceDB;

-- VERSION()：查看当前连接的数据库服务版本。
SELECT VERSION();

-- SHOW DATABASES：列出当前账号可以看到的数据库。
SHOW DATABASES;

-- CREATE TABLE：在当前数据库中创建表，括号内定义各列。
-- IF NOT EXISTS：同名表存在时跳过，不会检查或修改已有表的结构。
-- 建表前可用下面的 DATABASE() 查询确认当前库；本练习应使用 practicedb。
-- 也可以先单独执行 USE practicedb; 来选择数据库。
-- 每列之间用英文逗号分隔，最后一列后面不加逗号。
CREATE TABLE IF NOT EXISTS practice_table(
    -- INT：整数；PRIMARY KEY：主键，值不能重复，也不能为 NULL。
    id int PRIMARY KEY,
    -- VARCHAR(225)：最多 225 个字符；NOT NULL：不能存 NULL，但允许空字符串 ''。
    title VARCHAR(225) NOT NULL,
    -- 没有 NOT NULL 限制，这列可以暂时存 NULL。
    file_path VARCHAR(225),
    -- TEXT：保存较长的文本。
    description TEXT,
    -- DATE：保存日期；插入时可写成 '2026-10-15'。
    taken_on DATE
);

-- DATABASE()：查看当前连接实际选中的数据库。
SELECT DATABASE();

SELECT * FROM practice_table;

-- INSERT INTO：向表中添加记录；VALUES：提供要插入的值。
-- 省略列名时，必须按表的列顺序提供全部列的值。
-- 本表顺序为 id、title、file_path、description、taken_on。
-- 数字不加引号，文本和日期加单引号；NULL 不加引号，表示缺失值。
-- 逗号后可以加空格；不能用连续逗号代替 NULL。
-- 这条记录已插入；再次执行会因主键 id = 1 重复而报错。
INSERT INTO practice_table
VALUES(1, '龙娘的第一张照片', NULL, 'gpt撒娇要写进去的', '2026-01-01');

SELECT * FROM practice_table;

-- 检查编号 2 是否已使用；有结果表示存在，但这条查询不会自动阻止后续插入。
SELECT id FROM practicedb.practice_table WHERE id = 2;

-- 多行插入练习：显式列出列名，让每个值的对应关系更清楚。
-- practicedb.practice_table：明确指定数据库和表。
-- 每组括号是一条记录，都必须有 5 个值，并按上面列出的列名顺序对应。
-- 组与组之间用英文逗号分隔，最后一组后面用分号结束；换行不能代替逗号。
-- id = 4 的两个 NULL 分别对应 file_path 和 description。
-- 编号 3、4、5 已插入，保留代码作笔记，不要重复执行这条 INSERT。
INSERT INTO practicedb.practice_table
    (id, title, file_path, description, taken_on)
VALUES
    (3, '和龙娘一起吃早餐', NULL, '你捧着热豆浆,龙娘盯着最后一个小笼包,等你分一半。', '2026-10-16'),
    (4, '午后的陪伴', NULL, NULL, '2026-10-17'),
    (5, '睡前的小小庆祝', NULL, '你终于写对了 SQL,龙娘举起爪爪,和你轻轻击掌。', '2026-10-18');

SELECT * FROM practicedb.practice_table ORDER BY id;

-- 2026-10-16：修改、删除、限制返回条数，以及计算比例。
-- UPDATE：修改表中已有的记录；SET：指定要修改的列和新值。
-- 本句只把编号 4 的描述改为“龙娘暖暖的”，其他列保持原值。
-- UPDATE 不写 WHERE 会修改所有行；执行前先核对条件。
UPDATE practice_table
SET description = '龙娘暖暖的'
WHERE id = 4;
-- SQLBook: Code
-- 查询验证：检查编号 4 的 description 是否已更新。
SELECT * FROM practice_table;

-- DELETE FROM：删除符合条件的整行记录，不只是清空某一列。
-- 本句删除编号 5 的记录，表结构和其他编号的记录仍保留。
-- DELETE 不写 WHERE 会删除表中所有记录；执行前先核对条件。
-- 同一删除语句再次运行时，若编号 5 已不存在，通常影响 0 行。
DELETE FROM practice_table
WHERE id = 5;

-- 查询验证：检查编号 5 是否已从结果中消失。
SELECT * FROM practice_table;

-- LIMIT 3：最多返回 3 条记录；不足 3 条时返回现有记录。
-- LIMIT 只限制查询结果，不会删除其余记录。
-- 不写 ORDER BY，不能保证每次返回的是哪些行；要按编号取前 3 条，可在 LIMIT 前加 ORDER BY id。
SELECT * FROM practice_table
LIMIT 3;

-- COUNT(*) * 0.8：用总记录数乘以 80%。
-- CEIL(...)：向上取整，例如 CEIL(3.2) = 4，CEIL(4) = 4。
-- 本句只返回计算得到的条数，不会直接返回这些记录。
-- 例如总共 5 条时算出 4，总共 4 条时也算出 4；向上取整后，实际比例可能高于 80%。
SELECT CEIL(COUNT(*) * 0.8) FROM practice_table;

-- LIMIT 4：固定最多取 4 条，不会随总记录数自动变成 80%。
-- 如果想按上面的计算结果取记录，这里先手动填写算出的整数；总记录数变化后要重新计算。
-- 若要明确取编号最小的 4 条，同样应在 LIMIT 前加 ORDER BY id。
SELECT * FROM practice_table
LIMIT 4;
