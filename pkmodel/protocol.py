"""
Protocol parsing script
"""
import yaml
from schema import Schema, And, Use, Optional, SchemaError
import pytest 

#schema checks yaml file and raises error if values do not fit the type set
schema = Schema(
    [
        {
            "name": {"value": And(str, len)}, #checks name is a str, and not empty (length > 0)
            "num_comp": {"value": And(Use(int), lambda s: s in (1,2))},
            "dose_type": {"value": And(str, lambda s: s in ("IV"))},
            "y": {"value": And(list, [Use(float), lambda n: n >=0])},
            "Q_p1": {"value": And(Use(float), lambda n: n>=0)},
            "V_c": {"value": And(Use(float), lambda n: n>=0)},
            "V_p1": {"value": And(Use(float), lambda n: n>=0)},
            "CL": {"value": And(Use(float), lambda n: n>=0)},
            "X": {"value": And(Use(float), lambda n: n>=0)},
            "num_steps": {"value": And(Use(int), lambda n: n>=0)},
            "endpoint": {"value": And(Use(float), lambda n: n>=0)},
        }
    ],
    ignore_extra_keys= True #extra dictionary keys in the file is not counted
)

def load_parameters(yaml_file):
    """
    Load parameters from a YAML file, checks the schema and return a dictionary.

    Args:
        yaml_file (str): Path to the YAML file containing model parameters.

    Returns:
        dict: A dictionary containing the model parameters and their descriptions.
    """
    with open(yaml_file, 'r') as file:
        data = yaml.safe_load(file)
    
    try:
        return schema.validate([data])[0]
    except SchemaError as error_message:
        return f"yaml input has raised an error {error_message}"


if __name__ == "__main__":
#Test this file if run in debugger
    #with open("input.yaml") as stream:
        #data_yaml = [yaml.safe_load(stream)]
        #with pytest.raises(SchemaError) as error_message:
        #print(data_yaml)
        #print(schema.validate(data_yaml))
    
    print(load_parameters("input.yaml"))
