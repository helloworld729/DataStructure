反向遍历的两种方法：
1、在向下递归的过程中，控制区间, 变量始终是一个变量,例如：
id:1030174604168
id:1030174604168
id:1030174604168
id:1030174604168
id:1030174604168
id:1030174604168
[100, 89, 78, 56, 56, 45, 45, 23, 12, 12]

2、在向下递归的过程中，列表切片, 但是这样相当于创建了一个新的变量
412138929032
412138770824
412138881288
412136800584
412138881288
412138881224
[100, 89, 78, 56, 56, 45, 45, 23, 12, 12]

应该采用第一种方法较好

思路快速建立，以倒排为例：
1、右边的数字应该小，所以若当前指向较小(合理)则左滑，遇到大于pivot的值停下 ->合理左滑，否则停下
2、如果距离合适，把数据抛到对面的坑  -> 查距填坑
