##Multiple Qbits simulation

from qiskit import QuantumCircuit, execute, Aer, assemble
from qiskit.visualization import plot_histogram

qc3 = QuantumCircuit(2)
qc3.h(0)
qc3.x(1)

#backend qui permet de faire des opérateurs produits tensoriels
usim = Aer.get_backend('unitary_simulator')

qobj3 = assemble(qc3)
unitary = usim.run(qobj3).result().get_unitary()

#sur textbook
from qiskit_textbook.tools import array_to_latex
array_to_latex(unitary, pretext="\\text{Circuit = }\n") #affiche la matrice résultat (4*4)