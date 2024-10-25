# PK_the_other_side_of_the_story

This is a pharmacokinetic model that provides a line graph visualization of the quantity of a drug within a body "compartment." It uses a first-order differential equation to model the quantity of drug in the central compartment. Additional compartments, called 'peripheral' compartments, can also be specified in the input for the model.

## Usage

To use the program, each parameter for the model can be specified within a YAML config file. These include:

- **name**: the name of the model - e.g., one-compartment model (1 central, 0 peripheral)
- **num_comp**: the number of the total compartments to model (1 or 2 for the current version)
- **dose_type**: the type of dose administration (IV or SC)
- **$y$** [ng]: the initial quantity of drugs in central & peripheral compartments
- **$Q_{p1}$** [ng]: drug quantity in the peripheral compartment (0 for one-compartment model)
- **$V_c$** [mL]: the volume of the central compartment
- **$V_{p1}$** [mL]: the volume of the first peripheral compartment (0 for one-compartment model)
- **$CL$** [mL/h]: the clearance from the central compartment
- **$X$** [ng/h]: the rate at which the drugs are administered into the central compartment
- **$num$_$steps$**: the number of steps in the simulation (time)
- **$endpoint$** [h]: hours after the start time of the injection
- **$k_a$** [1/h]: For SC (dose_type): the absorption rate constant
- **$q$** [ng]: For SC (dose_type): the quantity of the drug administered

The equation of the model is as follow:
- $\frac{dq_{c}}{dt} = Dose(t) - q_{c}/V_{c}CL - Q_{p1}(\frac{q_{c}/V_{c}} - \frac{q_{p1}}{V_{p1}}$
- $\frac{dq_{p1}}{dt} = Q_{p1}(\frac{q_{c}{V_{c}}} - \frac{q_{p1}{V_{p1}}})$



To run the package, please revise the `input.yaml` file to provide the input, and run the `main.py` file in Python3. This should give you a set of values and a graph depicting the results.
