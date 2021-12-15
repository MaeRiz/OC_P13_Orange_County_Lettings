## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

## Tests et déploiement via CircleCI

Lors d'une mise à jour du code sur la branche master, CircleCI récupère le code pour lancer les tests et le peluchage du code.
Si cette action est satisfaite, il exécute une dockerisation de l'application et envoie l'image sur DockerHub.
Si l'action précédente a réussi, il exécute le déploiement de l'application sur Heroku.

### Prérequis

- Compte [CircleCI](https://circleci.com/signup/)
- Compte [DockerHub](https://hub.docker.com/)
- Compte [Heroku](https://signup.heroku.com/)
- Installer [Heroku CLI](https://devcenter.heroku.com/articles/getting-started-with-python#set-up)

### Installation

- Créer un projet CircleCI et le lier le à votre repository GitHub.
- Créer un projet DockerHub.
- Créer un projet Heroku.
- Obtenir un token d'authentification Heroku. [Voir documentation](https://devcenter.heroku.com/articles/authentication).
- Renseigner les variables d'environnement. Voir plus bas section **Variable d'environnement**.

### Utilisation

- Si toute l'installation est respectée, l'exécution du pipeline devrait se lancer à chaque mise à jour du code sur GitHub.
- Les tests et le peluchage du code se fera à chaque mise à jour de code dans n'importe quelle branche contenant la configuration CircleCI.
- La dockerization sur DockerHub et le déploiement sur Heroku s'exécuteront à chaque mise à jour du code dans la branche master tant qu'elle contient la configuration du pipeline.

## Exécution du docker en local

### Prérequis

- Compte [DockerHub](https://hub.docker.com/)
- Installer [Docker Desktop](https://www.docker.com/products/docker-desktop)
- Avoir exécuté le Pipeline précédent.

### Utilisation

En considérant:
- user = Nom d'utilisateur du compte DockerHub.
- repo = Application créée dans DockerHub.
- tag = Nom donné automatiquement à une image.
- .env = accès au fichier .env. (Voir plus bas section **Variables d'environnement**)

Etapes:
- Dans un invité de commande exécuté en Administrateur.
- Pour télécharger l'image docker `docker pull user/repo:tag`.
- Pour exécuter l'image docker `docker run --env-file .env user/repo:tag`.
- Pour accéder au serveur rendez-vous à l'adresse: [localhost:8000](http://localhost:8000)
- Il est en suite possible de manager le serveur avec l'interface Docker Desktop.

## Sentry

### Prérequis

- Compte [Sentry](https://sentry.io/signup/)

### Utilisation

- Créer un projet Sentry
- Ajouter l'adresse obtenue aux variables d'environnement. (Voir plus bas section **Variables d'environnement**)

## Variables d'environnements

Les variables d'environnement sont à placer à plusieurs endroits:
- Dans un fichier nommé **.env** à la racine du projet
- Dans la configuration de CircleCI
- Dans la configuration Heroku

| Clé  | Valeur          | Lieu |
| :--------------: |:---------------:|:---------:|
| DJANGO_SECRET_KEY  |   Clé secrète DJANGO  | Fichier/CircleCI/Heroku |
| DEBUG  | 0 / 1  | Fichier/CircleCI/Heroku |
| DOCKER_USER  | Utilisateur DockerHub  | CircleCI |
| DOCKER_PASS  | Mot de passe DockerHub  | CircleCI |
| HEROKU_TOKEN  | Tocken de connexion Heroku  | CircleCI |
| SENTRY  | Adresse Sentry  | Fichier/Heroku |
