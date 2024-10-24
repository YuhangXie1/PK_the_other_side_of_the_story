# __main__.py

# import solution, protocol, model

from solution import graph_output
from protocol import load_parameters
from model import Model

def main():
    """ Main function runs each module in tandem """

    parameters = load_parameters('input.yaml') # Run protocol and stores parameters
    obj = Model(parameters) # Run model and stores results
    results = obj.solve(t=0)
    graph_output(results, 0) # Run solution and prints output

if __name__ == "__main__":
    main()