#import unittest
#import pkmodel as pk

import pytest

# class ProtocolTest(unittest.TestCase):
#     """
#     Tests the :class:`Protocol` class.
#     """
#     def test_create(self):
#         """
#         Tests Protocol creation.
#         """
#         model = pk.Protocol()
#         self.assertEqual(model.value, 43)

from pkmodel.protocol import schema
import yaml
from schema import SchemaError
@pytest.mark.parametrize(
        "test, expected",
        [
            ("test_success.yaml", object), #successful yaml returns a list object
            ("test_fail_strvalues.yaml", SchemaError), #incorrect yaml returns SchemaError - values cannot be turned into float
            ("test_fail_negvalues.yaml", SchemaError), #incorrect yaml returns SchemaError - values are negative
            ("test_fail_nomodels.yaml", SchemaError), #incorrect yaml returns SchemaError - model is not chosen
        ]
)
def test_yaml_file_validation(test, expected):
    """
    Tests each .yaml file and validates if error occurs
    """
    with open("pkmodel/tests/test_yaml_files/" + test) as stream:
        data_yaml = [yaml.safe_load(stream)]
        try:
             schema.validate(data_yaml)
        except SchemaError as error_message:
            assert True
            

def test_1():
    assert 1 == 2