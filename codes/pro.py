import numpy as np
from numpy import random as rn

N = 500
x = rn.randint(0,4,size=N)
ctr_0 = np.count_nonzero(x==0)
ctr_2 = np.count_nonzero(x==2)
ctr_1 = N - ctr_0 - ctr_2

pr_0 = 105/500
pr_1 = 275/500
pr_2 = 120/500

print("Theoritical probabilities are",pr_0,pr_1,pr_2)
print("Expermental probabilities are",ctr_0/N,ctr_1/N,ctr_2/N)