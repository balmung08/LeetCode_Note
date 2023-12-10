### 一句话题目总结

关于刷题的基本准备：[**前置知识总览**](前置知识/笔记总览.md)
刷题中遇到的部分知识点：[**方法总览**](方法笔记/方法总览.md)

<details><summary><b>专题汇总</b></summary>

#####  DP-股票问题
* 关于DP的空间简化可以参照[LC回答](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iv/solutions/740596/5xing-dai-ma-gao-ding-suo-you-gu-piao-ma-j6zo/)，实际相当于只维护了DP表的最后一天

##### DP-背包问题
* 具体分类可以参照[LC解答](https://leetcode.cn/problems/word-break/solutions/1492673/bei-bao-by-wo-zhao-wo-de-bao-zhen-aog8/)
  > **关于为什么01背包的内循环要倒序而完全背包问题不需要**
  在同一循环内，更新列表后面的元素需要使用前面的元素；如果正序，前面的元素优先改变，则导致所有元素都是根据本次循环的信息进行改变；而01背包问题由于各个物品只能使用一次，更新元素时需要使用上一次循环的内容进行更新，因此必须先更新后面的。如果先更新前面的就会导致后面的元素使用前面的元素时，前面的元素已经按照本次循环的规则进行了更新从而丢失上一次循环的信息
</details>

<details><summary><b>LeetCode Hot100</b></summary>

> 加粗的题回头拿出来重新做一下
* **杂项与待做**
* 31.先把数据如何变换思考清楚以后再进行流程设计
* 48.矩阵的旋转就是找像素和目标点的关系，可以直接变或者组合翻转
* 56.对数据处理时按一定恰当顺序排序可以减少要处理的条件，极大简化过程
* 128.判断数列是否连续的通用思路是看前数字与后数字判断序列头与尾
* 136.位运算的交换律，以及0和一个数做异或，那个数结果不变
* **146.哈希链表这种组合数据结构的优点与应用场景**
* 155.对列表排序不一定要在最后排，一边加入表一边用辅助表记录也可以
* 238.如果时间复杂度为n，一次遍历又解决不了，可以试试正遍历后反向遍历一次
* 347.python的字典排序也可以起到和优先队列差不多的效果，但稍慢一些
* 448.python自己有个列表转集合，过程中可以去重
* 461.python的二进制本质上是加了头缀的字符串，可以直接用字符串的函数
* 581.尽量不要从待找区间去推待找边界外的项，而是从总体边界向内推得待找边界
------------------
#### 栈
* 20.经典栈问题，不过像这种比对操作就很适合用字典来进行
* 739.栈也可以不存数据本身而存数据序号，另外数据类型尽量直接写功能而不是一个完整的类再调用，python的函数调用需要花费额外的时间
------------------
#### 哈希表
* 1.把双循环改成单循环+枚举问题(in)，能用字典就用字典
* 49.算法的选择要看数据的性质，不一定理论上最快的真的最快
* 560.算数据的时候可以一边算，一边记录数据的出现情况并进行处理
------------------
#### 链表
* 2.少设标志位，链表逐位解决而不是拆除来处理
* 21.链表逐位操作的典型，两个头对应两个表
* **148.链表直接排序最适合用自底而顶的归并排序，最省空间**
* **160.看到交叉链表找交点就可以想想求差值一起走和“链表的爱情”方法**
* 206.链表反转本质上就是更改节点之间的联系关系
-----------------
#### 双指针
* 3.字典设置头尾位数指示位也可以起到类似于列表的效果，另外注意指示位初值
* **11.需要在一个循环内完成的问题可以考虑同向或异向双指针**
* 15.双指针如果无法做出来，找不到指针应该怎么移动的规律时可以给列表排个序
* 19.双指针同向时可以在题目里找找间隔怎么设计的条件
* **42.前后缀最大值交替前进，和11有类似的思路，回头拿出来一起做**
* 75.本质上就是手搓排序，多种数排序可多个指针分别指向每一段的尾部
* 141.双指针同向时除了等差还有等比
* 142.等比等差指针可以先后使用分步解决问题
* 234.回文链表本质上是找链表中心点；另外同向等比双指针思路也用于141
* 283.批量删除同一值元素的典型方法：错位前补
* **287.列表类比成链表双指针找环真是天才想法**
* 438.数组切片大部分情况下都可以用双指针替代，会快很多
----------------
#### 二分查找
* 33.二分法确定目标元素是什么、根据什么确定在哪一边是最重要的问题
* 34.常规的二分法找到就停，但是如果一直不停可找到连续相同元素的边界
* **287.二分查找法不一定要查找列表里的元素，也可以查找元素的属性来进行过滤**
----------------
#### 二叉树
* 94.二叉树的迭代和递归遍历法
  > **这几个题高强度递归和搜索，后面回来重新写一下**
  > 递归普遍更高效：101 102 104 226 543 617 
  > https://www.bilibili.com/video/BV1UD4y1Y769/
----------------
#### 动态规划
* 5.对字符串找回文问题，特殊方法中心扩散和马拉车，一般方法dp
* 10.二维DP，状态转移方程分析复杂
* 32.状态转移矩阵的情况分析复杂（好像DP都是因为这个难）
* 53.dp问题得到的结果不一定是最后一项，可能还需要按一定原则处理dp列表
* 62.要分析清楚dp在最小问题时的具体情况与初始值，一旦错就全错
* 64.带权重的找路径，可以和62题对比着进行分析，原理是相同的
* 70.这爬楼梯就是个斐波那契数列啊，动态规划包含的范围还挺大
* **72.dp状态转移方程太漂亮了，直接理解性背诵**
* 121.dp的关键就是找之前项和当前项的关系，关系可能与当前项的相关操作有关
* 139.其实也是背包问题的变形，但是最难的是问题的抽象这一思考过程
* 152.思路和53很像，但乘积负负得正的情况需要特殊处理，即同时记录max和min
* 198.动态规划降维与状态压缩的典型参考例题
* 221.非常特殊的状态转移方程思路，可以特殊记一下
* 279.完全平方数除了DP以外，还可以使用四平方和定理数学知识进行问题求解
* 300.递增子序列的标准解法，除DP外还有单调栈+二分的方法
* 309.股票问题的变式，关注状态转移方程即可
* 312.开区间拆分DP，不是简单的与附近的项相关
* 322.背包问题的经典模板，注意dp列表的初始化设置
* 338.python内置bin函数和count函数可以轻松统计二进制的0和1
* 416.01背包问题的标准模板，注意和完全背包问题的对比
* 494.01背包问题的变式，在true/false基础上变为了数量关系
* 647.在回文子串类问题里，DP似乎一直比中心扩散法慢

#### 回溯法
* 17.回溯法的最直观问题和最基本模板
* 22.括号的添加方法是一个一个添加才符合回溯法的思路
* 39.方法本身是标准的回溯法，但是要注意去重的特殊操作的思路
</details>

<details><summary><b>剑指offer第二版</b></summary>

> [题目列表](https://blog.csdn.net/weixin_43840280/article/details/119447204)，LeetCode版权到期以后题目很零散

#### 链表
> 除了35【复杂链表的复制】以外其他全是Hot100原题
* 35.对于链表的复制可以使用哈希表和原地复制后拆分，另外python有deepcopy

#### 动态规划
> 46【翻译字符串】、60【n个骰子的点数统计】.62【圆圈最后数】是新题
* 46.常规一维DP，注意一下状态转移公式即可
* 60.常规二维DP，和上面一个一样要注意状态转移公式在不同条件下可能有不同情况
* 62.本质上数学问题，记一下 **【约瑟夫环问题，f(n,m)=[f(n-1,m)+m]%n】**

#### 位运算
> python二进制数据存储格式特殊，位运算的一些细节非常抽象，理解方法即可
* 位运算的常规题目：n&(n−1)消除1、快速幂、按位分组、异或计数、异或代替加法
</details>