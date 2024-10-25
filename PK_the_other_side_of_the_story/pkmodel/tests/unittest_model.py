import unittest
from model import Model  # Import the Model class from the model.py

class TestModel(unittest.TestCase):

    def setUp(self):
        # Common setup code for your tests
        self.params = {
            'name': {'value': 'test_model'},
            'num_comp': {'value': 1},
            'dose_type': {'value': 'IV'},
            'Q_p1': {'value': 0},
            'V_c': {'value': 1},
            'V_p1': {'value': 0},
            'CL': {'value': 1},
            'X': {'value': 1},
            'num_steps': {'value': 100},
            'endpoint': {'value': 1},
            'y': {'value': [0.0, 0.0]},
            'ka': {'value': 1.0},
            'q': {'value': 0.4}
        }

    def test_model_1_comp_initialisation(self):
        model = Model(self.params)
        self.assertEqual(model.name, 'test_model')
        self.assertEqual(model.num_comp, 1)

    def test_model_2_comp_initialisation(self):
        model = Model(self.params)
        self.assertEqual(model.name, 'test_model')
        self.assertEqual(model.num_comp, 2)

    def test_invalid_y(self):
        invalid_params = self.params.copy()
        invalid_params['y'] = {'value': None}  # or any other invalid value
        with self.assertRaises(Exception):  # Replace with the specific exception
            model = Model(invalid_params)

    def test_zero_division(self):
        zero_division_params = self.params.copy()
        zero_division_params['V_c'] = {'value': 0}  # Set V_c to zero
        model = Model(zero_division_params)
        with self.assertRaises(ZeroDivisionError):
            model.solve(0)  # Call solve method to trigger the zero division

    def test_negative_numbers(self):
        negative_params = self.params.copy()
        negative_params['V_c'] = {'value': -1}  # Negative volume
        with self.assertRaises(ValueError):  # Replace with appropriate exception
            model = Model(negative_params)

    def test_no_container(self):
        no_container_params = self.params.copy()
        no_container_params['num_comp'] = {'value': 0}  # Set number of compartments to 0
        with self.assertRaises(Exception):  # Replace with the specific exception
            model = Model(no_container_params)

if __name__ == '__main__':
    unittest.main()
