#
# Solution
#
import matplotlib.pyplot as plt
import numpy as np
import pkmodel as pk
import os


def run_output():
    """Run the pharmokinetic model and output the result."""

    model_args = pk.load_parameters(file)
    res = pk.Model(model_args) # Make instance of model

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

    graph_output(res, 0)