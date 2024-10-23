#
# Protocol class
#

import yaml
from schema import Schema, And, Use, Optional, SchemaError

#Schema of input variable names and the expected type and formats
schema = Schema(
    [
        {
            "name": And(str, len), #checks name is a str, and not empty (length > 0)
            "Q_p1": And(Use(float), lambda n: n>=0), #turns input into float, check if positive number
            "V_c": And(Use(float), lambda n: n>=0),
            "V_p1": And(Use(float), lambda n: n>=0),
            "CL": And(Use(float), lambda n: n>=0),
            "X": And(Use(float), lambda n: n>=0),
        }
    ],
    ignore_extra_keys= True #extra dictionary keys in the file is not counted
)

#Opening the yaml file


class Protocol:
    """A Pharmokinetic (PK) protocol

    Parameters
    ----------

    value: numeric, optional
        an example paramter

    """
    def __init__(self, value=43):
        self.value = value

