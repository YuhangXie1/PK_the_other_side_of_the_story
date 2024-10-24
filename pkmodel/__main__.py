# __main__.py

from pkmodel import solution, protocol, model


def main():
    """ Main function runs each module in tandem """

    parameters = protocol.load_parameters # Run protocol and stores parameters
    results = model.Model(parameters) # Run model and stores results
    solution.graph_output(results, 0) # Run solution and prints output

if __name__ == "__main__":
    main()