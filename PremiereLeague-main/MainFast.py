import os
import sys
from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import traceback
from datetime import datetime
from functools import wraps

controller_path = os.path.join(os.path.dirname(__file__), 'controller')
sys.path.append(controller_path)



from controller import ButsC, EquipesC, JoueursC, ManagersC, MatchsC, SeasonsC
from model import ButsM, EquipesM, MatchsM, JoueursM, ManagersM, SeasonsM
app = Flask(__name__)


CORS(app, resources={r"/api/premierleague/postgresql/*": {"origins": "*"}})
LOG_FILE_PATH = './utils/logs.json'


@app.route('/api/premierleague/test', methods=['GET', 'POST']) #### pas sur de route 
def test_route():
    if request.method == 'GET':
        # Logique pour la méthode GET
        return jsonify({"message": "Test GET réussi"})
    elif request.method == 'POST':
        # Logique pour la méthode POST
        data = request.json
        return jsonify({"message": "Test POST réussi", "data": data})
def log_request_info(route_function):
    @wraps(route_function)
    def wrapper(*args, **kwargs):
        try:
            start_time = datetime.now()

            # Exécuter la fonction de route
            response = route_function(*args, **kwargs)

            end_time = datetime.now()
            execution_time = (end_time - start_time).total_seconds()

            # Récupérer les informations de la requête
            request_info = {
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'route': request.path,
                'method': request.method,
                'ip_address': request.headers.get('X-Forwarded-For', request.remote_addr),
                'execution_time': execution_time,
                'response': response
            }

            # Charger les anciens logs
            try:
                with open(LOG_FILE_PATH, 'r') as log_file:
                    logs = json.load(log_file)
            except (FileNotFoundError, json.JSONDecodeError):
                logs = []

            # Ajouter les nouveaux logs
            logs.append(request_info)

            # Enregistrer les logs dans le fichier
            with open(LOG_FILE_PATH, 'w') as log_file:
                json.dump(logs, log_file, indent=2)

            return response
        except Exception as e:
            error_message = f"Erreur lors de la journalisation de la requête : {e}"
            print(error_message)

            # Inclure les informations d'erreur dans la réponse JSON
            return {'error': 'Erreur interne du serveur', 'details': str(e), 'traceback': traceback.format_exc()}

    return wrapper

Privacy_Policy='''
Confidentiality and Security: We prioritize the protection of your information and have implemented appropriate security measures to prevent unauthorized access, disclosure, or alteration. Only authorized personnel have access to this information, and they are bound by confidentiality obligations.
Access Restrictions and Exploration: Unauthorized access to our application, including attempting to explore its functioning by accessing the root of the API, is strictly prohibited. Any violation of this privacy policy or our terms of use may result in disciplinary action, including account termination and, if necessary, legal action.
Information Retention: We retain your information for as long as necessary to fulfill the purposes stated in this privacy policy, unless a longer retention period is required or permitted by law.
Changes to the Privacy Policy: We reserve the right to modify this privacy policy at any time. Any changes will be effective upon publication on our website or within the application. It is your responsibility to regularly review this privacy policy for any updates.
Consent: By using our application, you consent to the collection, use, and disclosure of your information in accordance with this privacy policy.
Last Updated: 2023/11/30
'''
@app.route('/', methods=['GET'])
@log_request_info
def start():
    return {'Notice': "The api is protected, you could not do anything.",
            'A message for you ':"Hello dear dev./user WELCOME TO the Privacy Policy premier_league",
            'Pay attention':"We collect certain information, including your IP address and MAC address, for troubleshooting purposes. This information is collected automatically and anonymously and is not used to personally identify you unless there is a technical issue.",
            'Privacy Policy':Privacy_Policy}


@app.route(f'/api/premierleague/postgresql/getButs',methods=['GET'])
@log_request_info
def get_buts():
    """
    Obtenir la liste des buts.
    @return: Liste des buts au format JSON.
    """

    butsC = ButsC.Buits.visualiserUnBut()

    liste_buts = []

    if type(butsC)==list:
        for bc in butsC:

            but = {
                "but_id" : bc.getButId(),
                "minute" : bc.getMinute()
            }

            liste_buts.append(but)

        return {'response':liste_buts}

    return {'response':butsC}
