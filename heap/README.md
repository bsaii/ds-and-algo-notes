# Heap

In computer science, a heap is a specialized tree-based data structure which is essentially an almost complete tree that satisfies the heap property: in a max heap, for any given node C, if P is a parent node of C, then the key (the value) of P is greater than or equal to the key of C. In a min heap, the key of P is less than or equal to the key of C. The node at the "top" of the heap (with no parents) is called the root node.

**[Read More on Heap(Data Structure)](https://en.wikipedia.org/wiki/Heap_(data_structure)#:~:text=In%20computer%20science%2C%20a%20heap,to%20the%20key%20of%20C.)**

## Max Heap and Min Heap

There are two kinds of heaps - Min Heap and Max Heap. A Min Heap is a tree that has two properties:

1. almost complete, i.e. every level is filled except possibly the last(deepest) level. The filled items in the last level are left-justified.
2. for any node, its key (priority) is greater than its parent's key (Min Heap).

A Max Heap has the same property for #1 and opposite property for #2 of min heap, i.e. for any node, its key is less than its parent's key.

**Let's play "is it a heap?" game**:

![Heap Intro](https://algomonster.s3.us-east-2.amazonaws.com/heap_intro/heap_intro_2.png)

![Is it a heap?](https://algomonster.s3.us-east-2.amazonaws.com/heap_intro/heap_intro_3.png)

**Note That**:

- the number in each node is the key, not value (remember a tree node has a value). Keys are used to sort the nodes/construct the tree, and values are the data we want heap to store.
- unlike a binary search tree, there is no comparable relationship between children. For example, the third example in the first row, 17 and 8 are both larger than 2 but they are NOT sorted left to right. In fact, there is no comparable relationship across a level of a heap at all.

## Why heaps are useful?

By the first look, the heap is an odd data structure - it's required to be a complete tree but unlike binary search tree, it's not sorted across a level.

**What makes it so useful**?

- because a heap is a complete tree, the height of a heap is guaranteed to be _O(log(N))_. This makes operations that go from root to leaf guaranteed to be _O(log(N))_.
- because only nodes in a root-to-leaf path are sorted (nodes in the same level are not sorted), when we add/remove a node, we only have to fix the order in the vertical path the node is in. This makes inserting and deleting _O(log(N))_ too.
- being complete also makes array a good choice to store a heap since data is continuous. As we will see later in this module, we can find the parent and children of a node simply by doing index arithmetics.

## Operations

### insert

To insert a key into a heap,

- place the new key at the first free leaf
- if property #2 is violated, perform a bubble-up

  ```python
  def bubble_up(node):
      while node.parent exist and node.parent.key > node.key:
          swap node and node.parent
          node = node.parent
  ```
**Illustration**:

![Bubble Up 001](https://algomonster.s3.us-east-2.amazonaws.com/bubble_up/bubble_up.001.png)
![Bubble Up 002](https://algomonster.s3.us-east-2.amazonaws.com/bubble_up/bubble_up.002.png) 
![Bubble Up 003](https://algomonster.s3.us-east-2.amazonaws.com/bubble_up/bubble_up.003.png)
![Bubble Up 004](https://algomonster.s3.us-east-2.amazonaws.com/bubble_up/bubble_up.004.png)
![Bubble Up 005](https://algomonster.s3.us-east-2.amazonaws.com/bubble_up/bubble_up.005.png)

As the name of the algorithm suggests, it "bubbles up" the new node by swapping it with its parent until the order is correct

Since the height of a heap is _O(log(N))_, the complexity of bubble-up is _O(log(N))_.

### delete_min

What this operation does is:

- delete a node with min key and return it
- reorganize the heap so the two properties still hold

To do that, we:

- remove and return the root since the node with the minimum key is always at the root
- replace the root with the last node (the rightmost node at the bottom) of the heap
- if property #2 is violated, perform a bubble-down

  ```python
  def bubble_down(node):
    while node is not a leaf:
        smallest_child = child of node with smallest key
        if smallest_child < node:
            swap node and smallest_child
            node = smallest_child
        else:
            break
  ```
**Illustration**:

![Bubble Down 001](https://algomonster.s3.us-east-2.amazonaws.com/bubble_down/bubble_down.001.png)
![Bubble Down 002](https://algomonster.s3.us-east-2.amazonaws.com/bubble_down/bubble_down.002.png)
![Bubble Down 003](https://algomonster.s3.us-east-2.amazonaws.com/bubble_down/bubble_down.003.png)
![Bubble Down 004](https://algomonster.s3.us-east-2.amazonaws.com/bubble_down/bubble_down.004.png)
![Bubble Down 005](https://algomonster.s3.us-east-2.amazonaws.com/bubble_down/bubble_down.005.png)

What this says is we keep swapping between the current node and its smallest child until we get to the leaf, hence a "bubble down". Again the time complexity is _O(log(N))_ since the height of a heap is _O(log(N))_.

## Implementing Heap

Being a complete tree makes an array a natural choice to implement a heap since it can be stored compactly and no space is wasted. Pointers are not needed. The parent and children of each node can be calculated with index arithmetic

![Heap Intro 5](https://algomonster.s3.us-east-2.amazonaws.com/heap_intro/heap_intro_5.png)

For node `i`, its children are stored at `2i+1` and `2i+2`, and its parent is at `floor((i-1)/2)`. So instead of `node.left` we'd do `2*i+1`.

### Heap in Python (Heapify)

Python comes with a built-in `heapq` we can use, and it is a **min heap**, i.e. element at top is smallest.

`heapq.heappush` takes two arguments, the first is the heap (an array/list) we want to push the element into, the second argument can be anything as long as it can be used for comparison. Typically we push a tuple as in python tuples are compared item by item in order. For example, `(1, 10)` is smaller than `(2, 0)` because the first element is smaller. `(1, 10)` is smaller than `(1, 20)` because when the first item is same, we compare next one and in this case 10 is smaller than 20.

`heapq.heappop` takes a single argument heap, and pop and return the smallest element in the heap.

```python
import heapq
>>> h = []
>>> heapq.heappush(h, (5, 'write code'))
>>> heapq.heappush(h, (7, 'release product'))
>>> heapq.heappush(h, (1, 'write spec'))
>>> heapq.heappush(h, (3, 'create tests'))
>>> heapq.heappop(h) # returns
(1, 'write spec')
>>> h[0]
>>> (3, 'create tests')
```

If the list is known beforehand, we can create a heap out of it by simply using heapify, which is actually an _O(N)_ operation.

## Implementing Max Heap

The simplest way to implement a max heap is to reverse the sign of the number before we push it into the heap and reverse it again when you pop it out. For example, if we want to build a max heap out of `[3, 1, 2]`, we can push `[-3, -1, -2]` into the heap. Because default heap is a min heap, when we pop `-3` will be popped out and its reverse `3` is the max of the three and thus we have a max heap. We will see both min and max heaps in the following modules.
