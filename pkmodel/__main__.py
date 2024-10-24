# __main__.py

from pkmodel import solution, protocol, model


def main():

    res = model.Model(protocol.load_parameters)
    solution.graph_output(res, 0)

if __name__ == "__main__":
    main()