# Nodes
## What are nodes?
Fudamental building blocks of many computer science data structures.
An individual node contains data and links to other nodes. Each one adds additional constraints or behavior to these features to create the desired structure. 
The link or links within the node are sometimes referred to as pointers. This is because they “point” to another node.
Typically, data structures implement nodes with one or more links. If these links are null, it denotes that you have reached the end of the particular node or link path you were previously following.
Often, due to the data structure, nodes may only be linked to from a single other node. This makes it very important to consider how you implement modifying or removing nodes from a data structure.
If you inadvertently remove the single link to a node, that node’s data and any linked nodes could be “lost” to your application. When this happens to a node, it is called an orphaned node.
## Nodes in python
The node’s data will be specified when creating the node and immutable (can’t be updated). The link will be optional at initialization and can be updated.

class Node():
  def __init__(self, value, link_node=None):
    self.value = value
    self.link_node = link_node

  
