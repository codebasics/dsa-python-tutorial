class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return # node already exist

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)


    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

#finding  the  minimum element in the entire binary tree
  def find_min (self, data):
      if self.left = None:
         return self.data
      return  self.left.find_min()
    
# finding the maximum element in the entire binary  tree
  def find_max (self, data):
      if self.right = None:
          return self.data
      return  self.right.find_min()

#calculating sum of all elements

  def calculate_sum(self):
       total = self.data

     if  self.right:
         total +=self.right.calculate_sum() 

     if  self.left:
         total += self.left.calculate_sum()


#post_order_traversal
  def post_order_traversal(self):
          elements = []
          if self.left:
            elements += self.left.post_order_traversal()

          if self.right:
            elements += self.right.post_order_traversal()
            
        elements.append(self.data)
        return elements


  def pre_order_traversal(self):
          elements = []
          if self.left:
            elements += self.left.pre_order_traversal()

          if self.right:
            elements += self.right.pre_order_traversal()
            
       
        return elements   



def build_tree(elements):
    print("Building tree with these elements:",elements)
    root = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root




if __name__ == '__main__':
    countries = ["India","Pakistan","Germany", "USA","China","India","UK","USA"]
    country_tree = build_tree(countries)

    print("UK is in the list? ", country_tree.search("UK"))
    print("Sweden is in the list? ", country_tree.search("Sweden"))

    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    print("In order traversal gives this sorted list:",numbers_tree.in_order_traversal())



    print("In-order Traversal:", numbers_tree.in_order_traversal())
    print("Minimum value:", numbers_tree.find_min())
    print("Maximum value:", numbers_tree.find_max())
    print("Sum of all elements:", numbers_tree.calculate_sum())
    print("Post-order Traversal:", numbers_tree.post_order_traversal())
    print("Pre-order Traversal:", numbers_tree.pre_order_traversal())
