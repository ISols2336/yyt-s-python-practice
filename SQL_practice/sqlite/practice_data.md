# 网站数据库练习数据

在 VS Code 的 SQLite 扩展里打开 `practice.db`，并为 `sqlite.sql` 选择这个数据库。
表名仍为 `tech_sites_practice`，列名仍为 `id、name、category、url、description、country`。

精简后共有 20 条记录、13 个国家、19 个分类，ID 为 1–20。

原有网站包含 9 个分类。新增虚构网站涵盖数据库工具、云计算、网络安全、移动开发、游戏开发、运维工具、软件测试、技术资讯、科学计算、API工具。

- id 1–10：保留原有的网站记录。
- id 大于 10：虚构练习网站，网址使用 `.example`，不是实际网站；国家和分类是用于练习的设定。
- 原记录 ID 1–10 保留，虚构记录重新编号为 11–20，避免编号间隔影响辨认。一般情况下，记录总数应通过 COUNT(*) 查询，而不是看最大 ID。
- 国家包括美国、中国、挪威、日本、德国、英国、法国、加拿大、澳大利亚、印度、韩国、瑞典、新加坡。
- 原 Excel 文件仍只有原来的数据；本次新增数据直接写入数据库，没有修改 Excel。
- `practice.before_expansion.db` 是扩充前的备份；日常练习请选择 `practice.db`。
- `practice.before_category_update.db` 是增加分类前的备份。

可以先查看数据：

```sql
SELECT * FROM tech_sites_practice;
```

适合练习的条件组合：

```sql
SELECT name, category, country
FROM tech_sites_practice
WHERE country = '日本' AND category = '数据库工具';
```

还可以自行练习：列出所有国家、统计不同分类数、筛选某个国家的网站、按国家和名称排序。
