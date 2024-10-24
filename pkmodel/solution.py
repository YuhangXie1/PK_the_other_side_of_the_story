#
# Solution
#
import matplotlib.pyplot as plt
import numpy as np
import os

def graph_output(results, t):
    """Graph the pharmokinetic model

    Args:
        pk.Model object
        Dose time point (float): t

    """
    
    t = results.t
    qc = results.y[0] 
    qp1 = results.y[1] 

    if not os.path.exists('../output'):
       out_path = os.makedirs('../output') # Create directory to store output
    else:
        out_path = "../output"

    fig = plt.figure()
    plt.plot(t, qc, label= 'qc')
    plt.plot(t, qp1, label= 'qp1')
    plt.ylabel('Drug mass [ng]')
    plt.xlabel('Time [h]')
    fig.show()
    fig.savefig("test.png")

# if __name__ == "__main__":
#     graph_output(res, 0)