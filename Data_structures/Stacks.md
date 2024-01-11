# What is Stack?

   >> A stack is a linear data structure in which the insertion of a new element and removal of an existing element takes place at the same end represented as the top of the stack.

To implement the stack, it is required to maintain the pointer to the top of the stack, which is the last element to be inserted because we can access the elements only on the top of the stack.

## LIFO( Last In First Out ):

 >>   This strategy states that the element that is inserted last will come out first. You can take a pile of plates kept on top of each other as a real-life example. The plate which we put last is on the top and since we remove the plate that is at the top, we can say that the plate that was put last comes out first.

## Basic Operations on Stack

In order to make manipulations in a stack, there are certain operations provided to us.

+    push() to insert an element into the stack
 +   pop() to remove an element from the stack
  +  top() or peek() Returns the top element of the stack.
   + isEmpty() returns true if stack is empty else false.
   + size() returns the size of stack.

We also need to consider the stack’s size and tweak our methods a bit so that our stack does not “overflow”. If we’re not careful, we can accidentally over-fill them with data. Since we don’t want any stack overflow, we need to go back and make a few modifications to our methods that help us track and limit the stack size so we can keep our stacks healthy.

What do we do if someone tries to peek() or pop() when our stack is empty?

How do we keep someone from push()ing to a stack that has already reached its limit?

How do we even know how large our stack has gotten?

      from node import Node

      class Stack:
        def __init__(self, limit=1000):
          self.top_item = None
          self.size = 0
          self.limit = limit
  
        def push(self, value):
          if self.has_space():
            item = Node(value)
            item.set_next_node(self.top_item)
            self.top_item = item
            self.size += 1
          else:
            print("All out of space!")

        def pop(self):
          if not self.is_empty():
            item_to_remove = self.top_item
            self.top_item = item_to_remove.get_next_node()
            self.size -= 1
            return item_to_remove.get_value()
          else:
            print("This stack is totally empty.")
  
        def peek(self):
          if not self.is_empty():
	          return self.top_item.get_value()
          else:
            print("Nothing to see here!")
      
        def has_space(self):
          if self.limit > self.size:
            return True
          else:
            return False
      
        def is_empty(self):
          if self.size == 0:
            return True
          else:
            return False

