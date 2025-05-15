# PI2CChampionship_BOT
Ce programme est un bot développé dans le cadre du cours de projet informatique PI2C à l’ECAM, destiné au jeu Quarto. Il communique avec le projet GitHub suivant : [https://github.com/qlurkin/PI2CChampionshipRunner].

## Lancer le bot

Pour lancer le bot, procédez comme suit :

1. Installer les dépendances :
   ```powershell
   pip install -r requirements.txt

2. Lancer le code dans le terminal :

    ```powershell 
    python .../Communication <Port_du_bot> <Pseudo> <Adresse_IP_du_serveur> <Port_du_serveur> <Matricule> <Think|Random>





## Strategie:

Le bot utilise un algorithme Negamax avec élagage alpha-bêta. En lui fixant une profondeur (depth), il cherche à maximiser le score possible basé sur une heuristique, jusqu’à ce que la profondeur atteigne zéro ou que la partie soit terminée.

| Coup joué            | Score attribué      |
|----------------------|-----------------|
| Coups gagnant        | +100 |
| Trois pièces alignées partageant au moins une caractéristique        |       +10|
Deux pièces alignées partageant au moins deux caractéristiques| +3

Cela permet de faire ressortir en priorité le coup gagnant lorsqu’il est possible, tout en encourageant le bot à créer des opportunités de victoire et à placer les pièces de même characteristique côte à côte

Biensur il veille à ne faire aucun `Bad move`.

## Bibliotheque utilisées

- **json** : utilisé avec un `try-except` pour s’assurer que le message a bien été reçu et traité correctement.  
- **sys** : permet de lire les arguments passés lors du lancement du bot.  
- **pytest** : utilisé pour effectuer les tests unitaires.  
- **socket** : gère la communication avec le serveur.  
- **threading** : permet le multitâche, notamment pour écouter et envoyer des messages simultanément, ainsi que pour lancer plusieurs bots aléatoires en parallèle.  
- **time** : utilisé pour éviter de surcharger le système en espaçant l’envoi des commandes des bots aléatoires.  
- **random** : sert à générer des coups aléatoires pour le bot en mode random.

## Auteur:

Kalaï Tariq [23047]