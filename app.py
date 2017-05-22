import matplotlib.pyplot as plt
import numpy as np
import string
import sys
import parser

colors=['green', 'purple', 'red',  'blue', 'yellow']

with open(sys.argv[1], 'r') as f:
    struct = parser.parse_file(f)

for i in range(1, len(struct)):
    fig = plt.figure(i)
    plt.hist(struct[i].mylist, color=colors[i], label=struct[i].title)
    plt.legend()
    plt.xlabel(struct[i].title)
    plt.ylabel("frequency")
    fig.show()

raw_input()