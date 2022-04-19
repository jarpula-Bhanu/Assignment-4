import numpy as np
from numpy import random as rn

N = 500 #sample space
x = rn.randint(0,4,size=N)
ctr_0 = np.count_nonzero(x==0)
ctr_2 = np.count_nonzero(x==2)
ctr_1 = N - ctr_0 - ctr_2

pr_0 = 0.25     #probability of getting zero head
pr_1 = 0.5      #probability of getting one head
pr_2 = 0.25     #probability of getting two heads

################################
# pr(zero head) = T T          #
# pr(one head)  = T H and H T  #
# pr(two head)  = H H          #
################################

print("Theoritical probabilities are",pr_0,pr_1,pr_2)
print("Expermental probabilities are",ctr_0/N,ctr_1/N,ctr_2/N)
