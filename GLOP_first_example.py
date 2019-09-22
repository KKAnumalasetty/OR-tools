# -*- coding: utf-8 -*-
"""
GLOP
@author: Lalith
"""

from ortools.linear_solver import pywraplp

def LinearProgrammingExample():
    
    # Instantiate a Glop solver
    solver = pywraplp.Solver('LinearProgrammingExample',
                             pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)
    
    # Creating 2 variables; They are unconstrained
    x = solver.NumVar(-solver.infinity(), solver.infinity(), 'x')
    y = solver.NumVar(-solver.infinity(), solver.infinity(), 'y')
     
    # Constraint 0: x + 2y <= 14.
    constraint0 = solver.Constraint(-solver.infinity(), 14)
    constraint0.SetCoefficient(x, 1)
    constraint0.SetCoefficient(y, 2)
     
    # Constraint 1: 3x - y >= 0.
    constraint1 = solver.Constraint(0, solver.infinity())
    constraint1.SetCoefficient(x, 3)
    constraint1.SetCoefficient(y, -1)

    # Constraint 2: x - y <= 2.
    constraint2 = solver.Constraint(-solver.infinity(), 2)
    constraint2.SetCoefficient(x, 1)
    constraint2.SetCoefficient(y, -1)

    # Objective function: 3x + 4y.
    objective = solver.Objective()
    objective.SetCoefficient(x, 3)
    objective.SetCoefficient(y, 4)
    objective.SetMaximization()
    
    # Solve the system.
    solver.Solve()
    opt_solution = 3 * x.solution_value() + 4 * y.solution_value()
    print('Number of variables =', solver.NumVariables())
    print('Number of constraints =', solver.NumConstraints())
    # The value of each variable in the solution.
    print('Solution:')
    print('x = ', x.solution_value())
    print('y = ', y.solution_value())
    # The objective value of the solution.
    print('Optimal objective value =', opt_solution)

LinearProgrammingExample()

