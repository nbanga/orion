class Node:
    def __init__(self, value):
        self.parent = None
        self.children = dict()
        self.value = value

    def setParent(self, p):
        print "in set parent"
        if p == None:
            self.parent = p
            print "setted parent"

    def addChild(self, c):
        #create new node
        n = Node(c)
        n.parent = self

        #add it to the children map
        self.children[n.value] = [n,1]

        #return newly added node
        return n

    def hasChild(self, value):
        if self.children.has_key(value):
            return self.children[value][0]
        return None
      
#logic to make a list out of file entries
#input handling
f = open('input.txt','r')
l = f.readlines()[0]
l = l[1:-2].split(", ")

#get name of function from list
def getName(s):
    return s.split('-')[1]

def makeGraph(l):
    parent = Node(0)
    tmp = parent
    for each in l:
        if each.startswith("ENTER"):
            value = each.split('-')[1]#getName(each)
            print "checking ",value
            k = parent.hasChild(value)
            if k == None:
                print "adding ", value
                print "****"
                k = parent.addChild(value)
            else:
                parent.children[value][1] += 1
            parent = k
        else:
            if parent.parent == None:
                print "Have none type parent ", parent.value
                continue
            parent = parent.parent

    parent = tmp
    return parent

#print graph routine
visited = dict()
def printGraph(p):
    q = [p]
    while len(q) != 0:
        it = q[0]
        #print it, type(it)
        print "Printing children of Node "+ str(it.value)
        for each in it.children:
            print each
        print "-----------------------------------"

        for each in it.children:
            if visited.has_key(each):
                continue
            q.append(it.children[each][0])
            visited[each] = True
        
        q.remove(it)
        
def main():
    pa = makeGraph(l)
    printGraph(pa)
    
#caller
if __name__ == "__main__":
    main()
