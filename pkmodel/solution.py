#
# Solution
#
import matplotlib.pyplot as plt
import numpy as np
import model as model

results = model(num_compartments = 1, dosing_type = 'IV', protocol = None) # Make instance of model called "results"
results

# test data
results = np.array([np.random.uniform(0, 10, 100), np.random.uniform(0, 1, 100)])

def graph_output(data):
    """Plot line graphs of input as model.zero_comp or model.one_comp"""

    x = data[0] # Store x values
    y = data[1]

    if len(x) == len(y): # Check x and y are same length.

        fig = plt.figure()

        try:
            plt.plot(x, y, label=model['name'] + '- q_c')
            #plt.plot(x, y, label=model['name'] + '- q_p1')

            plt.ylabel('drug mass [ng]')
            plt.xlabel('time [h]')

        except ValueError:
            print("ValueError")

        fig.show()
    else:
        print("x and y not same length.")

graph_output(results)