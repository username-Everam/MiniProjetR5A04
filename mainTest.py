#Question 3 :

import element_commun1 as com
import numpy as np

n=10
Nmax=100
liste1 = np.random.randint(Nmax,size=n).tolist()
liste2 = np.random.randint(Nmax,size=n).tolist()

print(com.element_commun1(liste1,liste2))