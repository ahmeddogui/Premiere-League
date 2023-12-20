import sys
sys.path.insert(0, 'C:/Users/ahmed/OneDrive/Bureau/AHMED/PremiereLeague-main')
from dao import ModelDAO
from model.EquipesM import Equipes


class EquipesDAO(ModelDAO.modeleDAO):
    def __init__(self):
        params = ModelDAO.modeleDAO.connect_objet
        self.cur = params.cursor()

    def insererUn(self, objIns: Equipes) -> int:
        try:
            query = '''INSERT INTO equipes (equipe_id, nom_de_equipe, manager, joueurs) VALUES(%s, %s, %s, %s,);'''
            self.cur.execute(query,( objIns.getEquipeId(), objIns.getNomDeEquipe(), objIns.getManager(), objIns.getJoueur(),))
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount != 0 else 0
        except Exception as e:
            print(f"Erreur_EquipesDAO.insererUn() ::: {e}")
            self.cur.connection.rollback()
            return 0
        
    def insererToutList(self, objInsList: list[Equipes] = []) -> int:
        try:
            query = '''INSERT INTO equipes (equipe_id, nom_de_equipe, manager, joueurs) VALUES(%s, %s, %s, %s,);'''
            self.cur.execute(query, [(obj.getEquipeId(), obj.getNomDeEquipe(), obj.getManager(), obj.getJoueur()) for obj in objInsList])
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount != 0 else 0
        except Exception as e:
            print(f"Erreur_EquipesDAO.insererUn() ::: {e}")
            self.cur.connection.rollback()
            return 0

    def trouverUn(self, cleTrouv) -> Equipes:
        try:
            query = '''SELECT * FROM equipes WHERE equipe_id = %s;'''
            self.cur.execute(query, (cleTrouv,))
            res = self.cur.fetchone()

            if res:
                e = Equipes()
                e.setEquipeId(res[0])
                e.setNomDeEquipe(res[1])
                e.setManager(res[2])
                e.setJoueur(res[3])#это будет список
                return e
            else: 
                return None
            
        except Exception as e:
            print(f"Erreur_EquipesDAO.trouverUn() ::: {e}")

        
    def trouverTout(self) -> list[Equipes]:
        try: 
            query = '''SELECT * FROM equipes;'''
            self.cur.execute(query)
            res = self.cur.fetchall()

            liste_equipes = []

            if len(res) > 0:
                for r in res:
                    e = Equipes()
                    e.setEquipeId(r[0])
                    e.setNomDeEquipe(r[1])
                    e.setManager(r[2])
                    e.setJoueur(r[3])

                    liste_equipes.append(e)
                
                return liste_equipes
            
            else:

                return None
        
        except Exception as e:
            print(f"Erreur_EquipesDAO.trouverTout() ::: {e}")
        finally:
            self.cur.close()
            return None
        
    def trouverToutParUn(self, cleTrouv) -> list[Equipes]:
        try: 
            query = '''SELECT * from equipes WHERE nom_de_equipe = %s;'''
            self.cur.execute(query, (cleTrouv,))
            res = self.cur.fetchall()

            liste_equipes = []

            if len(res) > 0:
                for r in res:
                    e = Equipes()
                    e = Equipes()
                    e.setEquipeId(r[0])
                    e.setNomDeEquipe(r[1])
                    e.setManager(r[2])
                    e.setJoueur(r[3])

                    liste_equipes.append(e)
                
                return liste_equipes
            
            else:

                return None
        except Exception as e:
            print(f"Erreur_EquipesDAO.trouverToutParUn ::: {e}")

    def trouverToutParUnLike(self, val) -> list[Equipes]:       
        try: 
            query = '''SELECT * from equipes WHERE nom_de_equipe LIKE %s;'''
            self.cur.execute(query, (val,))
            res = self.cur.fetchall()

            liste_equipes = []

            if len(res) > 0:
                for r in res:
                    e = Equipes()
                    e = Equipes()
                    e.setEquipeId(r[0])
                    e.setNomDeEquipe(r[1])
                    e.setManager(r[2])
                    e.setJoueur(r[3])

                    liste_equipes.append(e)
                
                return liste_equipes
            
            else:

                return None
        except Exception as e:
            print(f"Erreur_EquipesDAO.trouverToutParUn ::: {e}")

    def modifierUn(self, cleAnc, objModif:Equipes) -> int:
        try:
            query = '''UPDATE equipes SET nomDeEquipe = %s WHERE equipe_id = %s;'''
            self.cur.execute(query, (objModif.getNomDeEquipe(), cleAnc))
            #подтверждает операцию
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount!=0 else 0
        except Exception as e:
            print(f"Erreur_EquipesDAO.modifierUn() ::: {e}")
            self.cur.connection.rollback()
        finally: 
            self.cur.close()

    def supprimerUn(self, cleSup) -> int:
        try:
            query = '''DELETE FROM equipes WHERE equipe_id = %s;'''
            self.cur.execute(query, (cleSup,))
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount!=0 else 0
        except Exception as e:
            print(f"Erreur_EquipesDAO.supprimerUn() ::: {e}")
            self.cur.connection.rollback()
        finally:
            self.cur.close()

    def searchPleinText(self, keyword) -> list[Equipes]:
        '''
        Effectue une recherche plein texte.

        :param keyword: Le mot-clé de recherche.
        :return: Une liste de résultats de recherche.
        '''
        try:
            query = '''SELECT * FROM equipes WHERE nom_de_equipe @@ %s;'''
            self.cur.execute(query, (f"'{keyword}'",))
            res = self.cur.fetchall()

            liste_equipes = []

            if len(res) > 0:
                for r in res:
                    equipe = Equipes()
                    equipe.setEquipeID(r[0])
                    equipe.setNomDeEquipe(r[1])
                    liste_equipes.append(equipe)

                return liste_equipes

            else:
                return None

        except Exception as e:
            print(f"Erreur_EquipesDAO.searchPleinText() ::: {e}")
        finally:
            self.cur.close()

        
