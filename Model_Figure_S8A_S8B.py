# Marianne Catanho, UCSD mcatanho@ucsd.edu
# March 20, 2017

from pysb.integrate import odesolve
import numpy
import matplotlib.pyplot as plt
from model_pcb_production import model


def fig1(t,numofint):
    # DECREASING BINDING HO-1/PCYA/FD showing species (k3,k9)
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
    Heme_0 = 100
    HO1_0 = 10
    Fd_0 = 5
    Fde_0 = Fd_0
    PcyA_0 = 10

    # param = numpy.array([k1, k2, k3, k4, k5, k6, k7, k8, k9, k10, k11,  kdegpcb, Heme_0, HO1_0, Fd_0, PcyA_0, 1])

    k3 = numpy.linspace(k3, 1e-3, numofint)
    k9 = numpy.linspace(k9, 1e-3, numofint)

    fig = plt.figure(figsize=(25,15))
    ax = fig.add_subplot(1, 1, 1)
    plt.rc('font', family='arial')



    param = []
    for i0 in range(0, numofint):
        temp = numpy.array([k1, k2, k3[i0], k4, k5, k6, k7, k8, k9[i0], k10, k11, k12, k13, kdegpcb, Heme_0, HO1_0, Fd_0, PcyA_0, 1])

        param.append(temp)
    param = numpy.asarray(param)

    print param.shape
    for i in param:
        x = odesolve(model, t, i)
        ax.plot(t, x['__s13'], color='red', marker='o', ls='solid', fillstyle='full', markersize=15,
                markerfacecolor='red',
                markevery=5, markeredgewidth=2, linewidth=2.0, label='Reduced & Oxidized')

    x = odesolve(model, t, param[0])
    # ax.plot(t, x['__s13'], color='blue', marker='^', ls='solid', fillstyle='full', markersize=15,
    #         markerfacecolor='blue',
    #         markevery=5, markeredgewidth=2, linewidth=2.0, label='Reduced & Oxidized')


    ax.set_xlabel('Time (h)', fontsize=28, fontweight='bold', labelpad=5)
    ax.set_ylabel('PCB concentration (RU)', fontsize=28, fontweight='bold', labelpad=5)
    ax.tick_params(axis='both', labelsize=20, pad=5)

    ax.tick_params(width=3, length=20)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    for axis in ['bottom', 'left']:
        ax.spines[axis].set_linewidth(8)
    plt.yticks(numpy.arange(0, 3, 1.), fontweight='bold')
    plt.xticks(numpy.arange(0, 80.5, 20), fontweight='bold')


    plt.show()
    plt.show()

def fig2(t):
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
    Heme_0 = 100
    HO1_0 = 10
    Fd_0 = 5
    Fde_0 = Fd_0
    PcyA_0 = 10

    # param = numpy.array([k1, k2, k3, k4, k5, k6, k7, k8, k9, k10, k11, kdegpcb, Heme_0, HO1_0, Fd_0, PcyA_0, 1])

    fig = plt.figure(figsize=(25,15))
    ax = fig.add_subplot(1, 1, 1)
    plt.rc('font', family='arial')

    param = numpy.array([k1, k2, k3, k4, k5, k6, k7, k8, k9, k10, k11, k12, k13, kdegpcb, Heme_0, HO1_0, Fd_0, PcyA_0, 1])
    x=odesolve(model,t,param)
    ax.plot(t, x['__s13'], color='red', marker='o', ls='solid', fillstyle='full', markersize=15, markerfacecolor='red',
            markevery=5, markeredgewidth=2, linewidth=2.0, label='')

    ax.set_xlabel('Time (h)', fontsize=28, fontweight='bold', labelpad=5)
    ax.set_ylabel('PCB concentration (RU)', fontsize=28, fontweight='bold', labelpad=5)
    ax.tick_params(axis='both', labelsize=20, pad=5)

    ax.tick_params(width=3, length=20)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    for axis in ['bottom', 'left']:
        ax.spines[axis].set_linewidth(8)
    plt.yticks(numpy.arange(0.9, 3, 1.), fontweight='bold')
    plt.xticks(numpy.arange(0, 80.5, 20), fontweight='bold')

    plt.show()


