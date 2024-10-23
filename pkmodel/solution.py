#
# Solution
#
import matplotlib.pyplot as plt
import numpy as np
import pkmodel as pk

# Testing
model_args = {
    'name': 'Test name',
    'num_comp': 1,
    'dose_type': 'IV',
    'y': [1, 10],
    'Q_p1': 10.0,
    'V_c': 100.0,
    'V_p1': 20.0,
    'CL': 0.5,
    'X': 10.0,
    'step_size': 10,
    'endpoint': 100
}

res = pk.Model(model_args) # Make instance of model

def graph_output(results, t, ):
    """Graph the pharmokinetic model

    Args:
        pk.Model object
        Dose time point (float): t

    """

    def check_results(results):
        """Check that data is correct type"""
        return True # if true

    print(results.solve(t))

    x = results.solve(t)['t']

    for y_vals in results.solve(t)['y']:

        try:
            fig = plt.figure()
            plt.plot(x, y_vals, label=f"Dose type:{results.dose_type} with {results.num_comp} compartments")
            plt.ylabel('Drug mass [ng]')
            plt.xlabel('Time [h]')
            fig.show()
            fig.savefig(f"../Plot_{results.name}_{results.num_comp}_comp_{results.dose_type}_dose.png")

        except ValueError:
            print("ValueError")

graph_output(res, 0)