---
icon: material/swap-horizontal
---
# 数据存储和交换

在数字世界里，数据是信息的载体，而数据交换则是信息传递的桥梁。本章将探讨数据交换的各种方法和技术。

为了便于数据交换，不同系统、服务和软件之间需要遵循一定的协议和标准。这些协议和标准确保了数据在传输过程中能够被正确理解和处理。现在比较通行的数据交换格式：JSON、XML、CSV、Yaml、Toml。而现行存储数据的数据库系统往往是用 SQL 数据库来存储结构化数据，用 NoSQL 数据库来存储非结构化数据。

## SQL数据库

SQL（Structured Query Language）是一种用于管理**关系型数据库**的标准语言。

关系型数据库的本质是**表格**。每个表格由行和列组成，行表示记录，列表示字段。SQL 数据库使用预定义的模式（schema）来组织数据，这意味着数据必须符合特定的结构。

SQL 有着不同的实现，常见的有 MySQL、PostgreSQL、SQLite 和 Microsoft SQL Server 等。这些实现大同小异，主要功能几乎相同，但在性能、扩展性和特定功能上有所区别。

### 键和表

刚刚说到，SQL 数据库组织数据的方式是通过表格。每个表格都有一个或多个**键**或字段，用于唯一标识每一行数据。常见的键类型有：

- 主键（Primary Key）：唯一标识表中的每一行数据，不能重复且不能为空。
- 外键（Foreign Key）：用于在两个表之间建立关系，引用另一个表的主键。

表格中的每一列都有一个数据类型，常见的数据类型包括整数、浮点数、字符串、日期等。通过定义合适的数据类型，可以确保数据的完整性和一致性。

在 SQL 中，表格之间可以通过关系进行连接（JOIN），这使得我们可以从多个表中提取相关数据。例如，我们可以有一个“用户”表和一个“订单”表，通过用户 ID 将它们连接起来，以获取每个用户的订单信息。SQL 鼓励用户把数据存在多个表格中，通过关系来组织数据（类似 MS Access 行为），而不是把所有数据都存储在一个大表格中（类似 Excel 行为）。

### SQL查询语言

查询语言分四种类型：数据查询语言（DQL）、数据定义语言（DDL）、数据操作语言（DML）和数据控制语言（DCL）。

- 数据查询语言（DQL）：用于从数据库中检索数据，最常用的命令是 SELECT。
- 数据定义语言（DDL）：用于定义和修改数据库结构，包括 CREATE、ALTER 和 DROP 等命令。
- 数据操作语言（DML）：用于插入、更新和删除数据，包括 INSERT、UPDATE 和 DELETE 等命令。
- 数据控制语言（DCL）：用于控制对数据库的访问权限，包括 GRANT 和 REVOKE 等命令。

SQL 的查询等相当类似自然语言，这使得它相对容易学习和使用。以下是一些常见的 SQL 查询示例：

- 选择所有列的数据：

```sql
SELECT * FROM table_name;
```

- 选择特定列的数据：

```sql
SELECT column1, column2 FROM table_name;
```

- 插入新数据：

```sql
INSERT INTO table_name (column1, column2) VALUES (value1, value2);
```

- 更新现有数据：

```sql
UPDATE table_name SET column1 = value1 WHERE condition;
```

- 删除数据：

```sql
DELETE FROM table_name WHERE condition;
```

### SQL数据库的自动更新

在实际应用中，数据经常需要自动更新以保持最新状态，例如想输入学生的成绩单就能自动计算其 GPA。实现自动更新的常见方法包括触发器（Triggers）和存储过程（Stored Procedures）。

- 触发器：是一种特殊的存储过程，当特定事件（如插入、更新或删除）发生时自动执行。触发器可以用于自动验证数据、维护审计日志或执行复杂的业务逻辑。
- 存储过程：是一组预编译的 SQL 语句，可以通过调用来执行。存储过程可以接受参数，返回结果，并且可以包含复杂的逻辑和控制结构。

例如，可以创建一个触发器，当学生的成绩被插入或更新时，自动计算并更新其 GPA：

```sql
CREATE TRIGGER update_gpa
AFTER INSERT OR UPDATE ON grades
FOR EACH ROW
BEGIN
  DECLARE new_gpa FLOAT;
  -- 计算新的GPA逻辑
  UPDATE students SET gpa = new_gpa WHERE student_id = NEW.student_id;
END;
```

上述 SQL 语言中，两个横线（`--`）表示注释内容。如果用存储过程实现类似功能，可以这样写：

```sql
CREATE PROCEDURE calculate_gpa(IN student_id INT)
BEGIN
  DECLARE new_gpa FLOAT;
  -- 计算新的GPA逻辑
  UPDATE students SET gpa = new_gpa WHERE student_id = student_id;
END;
```

