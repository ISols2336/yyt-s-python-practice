
-- SQL 中，两个短横线 -- 表示单行注释，注释不会被执行。
-- 本文件按顺序介绍知识点：后面重复出现的部分不再解释，重点说明新语法。

-- 1. 查询全部数据
-- SELECT：指定结果中要显示哪些列。
-- *：表示所有列。
-- FROM：指定从哪张表读取数据；这里的表名是 tech_sites_practice。
-- ;：表示一条语句结束；一条语句可以分多行写，但换行不能代替分号。
SELECT * FROM tech_sites_practice;

-- 2. 查询指定的列
-- name, url：只显示名称和网址；用逗号分隔多个列名。
-- SELECT 后面的列名顺序，也是查询结果中列的显示顺序。
SELECT name, url FROM tech_sites_practice;

-- 3. 查询不重复的国家
-- DISTINCT：去除查询结果中的重复值，这里让每个国家只显示一次。
-- 它只影响查询结果，不会删除或修改表里的原始数据。
SELECT DISTINCT country FROM tech_sites_practice;

-- 4. 统计有多少种不同的网站分类
-- COUNT(...)：计数函数，返回一个数量，而不是逐条列出数据。
-- COUNT(DISTINCT category)：统计 category 中不同的非 NULL 值有多少个。
-- NULL 表示缺失值；这里统计的是分类种数，不是网站总数。
-- 补充区别：COUNT(*) 统计行数，COUNT(category) 统计该列非 NULL 的值数。
SELECT COUNT(DISTINCT category) FROM tech_sites_practice;

-- 5. 按条件筛选行
-- WHERE：只保留符合条件的行；没有 WHERE 时，不按条件过滤行。
-- country = "中国"：只保留国家为中国的行；= 表示比较是否相等。
-- 文本值通常用单引号写，例如 '中国'；本句的双引号写法在当前 SQLite 中可用。
SELECT * FROM tech_sites_practice
WHERE country = "中国";

-- 6. 使用数值条件
-- >=：大于或等于，所以 id 为 5 的行也会被选中。
-- 数字 5 不需要加引号；这里按 id 的值筛选，不是取“第 5 行之后”的数据。
SELECT id FROM tech_sites_practice
WHERE id >= 5;

-- 7. 对结果排序
-- ORDER BY：指定结果按哪一列排序；本句按 name 排序。
-- 不写排序方向时，默认升序 ASC；文本先后顺序由数据库的排序规则决定。
-- 排序只改变结果的显示顺序，不会改变表中的数据。
-- 不写 ORDER BY 时，不应依赖查询结果具有固定顺序。
SELECT name, description FROM tech_sites_practice
ORDER BY name;

-- 8. 用没有显示在结果中的列排序
-- 本句显示 name 和 description，但使用 country 排序。
-- 排序依据不一定要出现在 SELECT 的列清单里。
SELECT name, description FROM tech_sites_practice
ORDER BY country;

-- 9. 多列排序，并分别指定方向
-- ASC：升序；DESC：降序。
-- country ASC, name DESC：先按国家升序，国家相同时再按名称降序。
-- 逗号分隔多个排序条件，越靠左的条件优先级越高。
SELECT * FROM tech_sites_practice
ORDER BY country ASC, name DESC;

-- 10. 多个条件同时满足，并按文字模式查找
-- AND：连接多个条件，只有所有条件都满足，这一行才会保留。
-- LIKE：判断文本是否符合指定模式，常用于模糊查找。
-- %：匹配零个或任意多个字符；'%i%' 表示名称中任意位置包含 i。
-- 'i%' 是以 i 开头，'%i' 是以 i 结尾；百分号位置会改变匹配要求。
-- 本句要求：国家是中国，并且名称包含 i；仅满足其中一个条件还不够。
-- SQLite 默认的 LIKE 对 ASCII 英文字母不区分大小写，因此 i 也能匹配 I。
SELECT * FROM tech_sites_practice
WHERE country = "中国" AND name LIKE '%i%';

-- 11. 多个条件至少满足一个
-- OR：左右条件至少满足一个就保留，两个都满足也会保留。
-- 本句选择人工智能或代码托管的网站；没有国家条件，所以不限国家。
-- OR 不会把同一条记录重复显示，也不是先筛一次再筛一次。
-- 筛选后的结果再按国家排序；这里排序没有增加国家筛选条件。
SELECT * FROM tech_sites_practice
WHERE category = "人工智能" OR category = "代码托管"
ORDER BY country;

-- 12. 对一组条件整体取反
-- NOT：对条件取反；本句对括号里的整个“法国或美国”条件取反。
-- 括号里的 OR 先判断是不是法国或美国，再由 NOT 排除这两种情况。
-- 因此本句保留的是：既不是法国，也不是美国的网站。
-- 对当前 country 没有 NULL 的数据，也可理解为 country <> '法国' AND country <> '美国'。
-- <> 表示不等于；排除多个国家时，这些“不等于”条件应使用 AND 连接。
-- 如果写成 NOT (country = '法国') OR NOT (country = '美国')，每个国家都会满足至少一个条件，反而全部保留。
-- 混合条件且没有括号时，优先级是 NOT 高于 AND，AND 高于 OR；用括号明确分组更容易读懂。
-- 补充：country 为 NULL 时，上面的国家比较结果不确定，不会被本句选中。
SELECT * FROM tech_sites_practice
WHERE NOT (country = "法国" OR country = "美国");
