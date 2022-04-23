import numpy as np
from numpy import random as rn
import math

N = 500 #sample space
x = rn.randint(0,3,size=N) #considering coins are fair 
ctr_1 = np.count_nonzero(x==1)
ctr_2 = np.count_nonzero(x==2)
ctr_0 = N - ctr_1 - ctr_2

################################
# pr(zero head) = T T          #
# pr(one head)  = T H and H T  #
# pr(two head)  = H H          #
################################

pr_0 = math.comb(2,0)/4 #probability of getting 0 heads when two coins are tossed    
pr_1 = math.comb(2,1)/4 #probability of getting 1 heads when two coins are tossed    
pr_2 = math.comb(2,2)/4 #probability of getting 2 heads when two coins are tossed    

print("Theoritical probabilities are",pr_0,pr_1,pr_2)
print("Expermental probabilities are",ctr_0/N,ctr_1/N,ctr_2/N)