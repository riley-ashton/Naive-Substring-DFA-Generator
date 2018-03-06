"""
@author: Riley Ashton
"""
import itertools
from functools import reduce
import graphviz as gv

def gen_DFA(partition_size, alphabet, pred):
    """
    Given a partition size, alphabet of single characters and a predicate 
    lambda expression, compute the DFA diagram so that the machine only
    accepts strings that satisfy the requirement in every partition.
    """
    g = gv.Digraph(format="pdf")
    trap_state = lambda x : not pred(x)
    node_name = lambda node : reduce(lambda x, y: x + y, node, "")
    
    nodes = itertools.product(alphabet, repeat = partition_size)    
    for node in nodes:
        name = node_name(node)
        g.node(name) if trap_state(name) else g.node(name,shape="doublecircle")

    nodes = itertools.product(alphabet, repeat = partition_size)    
    for node in nodes:
        name = node_name(node)
        if trap_state(name):
            g.edge(name, name, label = 
                reduce(lambda x,y: y if x=="" else x + ", " + y, alphabet, ""))
        else:
            for letter in alphabet:
                g.edge(name, name[1:] + letter, label = letter)
    
    g.render("./out")
