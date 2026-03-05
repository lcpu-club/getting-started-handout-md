# PKU计算机基础能力手册

本地部署：

```bash
pip install zensical
zensical serve
```

如果你修改了 `includes/abbreviations.md`（全局 tooltip 词库）后前端没变化，请使用“清缓存构建”：

```bash
zensical build -c
zensical serve
```
