class linkedlist:
    def __init__(self,data,pointer=None):
        self.data=data
        self.pointer=pointer
node3=linkedlist(3)
node2=linkedlist(2,node3)
node1=linkedlist(1,node2)
cur=node1
while(cur is not None):
    print(cur.data)
    cur=cur.pointer
