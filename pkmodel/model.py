import numpy as np
import scipy.integrate
import matplotlib.pyplot as plt

def dose(t, X):
    return X  # Simplified constant dose for now

class Model:
    """A Pharmacokinetic (PK) model with two compartments"""

    def __init__(self, params):
        self.name = params['name']  # Name of the model
        self.num_comp = params['num_comp']  # Number of compartments to model
        self.dose_type = params['dose_type']
        self.Q_p1 = params['Q_p1']  # [ng], drug quantity in peripheral compartment
        self.V_c = params['V_c']  # [ml], volume of central compartment
        self.V_p1 = params['V_p1']  # [ml], volume of peripheral compartment
        self.CL = params['CL']  # [ml/h], clearance rate from central compartment
        self.k_cp = params['k_cp']  # Rate constant for central to peripheral transfer
        self.k_pc = params['k_pc']  # Rate constant for peripheral to central transfer
        self.X = params['X']  # [ng/h], rate at which the drugs are administered into the central compartment
        self.num_steps = params['num_steps']
        self.endpoint = params['endpoint']
        self.y = params['y']  # Initial conditions (list of initial drug quantities in compartments)

    def ODE_sys(self, t, y):
        """
        Defines the system of ODEs for two compartments (central and peripheral).
        
        Args:
            t [h]: time
            y: array of drug quantities in central and peripheral compartments

        Returns:
            A list containing the rate of change of drug quantity in the central compartment (dqc_dt)
            and the peripheral compartment (dqp1_dt).
        """
        q_c, q_p1 = y
        
        # Change in drug quantity in the central compartment
        dqc_dt = dose(t, self.X) - (q_c / self.V_c) * self.CL  # Clearance from central compartment
        if self.num_comp == 2:
            dqc_dt += self.k_pc * q_p1 - self.k_cp * q_c  # Exchange between compartments
        
        # Change in drug quantity in the peripheral compartment
        if self.num_comp == 2:
            dqp1_dt = self.k_cp * q_c - self.k_pc * q_p1  # Exchange between compartments
            return [dqc_dt, dqp1_dt]
        else:
            return [dqc_dt]  # Single-compartment model

    def solve(self, t):
        y0 = np.array(self.y)  # Initial conditions q_c and q_p1
        t_eval = np.linspace(0, self.endpoint, self.num_steps)
        
        # Solve the ODE for the given parameters.
        sol = scipy.integrate.solve_ivp(
            fun=lambda t, y: self.ODE_sys(t, y),
            t_span=[t_eval[0], t_eval[-1]],
            y0=y0, t_eval=t_eval
        )
        return sol

# Testing
model_args = {
    'name': 'Intravenous Bolus Dosing',
    'num_comp': 2,  # Two-compartment model
    'dose_type': 'IV',
    'Q_p1': 1,
    'V_c': 1.0,
    'V_p1': 1,
    'CL': 1,
    'k_cp': 1,  # Transfer rate from central to peripheral
    'k_pc': 1,  # Transfer rate from peripheral to central
    'X': 1.0,
    'num_steps': 1000,
    'endpoint': 1,
    'y': [0, 0]  # Initial conditions for central and peripheral compartments
}

Model1 = Model(model_args)
res = Model1.solve(t=0)

# Plotting
print(Model1.name)
print(np.shape(res.y))
print(res.y)

plt.plot(res.t, res.y[0], label='Central Compartment')
if Model1.num_comp > 1:
    plt.plot(res.t, res.y[1], label='Peripheral Compartment')

plt.xlabel('Time (hours)')
plt.ylabel('Drug Quantity (ng)')
plt.legend()
plt.show()
