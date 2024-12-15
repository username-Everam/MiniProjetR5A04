import algo_base as com
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
        
#test qui chronometre le temps d'execution de element_commun1 pour N allant de 0 à n par 5 et en le faisant 5 fois pour chaque N
def test_chrono_moyenne(n, repetitions=5):
    temps_moyens = []
    for i in range(0, n, 5): 
        temps = [
            com.chronometre_element_commun1(
                np.random.randint(10**6, size=i).tolist(),
                np.random.randint(10**6, size=i).tolist()
            )
            for _ in range(repetitions)
        ]
        temps_moyens.append(np.mean(temps))
    return temps_moyens

# Assure-toi que x et y sont de la même taille
def afficher_graph1(n):
    x = list(range(0, n, 5))  # Convertir range en liste pour s'assurer du même nombre de points
    y = test_chrono_moyenne(n)
    
    # Vérification des tailles
    if len(x) != len(y):
        print(f"Taille de x: {len(x)}, Taille de y: {len(y)}")
        y = y[:len(x)]  # Ajuster y pour correspondre à x si nécessaire
    
    plt.plot(x, y, label="Temps d'exécution moyen", color='green', marker='o')
    plt.xlabel("Taille de la liste")
    plt.ylabel("Temps d'exécution en secondes (moyenne)")
    plt.title("Performance de l'algorithme 2")
    plt.legend()
    plt.grid()
    plt.show()

afficher_graph1(1000)
