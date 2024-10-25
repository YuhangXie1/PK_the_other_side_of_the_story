# PK_the_other_side_of_the_story

This is a pharmokinetic model which provides a line graph visualisation of the quantity of a drug within a body "compartment".
It uses a first order differential equation to model the quantity of drug in the central compartment. Additional compartments, called 'peripheral' compartments, can be also be specified in the input for the model.

To use the program, each parameter for the model can be specified within a yaml config file.
These include:

\begin{itemize}
    \item \( \text{name} \): the name of the model - e.g., one-compartment model (1 central, 0 peripheral)
    \item \( \text{num\_comp} \): the number of the total compartments to model (1 or 2 for the current version)
    \item \( \text{dose\_type} \): the type of dose administration (IV or SC)
    \item \( y \) [ng]: the initial quantity of drugs in central & peripheral compartments
    \item \( Q_{p1} \) [ng]: drug quantity in peripheral compartment (0 for one-compartment model)
    \item \( V_c \) [mL]: the volume of the central compartment
    \item \( V_{p1} \) [mL]: the volume of the first peripheral compartment (0 for one-compartment model)
    \item \( CL \) [mL/h]: the clearance from the central compartment
    \item \( X \) [ng/h]: the rate at which the drugs are administered into the central compartment
    \item \( \text{num\_steps} \): the number of steps in the simulation (time)
    \item \( \text{endpoint} \) [h]: hours after the start time of the injection
    \item \( k_a \) [1/h]: For SC (dose_type): the absorption rate constant
    \item \( q \) [ng]: For SC (dose_type): the quantity of the drug administered
\end{itemize}

To run the package, please revise the input.yaml file to provide the input, and run the the __main__.py file in Python3. This should give you a set of values and a graph depicting the results.