然后可以在需要时调用存储过程：

```sql
CALL calculate_gpa(12345);
```

可以看出，触发器是一个自动执行的函数，而存储过程是一个需要手动调用的函数。但两者都可以用于实现 SQL 数据库的自动更新功能。

想用好 SQL 数据库，实际上查询语言不是关键，其关键实际上在于怎样设计好数据库的表格和关系，以及哪些内容可以自动更新、哪些内容需要手动更新（如果数据量很大，自动更新可能会影响性能）。这需要根据具体的应用场景和需求来进行设计和优化，也需要数据库的编写者有着对业务逻辑的深刻理解和对数据的高敏感度，才能设计出高效的数据库结构。

## 数据交换格式

数据交换格式是指用于在不同系统之间传输和存储数据的标准化格式。常见的数据交换格式包括 JSON、XML、CSV、YAML 和 TOML 等。

当然，我们大可以自己创建自己的“数据交换格式”，但这样做会带来兼容性和可维护性的问题，因此通常建议使用已有的标准化格式。

### JSON

JSON（JavaScript Object Notation）是一种轻量级的数据交换格式，易于人类阅读和编写，同时也易于机器解析和生成。JSON 使用键值对的形式来表示数据，支持嵌套结构。例如，下面是一个简单的 JSON 示例：

```json
{
  "name": "Alice",
  "age": 30,
  "is_student": false,
  "courses": ["Math", "Science"],
  "address": {
    "street": "123 Main St",
    "city": "Wonderland"
  }
}
```

容易看出，JSON 的结构是“键值对”，其中值可以是字符串、数字、布尔值、数组或另一个对象（用大括号 `{}` 表示）。JSON 广泛应用于 Web 开发中，用于客户端和服务器之间的数据交换。

JSON 和 Python 的字典（dict）结构非常相似，Python 提供了内置的 `json` 模块来处理 JSON 数据。可以使用 `json` 模块将 Python 对象转换为 JSON 字符串，或将 JSON 字符串解析为 Python 对象。例如：

```python
import json

# 将Python对象转换为JSON字符串
data = {"name": "Alice", "age": 30}
json_string = json.dumps(data)
print(json_string)
# 将JSON字符串解析为Python对象
parsed_data = json.loads(json_string)
print(parsed_data)
```

而 C++ 则不得不调用著名的 nlohmann/json 库来处理 JSON 数据。

由于 JSON 和 JavaScript 的语法非常相似，JavaScript 也有内置的 JSON 对象来处理 JSON 数据。

### XML

XML（eXtensible Markup Language）是一种用于表示结构化数据的标记语言。与 HTML 类似，XML 使用标签来定义数据的结构和内容。XML 的标签是用户自定义的，可以根据需要创建任意数量的标签。例如，下面是一个简单的 XML 示例：

```xml
<person>
  <name>Alice</name>
  <age>30</age>
  <is_student>false</is_student>
  <courses>
    <course>Math</course>
    <course>Science</course>
  </courses>
  <address>
    <street>123 Main St</street>
    <city>Wonderland</city>
  </address>
</person>
```

上述内容是一段相当“原教旨主义”的 XML 代码，标签必须成对出现，并且区分大小写。XML 支持嵌套结构，可以表示复杂的数据关系。而稍现代的 XML 则允许自闭合标签，例如：

```xml
<person>
  <name="Alice" />
  <age="30" />
</person>
```

XML 相当重型且冗长，解析 XML 数据通常需要使用专门的库，例如 Python 的 `xml.etree.ElementTree` 模块或 C++ 的 TinyXML 库。但因为其更加严格的结构和自定义标签的灵活性，XML 在某些领域（如配置文件和文档存储）仍然被广泛使用。例如在游戏《物竞天择》中的自定义场景中，就使用了 XML 格式来存储场景中的事件信息；在 .NET 框架的 MAUI 应用程序中，XAML（eXtensible Application Markup Language）是一种基于 XML 的标记语言，用于定义用户界面布局和行为。

### CSV

CSV（Comma-Separated Values）是一种简单的文本文件格式，直译就是“逗号分隔的值”。CSV 文件中的每一行表示一条记录，字段之间使用逗号分隔。例如，下面是一个简单的 CSV 示例：

```text
name,age,is_student
Alice,30,false
Bob,25,true
```

CSV 可以表示简单的表格数据，易于阅读和编写。由于其简单性，CSV 文件可以使用任何文本编辑器打开和编辑。CSV 文件广泛应用于数据导入和导出，例如电子表格软件（如 Microsoft Excel）通常支持 CSV 格式。

在 Python 中，可以使用内置的 `csv` 模块来处理 CSV 数据。例如：

