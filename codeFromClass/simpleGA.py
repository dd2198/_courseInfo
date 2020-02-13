import random

CHROMOSOME_LENGTH = 8
POPULATION_SIZE = 8

# 1. Make one chromosome: list of 4 things with random values of 0 or 1
def chromosomeInit():
  chromosome = []
  for i in range(CHROMOSOME_LENGTH):
    chromosome.append(random.randint(0,1))
  return chromosome

# 2. Make an initial population of randomly generated chromosomes
def populationInit():
  population = []
  for i in range(POPULATION_SIZE):
    population.append(chromosomeInit())
  return population

# 3. Fitness function: 1-(length - sum of chromosome)/length 
def fitness(chromosome):

  chromosomeSum = 0
  for gene in chromosome:
    chromosomeSum += gene

  fitness = 1 - (CHROMOSOME_LENGTH - chromosomeSum)/CHROMOSOME_LENGTH

  return fitness

# 4. Get the fitness for the entire population
def populationFitness(population):
  fitnesses = []
  for chromosome in population:
    fitnesses.append(fitness(chromosome))
  return fitnesses

print(populationFitness(populationInit()))
