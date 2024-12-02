#Question 3 et 4 :

import element_commun1 as com
import numpy as np

def test_element_commun1() :
    for i in range(10):
        n=10
        Nmax=100
        liste1 = np.random.randint(Nmax,size=n).tolist()
        liste2 = np.random.randint(Nmax,size=n).tolist()
        liste_originelle1 = liste1.copy()
        liste_originelle2 = liste2.copy()
        liste_originelle1.sort()
        liste_originelle2.sort()
        x = com.element_commun1(liste1,liste2)
        print(x, liste_originelle1, liste_originelle2)

print(com.test_element_chrono(1000))