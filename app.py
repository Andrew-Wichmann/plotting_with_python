import matplotlib.pyplot as plt
import scipy.optimize as optimization
import numpy as np
import string
import sys
import parser

colors=['red','blue','green','yellow','purple']
figures=[]

with open(sys.argv[1], 'r') as f:
    struct = parser.parse_file(f)

def plot_figure():
    fig = plt.figure(i)

    reg_variable = struct[i].title
    dep_variable = struct[i+1].title
    x = np.array(struct[i].mylist)
    y = np.array(struct[i+1].mylist)

    plt.scatter(x, y, color=colors[i], label=reg_variable + " vs " + dep_variable)

    m, c = find_least_squares(x, y)

    plt.plot(x, m*x + c, 'r', label='Fitted line')
    plt.legend()
    fig.show()

def find_least_squares(x, y):
    A = np.vstack([x, np.ones(len(x))]).T
    m, c = np.linalg.lstsq(A, y)[0]
    return m, c

for i in range(0, len(struct)-1):
    plot_figure()
    
raw_input()