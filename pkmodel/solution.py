#
# Solution
#

import matplotlib.pyplot as plt
import numpy as np
from model import Model

model = Model(num_compartments=1, dosing_type='IV', protocol=None) # Make instance of model called "results"

# test data
#results = np.array([np.random.uniform(0, 10, 100), np.random.uniform(0, 1, 100)])

def graph_output(results):
    """Plot line graphs of input as model.zero_comp or model.one_comp"""
    # Create array of y values for both zero comp and one comp models
    # Check x and y are same length.
    # Plot line graph of zero model

    y_arr = np.array([results.zero_comp[1], results.one_comp[1]])
    x = results.zero_comp()[0]

    if len(x) == len(y):

        fig = plt.figure()

        for y in y_arr:

            try:
                plt.plot(x, y, label=f"Dose type:{results.dosing_type} with {results.num_compartments} compartments")
                plt.ylabel('Drug mass [ng]')
                plt.xlabel('Time [h]')

            except ValueError:
                print("ValueError")

        fig.show()
        fig.savefig(f"output-{results.name}.png")

    else:
        print("x and y not same length.")

graph_output(model)