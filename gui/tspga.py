def init_population(pop_number, countries_pool):
    population = []
    for i in range(pop_number):
        population.append(utils.shuffled(countries_pool))
    return population

#    def create_route(countries):
#        route = random.sample(countries, len(countries))
#        return route
    
#    #https://github.com/ezstoltz/genetic-algorithm/blob/master/genetic_algorithm_TSP.ipynb
#    def rankRoutes(population, distances):
#        fitnessDict = {}
#        for i in range(0,len(population)):
#            fitnessDict[i] = fitness_fn(population[i], distances)
#        return sorted(fitnessDict.items(), key = operator.itemgetter(1), reverse = True)

def recombine(state_a, state_b):
    start = random.randint(0, len(state_a) - 1)
    end = random.randint(start + 1, len(state_a))
    new_state = state_a[start:end]
    for city in state_b:
        if city not in new_state:
            new_state.append(city)
    return new_state
#
def mutate(state, mutation_rate):
    if random.uniform(0, 1) < mutation_rate:
        sample = random.sample(range(len(state)), 2)
        state[sample[0]], state[sample[1]] = state[sample[1]], state[sample[0]]
    return state


def fitness_fn(city, distances):
    if fitness == 0:
    # create string from list of characters
        for i in range(len(distances[city])):
            if city == distances[i]:
                fitness = 1 / float(distances[city][i])
    return fitness



population = init_population(100, len(["United Kingdom", "United States", "Vietnam"]))
all_time_best = current.state
while True:
    population = [mutate(recombine(*select(2, population, fitness_fn)), self.mutation_rate.get())
                  for _ in range(len(population))]
    current_best = np.argmax(population, key=fitness_fn)
    if fitness_fn(current_best, distances) > fitness_fn(all_time_best, distances):
        all_time_best = current_best
        self.cost.set("Cost = " + str('%0.3f' % (-1 * problem.value(all_time_best))))
