# Model description and reactions
# Marianne Catanho, UCSD mcatanho@ucsd.edu
# March 20, 2017

from pysb import *
from pysb.macros import *
from pysb.bng import generate_equations

# Model Generation
Model()

Parameter('k1', 0)
Parameter('k2', 0)
Parameter('k3', 0)
Parameter('k4', 0)
Parameter('k5', 0)
Parameter('k6', 0)
Parameter('k7', 0)
Parameter('k8', 0)
Parameter('k9', 0)
Parameter('k10', 0)
Parameter('k11', 0)
Parameter('k12', 0)
Parameter('k13', 0)
Parameter('k14', 0)

Monomer('Hem', ['S','b1'], {'S': ['Heme', 'Bv', 'PCB']})
Monomer('HO1', ['b1'])
Monomer('Fd', ['S', 'b1','b2'], {'S': ['A', 'I']}) # Active refers to Fd-, Inactive to Fd+
Monomer('PcyA', ['b1'])

Parameter('hem', 1)
Parameter('ho1', 1)
Parameter('fd',  1)
Parameter('pcya', 1)

Initial(Hem(S='Heme',b1=None), hem)
Initial(HO1(b1=None), ho1)
Initial(Fd(S='A', b1=None, b2=None), fd)
Initial(Fd(S='I', b1=None, b2=None), fd)
Initial(PcyA(b1=None), pcya)

# Produce Bv
Rule('R1', Hem(S='Heme', b1=None) + HO1(b1=None)  <> Hem(S='Heme', b1=1) % HO1(b1=1) , k1, k2)
Rule('R2', Hem(S='Heme', b1=1) % HO1(b1=1) + Fd(S='A', b1=None, b2=None) <> Fd(S='A', b1=1, b2=2) % Hem(S='Heme', b1=1) % HO1(b1=2), k3,k4)
Rule('R3', Fd(S='A', b1=1, b2=2) % Hem(S='Heme', b1=1) % HO1(b1=2) >> Hem(S='Bv', b1=1)%HO1(b1=1) +  Fd(S='I', b1=None, b2=None),  k5)
Rule('R32', Hem(S='Bv', b1=1)%HO1(b1=1) >> Hem(S='Bv', b1=None) + HO1(b1=None) ,  k6)
# Recycle HO1
Rule('R4', Hem(S='Bv', b1=None) +  PcyA(b1=None) <> Hem(S='Bv', b1=1) % PcyA(b1=1), k7,k8)
Rule('R5', Fd(S='A', b1=None, b2=None) + Hem(S='Bv', b1=1) % PcyA(b1=1) <> Fd(S='A', b1=1, b2=2) % Hem(S='Bv', b1=1) % PcyA(b1=2), k9,k10)
Rule('R6', Fd(S='A', b1=1, b2=2) % Hem(S='Bv', b1=1) % PcyA(b1=2) >> Hem(S='PCB', b1=1)%PcyA(b1=1) +  Fd(S='I', b1=None, b2=None) , k11)
Rule('R62', Hem(S='PCB', b1=1) % PcyA(b1=1) >> Hem(S='PCB', b1=None) +  PcyA(b1=None), k12)
Rule('R7', Fd(S='I', b1=None)  >>  Fd(S='A', b1=None), k13)
# Degradation
degrade(Hem(S='PCB', b1=None), k14)

#
generate_equations(model)
for i,ode in enumerate(model.odes):
    print i, model.species[i],":",ode


Observable('obsHeme', Hem(S='Heme',b1=None))
Observable('obsHO1', HO1(b1=None))
Observable('obsBv', Hem(S='Bv', b1=None))
Observable('obsPcyA', PcyA(b1=None))
Observable('obsFda', Fd(S='A', b1=None, b2=None))
Observable('obsFdi', Fd(S='I', b1=None, b2=None))
Observable('obsPCB', Hem(S='PCB', b1=None))

print model.parameters