@app.route(f'/api/premierleague/postgresql/getButs',methods=['GET'])
@log_request_info
def get_equipes():
    """
    Obtenir la liste des equipes.
    @return: Liste des equipes au format JSON.
    """

    equipesC = EquipesC.Equipes.visualiserUnEq()

    liste_equipes = []

    if type(equipesC)==list:
        for bc in equipesC:

            equipe = {
                "equipe_id" : bc.getEquipeId(),
                "nom_de_equipe" : bc.getNomDeEquipe()
            }

            liste_equipes.append(equipe)

        return {'response':liste_equipes}

    return {'response':equipesC}
@app.route(f'/api/premierleague/postgresql/getJoueurs',methods=['GET'])
@log_request_info
def get_joueurs():
    """
    Obtenir la liste des Joueurs.
    @return: Liste des joueurs au format JSON.
    """

    joueursC = JoueursC.Joueurs.visualiserUnJ()

    liste_joueurs= []

    if type(joueursC)==list:
        for bc in joueursC:

            joueur = {
                "joueur_id " : bc.getJoueurId(),
                "nom_joueur" : bc.getNom()
            }

            liste_joueurs.append(joueur)

        return {'response':liste_joueurs}

    return {'response':joueursC}
@app.route(f'/api/premierleague/postgresql/getManagers',methods=['GET'])
@log_request_info
def get_managers():
    """
    Obtenir la liste des Managers.
    @return: Liste des joueurs au format JSON.
    """

    managerC = ManagersC.Manager.visualiserUnM()

    liste_manager= []

    if type(managerC)==list:
        for bc in managerC:

            manager = {
                "manager_id" : bc.getManagerId(),
                "nom_manager" : bc.getNomManager()
            }

            liste_manager.append(manager)

        return {'response':liste_manager}

    return {'response':managerC}

app.route(f'/api/premierleague/postgresql/getMatch',methods=['GET'])
@log_request_info
def get_matchs():
    """
    Obtenir la liste des Managers.
    @return: Liste des joueurs au format JSON.
    """

    matchC = MatchsC.Matchs.visualiserUnMatch()

    liste_match= []

    if type(matchC)==list:
        for bc in matchC:

            match = {
                "match_id" : bc.getMatchId(),
                "date" : bc.getDate()
            }

            liste_match.append(match)

        return {'response':liste_match}

    return {'response':matchC}

app.route(f'/api/premierleague/postgresql/getMatch',methods=['GET'])
@log_request_info
def get_seasons():
    """
    Obtenir la liste des Managers.
    @return: Liste des joueurs au format JSON.
    """

    seasonsC = SeasonsC.Seasons.visualiserSeason()

    liste_season= []

    if type(seasonsC)==list:
        for bc in seasonsC:

            season = {
                "season_id" : bc.getSeasonId(),
                "annee" : bc.getAnnee()
            }

            liste_season.append(season)

        return {'response':liste_season}

    return {'response':seasonsC}

@app.route(f'/api/premierleague/postgresql/searchPleinText/<keyword>',methods=['GET'])
@log_request_info
def searchPleinText(keyword):
    """
    Rechercher des produits par texte intégral.
    @param keyword: Mot-clé pour la recherche.
    @return: Liste des produits correspondants au format JSON.
    """
    resultats: str | list[JoueursM.Joueurs] | None = JoueursC.Joueurs.search_product_by_name(keyword)

    if type(resultats)==list:

        liste_joueur = []

        for res in resultats:
            Jo = {
                "joueur_id": res.getJoueurID(),
                "nom_joueur": res.getNom(),
            }

            liste_joueur.append(Jo)

        return {'response':liste_joueur}


    return {'response':resultats}

@app.route('/api/premierleague/postgresql/create_user', methods=['POST'])
@log_request_info
def create_user():
    """
    Créer un nouvel utilisateur.
    @return: Réponse JSON indiquant le statut de la création.
    """
    try:
        password = request.json.get('password')
        username = request.json.get('username')

        response = sysadminC.SysAdmin.creerUnUser(password, username)

        if response == "ERROR":
            return {"response": "Erreur lors de la création de l'utilisateur."}
        else:
            return {"response": response}

    except Exception as e:
        print(f"Erreur lors de la création de l'utilisateur : {e}")
        return {"response": "Erreur interne du serveur."}
