# PK_the_other_side_of_the_story

This is a pharmokinetic model which provides a line graph visualisation of the quantity of a drug within a body "compartment".
It uses a first order differential equation to model the quantity of drug in the central compartment. Additional compartments, called 'peripheral' compartments, can be also be specified in the input for the model.

To use the program, each parameter for the model can be specified within a yaml config file.
These include:


Vc​ [mL], the volume of the central compartment

Vp1Vp1​ [mL], the volume of the first peripheral compartment

Vp1Vp1​ [mL], the volume of the peripheral compartment 1

CLCL [mL/h], the clearance/elimination rate from the central compartment

Qp1Qp1​ [mL/h], the transition rate between central compartment and peripheral compartment 1