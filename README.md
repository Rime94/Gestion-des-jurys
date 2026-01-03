 RJILI RILME 5IIR G2
 Ce projet est un module pédagogique personnalisé développé sous Odoo 17. Pour faciliter la gestion administrative des jurys d'examen et le suivi des décisions académiques.

Le module permet de centraliser les informations relatives aux sessions de jury, d'assigner des responsables et d'enregistrer les décisions finales (ex: Validé, Refusé) de manière structurée.

🚀 Fonctionnalités clés
Gestion des dossiers : Création et suivi des fiches de jury individuelles.

Suivi des décisions : Attribution d'un statut clair pour chaque session (ex: "Validé").

Interface ergonomique : Utilisation des vues Kanban, Liste et Formulaire natives d'Odoo pour une navigation intuitive.

Architecture modulaire : Respect des standards de développement Odoo avec séparation des modèles, des vues et de la sécurité.

📂 Structure du Module
Le module suit l'architecture standard d'Odoo pour assurer sa portabilité et sa maintenance :

models/ : Logique métier et définition de la base de données (tp.jury).

views/ : Définition des interfaces utilisateur en XML (jury_views.xml).

security/ : Gestion des droits d'accès via ir.model.access.csv.

__manifest__.py : Fichier de configuration contenant les métadonnées du module (version 17.0.1.0, auteur, dépendances).

🛠️ Installation et Environnement
Ce projet est configuré pour être déployé rapidement grâce à Docker.

Prérequis : Docker et Docker-Compose installés.

Lancement : Exécuter la commande docker-compose up à la racine du projet.

Accès : Ouvrez votre navigateur sur http://localhost:8069.

Activation : Recherchez le module "TP - Gestion des Jurys" dans le menu Applications et cliquez sur Activate.

📋 Détails Techniques
Framework : Odoo 17.0.

Langages : Python (Logique) et XML (Interface).

Licence : LGPL-3.