def search_Equipe(keyword):
    """
    Rechercher des produits par texte intégral.
    @param keyword: Mot-clé pour la recherche.
    @return: Liste des produits correspondants au format JSON.
    """
    resultats: str | list[EquipesM.Equipes] | None = EquipesC.Equipes.search_Equipes_by_name(keyword)

    if type(resultats)==list:

        liste_joueur = []

        for res in resultats:
            Eq = {
                "joueur_id": res.getJoueurID(),
                "nom_joueur": res.NomDeEquipe(),
            }

            liste_joueur.append(Eq)

        return {'response':liste_joueur}


    return {'response':resultats}

def search_Manager(keyword):
    """
    Rechercher des produits par texte intégral.
    @param keyword: Mot-clé pour la recherche.
    @return: Liste des produits correspondants au format JSON.
    """
    resultats: str | list[ManagersM.Managers] | None = ManagersC.Managers.search_Managers_by_name(keyword)

    if type(resultats)==list:

        liste_manager = []

        for res in resultats:
            Mo = {
                "joueur_id": res.getManagerID(),
                "nom_joueur": res.NomManager(),
            }

            liste_manager.append(Mo)

        return {'response':liste_manager}


    return {'response':resultats}
def search_Match(keyword):
    """
    Rechercher des produits par texte intégral.
    @param keyword: Mot-clé pour la recherche.
    @return: Liste des produits correspondants au format JSON.
    """
    resultats: str | list[MatchsM.Matchs] | None = MatchsC.Matchs.search_Match_by_date(keyword)

    if type(resultats)==list:

        liste_match = []

        for res in resultats:
            Mt = {
                "match_id": res.getManagerID(),
                "date": res.NomManager(),
            }

            liste_match.append(Mt)

        return {'response':liste_match}


    return {'response':resultats}

@app.route('/api/premierleague/postgresql/create_role', methods=['POST'])
@log_request_info
def create_role():
    """
    Créer un nouveau rôle.
    @return: Réponse JSON indiquant le statut de la création.
    """
    try:
        role = request.json.get('role')

        response = sysadminC.SysAdmin.creerUnRole(role)

        if response == "ERROR":
            return {"response": "Erreur lors de la création du rôle."}
        else:
            return {"response": response}

    except Exception as e:
        print(f"Erreur lors de la création du rôle : {e}")
        return {"response": "Erreur interne du serveur."}
@app.route('/api/premierleague/postgresql/assign_privileges', methods=['POST'])
@log_request_info
def assign_privileges():
    """
    Attribuer des privilèges à un rôle.
    @return: Réponse JSON indiquant le statut de l'attribution.
    """
    try:
        privileges = request.json.get('privileges')
        tables = request.json.get('tables')
        roles = request.json.get('roles')

        response = sysadminC.SysAdmin.privilege_Role(privileges, tables, roles)

        if response == "ERROR":
            return {"response": "Erreur lors de l'attribution des privilèges."}
        else:
            return {"response": response}

    except Exception as e:
        print(f"Erreur lors de l'attribution des privilèges : {e}")
        return {"response": "Erreur interne du serveur."}

@app.route('/api/premierleague/postgresql/assign_role', methods=['POST'])
@log_request_info
def assign_role():
    """
    Attribuer un rôle à un utilisateur.
    @return: Réponse JSON indiquant le statut de l'attribution.
    """
    try:
        user = request.json.get('user')
        roles = request.json.get('roles')

        response = sysadminC.SysAdmin.attribution_Role(user, roles)

        if response == "ERROR":
            return {"response": "Erreur lors de l'attribution des rôles."}
        else:
            return {"response": response}

    except Exception as e:
        print(f"Erreur lors de l'attribution des rôles : {e}")
        return {"response": "Erreur interne du serveur."}

if __name__=='__main__':

    # Run flask with the following defaults
    app.run(debug=True, port=5000, host='0.0.0.0', )