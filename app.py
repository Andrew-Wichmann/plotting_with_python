import matplotlib.pyplot as plt
import numpy as np
import string
import sys
import parser

colors=['red','blue','green','yellow','purple']
figures=[]

with open(sys.argv[1], 'r') as f:
    struct = parser.parse_file(f)

for i in range(0, len(struct)-1):
    fig = plt.figure(i)
    plt.scatter(struct[i].mylist,struct[i+1].mylist, color=colors[i], label=struct[i].title + " vs " + struct[i+1].title)
    plt.legend()
    fig.show()
    
raw_input()