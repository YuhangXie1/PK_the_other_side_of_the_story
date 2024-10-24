#
# Model class
#
import numpy as np
import scipy.integrate
import matplotlib.pyplot as plt

def dose(t, X):
    return X
class Model:
    """
    
    A Pharmokinetic (PK) model

    """
    def __init__(self, params):
        self.name = params['name']['value'] # name of the model.
        self.num_comp = params['num_comp']['value'] # number of compartments to model.
        self.dose_type = params['dose_type']['value'] # Type of dose administered.
        self.Q_p1 = params['Q_p1']['value'] # [ng], drug quantity in periferal compartment.
        self.V_c = params['V_c']['value'] # [ml], volume central compartment.
        self.V_p1 = params['V_p1']['value'] # [ml], volume periferal compartment.
        self.CL = params['CL']['value'] # [ml/h], clearance rate from central compartment.
        self.X = params['X']['value'] # [ng/h], rate at which the drugs are administered into the central compartment.
        self.num_steps = params['num_steps']['value'] # number of time steps.
        self.endpoint = params['endpoint']['value'] # last timepoint.
        self.y = params['y']['value']  # initial conditions (list of initial drug quantities in compartments).
        self.ka = params['ka']['value']  
        self.q = params['q']['value']  

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
        dqc_dt = dose(t, self.X) - (q_c / self.V_c) * self.CL

        if self.num_comp == 1 and self.dose_type == "IV":
                return [dqc_dt]
        elif self.num_comp == 2 and self.dose_type == "IV":
                dqp1_dt = self.Q_p1 * ((q_c / self.V_c) - (q_p1 / self.V_p1))
                dqc_dt -= dqp1_dt
                return [dqc_dt, dqp1_dt]
        elif self.dose_type == "SC":
             dqc_dt = self.ka * self.q - (q_c / self.V_c) * self.CL
             dqp1_dt = self.Q_p1 * ((q_c / self.V_c) - (q_p1 / self.V_p1))
             dqc_dt -= dqp1_dt
             return [dqc_dt, dqp1_dt]
        else:
             raise Exception(f"Incorrect specification of .yaml file")

    def solve(self, t):
        y0 = np.array(self.y) # initial conditions q_c and q_p1
        t_eval = np.linspace(0, self.endpoint, self.num_steps)
        # solve the ODE for the given parameters.
        sol = scipy.integrate.solve_ivp(
        fun=lambda t, y: self.ODE_sys(t, y),
        t_span=[t_eval[0], t_eval[-1]],
        y0=y0, t_eval=t_eval
        )
        return sol

# --------------------------------- Testing -----------------------------------------
# model_args = {
#     'name': 'Intravenous Bolus Dosing',
#     'num_comp': 2,
#     'dose_type': 'IV',
#     'Q_p1': 1.0,
#     'V_c': 1.0,
#     'V_p1': 1.0,
#     'CL': 1.0,
#     'X': 1.0,
#     'num_steps': 1000,
#     'endpoint': 1,
#     'y': [0, 0]  # Initial conditions for central and peripheral compartments
# }

# Model1 = Model(model_args)
# res = Model1.solve(t=0)

# # Plotting
# print(Model1.name)
# print(np.shape(res.y))
# print(res.y)

# plt.plot(res.t, res.y[0], label='qc')
# if Model1.num_comp > 1:
#     plt.plot(res.t, res.y[1], label='qp1')
    
# plt.xlabel('Time (hours)')
# plt.ylabel('Drug Quantity (ng)')
# plt.legend()
# plt.show()
