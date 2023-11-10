class Node():
  def __init__(self, value, link_node=None):
    self.value = value
    self.link_node = link_node
    
  def get_value(self):
    return self.value
    
  def get_link_node(self):
    return self.link_node
    
  def set_link_value(self, link_node):
    self.link_node = link_ node

#creating three objects of Node class
a = Node(48)
b = Node(37)
c = Node(989)

#stablish links
a.set_link_node(b)
b.set_link_node(c)
# a -> b -> c

#getting data from one node to another
bs_data = a.get_link_node().get_value()
cs_data = b.get_link_node().get_value()

print(bs_data)
print(cs_data)

  
