n_E1 = 105 #No. of two heads
n_E2 = 275 #No. of one head
n_E3 = 120 #No. of no head
n_tot = 500 #total outcomes

P_E_1 =(n_E1/n_tot) #probability of event two heads
P_E_2 =(n_E2/n_tot) #probability of event one head
P_E_3 =(n_E3/n_tot) #probability of event no head

print('P(E_1) =',P_E_1)
print('P(E_2) =',P_E_2)
print('P(E_3) =',P_E_3)

print('P(E_1) + P(E_2) + P(E_3) =',P_E_1+P_E_2+P_E_3) #sum of individual probabilities