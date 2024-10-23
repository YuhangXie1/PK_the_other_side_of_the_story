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
        'Vc': {
            'description': data['param']['Vc']['description'],
            'value': data['param']['Vc']['value'],
            'units': data['param']['Vc']['units']
        },
        'Vp1': {
            'description': data['param']['Vp1']['description'],
            'value': data['param']['Vp1']['value'],
            'units': data['param']['Vp1']['units']
        },
        'CL': {
            'description': data['param']['CL']['description'],
            'value': data['param']['CL']['value'],
            'units': data['param']['CL']['units']
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
