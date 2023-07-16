from pysat.solvers import Solver
from pysat.formula import CNF

solvers = ['cadical103',
           'cadical153',
           'gluecard30',
           'gluecard41',
           'glucose30',
           'glucose42',
           'lingeling',
           'maplechrono',
           'maplecm',
           'maplesat']
# Note: get_proof() is unsupported in MinisatGH, Minisat22, Minicard.  

def test_get_proof():
    cnf = CNF(from_clauses=[[-1, 2], [1, -2], [-1, -2], [1, 2]])

    for name in solvers:
        print("Name = {}".format(name))
        with Solver(name=name, bootstrap_with=cnf, with_proof=True) as solver:
            assert solver.solve() == False
            p = solver.get_proof()
            print(solver.get_proof())
            #assert '2 0' in p or '-2 0' in p or '1 0' in p or '-1 0' in p
