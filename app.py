import matplotlib.pyplot as plt
import numpy as np
import string
import sys
import parser

with open(sys.argv[1], 'r') as f:
    struct = parser.parse_file(f)

plt.scatter(struct[1].mylist,struct[2].mylist, color="red", label=struct[1].title + " vs " + struct[2].title)
plt.legend()
plt.xlabel(struct[1].title)
plt.ylabel(struct[2].title)

plt.scatter(struct[0].mylist,struct[1].mylist, color="blue", label=struct[0].title + " vs " + struct[1].title)
plt.legend()
plt.xlabel(struct[0].title)
plt.ylabel(struct[1].title)

plt.show()
