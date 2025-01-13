# Découverte de Fast API

## Contexte
Dans le cadre de ma formation de développeur en IA, exercice pour prendre ses marques avec la mise en place d'une API. L'occasion aussi de travailler la structure d'un petit projet de développement.

## Prérequis
Avant de démarrer le développement le projet, il est nécessaire d'installer FastAPI, Uvicorn, et SQLite sur l'environnement de travail. Pour effectuer ces installations, vous pouvez éxécuter la commande suivante :
```bash
pip install -r requirements.txt
```

## Data
[Lien vers les données à utiliser](https://www.kaggle.com/datasets/benoitfavier/immobilier-france/data)

## Structure du projet
```bash
project/
│
├── data/
│   └── immo_fr.db          # Fichier .db généré à partir des .csv sélectionnés
│
├── src/
│   ├── api/
│   │   ├── database.py     # Fonctions de connexion avec la base de données (fichier .db dans ce contexte)
│   │   └── queries.py      # Requêtes SQL pour chaque cas
│   │
│   └── utils.py            # Fonctions utilitaires, vérifications
│
├── .env                    # Variables d'environnement à définir, fichier ignoré par Git
├── .gitignore
├── main.py                 # Script de l'API, à exécuter pour démarrer le serveur
├── README.md
└── requirements.txt        # Dépendances à installer pour la bonne exécution du script
```

## Notes
Il s'agit d'un projet de test, le fichier .csv des transactions n'est qu'un échantillon de données. Ainsi, peu de requêtes renvoient un résultat.

## Procédure
1 / Télécharger les données sur kaggle (voir partie Data) <br>

2 / Exporter les .csv utilisés (foyers_fiscaux et transactions_sample) en un seul fichier .db (j'ai utilisé [SQLite Online](https://sqliteonline.com/) pour cette opération) <br>

3 / Placer le fichier .db obtenu dans le repo du projet (voir partie Structure) <br>

4 / Créer le fichier .env à la racine du projet et définir le chemin vers le fichier .db
```py
DB_PATH="data/immo_fr.db"
```

5 / Depuis le terminal, lancer l'API en se plaçant à la racine du projet et en exécutant :
```bash
python main.py
```
L'API sera accessible à l'adresse http://localhost:8000.

## Documentation de l'API

### 1. Revenu moyen d'une ville
```
GET /average_revenue/{city}
```
Retourne le revenu fiscal moyen le plus récent pour la ville spécifiée.

### 2. Dernières transactions d'une ville
```
GET /last_transactions/{city}_last_{number}
```
Retourne les {number} dernières transactions pour la ville spécifiée.

### 3. Nombre de transactions par ville et année
```
GET /transactions_count/{city}_{year}
```
Retourne le nombre de transactions pour la ville et l'année spécifiées.

### 4. Prix moyen au mètre carré par année et type de bien
```
GET /average_price_per_square_meter/{year}_{type}
```
Retourne le prix moyen au mètre carré pour l'année et le type de bien spécifiés.

### 5. Nombre de transactions par critères
```
GET /transactions_count2/{city}_{year}_{type}_{rooms}
```
Retourne le nombre de transactions pour la ville, l'année, le type de bien et le nombre de pièces spécifiés.

### 6. Transactions par nombre de pièces
```
GET /transactions_by_pieces/{city}_{year}_{type}
```
Retourne le nombre de transactions par nombre de pièces pour la ville, l'année et le type de bien spécifiés.

### 7. Prix moyen au mètre carré par ville
```
GET /average_price_per_square_meter2/{city}_{year}_{type}
```
Retourne le prix moyen au mètre carré pour la ville, l'année et le type de bien spécifiés.

### 8. Transactions par département
```
GET /transactions_by_dpt/
```
Retourne le nombre de transactions par département, triées par ordre décroissant.

### 9. Nombre de transactions par revenu et type de bien
```
GET /transactions_count3/{year1}_{revenu}_{year2}_{type}
```
Retourne le nombre de transactions pour les critères spécifiés : année du revenu fiscal, montant du revenu, année de transaction et type de bien.

### 10. Top 10 des villes par nombre de transactions
```
GET /cities_top10_transactions/
```
Retourne les 10 villes ayant le plus grand nombre de transactions.

### 11 & 12. Top 10 des villes les moins chères par type de bien
```
GET /cities_top10_price/{type}
```
Retourne les 10 villes les moins chères (prix au mètre carré) pour le type de bien spécifié.

### Remarques
- Les années doivent être au format YYYY.  
- Les types de biens doivent être spécifiés en français (ex: "Maison", "Appartement").  
- Les noms de villes sont insensibles à la casse.