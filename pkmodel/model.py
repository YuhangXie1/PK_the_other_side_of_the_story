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
        #self.protocol = params['protocol']
        self.y = params['y'] # [ng], initial quantity of drugs in central and periferal compartments.
        self.Q_p1 = params['Q_p1'] # [ng], drug quantity in periferal compartment
        self.V_c = params['V_c'] # [ml], volume central compartment.
        self.V_p1 = params['V_p1'] # [ml], volume periferal compartment.
        self.CL = params['CL'] # [ml/h], clearance rate from central compartment.
        self.X = params['X'] # [ng/h], rate at which the drugs are administered into the central compartment.
        self.step_size = params['step_size']
        self.endpoint = params['endpoint']

    def ODE_sys(self, t):
        """
        Creates the Right-Hand-Side function, rhs, of the ODE specifying the quantity of drugs in the central and periferal compartments. 

        Args:
            param1: t [h], duration for which the drug is administered.

        Returns:
            A list containing the rhs of the change in qc (drug quantity in central channel [ng]) and qp1 over time.

        Raises:
            KeyError: Raises an exception if input for parameters 2-6 is not an int or float type.
        """

        # if  self.y or self.Q_p1 or self.V_c or self.V_p1 or self.CL or self.X != isinstance((int, float)):
        #    raise Exception(f"Invalid input.")
        
        q_c, q_p1 = self.y
        dqc_dt = dose(t, self.X) - q_c / self.V_c * self.CL

        if self.num_comp < 2:
                return dqc_dt
        else:
                transition = self.Q_p1 * (q_c / self.V_c - q_p1 / self.V_p1)
                dqp1_dt = transition
                return dqc_dt - dqp1_dt

    def solve(self, t):
        # initial conditions
        y0 = np.zeros(self.num_comp + 1)
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
        t_eval = np.linspace(0, self.step_size, self.endpoint)
        # solve the ODE for the given parameters.
        sol = scipy.integrate.solve_ivp(
        fun=lambda t, y: self.ODE_sys(t),
        t_span=[t_eval[0], t_eval[-1]],
        y0=y0, t_eval=t_eval
        )
        return sol

# Testing
model_args = {
    'name': 'Garry',
    'num_comp': 1,
    'dose_type': 'IV',
    'y': [1, 1],
    'Q_p1': 1.0,
    'V_c': 1.0,
    'V_p1': 1.0,
    'CL': 1.0,
    'X': 1.0,
    'step_size': 1,
    'endpoint': 10
}

Garry = Model(model_args)
res = Garry.solve(t=0)
print(Garry.name)
print(res.y)
plt.plot(res.y[0], res.t)
plt.plot(res.y[1], res.t)
plt.show()