def fig3(t,numofint):
    # DECREASING RENEWAL FD:FNR RATE  (k13)
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
    kdegpcb = 1.87e-1
    # Initial Conditions
    Heme_0 = 100
    HO1_0 = 10
    Fd_0 = 5
    Fde_0 = Fd_0
    PcyA_0 = 10

    param = []
    k13 = numpy.linspace(k13, 1e-3, numofint)
    for i0 in range(0,numofint):
        temp = numpy.array([k1, k2, k3, k4, k5, k6, k7, k8, k9, k10, k11, k12, k13[i0], kdegpcb, Heme_0, HO1_0, Fd_0, PcyA_0, 1])

        param.append(temp)
    param = numpy.asarray(param)

    plt.rc('font', family='arial')
    fig = plt.figure(figsize=(25,15))
    ax = fig.add_subplot(1, 1, 1)

    for i in param:
        x=odesolve(model,t,i)

        ax.plot(t, x['__s13'], color='red', marker='o', ls='solid', fillstyle='full', markersize=15, markerfacecolor='red',
            markevery=5, markeredgewidth=2, linewidth=2.0, label='')

    ax.set_xlabel('Time (h)', fontsize=28, fontweight='bold',labelpad=5)
    ax.set_ylabel('PCB concentration (RU)', fontsize=28, fontweight='bold',labelpad=5)
    ax.tick_params(axis='both', labelsize=28, pad=5)
    ax.tick_params(width=3,length=20)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    for axis in ['bottom','left']:
        ax.spines[axis].set_linewidth(8)
    plt.yticks(numpy.arange(0,3.1,1.0), fontweight='bold')
    plt.xticks(numpy.arange(0,80.5,20),fontweight='bold')

    plt.show()


def fig4(t):
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
    Heme_0 = 100
    HO1_0 = 10
    Fd_0 = 5
    Fde_0 = Fd_0
    PcyA_0 = 10

    param4E = numpy.array([k1, k2, k3, k4, k5, k6, k7, k8, k9, k10, k11, k12, k13, kdegpcb, Heme_0, HO1_0, Fd_0, PcyA_0, 1])

    plt.rc('font', family='arial')
    fig = plt.figure(figsize=(25,15))
    ax = fig.add_subplot(1, 1, 1)
    #plt.rc('font', family='arial')

    x4E=odesolve(model,t,param4E)

    ax.plot(t, x4E['__s13'], color='red', marker='o', ls='solid', fillstyle='full', markersize=15, markerfacecolor='red',
            markevery=5, markeredgewidth=2, linewidth=2.0, label='4E')

# 2E
    param2E = numpy.array([k1, k2, k3, k4, k5, k6, k7, k8, k9, k10, k11, k12, k13, kdegpcb, Heme_0, HO1_0, 0, PcyA_0, 1])

    x=odesolve(model,t,param2E)

    ax.plot(t, x['__s13'], color='blue', marker='v', ls='solid', fillstyle='full', markersize=15, markerfacecolor='blue',
            markevery=5, markeredgewidth=2, linewidth=2.0, label='2E')

    ax.set_xlabel('Time (h)', fontsize=28, fontweight='bold',labelpad=5)
    ax.set_ylabel('PCB concentration (RU)', fontsize=28, fontweight='bold',labelpad=5)
    ax.tick_params(axis='both', labelsize=28, pad=5)
    plt.legend(fontsize=28, loc=5)
    ax.tick_params(width=3,length=20)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    for axis in ['bottom','left']:
        ax.spines[axis].set_linewidth(8)
    plt.yticks(numpy.arange(0.,3.1,1.0), fontweight='bold')
    plt.xticks(numpy.arange(0,80.5,20),fontweight='bold')

    plt.show()


def main():
    t = numpy.linspace(0,100,100)
    # SPECIES SPECIFICITY
    fig1(t,40)
    #
    # # NORMAL MODEL
    # fig2(t)

    # DECREASING RENEWAL FD:FNR RATE
    fig3(t,40)

    # # 2E vs 4E
    # fig4(t)

main()

