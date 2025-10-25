---
icon: material/database
---
# 数据结构基础

!!! warning
    该文章仍未经过正式校正

!!! note 作者
    本文作者：[username](https://github.com/username)

数据结构是计算机科学中的基础概念，它描述了数据在计算机中的组织、管理和存储方式。选择合适的数据结构可以显著提高程序的效率和性能。在本节中，我们将介绍几种常用的数据结构，并通过 C++ STL（标准模板库）来展示它们的基本使用方法。

## 什么是数据结构

数据结构是一种组织和存储数据的方式，使得我们可以高效地访问和修改数据。不同的数据结构适用于不同的应用场景。例如，如果需要频繁地在序列中间插入或删除元素，链表可能是更好的选择；如果需要快速查找元素，哈希表可能更合适。

理解数据结构的关键在于理解它们的**时间复杂度**和**空间复杂度**。时间复杂度描述了算法执行所需的时间，空间复杂度描述了算法执行所需的内存空间。

## 常用数据结构

### 数组（Array）

数组是最基本的数据结构之一，它是一组连续存储的相同类型的元素。数组的优点是可以通过索引快速访问任意元素（O(1) 时间复杂度），缺点是大小固定，插入和删除操作效率较低。

在 C++ 中，可以使用 `std::array`（固定大小）或 `std::vector`（动态大小）来表示数组：

```cpp
#include <iostream>
#include <vector>
#include <array>

int main() {
    // 固定大小的数组
    std::array<int, 5> arr = {1, 2, 3, 4, 5};
    std::cout << "第一个元素: " << arr[0] << std::endl;
    
    // 动态数组
    std::vector<int> vec = {1, 2, 3, 4, 5};
    vec.push_back(6);  // 在末尾添加元素
    std::cout << "向量大小: " << vec.size() << std::endl;
    
    return 0;
}
```

`std::vector` 是最常用的容器之一，它提供了动态数组的功能，可以自动调整大小。常用操作包括：
- `push_back()`: 在末尾添加元素
- `pop_back()`: 删除末尾元素
- `size()`: 获取元素个数
- `[]` 或 `at()`: 访问指定位置的元素

### 链表（Linked List）

链表是一种线性数据结构，其中每个元素（节点）包含数据和指向下一个节点的指针。链表的优点是插入和删除操作效率高（O(1) 时间复杂度，如果已知位置），缺点是访问任意元素需要遍历（O(n) 时间复杂度）。

C++ STL 提供了 `std::list`（双向链表）和 `std::forward_list`（单向链表）：

```cpp
#include <iostream>
#include <list>

int main() {
    std::list<int> mylist = {1, 2, 3, 4, 5};
    
    // 在开头插入元素
    mylist.push_front(0);
    
    // 在末尾插入元素
    mylist.push_back(6);
    
    // 遍历链表
    for (int val : mylist) {
        std::cout << val << " ";
    }
    std::cout << std::endl;
    
    return 0;
}
```

链表适用于需要频繁插入和删除操作的场景，但不适合需要随机访问的场景。

### 栈（Stack）

栈是一种后进先出（LIFO, Last In First Out）的数据结构。可以想象成一摞盘子，只能从顶部添加或移除盘子。栈的主要操作包括：
- `push()`: 将元素压入栈顶
- `pop()`: 弹出栈顶元素
- `top()`: 查看栈顶元素

C++ STL 提供了 `std::stack`：

```cpp
#include <iostream>
#include <stack>

int main() {
    std::stack<int> s;
    
    // 压入元素
    s.push(1);
    s.push(2);
    s.push(3);
    
    // 查看栈顶元素
    std::cout << "栈顶元素: " << s.top() << std::endl;
    
    // 弹出元素
    s.pop();
    std::cout << "弹出后的栈顶: " << s.top() << std::endl;
    
    return 0;
}
```

栈常用于函数调用、表达式求值、括号匹配等场景。

### 队列（Queue）

队列是一种先进先出（FIFO, First In First Out）的数据结构。可以想象成排队买票，先到的人先服务。队列的主要操作包括：
- `push()`: 在队尾添加元素
- `pop()`: 移除队首元素
- `front()`: 查看队首元素
- `back()`: 查看队尾元素

C++ STL 提供了 `std::queue`：

```cpp
#include <iostream>
#include <queue>

int main() {
    std::queue<int> q;
    
    // 入队
    q.push(1);
    q.push(2);
    q.push(3);
    
    // 查看队首元素
    std::cout << "队首元素: " << q.front() << std::endl;
    
    // 出队
    q.pop();
    std::cout << "出队后的队首: " << q.front() << std::endl;
    
    return 0;
}
```

队列常用于任务调度、广度优先搜索（BFS）等场景。

### 优先队列（Priority Queue）

优先队列是一种特殊的队列，每个元素都有一个优先级，优先级高的元素先出队。可以想象成医院的急诊室，病情严重的患者优先处理。

C++ STL 提供了 `std::priority_queue`，默认是最大堆（最大元素在顶部）：

```cpp
#include <iostream>
#include <queue>

int main() {
    std::priority_queue<int> pq;
    
    // 插入元素
    pq.push(3);
    pq.push(1);
    pq.push(4);
    pq.push(2);
    
    // 输出元素（按优先级从高到低）
    while (!pq.empty()) {
        std::cout << pq.top() << " ";
        pq.pop();
    }
    std::cout << std::endl;
    
    return 0;
}
```

优先队列常用于任务调度、Dijkstra 最短路径算法等场景。

### 集合（Set）

集合是一种不包含重复元素的数据结构，元素会自动排序。C++ STL 提供了 `std::set`（有序集合）和 `std::unordered_set`（无序集合）。

```cpp
#include <iostream>
#include <set>

int main() {
    std::set<int> s = {3, 1, 4, 1, 5, 9, 2, 6};
    
    // 自动去重和排序
    for (int val : s) {
        std::cout << val << " ";
    }
    std::cout << std::endl;
    
    // 查找元素
    if (s.find(4) != s.end()) {
        std::cout << "找到了 4" << std::endl;
    }
    
    // 插入元素
    s.insert(7);
    
    // 删除元素
    s.erase(1);
    
    return 0;
}
```

`std::set` 基于红黑树实现，查找、插入、删除的时间复杂度都是 O(log n)。`std::unordered_set` 基于哈希表实现，平均时间复杂度为 O(1)，但不保证元素有序。

### 映射（Map）

映射是一种键值对（key-value）的数据结构，每个键对应一个值。C++ STL 提供了 `std::map`（有序映射）和 `std::unordered_map`（无序映射）。

```cpp
#include <iostream>
#include <map>
#include <string>

int main() {
    std::map<std::string, int> age;
    
    // 插入键值对
    age["Alice"] = 25;
    age["Bob"] = 30;
    age["Charlie"] = 35;
    
    // 访问值
    std::cout << "Alice 的年龄: " << age["Alice"] << std::endl;
    
    // 遍历映射
    for (const auto& pair : age) {
        std::cout << pair.first << ": " << pair.second << std::endl;
    }
    
    // 查找键
    if (age.find("Bob") != age.end()) {
        std::cout << "找到了 Bob" << std::endl;
    }
    
    return 0;
}
```

`std::map` 基于红黑树实现，键会自动排序。`std::unordered_map` 基于哈希表实现，查找效率更高但不保证顺序。

### 树（Tree）

树是一种层次化的数据结构，由节点组成，每个节点可以有零个或多个子节点。树的根节点没有父节点，叶子节点没有子节点。

常见的树结构包括：
- **二叉树**：每个节点最多有两个子节点
- **二叉搜索树（BST）**：左子树的所有节点值小于根节点，右子树的所有节点值大于根节点
- **平衡树**：如红黑树、AVL树，保证树的高度平衡以提高查找效率

C++ STL 中的 `std::set` 和 `std::map` 内部就是使用红黑树实现的。如果需要自定义树结构，通常需要自己实现：

```cpp
#include <iostream>

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

// 中序遍历
void inorderTraversal(TreeNode* root) {
    if (root == nullptr) return;
    inorderTraversal(root->left);
    std::cout << root->val << " ";
    inorderTraversal(root->right);
}

int main() {
    // 构建一个简单的二叉树
    TreeNode* root = new TreeNode(1);
    root->left = new TreeNode(2);
    root->right = new TreeNode(3);
    root->left->left = new TreeNode(4);
    root->left->right = new TreeNode(5);
    
    std::cout << "中序遍历: ";
    inorderTraversal(root);
    std::cout << std::endl;
    
    // 记得释放内存
    // ...
    
    return 0;
}
```

树常用于文件系统、数据库索引、表达式解析等场景。

### 图（Graph）

图是一种由节点（顶点）和边组成的数据结构，用于表示对象之间的关系。图可以是有向的（边有方向）或无向的（边无方向），也可以是加权的（边有权重）或无权的。

图的表示方法主要有两种：
- **邻接矩阵**：使用二维数组表示，适合稠密图
- **邻接表**：使用链表或向量表示，适合稀疏图

在 C++ 中，可以使用 `std::vector` 来实现邻接表：

```cpp
#include <iostream>
#include <vector>

int main() {
    int n = 5;  // 5个节点
    std::vector<std::vector<int>> graph(n);
    
    // 添加边（无向图）
    graph[0].push_back(1);
    graph[1].push_back(0);
    
    graph[0].push_back(4);
    graph[4].push_back(0);
    
    graph[1].push_back(2);
    graph[2].push_back(1);
    
    graph[1].push_back(3);
    graph[3].push_back(1);
    
    graph[1].push_back(4);
    graph[4].push_back(1);
    
    graph[2].push_back(3);
    graph[3].push_back(2);
    
    graph[3].push_back(4);
    graph[4].push_back(3);
    
    // 输出邻接表
    for (int i = 0; i < n; i++) {
        std::cout << "节点 " << i << " 的邻居: ";
        for (int neighbor : graph[i]) {
            std::cout << neighbor << " ";
        }
        std::cout << std::endl;
    }
    
    return 0;
}
```

图常用于社交网络、地图导航、网络路由等场景。常见的图算法包括深度优先搜索（DFS）、广度优先搜索（BFS）、最短路径算法（Dijkstra、Floyd）、最小生成树（Prim、Kruskal）等。

## 如何选择数据结构

选择合适的数据结构取决于具体的应用场景：

- **需要快速随机访问**：使用 `std::vector` 或 `std::array`
- **需要频繁插入/删除**：使用 `std::list`
- **需要后进先出**：使用 `std::stack`
- **需要先进先出**：使用 `std::queue`
- **需要按优先级处理**：使用 `std::priority_queue`
- **需要快速查找且不重复**：使用 `std::set` 或 `std::unordered_set`
- **需要键值对映射**：使用 `std::map` 或 `std::unordered_map`
- **需要层次结构**：使用树
- **需要表示关系网络**：使用图

## 时间复杂度对比
| 数据结构 | 访问 | 查找 | 插入 | 删除 |
|---------|------|------|------|------|
| 数组 | $O(1)$ | $O(n)$ | $O(n)$ | $O(n)$ |
| 链表 | $O(n)$ | $O(n)$ | $O(1)$ | $O(1)$ |
| 栈 | $O(n)$ | $O(n)$ | $O(1)$ | $O(1)$ |
| 队列 | $O(n)$ | $O(n)$ | $O(1)$ | $O(1)$ |
| 哈希表 | - | $O(1)$ | $O(1)$ | $O(1)$ |
| 二叉搜索树 | $O(\log n)$ | $O(\log n)$ | $O(\log n)$ | $O(\log n)$ |

\* 假设已知位置  
\** 平均情况

## 总结

数据结构是编程的基础，掌握常用的数据结构可以帮助我们编写更高效的程序。C++ STL 提供了丰富的数据结构实现，我们应该根据具体需求选择合适的数据结构。在实际开发中，往往需要结合多种数据结构来解决复杂的问题。

建议在学习数据结构时，不仅要理解它们的原理，还要多动手实践，通过编写代码来加深理解。可以尝试在 LeetCode、Codeforces 等平台上练习相关的算法题目。
