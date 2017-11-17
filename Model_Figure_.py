from model_pcb_production import model
from pysb.integrate import odesolve
import numpy as np
import matplotlib.pyplot as plt


def pltmydata(t):
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
    # Heme_0 = 100
    HO1_0 = 10
    Fd_0 = 5
    Fde_0 = Fd_0
    PcyA_0 = 10

    Heme_0 = [100, 10, 1, 0.1, 0.01]
    param = []

    plt.rc('font', family='arial')
    for i0 in range (0,5):
        temp = np.array([k1, k2, k3, k4, k5, k6, k7, k8, k9, k10, k11, k12,k13, kdegpcb, Heme_0[i0], HO1_0, Fd_0, PcyA_0, 1])
        param.append(temp)
    param = np.asarray(param)

    fig = plt.figure(figsize=(12, 16))
    ax = fig.add_subplot(1,1,1)


    x=odesolve(model,t,param[0,:])
    ax.plot(t,x['__s13'], color='k', marker='o', ls='solid', fillstyle='full', markersize=15, markerfacecolor='0.5', markevery=5, markeredgewidth=2, linewidth=2.0, label='[Heme]=100c')

    x=odesolve(model,t,param[1,:])
    ax.plot(t,x['__s13'], color='k', marker='v', ls='solid', fillstyle='full', markersize=15, markerfacecolor='white', markevery=4,markeredgewidth=2, linewidth=2.0, label='[Heme]=10.0c')

    x=odesolve(model,t,param[2,:])
    ax.plot(t,x['__s13'], color='k', marker='^', ls='solid', fillstyle='full', markersize=15, markerfacecolor='0.3', markevery=5,markeredgewidth=2, linewidth=2.0, label='[Heme]=5.0c')

    x=odesolve(model,t,param[3,:])
    ax.plot(t,x['__s13'], color='k', marker='x', ls='solid', fillstyle='full', markersize=15, markerfacecolor='black', markevery=5,markeredgewidth=2, linewidth=2.0, label='[Heme]=1.0c')

    x=odesolve(model,t,param[4,:])
    ax.plot(t,x['__s13'], color='k', marker='d', ls='solid', fillstyle='full', markersize=15, markerfacecolor='black', markevery=5,markeredgewidth=2, linewidth=2.0, label='[Heme]=0.01c')

    ax.set_xlabel('Time (h)', fontsize=28, fontweight='bold', labelpad=5)
    ax.set_ylabel('PCB concentration (RU)', fontsize=28, fontweight='bold', labelpad=5)
    ax.tick_params(axis='both', labelsize=28, pad=5)
    ax.tick_params(width=3, length=20)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    for axis in ['bottom', 'left']:
        ax.spines[axis].set_linewidth(8)
    plt.yticks(np.arange(0.0, 4, 1.), fontweight='bold')
    plt.xticks(np.arange(0, 100, 20), fontweight='bold')

    plt.legend(fontsize=28, loc=1)
    plt.show()

def main():
    t = np.linspace(0,100,100)
    pltmydata(t)
    plt.show()


main()
