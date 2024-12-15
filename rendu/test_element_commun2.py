import element_commun2 as com
import numpy as np
import matplotlib.pyplot as plt

# Teste la fonction `element_commun2` avec des listes aléatoires
def test_element_commun2():
    for _ in range(10):
        n = 10
        Nmax = 100
        liste1 = np.random.randint(Nmax, size=n).tolist()
        liste2 = np.random.randint(Nmax, size=n).tolist()
        print("Résultat:", com.element_commun2(liste1[:], liste2[:]), 
              "Listes triées:", sorted(liste1), sorted(liste2))


# Fonction avec moyenne glissante pour lisser les résultats
def moyenne_glissante(data, window_size=5):
    return np.convolve(data, np.ones(window_size)/window_size, mode='valid')

# Test de l'algo 2 avec tas avec N allant de 0 à n par 5 et en le faisant 10 fois pour chaque N pour avoir une moyenne
def test_chrono_moyenne_tas(n, repetitions=5):
    temps_moyens = []
    tailles = range(0, n, 10)
    for i in tailles:
        temps = [
            com.chronometre_element_commun2(
                np.random.randint(10**6, size=i).tolist(),
                np.random.randint(10**6, size=i).tolist()
            )
            for _ in range(repetitions)
        ]
        temps_moyens.append(np.mean(temps))
    return tailles, temps_moyens

# Affichage avec améliorations
def afficher_graph_tas_lisse(n):
    tailles, temps_moyens = test_chrono_moyenne_tas(n)
    temps_lisses = moyenne_glissante(temps_moyens)

    # Découpage des tailles pour matcher la moyenne glissante
    tailles_lisses = tailles[:len(temps_lisses)]

    plt.figure(figsize=(8, 6))  # Ajuste la taille du graphique
    plt.plot(tailles_lisses, temps_lisses, color='blue', linewidth=2, label="Temps lissé (moyenne)")
    plt.xlabel("Taille de la liste", fontsize=12)
    plt.ylabel("Temps d'exécution en secondes", fontsize=12)
    plt.title("Performance de l'algorithme 2 avec structure de tas (lissé)", fontsize=14)
    plt.legend(loc="upper left")  # Déplace la légende
    plt.grid(True)  # Ajoute une grille pour une meilleure lecture
    plt.tight_layout()  # Ajuste les marges pour que tout soit visible
    plt.show()

#afficher_graph_tas_lisse(1000)
