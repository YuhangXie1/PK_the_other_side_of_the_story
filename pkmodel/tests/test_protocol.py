#import unittest
#import pkmodel as pk

import pytest
from pkmodel.protocol import schema
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
    with open("pkmodel/tests/test_yaml_files/" + test) as stream:
        data_yaml = [yaml.safe_load(stream)]
        if expected == object:
            assert schema.validate(data_yaml)
        elif expected == SchemaError:
            with pytest.raises(SchemaError):
                schema.validate(data_yaml)
        else:
            raise Exception("wrong error received, instead of SchemaError")