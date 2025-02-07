class linkedlist:
    data=None
    pointer=None
    #we dont assign a pointer to a linked node as soon as we create , after another node, we'll assign a pointer
    def __init__(self,data):
        self.data=data
node1=linkedlist("data1")
print(node1.data)
print(node1.pointer)