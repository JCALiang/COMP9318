## import modules here 

################# Question 0 #################

def add(a, b): # do not change the heading of the function
    return a + b


################# Question 1 #################

def nsqrt(x): # do not change the heading of the function
    guess= x/2
    while abs(guess*guess - x) > 0.1:
        guess= 0.5*(guess+x/guess)
    return int(guess)

################# Question 2 #################

# x_0: initial guess
# EPSILON: stop when abs(x - x_new) < EPSILON
# MAX_ITER: maximum number of iterations

## NOTE: you must use the default values of the above parameters, do not change them

def find_root(f, fprime, x_0=1.0, EPSILON = 1E-7, MAX_ITER = 1000): # do not change the heading of the function
    print('x_0')
    x_new= x_0- f(x_0)/fprime(x_0)
    print(x_0)
    while abs(x_0- x_new) > EPSILON and MAX_ITER>0:
        x_0= x_new
        x_new= x_0- f(x_0)/fprime(x_0)
        MAX_ITER-=1
        
    return x_new

################# Question 3 #################

class Tree(object):
    def __init__(self, name='ROOT', children=None):
        self.name = name
        self.children = []
        if children is not None:
            for child in children:
                self.add_child(child)
    def __repr__(self):
        return self.name
    def add_child(self, node):
        assert isinstance(node, Tree)
        self.children.append(node)

def re(tree, leaves, d):
    for i in reversed(leaves):
        if i in d:
            t=Tree(i)
            c=re(t, d[i], d)
            tree.add_child(t)
        else:
            tree.add_child(Tree(i))
    return tree
    

    
def make_tree(tokens): # do not change the heading of the function
    
    stack=[]
    d=dict()
    
    for i in range(0, len(tokens)):
        if tokens[i] !="]":
            stack.append(tokens[i])
        else:
           
            child=[]
            for i in reversed(stack):
            
                if i != "[":
                    child.append(i)
                    stack.pop()
                else:
                    stack.pop()
                    break
            
            node=stack[-1]
            d[node]=child
            root=[node, child]

    tree=Tree(root[0])
    leaves=root[1]
    tree= re(tree, leaves, d)
    return tree
    

def rec(tt, layer):
    global maxx
    if not tt.children:
        return

    layer+=1
    if layer>=maxx:
        maxx=layer
    for i in tt.children:
        rec(i, layer)
            
    return

def max_depth(root): # do not change the heading of the function
    global maxx
    maxx=1
    rec(root,1)
    return maxx


