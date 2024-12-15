import numpy as np
import matplotlib.pyplot as plt
import element_commun1 as com 
import element_commun2 as com2  

# Fonction de lissage avec moyenne glissante
def moyenne_glissante(data, window_size=10):
    return np.convolve(data, np.ones(window_size)/window_size, mode='valid')

# Fonction de test pour chronométrer les algos
def test_chrono_algos(n, repetitions=5):
    tailles = range(0, n, 50)  # Taille des listes en pas de 50
    temps_algo_base = []
    temps_algo_tas = []

    for i in tailles:
        # Temps pour l'algo de base
        temps_base = [
            com.chronometre_element_commun1(
                np.random.randint(10**6, size=i).tolist(),
                np.random.randint(10**6, size=i).tolist()
            )
            for _ in range(repetitions)
        ]
        temps_algo_base.append(np.mean(temps_base))

        # Temps pour l'algo avec structure de tas
        temps_tas = [
            com2.chronometre_element_commun2(
                np.random.randint(10**6, size=i).tolist(),
                np.random.randint(10**6, size=i).tolist()
            )
            for _ in range(repetitions)
        ]
        temps_algo_tas.append(np.mean(temps_tas))

    return tailles, temps_algo_base, temps_algo_tas

# Fonction d'affichage des résultats comparés
def afficher_comparaison_algos(n):
    tailles, temps_base, temps_tas = test_chrono_algos(n)

    # Calcul des moyennes glissantes pour lisser les résultats
    temps_base_lisse = moyenne_glissante(temps_base, window_size=5)
    temps_tas_lisse = moyenne_glissante(temps_tas, window_size=5)

    # Ajuste les tailles pour correspondre aux courbes lissées
    tailles_lisse = list(tailles)[:len(temps_base_lisse)]

    # Création du graphique
    plt.figure(figsize=(10, 6))  # Taille du graphique

    plt.plot(tailles_lisse, temps_base_lisse, color='blue', linewidth=2, linestyle='--', label="Algo de base (lissé)")

    plt.plot(tailles_lisse, temps_tas_lisse, color='red', linewidth=2, linestyle='-', label="Algo par tas (lissé)")

    # Ajustements visuels
    plt.xlabel("Taille de la liste", fontsize=12)
    plt.ylabel("Temps d'exécution en secondes", fontsize=12)
    plt.title("Comparaison des performances : Algo de base vs Algo par tas", fontsize=14)
    plt.legend(loc="upper left") # Déplace la légende
    plt.grid(True) # Ajoute une grille pour une meilleure lecture
    plt.tight_layout() # Ajuste les marges pour que tout soit visible

    plt.show()

# Appel de la fonction pour comparer les deux algos
afficher_comparaison_algos(1000)
