#import unittest
#import pkmodel as pk

import pytest
from pkmodel.protocol import schema, load_parameters
import yaml
from schema import SchemaError



#Tests the loading and parsing of the yaml file
@pytest.mark.parametrize(
        "test, expected",
        [
            ("test_success.yaml", object), #successful yaml returns a list object
            ("test_fail_strvalues.yaml", SchemaError), #incorrect yaml returns SchemaError - values cannot be turned into float
            ("test_fail_negvalues.yaml", SchemaError), #incorrect yaml returns SchemaError - values are negative
            ("test_fail_nocompartments.yaml", SchemaError), #incorrect yaml returns SchemaError - number of components are out of range
            ("test_fail_y_list.yaml", SchemaError), #incorrect yaml returns SchemaError - number of components are out of range
        ]
)
def test_yaml_file_validation(test, expected):
    """
    Tests each .yaml file and validates if error occurs
    """
    if expected == object:
        assert load_parameters("pkmodel/tests/test_yaml_files/" + test)
        
    elif expected == SchemaError:
        with pytest.raises(SchemaError):
            load_parameters("pkmodel/tests/test_yaml_files/" + test)
    else:
        raise Exception("wrong error received, instead of SchemaError")
    
