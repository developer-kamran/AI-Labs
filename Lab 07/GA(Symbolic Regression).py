# Install DEAP if not already installed
# !pip install deap

import operator
import math
import random
import numpy as np
from deap import base, creator, gp, tools, algorithms

# Define a set of operators and terminals (Primitive Set)
pset = gp.PrimitiveSet("MAIN", 1)  # 1 input variable (X)

# Adding basic operators
pset.addPrimitive(operator.add, 2)    # +
pset.addPrimitive(operator.sub, 2)    # -
pset.addPrimitive(operator.mul, 2)    # *
pset.addPrimitive(operator.neg, 1)    # negation (unary -)

# Add ephemeral constant (random constants)
pset.addEphemeralConstant("rand101", lambda: random.randint(-1, 1))

# Rename the argument for clarity
pset.renameArguments(ARG0='x')

# Define Fitness and Individual
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))  # Minimize error
creator.create("Individual", gp.PrimitiveTree, fitness=creator.FitnessMin)

# Toolbox setup
toolbox = base.Toolbox()
toolbox.register("expr", gp.genHalfAndHalf, pset=pset, min_=1, max_=3)
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.expr)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

# Define evaluation function
def eval_symb_reg(individual):
    func = toolbox.compile(expr=individual)
    
    # Training points
    X = np.linspace(-10, 10, 50)
    Y_true = 5*X**3 - 6*X**2 + 8*X - 1  # Slightly rearranged to equal zero
    
    # Compute predicted Y
    Y_pred = np.array([func(x) for x in X])
    
    # Compute RMSE
    rmse = np.sqrt(np.mean((Y_true - Y_pred)**2))
    return (rmse,)

toolbox.register("compile", gp.compile, pset=pset)
toolbox.register("evaluate", eval_symb_reg)
toolbox.register("select", tools.selTournament, tournsize=3)
toolbox.register("mate", gp.cxOnePoint)
toolbox.register("expr_mut", gp.genFull, min_=0, max_=2)
toolbox.register("mutate", gp.mutUniform, expr=toolbox.expr_mut, pset=pset)

# Decorate (limit height of trees to avoid bloat)
toolbox.decorate("mate", gp.staticLimit(key=operator.attrgetter("height"), max_value=17))
toolbox.decorate("mutate", gp.staticLimit(key=operator.attrgetter("height"), max_value=17))

# Genetic Algorithm parameters
def main():
    random.seed(42)
    
    pop = toolbox.population(n=300)
    hof = tools.HallOfFame(1)  # Best individual
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", np.mean)
    stats.register("std", np.std)
    stats.register("min", np.min)
    stats.register("max", np.max)
    
    print("Starting Evolution...")

    pop, log = algorithms.eaSimple(pop, toolbox,
                                    cxpb=0.5, mutpb=0.2,
                                    ngen=40,
                                    stats=stats, halloffame=hof,
                                    verbose=True)

    print("\nBest individual:")
    print(hof[0])
    print("\nFitness (RMSE):", hof[0].fitness.values[0])

if __name__ == "__main__":
    main()
