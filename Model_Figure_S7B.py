from pysb.integrate import odesolve
import numpy as np
import matplotlib.pyplot as plt
from model_pcb_production import model
import seaborn
from mpl_toolkits.mplot3d import Axes3D

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
    Heme_0 = np.linspace(2,100,numofint)
    HO1_0 = 10
    Fd_0 = np.linspace(0,5,numofint)
    Fde_0 = Fd_0
    PcyA_0 = 10




    saved_res = np.zeros([numofint,numofint])
    for i0 in range(0,numofint): #y
        for i1 in range(0,numofint): #x
            temp = np.array([k1, k2, k3, k4, k5, k6, k7, k8, k9, k10, k11, k12, k13, kdegpcb,Heme_0[i0], HO1_0, Fd_0[i1], PcyA_0, 1])
            x=odesolve(model,t,temp)
            saved_res[i0,i1]=x['__s11'][-1]
    saved_res = np.asarray(saved_res)

    # Display image
    # Y FD, X Heme
    x= Fd_0
    y= Heme_0
    fig = plt.figure(figsize=(20,20))
    plt.rc('font', family='arial')
    #
    ax = Axes3D(fig)
    #
    X, Y = np.meshgrid(x,y)
    Z = saved_res

    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='jet')

    ax.set_xlabel('Initial Fd concentration (RU) ', fontsize=18)
    ax.set_ylabel('Initial Heme concentration(RU)', fontsize=18)
    ax.set_zlabel('Final PCB concentration(RU)', fontsize=18)

    #
    plt.show()

def main():
    t = np.linspace(0,80,100)
    fig1(t,50)

main()
