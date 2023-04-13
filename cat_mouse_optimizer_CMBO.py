import random, numpy as np
import numpy

pop = 10  # population, dimension
dim = 5  # dimension,column
lb = 1  # Lower Bound
ub = 5  # Upper Bound
g, matrix = 0, 100  # initial, max. iteration


# generation of random data
def generate(pop, dim, lb, ub):
    gen_data = []
    for i in range(pop):
        tem = []
        for j in range(dim):
            tem.append(random.uniform(lb, ub))
        gen_data.append(tem)

    return gen_data


def fitness(sol):
    return random.random()


# Sort population matrix based on objective function value using Equations (3) and (4)
def sorted(soln, fit):
    sort_index, sort_soln, sort_fit = [], [], []
    s = numpy.array(fit)
    sort_index = numpy.argsort(s)
    for i in range(len(sort_index)):
        ind = sort_index[i]
        sort_fit.append(fit[ind])
        sort_soln.append(soln[ind])
    return sort_soln, sort_fit


# Select population of mice m using Equation
# Select population of cats c using Equation
def mice_cat_selection(soln, fit):
    mice, m_f, cat, c_f = [], [], [], []
    for i in range(len(soln)):
        if i < (len(soln) / 2):
            mice.append(soln[i])
            m_f.append(fit[i])
        else:
            cat.append(soln[i])
            c_f.append(fit[i])
    return mice, m_f, cat, c_f


# Phase 1: update status of cats
def bound(v):
    if v < lb or v > ub: v = random.uniform(lb, ub)
    return v


def update_cat(cat, c_f):
    for j in range(len(cat)):
        tem = []
        for d in range(len(cat[j])):
            m_k_d = d
            r, rand = random.random(), random.random()
            I = round(1 + rand)  # eqn. (8)
            c_new = bound(cat[j][d] + r * (m_k_d - I * cat[j][d]))  # eqn. (7)
            tem.append(c_new)
        f_new = fitness(tem)

        # eqn. (9)
        if f_new < c_f[j]:
            cat[j] = tem
            c_f[j] = f_new


# Phase 2: update status of mice.
def update_mice(mice, m_f):
    global f_new
    for i in range(len(mice)):
        tem = []
        for d in range(len(mice[i])):
            h_i_d = random.randint(0, len(mice) - 1)
            r, rand = random.random(), random.random()
            I = round(1 + rand)
            m_new = bound(mice[i][d] + r * (h_i_d - I * mice[i][d]) * np.sign(m_f[i] - m_f[h_i_d]))  # eqn. (11)
            tem.append(m_new)
        f_new = fitness(tem)

        # eqn. (12)
        if f_new < m_f[i]:
            mice[i] = tem
            m_f[i] = f_new


# loop begins
soln = generate(pop, dim, lb, ub)

while g < matrix:
    fit = []
    for i in range(len(soln)):  # fitness
        fit.append(fitness(soln[i]))
    soln, fit = sorted(soln, fit)
    X_best = soln[0]
    mice, m_f, cat, c_f = mice_cat_selection(soln, fit)
    update_cat(cat, c_f)  # Update status of the jth cat using Equations
    update_mice(mice, m_f)  # Update status of the ith mouse using Equations
    soln = mice + cat
    fit = m_f + c_f

    g += 1

