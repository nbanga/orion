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

    def addChild(self, c, allNodes):
        #create new node
        n = Node(c)
        n.parent = self

        #add it to the children map
        self.children[n.value] = [n,1]

        allNodes[n.value] = n

        #return newly added node
        return n

    def hasChild(self, value):
        if self.children.has_key(value):
            return self.children[value][0]
        return None
      
#get name of function from list
def getName(s):
    return s.split('-')[1]

def makeGraph(ig, allNodes):
    parent = Node('X')
    allNodes['X'] = parent
    tmp = parent
    for each in ig:
        if each.startswith("ENTER"):
            value = each.split('-')[1]
            k = parent.hasChild(value)
            if k == None:
                k = parent.addChild(value,allNodes)
            else:
                if(parent.children[value][1] == 0):
                    parent.children[value][1] += 1
            parent = k
        else:
            if parent.parent == None:
                continue
            parent = parent.parent

    parent = tmp
    print "Ran makeGraph"
    return parent

#print graph routine
visited = dict()
def printGraph(p):
    q = [p]
    while len(q) != 0:
        it = q[0]
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

def pruneGraph(ng, allNodes):
    countset = set()
    stack = ['X']
    for each in ng :
        if each.startswith("ENTER"):
            fname = each.split('-')[1]
            if allNodes.has_key(fname):
                pfname = stack[-1]
                if allNodes.has_key(pfname):
                    node = allNodes[pfname]
                    if node.hasChild(fname):
                        countset.add((pfname, fname))

            stack.append(fname)
        else:
            if len(each) != 0 and each.split('-')[1] == stack[-1]:
                stack.pop()

    for each in countset:
        node = allNodes[each[0]]
        node.children[each[1]][1] += 1
    print "printing allNodes "
    for each in allNodes:
        for every in allNodes[each].children.keys():
            print "(",each,",",every,")", " : ",allNodes[each].children[every][1] 
