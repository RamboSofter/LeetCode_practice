# python常用数据结构

[链接](https://www.yiibai.com/python/py_data_structure)

## 数组

## 链表

### 创建链表

通过使用在上一章中学习的节点类来创建链表。创建一个Node对象并创建另一个类来使用这个节点对象。 通过节点对象传递适当的值来指向下一个数据元素。 
下面的程序使用三个数据元素创建链接列表。 在下一节中，将学习如何遍历链表。

```python
class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

list1 = SLinkedList()
list1.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
# Link first Node to second node
list1.headval.nextval = e2

# Link second Node to third node
e2.nextval = e3
Python
```

### 遍历链表

从第一个数据元素开始，单向链表只能在向前遍历。 只需通过将下一个节点的指针指向当前数据元素来打印下一个数据元素的值。

```python
class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print (printval.dataval)
            printval = printval.nextval

list = SLinkedList()
list.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

# Link first Node to second node
list.headval.nextval = e2

# Link second Node to third node
e2.nextval = e3

list.listprint()

# 执行上面示例代码，得到以下结果 - 
# Mon
# Tue
# Wed
# Shell
```

向链表插入数据在链表中插入元素涉及将指针从现有节点重新分配给新插入的节点。 取决于新数据元素是在链表的开始位置还是在中间位置或末尾插入。

### 在链接列表的开头插入

这涉及到将新数据节点的下一个指针指向链表的当前头部。 因此，链表的当前头成为第二个数据元素，新节点成为链表的头部。

```python
class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

# Print the linked list
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print (printval.dataval)
            printval = printval.nextval
    def AtBegining(self,newdata):
        NewNode = Node(newdata)

# Update the new nodes next val to existing node
        NewNode.nextval = self.headval
        self.headval = NewNode

list = SLinkedList()
list.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

list.headval.nextval = e2
e2.nextval = e3

list.AtBegining("Sun")

list.listprint()

# 执行上面示例代码，得到以下结果 - 
# Sun
# Mon
# Tue
# Wed

```

### 在链表的末尾插入

这包括将链表的当前最后一个节点的下一个指针指向新的数据节点。 因此链表的当前最后一个节点成为倒数第二个数据节点，新节点成为链表的最后一个节点。
参考以下代码实现 - 

```python
class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

# Function to add newnode
    def AtEnd(self, newdata):
        NewNode = Node(newdata)
        if self.headval is None:
            self.headval = NewNode
            return
        laste = self.headval
        while(laste.nextval):
            laste = laste.nextval
        laste.nextval=NewNode

# Print the linked list
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print (printval.dataval)
            printval = printval.nextval


list = SLinkedList()
list.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

list.headval.nextval = e2
e2.nextval = e3

list.AtEnd("Thu")

list.listprint()

# 执行上面代码，得到以下结果 - 
# Mon
# Tue
# Wed
# Thu
# Shell
```

### 在两个数据节点之间插入

这涉及到将指定节点的指针指向新节点。 这可以通过传入新节点和现有节点，然后插入新节点。 所以定义一个额外的类，将新节点的下一个指针改变为中间节点的下一个指针。 
然后将新节点分配给中间节点的下一个指针。参考以下代码实现 - 

```python
class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

# Function to add node
    def Inbetween(self,middle_node,newdata):
        if middle_node is None:
            print("The mentioned node is absent")
            return

        NewNode = Node(newdata)
        NewNode.nextval = middle_node.nextval
        middle_node.nextval = NewNode

# Print the linked list
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print (printval.dataval)
            printval = printval.nextval


list = SLinkedList()
list.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Thu")

list.headval.nextval = e2
e2.nextval = e3

list.Inbetween(list.headval.nextval,"Fri")

list.listprint()

# 执行上面示例代码，得到以下结果 - 
# Mon
# Tue
# Fri
# Thu
# Shell
```

### 从链表中删除项目

可以使用该节点的键来删除一个节点。 在下面的程序中，找到要删除的节点的前一个节点。 然后将该节点的下一个指针指向要删除的节点的下一个节点。

```python
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None

    def Atbegining(self, data_in):
        NewNode = Node(data_in)
        NewNode.next = self.head
        self.head = NewNode

# Function to remove node
    def RemoveNode(self, Removekey):

        HeadVal = self.head

        if (HeadVal is not None):
            if (HeadVal.data == Removekey):
                self.head = HeadVal.next
                HeadVal = None
                return

        while (HeadVal is not None):
            if HeadVal.data == Removekey:
                break
            prev = HeadVal
            HeadVal = HeadVal.next

        if (HeadVal == None):
            return

        prev.next = HeadVal.next

        HeadVal = None

    def LListprint(self):
        printval = self.head
        while (printval):
            print(printval.data),
            printval = printval.next


llist = SLinkedList()
llist.Atbegining("Mon")
llist.Atbegining("Tue")
llist.Atbegining("Wed")
llist.Atbegining("Thu")
llist.RemoveNode("Tue")
llist.LListprint()

# 执行上面示例代码，得到以下结果 - 
# Thu
# Wed
# Mon
```

## 队列

### 双端队列

collections.deque

```python
class collections.deque([iterable[, maxlen]])
    '''双向队列对象
    从左到右初始化(用方法 append()) ，从 iterable （迭代对象) 数据创建。如果 iterable 没有指定，新队列为空。
    Deque队列是由栈或者queue队列生成的
    '''
    append(x) # 添加 x 到右端。

    appendleft(x) # 添加 x 到左端。 

    clear() # 移除所有元素，使其长度为0.

    copy() # 创建一份浅拷贝。

    count(x) # 计算 deque 中元素等于 x 的个数。

    extend(iterable) # 扩展deque的右侧，通过添加iterable参数中的元素。
    
    # 扩展deque的左侧，通过添加iterable参数中的元素。注意，左添加时，在结果中iterable参数中的顺序将被反过来添加。
    extendleft(iterable)

    # 返回 x 在 deque 中的位置（在索引 start 之后，索引 stop 之前）。 返回第一个匹配项，如果未找到则引发 ValueError。
    index(x[, start[, stop]])

    insert(i, x) # 在位置 i 插入 x  如果插入会导致一个限长 deque 超出长度 maxlen 的话，就引发一个 IndexError。

    pop() # 移去并且返回一个元素，deque 最右侧的那一个。 如果没有元素的话，就引发一个 IndexError。

    popleft() # 移去并且返回一个元素，deque 最左侧的那一个。 如果没有元素的话，就引发 IndexError。
    
    remove(value) # 移除找到的第一个 value。 如果没有的话就引发 ValueError。
    
    reverse() # 将deque逆序排列。返回 None 。

    rotate(n=1) # 向右循环移动 n 步。 如果 n 是负数，就向左循环。
    
    # 如果deque不是空的，向右循环移动一步就等价于 d.appendleft(d.pop()) ， 向左循环一步就等价于 d.append(d.popleft()) 。

    maxlen # Deque的最大尺寸，如果没有限定的话就是 None 。

>>> from collections import deque
>>> d = deque('ghi')                 # make a new deque with three items
>>> for elem in d:                   # iterate over the deque's elements
...     print(elem.upper())
G
H
I

>>> d.append('j')                    # add a new entry to the right side
>>> d.appendleft('f')                # add a new entry to the left side
>>> d                                # show the representation of the deque
deque(['f', 'g', 'h', 'i', 'j'])

>>> d.pop()                          # return and remove the rightmost item
'j'
>>> d.popleft()                      # return and remove the leftmost item
'f'
>>> list(d)                          # list the contents of the deque
['g', 'h', 'i']
>>> d[0]                             # peek at leftmost item
'g'
>>> d[-1]                            # peek at rightmost item
'i'

>>> list(reversed(d))                # list the contents of a deque in reverse
['i', 'h', 'g']
>>> 'h' in d                         # search the deque
True
>>> d.extend('jkl')                  # add multiple elements at once
>>> d
deque(['g', 'h', 'i', 'j', 'k', 'l'])
>>> d.rotate(1)                      # right rotation
>>> d
deque(['l', 'g', 'h', 'i', 'j', 'k'])
>>> d.rotate(-1)                     # left rotation
>>> d
deque(['g', 'h', 'i', 'j', 'k', 'l'])

>>> deque(reversed(d))               # make a new deque in reverse order
deque(['l', 'k', 'j', 'i', 'h', 'g'])
>>> d.clear()                        # empty the deque
>>> d.pop()                          # cannot pop from an empty deque
Traceback (most recent call last):
    File "<pyshell#6>", line 1, in -toplevel-
        d.pop()
IndexError: pop from an empty deque

>>> d.extendleft('abc')              # extendleft() reverses the input order
>>> d
deque(['c', 'b', 'a'])
```

### 优先队列

queue.PriorityQueue

queue.PriorityQueue这个优先级队列的实现在内部使用了heapq，时间和空间复杂度与heapq相同。
区别在于PriorityQueue是同步的，提供了锁语义来支持多个并发的生产者和消费者。

```python
from queue import PriorityQueue

q = PriorityQueue()

q.put((2, 'code'))
q.put((1, 'eat'))
q.put((3, 'sleep'))

while not q.empty():
    next_item = q.get()
    print(next_item)

# 结果：
#   (1, 'eat')
#   (2, 'code')
#   (3, 'sleep')
```

## 栈

```python
# 创建栈
stack=[]

# 添加元素
#O(1)
stack.append(1)
stack.append(2)
stack.append(3)
print(stack) #[1,2,3]

# 获取栈顶元素
#O(1)
stack[-1] #由于栈的性质 因此这里我们需要从后往前读 

# 删除栈顶元素
#O(1)
temp=stack.pop() #pop 删除并返回元素
print(temp)  #3

# 栈的大小
#O(1)
len(stack)

# 栈是否为空
#O(1)
len(stack)==0

# 栈的遍历(边删除边遍历)
#O(N)
while len(stack)>0:
    temp=stack.pop()
    print(temp)
```

## 哈希表

在Python中，字典数据类型表示哈希表的实现。字典中的键满足以下要求。

字典的键是可散列的，即通过散列函数生成该散列函数，该散列函数为提供给散列函数的每个唯一值生成唯一结果。字典中数据元素的顺序不固定。
所以可通过使用下面的字典数据类型来看到哈希表的实现。

collections.defaultdict类

```python
class collections.defaultdict(default_factory=None, /[, ...])
    '''返回一个新的类似字典的对象。 defaultdict 是内置 dict 类的子类。
    本对象包含一个名为 default_factory 的属性，构造时，第一个参数用于为该属性提供初始值，默认为 None。所有其他参数（包括关键字参数）都相当于传递给 dict 的构造函数。
    defaultdict 对象除了支持标准 dict 的操作，还支持以下方法作为扩展：
    '''
    __missing__(key)
    # 如果 default_factory 属性为 None，则调用本方法会抛出 KeyError 异常，附带参数 key。

class dict(iterable, **kwargs)
    list(d) # 返回字典 d 中使用的所有键的列表。
    
    len(d) #  返回字典 d 中的项数。
    
    d[key] # 返回 d 中以 key 为键的项。 如果映射中不存在 key 则会引发 KeyError。
    
    d[key] = value # 将 d[key] 设为 value。

    del d[key] #  将 d[key] 从 d 中移除。 如果映射中不存在 key 则会引发 KeyError。
    
    key in d #  如果 d 中存在键 key 则返回 True，否则返回 False。

    key not in d # 等价于 not key in d。   

    iter(d) # 返回以字典的键为元素的迭代器。 这是 iter(d.keys()) 的快捷方式。
    
    clear() # 移除字典中的所有元素。
    

    copy() #  返回原字典的浅拷贝。
    
    get(key[, default]) # 如果 key 存在于字典中则返回 key 的值，否则返回 default。 如果 default 未给出则默认为 None，因而此方法绝不会引发 KeyError。
    
    items() # 返回由字典项 ((键, 值) 对) 组成的一个新视图。 参见 视图对象文档。
    

    keys() #  返回由字典键组成的一个新视图。 参见 视图对象文档。

    pop(key[, default]) # 如果 key 存在于字典中则将其移除并返回其值，否则返回 default。 如果 default 未给出且 key 不存在于字典中，则会引发 KeyError。
    

    popitem() # 从字典中移除并返回一个 (键, 值) 对。 键值对会按 LIFO 的顺序被返回。
    

    popitem() # 适用于对字典进行消耗性的迭代，这在集合算法中经常被使用。 如果字典为空，调用 popitem() 将引发 KeyError。

    reversed(d) # 返回一个逆序获取字典键的迭代器。 这是 reversed(d.keys()) 的快捷方式。

    setdefault(key[, default]) # 如果字典存在键 key ，返回它的值。如果不存在，插入值为 default 的键 key ，并返回 default 。 default 默认为 None。
    
    update([other]) # 使用来自 other 的键/值对更新字典，覆盖原有的键。 返回 None。
    
    update() # 接受另一个字典对象，或者一个包含键/值对（以长度为二的元组或其他可迭代对象表示）的可迭代对象。 如果给出了关键字参数，则会以其所指定的键/值对更新字典: d.update(red=1, blue=2)。

    values() # 返回由字典值组成的一个新视图。 
```

## 堆

堆是一种特殊的树结构，其中每个父节点小于或等于其子节点。 然后它被称为最小堆(Min Heap)。 如果每个父节点大于或等于其子节点，则称它为最大堆(Max Heap)。 
实施优先级队列是非常有用的，在该队列中，具有较高权重的队列项目在处理中具有更高的优先级。在本章中，我们将学习使用python实现堆数据结构。

### 创建一个堆

堆是通过使用python内建的名称为heapq的库创建的。 该库具有对堆数据结构进行各种操作的相关功能。 以下是这些函数的列表 - 

heapify - 此函数将常规列表转换为堆。 在结果堆中，最小的元素被推到索引位置0。但是其余的数据元素不一定被排序。heappush - 这个函数在堆中添加一个元素而不改变当前堆。heappop - 该函数返回堆中最小的数据元素。heapreplace - 该函数用函数中提供的新值替换最小的数据元素。
通过简单地使用具有heapify函数的元素列表来创建堆。 在下面的例子中，提供了一个元素列表，heapify函数重新排列了元素到最初位置的元素。

```python
import heapq

H = [21,1,45,78,3,5]
# Use heapify to rearrange the elements
heapq.heapify(H)
print(H)
Python
执行上面示例代码，得到以下结果 - 
[1, 3, 5, 78, 21, 45]
```

### 插入堆

将数据元素插入堆总是在最后一个索引处添加元素。 但是，只有在值最小的情况下，才可以再次应用heapify函数将新添加的元素添加到第一个索引。 
在下面的例子中，插入数字 - 8 。

```python
import heapq
H = [21,1,45,78,3,5]
# Covert to a heap
heapq.heapify(H)
print(H)
# Add element
heapq.heappush(H,8)
print(H)
Python
执行上面示例代码，得到以下结果 - 
[1, 3, 5, 78, 21, 45]
[1, 3, 5, 78, 21, 45, 8]
```

### 从堆中移除

可以使用此功能在第一个索引处移除元素。 在下面的例子中，函数将始终删除索引位置1处的元素。

```python
import heapq

H = [21,1,45,78,3,5]
# Create the heap

heapq.heapify(H)
print(H)

# Remove element from the heap
heapq.heappop(H)

print(H)

# 执行上面示例代码，得到以下结果 - 
# [1, 3, 5, 78, 21, 45]
# [3, 21, 5, 78, 45]
# Shell
```

### 替换堆

heapreplace函数总是删除堆中最小的元素，并在未被任何顺序修复的地方插入新的传入元素。参考以下示例 - 

```python
import heapq

H = [21,1,45,78,3,5]
# Create the heap

heapq.heapify(H)
print(H)

# Replace an element
heapq.heapreplace(H,6)
print(H)

执行上面示例代码，得到以下结果 - 
[1, 3, 5, 78, 21, 45]
[3, 6, 5, 78, 21, 45]
```

## 二叉搜索树、平衡树、红黑树

### 二叉搜索树

二叉搜索树(BST)是一棵树，其所有节点都遵循下述属性 - 节点的左子树的键小于或等于其父节点的键。 节点的右子树的键大于其父节点的键。

因此，BST将其所有子树分成两部分; 左边的子树和右边的子树，可以定义为 -
```left_subtree (keys)  ≤  node (key)  ≤  right_subtree (keys)```

#### 在B树搜索的值

在树中搜索值涉及比较输入值与退出节点的值。 在这里，也从左到右遍历节点，最后是父节点。 如果搜索到的值与任何退出值都不匹配，则返回未找到的消息，否则返回找到的消息。

```python
class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

# Insert method to create nodes
    def insert(self, data):

        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
# findval method to compare the value with nodes
    def findval(self, lkpval):
        if lkpval < self.data:
            if self.left is None:
                return str(lkpval)+" Not Found"
            return self.left.findval(lkpval)
        elif lkpval > self.data:
            if self.right is None:
                return str(lkpval)+" Not Found"
            return self.right.findval(lkpval)
        else:
            print(str(self.data) + ' is found')
# Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()


root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
print(root.findval(7))
print(root.findval(14))
Python
执行上面示例代码，得到以下结果 - 
7 Not Found
14 is found
None
```

### 平衡树

[参考](https://blog.csdn.net/geosipe/article/details/124433635)

### 红黑树

[参考](https://blog.csdn.net/net_wolf_007/article/details/79706498)