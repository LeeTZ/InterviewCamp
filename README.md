Interview Training for Impatients
======================

by TTT

[TOC]

知识点
---------------
### 基础知识
* 算法复杂度 Big-O Notation
* 编译原理 Compiler
* 浮点数数的表示和存储 Floating Point Representation

### 算法
* 二分搜索 Binary Search 
* 分治 Divide Conquer 
* 宽度优先搜索 Breadth First Search 
* 深度优先搜索 Depth First Search
* 回溯法 Backtracking 
* 动态规划 Dynamic Programming 
* 扫描线 Scan-line algorithm
* 快排和归并排序 Quick Sort and Merge Sort
* 位运算 Bitwise operations

### 数据结构
* 栈 Stack
* 队列 Queue
* 链表 Linked List 
* 数组 Array 
* 哈希表 Hash Table
* 二叉树 Binary Tree  
* 堆 Heap
* 并查集 Union Find
* 字典树 Trie

练习题
---------------
使用方法：
对于自己自信的知识点，做该类别下的第一道，简单调试后一遍通过的话即可跳过该知识点。否则，继续做第二道题目。

* 二分 
	* [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/description/)
	* [Search a 2d Matrix II](https://leetcode.com/problems/search-a-2d-matrix-ii/description/)
* 分治
	* [Merge K Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/description/)
	* [The Skyline Problem](https://leetcode.com/problems/the-skyline-problem/description/)
* BFS
	* [Number of Islands](https://leetcode.com/problems/number-of-islands/description/)
	* [Perfect Squares](https://leetcode.com/problems/perfect-squares/description/)
* DFS
	* [Binary Tree Path](https://leetcode.com/problems/binary-tree-paths/description/)
	* [Longest Increasing Path in a Matrix](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/description/)
* 回溯
	* [Generate Parentheses](https://leetcode.com/problems/generate-parentheses/description/)
	* [Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/)
* 动态规划 (简单了解）
	* [Word Break](https://leetcode.com/problems/word-break/description/) 
	* [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/solution/)
* 排序
	* [Merge Intervals](https://leetcode.com/problems/merge-intervals/solution/)
	* [Largest Number](https://leetcode.com/problems/largest-number/description/)
* 位运算（简单了解）
	* [Power of Two](https://leetcode.com/problems/power-of-two/description/-)
	* [Repeated DNA Sequences](https://leetcode.com/problems/repeated-dna-sequences/description/)
* 树
	* [Binary Tree Paths](https://leetcode.com/problems/binary-tree-paths/description/)
	* [Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/)
* 堆
	* [Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/description/)
* 字典树
	* [Palindrome Pairs](https://leetcode.com/problems/palindrome-pairs/description/)


阅读材料
---------------

## 简单编译原理
* 计算机如何处理一段程序：
    - [CPU 是如何执行代码的](https://www.youtube.com/watch?v=42KTvGYQYnA)
    - [机器码指令](https://www.youtube.com/watch?v=Mv2XQgpbTNE)
* 编译器
    - [一分钟理解编译器](https://www.youtube.com/watch?v=IhC7sdYe-Jg)
* 浮点数的储存：
    - [IEEE754 32-bit 浮点二进制](https://www.youtube.com/watch?v=50ZYcZebIec)

## 算法复杂度分析

#### 大 O 表示
* **大 O 表示** 用于表示某个算法的上限，往往用于描述最坏的情况。

![Alt text](/Images/bigO.png?raw=true "Theta Notation")

#### 小 O 表示
* **小 O 表示**用于描述某个算法的渐进上界，不过二者要更为紧密。

#### 大 Ω 表示
* **大 Ω 表示**用于描述某个算法的渐进下界。

![Alt text](/Images/bigOmega.png?raw=true "Theta Notation")

#### 小 ω 表示
* **Little Omega Notation**用于描述某个特定算法的下界，不过不一定很靠近。

#### Theta Θ 表示
* **Theta Notation**用于描述某个确定算法的确界。

![Alt text](/Images/theta.png?raw=true "Theta Notation")

#### 算法复杂度：
    - [时间复杂度入门](http://www.jianshu.com/p/99bac69fdd97)
    - [速查表](http://bigocheatsheet.com/)

## 数据结构

### Linked List
 * 链表即是由节点（Node）组成的线性集合，每个节点可以利用指针指向其他节点。它是一种包含了多个节点的、能够用于表示序列的数据结构。
 * **单向链表**: 链表中的节点仅指向下一个节点，并且最后一个节点指向空。
 * **双向链表**: 其中每个节点具有两个指针 p、n，使得 p 指向先前节点并且 n 指向下一个节点；最后一个节点的 n 指针指向 null。
 * **循环链表**：每个节点指向下一个节点并且最后一个节点指向第一个节点的链表。
 * 时间复杂度:
   * 索引: `O(n)`
   * 搜索: `O(n)`
   * 插入: `O(1)`
   * 移除: `O(1)`

### Stack
 * 栈是元素的集合，其包含了两个基本操作：push 操作可以用于将元素压入栈，pop 操作可以将栈顶元素移除。
 * 遵循后入先出（LIFO）原则。
 * 时间复杂度:
  * 索引: `O(n)`
  * 搜索: `O(n)`
  * 插入: `O(1)`
  * 移除: `O(1)`

### Queue
 * 队列是元素的集合，其包含了两个基本操作：enqueue 操作可以用于将元素插入到队列中，而 dequeue 操作则是将元素从队列中移除。
 * 遵循先入先出原则 (FIFO)。
 * 时间复杂度:
  * 索引: `O(n)`
  * 搜索: `O(n)`
  * 插入: `O(1)`
  * 移除: `O(1)`

### Tree
* 树是无向、连通的无环图。

### Binary Tree
 * 二叉树即是每个节点最多包含左子节点与右子节点这两个节点的树形数据结构。
 * **满二叉树**: 树中的每个节点仅包含 0 或 2 个节点。
 * **完美二叉树（Perfect Binary Tree）**: 二叉树中的每个叶节点都拥有两个子节点，并且具有相同的高度。
 * **完全二叉树**: 除最后一层外，每一层上的结点数均达到最大值；在最后一层上只缺少右边的若干结点。

### Binary Search Tree

* 二叉搜索树（BST）是一种特殊的二叉树，其任何节点中的值都会大于或者等于其左子树中存储的值并且小于或者等于其右子树中存储的值。
* 时间复杂度:
  * 索引: `O(log(n))`
  * 搜索: `O(log(n))`
  * 插入: `O(log(n))`
  * 删除: `O(log(n))`

<img src="/Images/BST.png?raw=true" alt="Binary Search Tree" width="400" height="500">

### Trie
* 字典树，又称基数树或者前缀树，能够用于存储键为字符串的动态集合或者关联数组的搜索树。树中的节点并没有直接存储关联键值，而是该节点在树中的挂载位置决定了其关联键值。某个节点的所有子节点都拥有相同的前缀，整棵树的根节点则是空字符串。

![Alt text](/Images/trie.png?raw=true "Trie")

### Fenwick Tree
* 树状数组又称 Binary Indexed Tree，其表现形式为树，不过本质上是以数组实现。数组中的下标代表着树中的顶点，每个顶点的父节点或者子节点的下标能够通过位运算获得。数组中的每个元素包含了预计算的区间值之和，在整棵树更新的过程中同样会更新这些预计算的值。
* 时间复杂度:
  * 区间求值: `O(log(n))`
  * 更新: `O(log(n))`

![Alt text](/Images/fenwickTree.png?raw=true "Fenwick Tree")

### Segment Tree
* 线段树是用于存放间隔或者线段的树形数据结构，它允许快速的查找某一个节点在若干条线段中出现的次数.
* 时间复杂度:
  * 区间查询: `O(log(n))`
  * 更新: `O(log(n))`

![Alt text](/Images/segmentTree.png?raw=true "Segment Tree")

### Heap
* 堆是一种特殊的基于树的满足某些特性的数据结构，整个堆中的所有父子节点的键值都会满足相同的排序条件。堆更准确地可以分为最大堆与最小堆，在最大堆中，父节点的键值永远大于或者等于子节点的值，并且整个堆中的最大值存储于根节点；而最小堆中，父节点的键值永远小于或者等于其子节点的键值，并且整个堆中的最小值存储于根节点。
* 时间复杂度:
  * 访问最大值 / 最小值: `O(1)`
  * 插入: `O(log(n))`
  * 移除最大值 / 最小值: `O(log(n))`

<img src="/Images/heap.png?raw=true" alt="Max Heap" width="400" height="500">


### Hashing
* 哈希能够将任意长度的数据映射到固定长度的数据。哈希函数返回的即是哈希值，如果两个不同的键得到相同的哈希值，即将这种现象称为碰撞。
* **Hash Map**: Hash Map 是一种能够建立起键与值之间关系的数据结构，Hash Map 能够使用哈希函数将键转化为桶或者槽中的下标，从而优化对于目标值的搜索速度。
* 碰撞解决
  * **链地址法（Separate Chaining）**: 链地址法中，每个桶是相互独立的，包含了一系列索引的列表。搜索操作的时间复杂度即是搜索桶的时间（固定时间）与遍历列表的时间之和。
  * **开地址法（Open Addressing）**: 在开地址法中，当插入新值时，会判断该值对应的哈希桶是否存在，如果存在则根据某种算法依次选择下一个可能的位置，直到找到一个尚未被占用的地址。所谓开地址法也是指某个元素的位置并不永远由其哈希值决定。

![Alt text](/Images/hash.png?raw=true "Hashing")

### Graph
* 图是一种数据元素间为多对多关系的数据结构，加上一组基本操作构成的抽象数据类型。
    * **无向图（Undirected Graph）**: 无向图具有对称的邻接矩阵，因此如果存在某条从节点 u 到节点 v 的边，反之从 v 到 u 的边也存在。
    * **有向图（Directed Graph）**: 有向图的邻接矩阵是非对称的，即如果存在从 u 到 v 的边并不意味着一定存在从 v 到 u 的边。

<img src="/Images/graph.png?raw=true" alt="Graph" width="400" height="500">

## 算法

### 排序

#### 快速排序
* 稳定: 否
* 时间复杂度:
  * 最优时间: `O(nlog(n))`
  * 最坏时间: `O(n^2)`
  * 平均时间: `O(nlog(n))`

![Alt text](/Images/quicksort.gif?raw=true "Quicksort")

#### 归并排序
* 归并排序是典型的分治算法，它不断地将某个数组分为两个部分，分别对左子数组与右子数组进行排序，然后将两个数组合并为新的有序数组。
* 稳定: 是
* 时间复杂度:
  * 最优时间: `O(nlog(n))`
  * 最坏时间: `O(nlog(n))`
  * 平均时间: `O(nlog(n))`

![Alt text](/Images/mergesort.gif?raw=true "Mergesort")

#### 桶排序
* 桶排序将数组分到有限数量的桶子里。每个桶子再个别排序（有可能再使用别的排序算法或是以递归方式继续使用桶排序进行排序）。
* 时间复杂度:
  * 最优时间: `Ω(n + k)`
  * 最坏时间: `O(n^2)`
  * 平均时间:`Θ(n + k)`


![Alt text](/Images/bucketsort.png?raw=true "Bucket Sort")

#### 基数排序
* 基数排序类似于桶排序，将数组分割到有限数目的桶中；不过其在分割之后并没有让每个桶单独地进行排序，而是直接进行了合并操作。
* 时间复杂度:
  * 最优时间: `Ω(nk)`
  * 最坏时间: `O(nk)`
  * 平均时间: `Θ(nk)`

### 图算法

#### 深度优先搜索
* 深度优先算法是一种优先遍历子节点而不是回溯的算法。
* 时间复杂度: `O(|V| + |E|)`

![Alt text](/Images/dfsbfs.gif?raw=true "DFS / BFS Traversal")

#### 广度优先搜索
* 广度优先搜索是优先遍历邻居节点而不是子节点的图遍历算法。
* 时间复杂度: `O(|V| + |E|)`

![Alt text](/Images/dfsbfs.gif?raw=true "DFS / BFS Traversal")

#### 拓扑排序
* 拓扑排序是对于有向图节点的线性排序，如果存在某条从 u 到 v 的边，则认为 u 的下标先于 v。
* 时间复杂度: `O(|V| + |E|)`

#### Dijkstra 算法
* **Dijkstra 算法** 用于计算有向图中单源最短路径问题。
* 时间复杂度: `O(|V|^2)`

![Alt text](/Images/dijkstra.gif?raw=true "Dijkstra's")

#### Bellman-Ford 算法
* **Bellman-Ford 算法**是在带权图中计算从单一源点出发到其他节点的最短路径的算法。
* 尽管算法复杂度大于 Dijkstra 算法，但是它适用于包含了负值边的图。
* 时间复杂度:
  * 最优时间: `O(|E|)`
  - 最坏时间: `O(|V||E|)`

![Alt text](/Images/bellman-ford.gif?raw=true "Bellman-Ford")

#### Floyd-Warshall 算法
* **Floyd-Warshall 算法** 能够用于在无环带权图中寻找任意节点的最短路径。
* 时间复杂度:
  * 最优时间: `O(|V|^3)`
  * 最坏时间: `O(|V|^3)`
  * 平均时间: `O(|V|^3)`

#### Prim 算法
* **Prim 算法**是用于在带权无向图中计算最小生成树的贪婪算法。换言之，Prim 算法能够在图中抽取出连接所有节点的边的最小代价子集。
* 时间复杂度: `O(|V|^2)`

![Alt text](/Images/prim.gif?raw=true "Prim's Algorithm")

#### Kruskal 算法
* **Kruskal 算法**同样是计算图的最小生成树的算法，与 Prim 的区别在于并不需要图是连通的。
* 时间复杂度: `O(|E|log|V|)`

![Alt text](/Images/kruskal.gif?raw=true "Kruskal's Algorithm")

## 位运算
* 位运算即是在位级别进行操作的技术，合适的位运算能够帮助我们得到更快地运算速度与更小的内存使用。
* 测试第 k 位: `s & (1 << k)`
* 设置第 k 位: `s |= (1 << k)`
* 第 k 位置零: `s &= ~(1 << k)`
* 切换第 k 位值: `s ^= ~(1 << k)`
* 乘以 2: `s << n`
* 除以 2: `s >> n`
* 交集: `s & t`
* 并集: `s | t`
* 减法: `s & ~t`
* 交换 `x = x ^ y ^ (y = x)`
* 取出最小非 0 位（Extract lowest set bit）: `s & (-s)`
* 取出最小 0 位（Extract lowest unset bit）: `~s & (s + 1)`
* 交换值:
             ```
                x ^= y;
                y ^= x;
                x ^= y;
             ```
