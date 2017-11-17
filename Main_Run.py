from model_pcb_production import model
from pysb.integrate import odesolve
import numpy as np
import matplotlib.pyplot as plt
#============================================================================================#
def bio_pcb(t):
    x0,a,b,c = [ 3.9401215, 0.93001123, 0.46248589, 0.17678898]
    vx0, va, vb, vc = [2.39823423e+06,3.94074420e+05,1.95969480e+05,7.16685525e-03]
    ra = np.random.normal(a, 0.01, 1)
    rb = np.random.normal(b, 0.01, 1)
    rc = np.random.normal(c, 0.01, 1)
    rx0 = np.random.normal(x0, 0.01, 1)
    print(ra,rb,rc,rx0)
    y = ra / (rb + np.exp(-rc * (t - rx0)))
    return y
#============================================================================================#
def Biodata(t):
    y1 = bio_pcb(t)
    y2 = bio_pcb(t)
    y3= bio_pcb(t)
    y4 = bio_pcb(t)

    ymean = y1#np.mean([y1,y2,y3,y4],0)
    yvar = np.std([y1,y2,y3,y4],0)
    return y1,y2,y3,y4,ymean, yvar
#============================================================================================#
k1 = 1.228e-01
k2 = 1e-12
k3 = 5.68750000e-01
k4 = 1e-12
k5 = 2.22857143e-01
k6 = 4.75000000e-01
k7 = 1.82500000e-01
k8 = 1e-12
k9 = 2.5000000e-01
k10 = 1e-12
k11 = 0.122
k12 = 0.2667
k13 = 0.225
kdegpcb = 0.1567
# Initial Conditions
Heme_0 = 10
HO1_0 = 10
Fd_0 = 5
Fde_0 = Fd_0
PcyA_0 = 10

param = np.array([k1, k2, k3, k4, k5, k6, k7, k8, k9, k10, k11, k12,k13, kdegpcb,Heme_0, HO1_0, Fd_0, PcyA_0, 1])
print(param.shape)
t = np.linspace(200, 1000, 1000)
y1s, y2s, y3s, y4s, ymean, yvar = Biodata(t)
ystd=np.sqrt(yvar)
x=odesolve(model,t,param)
soln = x['__s13']
print x['__s3']

plt.plot(t,soln, label='PCB')
#
# plt.plot(t,x['__s0'], label='Heme')
# plt.plot(t,x['__s1'], label='HO1')
# plt.plot(t,x['__s2'], label='Fd-A')
# plt.plot(t,x['__s3'], label='Fd-I')
# plt.plot(t,x['__s4'], label='PcyA')
# plt.plot(t,x['__s8'], label='Bv')
#

plt.plot(t, ymean, 'k', color='#CC4F1B', label='Synt. PCB')
plt.fill_between(t, ymean-ystd, ymean+ystd, alpha=0.5, edgecolor='#CC4F1B', facecolor='#FF9848')
plt.legend()
# Calculate Error
cte = (0.5) * (1 / ystd[4] ** 2)

error1 = np.sum([(soln - y1s) ** 2])
error2 = np.sum([(soln - y2s) ** 2])
error3 = np.sum([(soln - y3s) ** 2])
error4 = np.sum([(soln - y2s) ** 2])
error = np.sum([error1,error2,error3,error4],0)*cte
print error

plt.ylabel('PCB concentration')
plt.xlabel('time (h)')
plt.title('Concentration of Endogenous PCB with time (Weber et al)')
plt.show()


