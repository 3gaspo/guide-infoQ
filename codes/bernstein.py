# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 16:15:46 2021

@author: Gaspard
"""

from qiskit import QuantumCircuit, execute, Aer

def fonction_bernstein(a):
    '''
    Code un circuit qui correspond à fa
    on suppose que a est donné sous la forme d'une chaine de caractère en binaire
    '''
    
    n = len(a)
    qc = QuantumCircuit(n+1,n)
    
    for k in range(n):
        if int(a[k])==1:
            qc.cx(k+1,0)
    
    return qc,n


def Bernstein(a):
    '''
    Code le circuit de Bernstein Varizani
    '''
    qcf,n = fonction_bernstein(a)
    
    qc = QuantumCircuit(n+1,n)
    qc.initialize([0,1],0)
    qc.barrier()
    
    for k in range(n+1):
        qc.h(k)
    qc.barrier()
    
    qcc = qc+qcf
    qcc.barrier()
    
    for k in range(n+1):
        qcc.h(k)
    qcc.barrier()
    
    for k in range(n+1,1,-1):
        qcc.measure(k-1,k-2)
        
    return qcc

def resultat_bernstein(a):
    '''
    Renvoie le résultat de l'algorithme de Bernstein Varizani'

    '''
    
    qc = Bernstein(a)
    backend = Aer.get_backend('qasm_simulator')
    counts = execute(qc,backend).result().get_counts()
    
    for a in counts.keys():
        return(a)