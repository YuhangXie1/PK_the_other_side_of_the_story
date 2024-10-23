#
# Solution
#

import matplotlib.pyplot as plt
import numpy as np

def out_graph():
    '''Plot line graphs of input as model.zero_comp or model.one_comp'''
       
    results = model()  # Make instance of model called "results"

    x = results.zero_comp() # Store x values 
    y = results.zero_comp()

    fig = plt.figure()

    try: 

        plt.plot(x, y, label='zero compartment model')

    except: # some error 

    plt.legend()
    plt.ylabel('drug mass [ng]')
    plt.xlabel('time [h]')
    plt.show()

