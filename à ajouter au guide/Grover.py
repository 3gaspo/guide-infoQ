# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 22:38:16 2021

@author: Gaspard
"""

##Grover pour n = 3
from qiskit import QuantumCircuit, execute, Aer
n = 3

##Construction de Psi

qcp = QuantumCircuit(3,1)
for k in range(n):
    qcp.h(k)

#Construction de V

qcv = QuantumCircuit(5,5)
qcv.initialize([1,0],4)
qcv.x(0)
qcv.x(2)
qcv.barrier()
qcv.ccx(0,1,4)
qcv.ccx(4,2,3)
qcv.barrier()
qcv.x(0)
qcv.x(2)

#Construction de W

qcw = QuantumCircuit(3,1)
for i in range(3):
    qcw.h(i)
    qcw.x(i)
qcw.barrier()



qcw.barrier()
for i in range(3):
    qcw.h(i)
    qcw.x(i)
qcw.barrier()