from pysb.integrate import odesolve
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from model_pcb_production import model
import seaborn
import matplotlib.ticker as ticker

def fig1(t,numofint):

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
    Heme_0 = np.linspace(0,100,numofint)
    HO1_0 = 10
    Fd_0 = 5
    Fde_0 = Fd_0
    PcyA_0 = 10
    k13 = np.linspace(k13,1e-3,numofint)#0.1/5
    # param = np.array([k1, k2, k3, k4, k5, k6, k7, k8, k9, k10, k11, kdegpcb, Heme_0, HO1_0, Fd_0, PcyA_0, 1])


    saved_res = np.zeros([numofint,numofint])
    for i0 in range(0,numofint):
        for i1 in range(0,numofint):
            temp = np.array([k1, k2, k3, k4, k5, k6, k7, k8, k9, k10, k11, k12,k13[i0], kdegpcb, Heme_0[i1], HO1_0, Fd_0, PcyA_0, 1])
            x=odesolve(model,t,temp)
            saved_res[i0,i1]=x['__s13'][-1]
    saved_res = np.asarray(saved_res)

    # Display image
    # Y FD, X Heme
    x=k13
    y=Heme_0
    f, ax = plt.subplots(figsize=(20,20))
    plt.rc('font', family='arial')

    seaborn.heatmap(saved_res,linewidths=.25,cmap='jet',ax=ax)
    plt.locator_params(axis='both',tight=True, nbins=10)
    plt.xticks(np.arange(40),['%.2f'%i for i in x], rotation=45, fontsize=16)

    plt.yticks(np.arange(40),['%.0f'%i for i in y], rotation=45, fontsize=16)
    plt.ylabel('Heme Concentration (RU) ', fontsize=28)
    plt.xlabel('NADP/NADPH Activity (or Fd_red renewal), k13 ', fontsize=28)

    plt.show()

def main():
    t = np.linspace(0,100,100)
    fig1(t,40)

main()
