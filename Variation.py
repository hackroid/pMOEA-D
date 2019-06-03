import numpy

ita = 20


# 输入需要交叉互换的p1和p2
def CrossOver(p1, p2, N):
    chil1 = numpy.zeros(N)
    chil2 = numpy.zeros(N)
    for i in range(N):
        u = numpy.random.rand()
        if u <= 0.5:
            beta = (2 * u) ** (1 / (ita + 1))
        else:
            beta = (2 * (1 - u)) ** (-1 / (ita + 1))
        chil1[i] = 0.5 * ((1 + beta) * p1[i] + (1 - beta) * p2[i])
        chil2[i] = 0.5 * ((1 + beta) * p1[i] + (1 - beta) * p2[i])
    low = numpy.zeros(N)
    up = numpy.ones(N)
    return mutPolynomialBounded(chil1, 1, low, up, 0.5)


def mutPolynomialBounded(individual, eta, low, up, indpb):
    """Polynomial mutation as implemented in original NSGA-II algorithm in
    C by Deb.
    :param individual: :term:`Sequence <sequence>` individual to be mutated.
    :param eta: Crowding degree of the mutation. A high eta will produce
                a mutant resembling its parent, while a small eta will
                produce a solution much more different.
    :param low: A value or a :term:`python:sequence` of values that
                is the lower bound of the search space.
    :param up: A value or a :term:`python:sequence` of values that
               is the upper bound of the search space.
    :returns: A tuple of one individual.
    """
    size = len(individual)
    for i, xl, xu in zip(range(size), low, up):
        if numpy.random.rand() <= indpb:
            x = individual[i]
            delta_1 = (x - xl) / (xu - xl)
            delta_2 = (xu - x) / (xu - xl)
            rand = numpy.random.rand()
            mut_pow = 1.0 / (eta + 1.)

            if rand < 0.5:
                xy = 1.0 - delta_1
                val = 2.0 * rand + (1.0 - 2.0 * rand) * xy ** (eta + 1)
                delta_q = val ** mut_pow - 1.0
            else:
                xy = 1.0 - delta_2
                val = 2.0 * (1.0 - rand) + 2.0 * (rand - 0.5) * xy ** (eta + 1)
                delta_q = 1.0 - val ** mut_pow

            x = x + delta_q * (xu - xl)
            x = min(max(x, xl), xu)
            individual[i] = x
    for i in range(size):
        if individual[i] > 0.5:
            individual[i] = 1
        else:
            individual[i] = 0
    return individual

if __name__ == '__main__':
    p = CrossOver([1,0,1,1,1,0], [0,0,0,1,0,1], 6)

    print(p)
