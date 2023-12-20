import sys
sys.path.insert(0, 'C:/Users/ahmed/OneDrive/Bureau/AHMED/PremiereLeague-main')
from dao import ModelDAO
from model.JoueursM import Joueurs


class JoueursDAO(ModelDAO.modeleDAO):
    def __init__(self):
        params = ModelDAO.modeleDAO.connect_objet
        self.cur = params.cursor()

    def insererUn(self, objIns: Joueurs) -> int:
        try:
            query = '''INSERT INTO joueurs (joueur_id, nom_joueur, prenom_joueur, position, nombre_de_but, nombre_de_passes_d, distance_parcurue) VALUES(%s, %s, %s, %s, %s, %s, %s);'''
            self.cur.execute(query,( objIns.getJoueurId(), objIns.getNom(), objIns.getPrenom(), objIns.getPosition(), objIns.getNombreDeBut(), objIns.getNombreDePassesD(), objIns.getDistanceParcurue(),))
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount != 0 else 0
        except Exception as e:
            print(f"Erreur_JoueursDAO.insererUn() ::: {e}")
            self.cur.connection.rollback()
            return 0
        
    def insererToutList(self, objInsList: list[Joueurs] = []) -> int:
        try:
            query = '''INSERT INTO joueurs (joueur_id, nom_joueur, prenom_joueur, position, nombre_de_but, nombre_de_passes_d, distance_parcurue) VALUES(%s, %s, %s, %s, %s, %s, %s);'''
            self.cur.execute(query,[(obj.getJoueurId(), obj.getNom(), obj.getPrenom(), obj.getPosition(), obj.getNombreDeBut(), obj.getNombreDePassesD(), obj.getDistanceParcurue()) for obj in objInsList])
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount != 0 else 0
        except Exception as e:
            print(f"Erreur_JoueursDAO.insererUn() ::: {e}")
            self.cur.connection.rollback()
            return 0        

    def trouverUn(self, cleTrouv) -> Joueurs:
        try:
            query = '''SELECT * FROM joueurs WHERE equipe_id = %s;'''
            self.cur.execute(query, (cleTrouv,))
            res = self.cur.fetchone()

            if res:
                j = Joueurs()
                j.setNom(res[0])
                j.setPrenom(res[1])
                j.setPosition(res[2])
                j.setNombreDeBut(res[3])
                j.setDistanceParcurue(res[4])
                return j
            else: 
                return None
            
        except Exception as e:
            print(f"Erreur_JoueursDAO.trouverUn() ::: {e}")

        
    def trouverTout(self) -> list[Joueurs]:
        try: 
            query = '''SELECT * FROM joueurs;'''
            self.cur.execute(query)
            res = self.cur.fetchall()

            liste_joueurs = []

            if len(res) > 0:

                for r in res:
                    j = Joueurs()
                    j.setNom(r[0])
                    j.setPrenom(r[1])
                    j.setPosition(r[2])
                    j.setNombreDeBut(r[3])
                    j.setDistanceParcurue(r[4])

                    liste_joueurs.append(j)
                return liste_joueurs
                
            else: 
                return None
        
        except Exception as e:
            print(f"Erreur_JoueursDAO.trouverTout() ::: {e}")
        finally:
            self.cur.close()
            return None
        
    def trouverToutParUn(self, cleTrouv) -> list[Joueurs]:
        try: 
            query = '''SELECT * from equipes WHERE nom_joueur = %s && prenom_joueur = %s;'''
            self.cur.execute(query, (cleTrouv,))
            res = self.cur.fetchall()

            liste_joueurs = []

            if len(res) > 0:
                for r in res:
                    j = Joueurs()
                    j.setNom(r[0])
                    j.setPrenom(r[1])
                    j.setPosition(r[2])
                    j.setNombreDeBut(r[3])
                    j.setDistanceParcurue(r[4])

                    liste_joueurs.append(j)
                
                return liste_joueurs
            
            else:

                return None
        except Exception as e:
            print(f"Erreur_JoueursDAO.trouverToutParUn ::: {e}")

    def trouverToutParUnLike(self, val) -> list[Joueurs]:       
        try: 
            query = '''SELECT * from joueurs WHERE nom_joueur LIKE %s && prenom_joueur LIKE %s;'''
            self.cur.execute(query, (val,))
            res = self.cur.fetchall()

            liste_joueurs = []

            if len(res) > 0:
                for r in res:
                    j = Joueurs()
                    j.setNom(r[0])
                    j.setPrenom(r[1])
                    j.setPosition(r[2])
                    j.setNombreDeBut(r[3])
                    j.setDistanceParcurue(r[4])

                    liste_joueurs.append(e)
                
                return liste_joueurs
            
            else:

                return None
        except Exception as e:
            print(f"Erreur_JoueursDAO.trouverToutParUn ::: {e}")

    def modifierUn(self, cleAnc, objModif:Joueurs) -> int:
        try:
            query = '''UPDATE joueurs SET nom_joueur = %s, prenom_joueur = %s  WHERE equipe_id = %s;'''
            self.cur.execute(query, (objModif.getNom(), objModif.getPrenom(), cleAnc))
            #подтверждает операцию
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount!=0 else 0
        except Exception as e:
            print(f"Erreur_JoueursDAO.modifierUn() ::: {e}")
            self.cur.connection.rollback()
        finally: 
            self.cur.close()

    def supprimerUn(self, cleSup) -> int:
        try:
            query = '''DELETE FROM joueurs WHERE joueur_id = %s;'''
            self.cur.execute(query, (cleSup,))
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount!=0 else 0
        except Exception as e:
            print(f"Erreur_JoueursDAO.supprimerUn() ::: {e}")
            self.cur.connection.rollback()
        finally:
            self.cur.close()

    def searchPleinText(self, keyword) -> list[Joueurs]:
        '''
        Effectue une recherche plein texte.

        :param keyword: Le mot-clé de recherche.
        :return: Une liste de résultats de recherche.
        '''
        try:
            query = '''SELECT * FROM joueurs WHERE nom_joueur @@ %s;'''
            self.cur.execute(query, (f"'{keyword}'",))
            res = self.cur.fetchall()

            liste_joueurs = []

            if len(res) > 0:
                for r in res:
                    joueur = Joueurs()
                    joueur.setJoueurID(r[0])
                    joueur.setNom(r[1])
                    liste_joueurs.append(joueur)

                return liste_joueurs

            else:
                return None

        except Exception as e:
            print(f"Erreur_JoueursDAO.searchPleinText() ::: {e}")
        finally:
            self.cur.close()
        
