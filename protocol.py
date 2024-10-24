import yaml

def load_parameters(yaml_file):
    """
    Load parameters from a YAML file and return a dictionary.

    Args:
        yaml_file (str): Path to the YAML file containing model parameters.

    Returns:
        dict: A dictionary containing the model parameters and their descriptions.
    """
    with open(yaml_file, 'r') as file:
        data = yaml.safe_load(file)

    # Extract parameters
    parameters = {
        't': { # [h] duration for which the drug is administered
            'value': data['param']['t']['value'],
            'units': data['param']['t']['units']
        },
        'y': { # [ng] initial quantity of drugs in central and periferal compartments
            'value': data['param']['y']['value'],
            'units': data['param']['y']['units']
        },
        'Q_p1': { # [ng] drug quantity in periferal compartment - should be 0 here for zero-compartment model
            'value': data['param']['Q_p1']['value'],
            'units': data['param']['Q_p1']['units']
        },
        'V_c': { # [ml] volume central compartment
            'value': data['param']['V_c']['value'],
            'units': data['param']['V_c']['units']
        },
        'V_p1': { # [ml] volume periferal compartment - should be 0 here for zero-compartment model
            'value': data['param']['V_p1']['value'],
            'units': data['param']['V_p1']['units']
        },
        'CL': { # [ml/h] clearance rate from central compartment
            'value': data['param']['CL']['value'],
            'units': data['param']['CL']['units']
        },
        'X': { # [ng/h] rate at which the drugs are administered into the central compartment
            'value': data['param']['X']['value'],
            'units': data['param']['X']['units']
        }
    }

    return parameters

if __name__ == "__main__":
    # Specify the path to your YAML file
    yaml_file_path = "input.yaml"  # Adjust the path if necessary

    # Load parameters
    parameters = load_parameters(yaml_file_path)

    # Output the parameters
    print("Parameters:")
    for param, details in parameters.items():
        print(f"{param}:")p
        print(f"  Description: {details['description']}")
        print(f"  Value: {details['value']}")
        print(f"  Units: {details['units']}")