```python
import csv
# 读取CSV文件
with open('data.csv', mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
# 写入CSV文件
with open('data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['name', 'age', 'is_student'])
    writer.writerow(['Alice', 30, False])
```

但在仅分析 CSV 文件时，Pandas 库更为强大和方便。

C++ 中可以使用诸如 RapidCSV 等第三方库来处理 CSV 数据。

### YAML

YAML（YAML Ain't Markup Language）是一种人类可读的数据序列化格式，设计目标是简洁和易读。YAML 使用缩进来表示数据的层次结构，类似于 Python 的代码风格。例如，下面是一个简单的 YAML 示例：

```yaml
name: Alice
age: 30
is_student: false
courses:
  - Math
  - Science
address:
  street: 123 Main St
  city: Wonderland
```

YAML 是键值对结构，比 JSON 更简洁，支持复杂的数据类型和嵌套结构；但是其缩进要求相当严格，且冒号后面必须有空格，否则会报错。游戏《物竞天择》的自定义场景文件就使用了假的 YAML 格式来存储各种参数设置，虽然一眼望上去很像 YAML，但实际上并不符合 YAML 的语法规范（冒号后面没有空格），这让笔者当年编写解析器时吃了不少苦头。

YAML 广泛应用于配置文件和数据交换，配置文件通常使用 YAML 格式。

### Toml

TOML（Tom's Obvious, Minimal Language）是一种简洁易读的配置文件格式，设计目标是易于编写和理解。TOML 使用键值对和表格来表示数据的层次结构。例如，下面是一个简单的 TOML 示例：

```toml
name = "Alice"
age = 30
is_student = false
[courses]
courses = ["Math", "Science"]
[address]
street = "123 Main St"
city = "Wonderland"
```

TOML 的语法相对简单，支持多种数据类型和嵌套结构。TOML 广泛应用于配置文件和数据交换，特别是在 Rust 编程语言的生态系统中，TOML 被用作 Cargo 包管理器的配置文件格式。

### INI

INI 是一种简单的配置文件格式，使用键值对和节（section）来组织数据。INI 文件通常由多个节组成，每个节包含若干键值对。例如，下面是一个简单的 INI 示例：

```ini
[person]
name=Alice
age=30
is_student=false
[courses]
course1=Math
course2=Science
```

INI 看起来很像 YAML 和 TOML，但实际上语法更为简单，甚至到了简陋的地步。INI 缺乏对复杂数据结构的支持，因此在现代应用中逐渐被 YAML 和 TOML 等更强大的格式所取代。但由于其简单性，INI 文件仍然被一些应用程序用作配置文件格式，例如古老的游戏《红色警戒2》的配置文件就使用了 INI 格式，即使是现代移植版本（如 OpenRA）也继续沿用这种格式，mod 作者也往往被称作 ini 玩家。

### 非显式数据交换格式

除了上述显式的数据交换格式外，还有一些非显式的数据交换格式，例如二进制格式。此类格式与上述文本格式不同，通常用于高效存储和传输数据。常见的二进制格式包括 Protocol Buffers、Avro 和 MessagePack 等。这些格式人类不可读，但在性能和存储效率方面具有优势，适用于需要高效数据交换的场景。

与之类似的还有 Base64 编码，它并不是一种数据交换格式，而是一种将二进制数据转换为文本格式的方法。Base64 编码使用 64 个字符来表示二进制数据，使任何类型的数据（甚至包括图片和音频）都可以以文本形式进行传输和存储。Base64 编码常用于电子邮件和 Web 应用程序中，以确保数据在传输过程中不会被损坏。

## NoSQL

NoSQL 不是一种产品，而是一类数据库管理系统的总称，旨在处理大规模分布式数据存储和高并发访问。NoSQL 数据库通常不使用传统的关系型数据库模型，而是采用更灵活的数据模型，如键值对、文档、列族和图形等。

常见的 NoSQL 数据库包括 MongoDB、Cassandra、Redis 和 Neo4j 等。NoSQL 数据库通常具有高可扩展性和高性能，适用于大数据分析、实时应用和分布式系统等场景。

笔者对于 NoSQL 的了解甚少，因此希望同学们能够自行查阅相关资料以深入了解 NoSQL 数据库的工作原理和应用场景。但现在的 SQL 数据库也加入了对非结构化数据的支持，例如 PostgreSQL 现在也支持 JSON 数据类型，因此在选择数据库时需要根据具体的应用需求进行权衡和选择。

## 正则表达式

正则表达式（Regular Expression，简称 Regex 或 RegExp）是一种用于描述字符串模式的工具。它可以帮助我们在文本中查找、替换和提取特定的字符串。正则表达式在搜索、文本处理、数据验证等方面有着广泛的应用，合理使用也能够提高工作效率。

