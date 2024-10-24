#
# Model class
#
import numpy as np
import scipy.integrate
import matplotlib.pyplot as plt

def dose(t, X):
    return X
class Model:
    """A Pharmokinetic (PK) model

    Parameters
    ----------

    value: numeric, optional
        an example paramter

    """
    def __init__(self, params):
        self.name = params['name'] # name of the model
        self.num_comp = params['num_comp'] # number of compartments to model
        self.dose_type = params['dose_type']
        self.Q_p1 = params['Q_p1'] # [ng], drug quantity in periferal compartment
        self.V_c = params['V_c'] # [ml], volume central compartment.
        self.V_p1 = params['V_p1'] # [ml], volume periferal compartment.
        self.CL = params['CL'] # [ml/h], clearance rate from central compartment.
        self.X = params['X'] # [ng/h], rate at which the drugs are administered into the central compartment.
        self.num_steps = params['num_steps']
        self.endpoint = params['endpoint']

    def ODE_sys(self, t, y):
        """
        Creates the Right-Hand-Side function, rhs, of the ODE specifying the quantity of drugs in the central and periferal compartments. 

        Args:
            param1: t [h], duration for which the drug is administered.

        Returns:
            A list containing the rhs of the change in qc (drug quantity in central channel [ng]) and qp1 over time.

        Raises:
            KeyError: Raises an exception if input for parameters 2-6 is not an int or float type.
        """
        #if for any in type(i) != "float":
        #any in [for i in [self.Q_p1, self.V_c, self.V_p1, self.CL, self.X]]
        #if  self.Q_p1 or self.V_c or self.V_p1 or self.CL or self.X != type(float):
        #    raise Exception(f"Invalid input.")
        
        q_c, q_p1 = y
        dqc_dt = dose(t, self.X) - q_c / self.V_c * self.CL

        if self.num_comp == 1:
                return dqc_dt
        elif self.num_comp == 2:
                transition = self.Q_p1 * (q_c / self.V_c - q_p1 / self.V_p1)
                dqp1_dt = transition
                return dqc_dt - dqp1_dt
        else:
             raise Exception(f"No compartments")

    def solve(self, t):
        #y0 = np.zeros(self.num_comp + 1)
        y0 = np.array([0, 0.2]) # initial conditions q_c and q_p1
        t_eval = np.linspace(0, self.endpoint, self.num_steps)
        # solve the ODE for the given parameters.
        sol = scipy.integrate.solve_ivp(
        fun=lambda t, y: self.ODE_sys(t, y),
        t_span=[t_eval[0], t_eval[-1]],
        y0=y0, t_eval=t_eval
        )
        return sol

# Testing
model_args = {
    'name': 'Intravenous Bolus Dosing',
    'num_comp': 1,
    'dose_type': 'IV',
    'Q_p1': 0.5,
    'V_c': 1,
    'V_p1': 0.6,
    'CL': 0.7,
    'X': 1.0,
    'num_steps': 1000,
    'endpoint': 100
}

Model1 = Model(model_args)
res = Model1.solve(t=0)
print(Model1.name)
print(np.shape(res.y))
print(res.y)
plt.plot(res.t, res.y[0])
plt.plot(res.t, res.y[1])
plt.show()

        # A vector of zeros representing the initial concentration of drug in all compartments
        # unpack arguments of params dict and store in args list.
        # Handle dosing type and protocol
        # if protocol is provided initial conc is set to dose provided
        # if self.protocol:
        #     y0[0] = self.protocol.dose  # Initial dose in central compartment
        
        # # Solve the system of ODEs
        # solution = odeint(self.system_of_odes, y0, t, args=(params,))
        # return solution
        # unpack timepoints for which to evaluate the function.