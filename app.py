import matplotlib.pyplot as plt
import numpy as np
import string
import sys
import parser

colors=['green', 'purple', 'red',  'blue', 'yellow']

with open(sys.argv[1], 'r') as f:
    struct = parser.parse_file(f)

for i in range(1, len(struct)):
    plt.hist(struct[i].mylist, color=colors[i], label=struct[i].title)
    plt.legend()
    plt.xlabel(struct[1].title)
    plt.ylabel(struct[2].title)

plt.show()