### 语法概要

正则表达式的本质是“字符串匹配”，因此包括三种元素：普通字符、元字符和量词。

**普通字符**是指字母、数字和其他非特殊字符，这些字符在正则表达式中表示它们本身，例如 `a`、`1` 等。

**元字符**则指的是“这个字符我不确定”，例如：

- `.`：匹配除换行符以外的任意单个字符。
- `\d`：匹配任意数字，等价于 `[0-9]`。
- `\D`：匹配任意非数字，等价于 `[^0-9]`。
- `\w`：匹配任意字母、数字和下划线，等价于 `[a-zA-Z0-9_]`。
- `\W`：匹配任意非字母、数字和下划线，等价于 `[^a-zA-Z0-9_]`。
- `\s`：匹配任意空白字符（空格、制表符、换行符等）。
- `\S`：匹配任意非空白字符。
- `^`：匹配字符串的开头。
- `$`：匹配字符串的结尾。

另外，如果想要匹配一组已知字符中的一个，可以使用方括号，例如 `[abc]` 表示匹配字符“a”、“b”或者“c”中的一个；也可以反选，例如 `[^abc]` 表示匹配除“a”、“b”、“c”以外的任意字符。为了简便起见，还可以使用短横线来表示范围，例如 `[a-z]` 表示匹配任意小写字母。如果想匹配字符 `.` 本身而不是把它当作元字符使用，可以使用反斜杠进行转义，例如 `\.` 表示匹配该字符本身。

而**量词**指的是“这个字符出现多少次”，例如：

- `*`：匹配前面的字符零次或多次。
- `+`：匹配前面的字符一次或多次。
- `?`：匹配前面的字符零次或一次。
- `{n}`：匹配前面的字符恰好 n 次。
- `{n,}`：匹配前面的字符至少 n 次。
- `{n,m}`：匹配前面的字符至少 n 次，至多 m 次。

其中，问号 `?` 还有一个用法。首先，我们要知道正则表达式的匹配是“贪婪”的，也就是说它会尽可能多地匹配字符。例如，正则表达式 `a.*b` 在字符串 `axxxbxxxb` 中会匹配整个字符串，因为 `.*` 会尽可能多地匹配字符。如果我们希望它“非贪婪”地匹配，也就是尽可能少地匹配字符，可以在量词后面加上一个问号 `?`，例如 `a.*?b` 在字符串 `axxxbxxxb` 中只会匹配到 `axxxb`。

以上便是正则表达式的基本语法。通过组合这些元素，我们可以构建出复杂的字符串模式，从而实现强大的文本处理功能。

### 使用示例

!!! example
    我们有一个文本文件，里面包含了很多电子邮件地址。我们想要提取出所有的电子邮件地址。如何使用正则表达式实现？

    提示：电子邮件地址的格式通常是 `用户名@域名`，其中用户名可以包含字母、数字、点、下划线和短横线，域名可以包含字母、数字和点。

!!! success "答案"
    把一类文本转写成正则表达式的一般步骤是：先分块，然后把每一块转写成正则表达式，最后把这些正则表达式组合在一起。这个题目便是一个很好的例子。

    我们把电子邮件地址分成三部分：用户名、`@` 符号和域名。然后，我们分别为每一部分编写正则表达式。

    首先，`@` 符号是最简单的，因为它本身就是一个普通字符。其正则表达式就是 `@`。

    然后，我们来看用户名部分。用户名可以包含字母、数字、点、下划线和短横线，因此我们可以使用方括号来表示这些字符的集合：`[a-zA-Z0-9._\-]`。由于用户名至少需要一个字符，因此我们可以使用量词 `+` 来表示这一点：`[a-zA-Z0-9._\-]+`。

    域名部分类似，其正则表达式为 `[a-zA-Z0-9.\-]+`。注意，域名中不允许出现下划线，因此我们没有把下划线包含在方括号中。

    最后，我们将这三部分组合在一起，得到完整的正则表达式：`[a-zA-Z0-9._\-]+@[a-zA-Z0-9.\-]+`。这个正则表达式可以匹配所有符合电子邮件地址格式的字符串。

这便是正则表达式的基本用法。正则表达式的语法和功能虽然只有这么多，但是它的应用却非常广泛。我们可以使用正则表达式来处理各种文本数据，例如日志文件、配置文件、代码文件等；还可以帮助我们进行数据清洗和转换，例如提取特定字段、替换字符串等，或者仅仅是在 LaTeX 的 `texttt` 前后加上空格。正则表达式还可以用于数据验证，例如验证电子邮件地址、电话号码、身份证号码等。网上有一些有趣的正则化习题，例如一些类似 word puzzle 的游戏，可以帮助我们更好地理解和掌握正则表达式。
