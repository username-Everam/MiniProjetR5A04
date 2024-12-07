#Question 3 et 4 :

import element_commun1 as com
import numpy as np
import matplotlib.pyplot as plt

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

def test_element_chrono(n):
    tableau_temps=[]
    for i in range(0 ,n, 10):
        Nmax=10000000
        liste1 = np.random.randint(Nmax,size=i).tolist()
        liste2 = np.random.randint(Nmax,size=i).tolist()
        temps=com.chronometre_element_commun1(liste1,liste2)
        tableau_temps.append(temps)
    return tableau_temps

def afficher_graph(n):
    tableau=test_element_chrono(n)
    x=[*range(0,n,10)]
    plt.scatter(x,tableau)
    plt.show()
    
afficher_graph(5000)