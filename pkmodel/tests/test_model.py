import pytest
from main import main
from schema import SchemaError

#Tests the loading and parsing of the yaml file
@pytest.mark.parametrize(
        "test, expected",
        [
            ("test_success.yaml", object), #successful yaml raises no errors
        ]
)
def test_model_fully(test, expected):
    """
    Tests each .yaml file into the model and validates if error occurs
    """
    file_path = "pkmodel/tests/test_yaml_files/" + test

    if expected == object:
        assert main(file_path) is None
        
    elif expected == SchemaError:
        pass
    #     with pytest.raises(SchemaError):
    #         load_parameters("pkmodel/tests/test_yaml_files/" + test)
    # else:
    #     raise Exception("wrong error received, instead of SchemaError")
    
