#
# Model class
#
import numpy as np
import scipy.integrate

def dose(t, X):
    return X

def rhs(t, y, Q_p1, V_c, V_p1, CL, X):
    """
    Creates the Right-Hand-Side function, rhs, of the ODE specifying the quantity of drugs in the central and periferal compartments. 

    Args:
        param1: t [h], duration for which the drug is administered.
        param2: y [ng], initial quantity of drugs in central and periferal compartments.
        param3: Q_p1 [ng], drug quantity in periferal compartment
        param4: V_c [ml], volume central compartment.
        param5: V_p1 [ml], volume periferal compartment.
        param6: CL [ml/h], clearance rate from central compartment.
        param6: X [ng/h], rate at which the drugs are administered into the central compartment.

    Returns:
        A list containing the rhs of the change in qc (drug quantity in central channel [ng]) and qp1 over time.

    Raises:
        KeyError: Raises an exception if input for parameters 2-6 is not an int or float type.
    """
    if  y or Q_p1 or V_c or V_p1 or CL or X != isinstance((int, float)):
        raise Exception(f"Invalid input.")
    
    q_c, q_p1 = y
    transition = Q_p1 * (q_c / V_c - q_p1 / V_p1)
    dqc_dt = dose(t, X) - q_c / V_c * CL - transition
    dqp1_dt = transition
    return [dqc_dt, dqp1_dt]

class Model:
    """A Pharmokinetic (PK) model

    Parameters
    ----------

    value: numeric, optional
        an example paramter

    """
    def __init__(self, num_compartments = 1, dosing_type = 'IV', protocol = None):
        self.num_compartments = num_compartments
        self.dosing_type = dosing_type
        self.protocol = protocol

    def ode_system(self, y, t, params):
        # Example: y[0] is the central compartment, y[1]..y[n] are peripheral
        # Modify ODEs depending on the number of compartments
        # unpack params
        # dydt
        # central compartment ODEs dydt[0] = #elimination from central compartment
        # peripheral compartment ODEs
            # if num_compartments > 1
                #dydt[1] = exchange with central compartment

        #return dydt
        pass
    
    def zero_comp(self, t, params):
        # initial conditions
        # y[0] = np.zeros(self.num_compartments + 1)
        # A vector of zeros representing the initial concentration of drug in all compartments
        # unpack arguments of params dict and store in args list.
        # Handle dosing type and protocol
        # if protocol is provided initial conc is set to dose provided
        # if self.protocol:
        #     y0[0] = self.protocol.dose  # Initial dose in central compartment
        
        # # Solve the system of ODEs
        # solution = odeint(self.system_of_odes, y0, t, args=(params,))
        # return solution

        args = [
            params['Q_p1'], params['V_c'], params['V_p1'], params['CL'], params['X']
            ]
        # unpack timepoints for which to evaluate the function.
        step_size, end_point = params['step_size'], params['end_point']
        t_eval = np.linspace(0, step_size, end_point)
        # solve the ODE for the given parameters.
        sol = scipy.integrate.solve_ivp(
        fun=lambda t, y: rhs(t, y, *args),
        t_span=[t_eval[0], t_eval[-1]],
        y0=params['y0'], t_eval=t_eval
        )
        return sol
    
    def one_comp(self, params):
            return

