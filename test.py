import element_commun as com
import numpy as np
import matplotlib.pyplot as plt

# Teste la fonction `element_commun1` avec des listes aléatoires
def test_element_commun1():
    for _ in range(10):
        n = 10
        Nmax = 100
        liste1 = np.random.randint(Nmax, size=n).tolist()
        liste2 = np.random.randint(Nmax, size=n).tolist()
        print("Résultat:", com.element_commun1(liste1[:], liste2[:]), 
              "Listes triées:", sorted(liste1), sorted(liste2))

# Teste la fonction `element_commun2` avec des listes aléatoires
def test_element_commun2():
    for _ in range(10):
        n = 10
        Nmax = 100
        liste1 = np.random.randint(Nmax, size=n).tolist()
        liste2 = np.random.randint(Nmax, size=n).tolist()
        print("Résultat:", com.element_commun2(liste1[:], liste2[:]), 
              "Listes triées:", sorted(liste1), sorted(liste2))

# Teste le temps d'exécution de `chronometre_element_commun1`
def test_chrono_element_commun1(n):
    return [
        com.chronometre_element_commun1(
            np.random.randint(10**6, size=i).tolist(),
            np.random.randint(10**6, size=i).tolist()
        )
        for i in range(0, n, 10)
    ]

# Teste le temps d'exécution de `chronometre_element_commun2`
def test_chrono_element_commun2(n):
    return [
        com.chronometre_element_commun2(
            np.random.randint(10**6, size=i).tolist(),
            np.random.randint(10**6, size=i).tolist()
        )
        for i in range(0, n, 10)
    ]

# Affiche un graphe des temps d'exécution de `element_commun1`
def afficher_graph1(n):
    plt.scatter(range(0, n, 10), test_chrono_element_commun1(n), label="Liste")
    plt.legend()
    plt.show()

# Affiche un graphe des temps d'exécution de `element_commun2`
def afficher_graph2(n):
    plt.scatter(range(0, n, 10), test_chrono_element_commun2(n), label="Tas")
    plt.legend()
    plt.show()

# Compare les temps des deux fonctions
def afficher_graph_comparaison(n):
    plt.scatter(range(0, n, 10), test_chrono_element_commun1(n), label="Liste")
    plt.scatter(range(0, n, 10), test_chrono_element_commun2(n), label="Tas")
    plt.legend()
    plt.show()

# Exécution des tests
afficher_graph1(500)
afficher_graph2(500)
afficher_graph_comparaison(500)
