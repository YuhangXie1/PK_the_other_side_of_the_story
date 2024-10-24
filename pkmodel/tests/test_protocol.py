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
            ("test.yaml", object), #successful yaml returns a list object
            ("test2.yaml", SchemaError), #incorrect yaml returns SchemaError

        ]
)
def test_yaml_file_validation(test, expected):
    """
    Tests each .yaml file and validates if error occurs
    """
    with open(test) as stream:
        data_yaml = [yaml.safe_load(stream)]
        with pytest.raises(SchemaError) as error_message:
            schema.validate(data_yaml)