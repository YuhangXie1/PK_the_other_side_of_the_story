#
# Solution
#
import matplotlib.pyplot as plt
import numpy as np
import pkmodel as pk
import os

def graph_output(results, t):
    """Graph the pharmokinetic model

    Args:
        pk.Model object
        Dose time point (float): t

    """
    t = results.solve(t)['t'] # Solve for t values
    y_vals = results.solve(t)['y'] # Solve for y values

   if not os.path.exists('../output'):
        out_path = os.makedirs('../output') # Create directory to store output
    else:
        out_path = "../output"

    for y in y_vals:
        fig = plt.figure()
        plt.plot(t, y, label=f"Dose type:{results.dose_type} with {results.num_comp} compartments")
        plt.ylabel('Drug mass [ng]')
        plt.xlabel('Time [h]')
        fig.show()
        fig.savefig(f"{out_path}\\Plot_{results.name}_{results.num_comp}_comp_{results.dose_type}_dose.png")


if __name__ == "__main__":
    graph_output(res, 0)