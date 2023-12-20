import sys
sys.path.insert(0, 'C:/Users/ahmed/OneDrive/Bureau/AHMED/PremiereLeague-main')
from dao import ModelDAO
from model.ManagersM import Managers


class ManagersDAO(ModelDAO.modeleDAO):
    def __init__(self):
        params = ModelDAO.modeleDAO.connect_objet
        self.cur = params.cursor()

    def insererUn(self, objIns: Managers) -> int:
        try:
            query = '''INSERT INTO managers (manager_id, nom_manager, prenom_manager, equipe, poste_de_manager) VALUES(%s, %s, %s, %s, %s);'''
            self.cur.execute(query,( objIns.getManagerId(), objIns.getNomManager(), objIns.getPrenomManager(), objIns.getEquipe(), objIns.getPosteManager(),))
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount != 0 else 0
        except Exception as e:
            print(f"Erreur_ManagersDAO.insererUn() ::: {e}")
            self.cur.connection.rollback()
            return 0
        
    def insererToutList(self, objInsList: list[Managers] = []) -> int:
        try:
            query = '''INSERT INTO managers (manager_id, nom_manager, prenom_manager, equipe, poste_de_manager) VALUES(%s, %s, %s, %s, %s);'''
            self.cur.execute(query,[(obj.getManagerId(), obj.getNomManager(), obj.getPrenomManager(), obj.getEquipe(), obj.getPosteManager()) for obj in objInsList])
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount != 0 else 0
        except Exception as e:
            print(f"Erreur_ManagersDAO.insererUn() ::: {e}")
            self.cur.connection.rollback()
            return 0

    def trouverUn(self, cleTrouv) -> Managers:
        try:
            query = '''SELECT * FROM managers WHERE equipe_id = %s;'''
            self.cur.execute(query, (cleTrouv,))
            res = self.cur.fetchone()

            if res:
                m = Managers()
                m.setManagerId(res[0])
                m.setNomManager(res[1])
                m.setPrenomManager(res[2])
                m.setEquipe(res[3])
                m.setPosteManager(res[4])

                return m
            else: 
                return None
            
        except Exception as e:
            print(f"Erreur_ManagersDAO.trouverUn() ::: {e}")

        
    def trouverTout(self) -> list[Managers]:
        try: 
            query = '''SELECT * FROM managers;'''
            self.cur.execute(query)
            res = self.cur.fetchall()

            liste_managers = []

            if len(res) > 0:

                for r in res:
                    m = Managers()
                    m.setManagerId(r[0])
                    m.setNomManager(r[1])
                    m.setPrenomManager(r[2])
                    m.setEquipe(r[3])
                    m.setPosteManager(r[4])

                    liste_managers.append(m)
                return liste_managers
                
            else: 
                return None
        
        except Exception as e:
            print(f"Erreur_ManagersDAO.trouverTout() ::: {e}")
        finally:
            self.cur.close()
            return None
        
    def trouverToutParUn(self, cleTrouv) -> list[Managers]:
        try: 
            query = '''SELECT * from managers WHERE nom_manager = %s && prenom_manager = %s;'''
            self.cur.execute(query, (cleTrouv,))
            res = self.cur.fetchall()

            liste_managers = []

            if len(res) > 0:
                for r in res:
                    m = Managers()
                    m.setManagerId(r[0])
                    m.setNomManager(r[1])
                    m.setPrenomManager(r[2])
                    m.setEquipe(r[3])
                    m.setPosteManager(r[4])

                    liste_managers.append(m)
                
                return liste_managers
            
            else:

                return None
        except Exception as e:
            print(f"Erreur_ManagersDAO.trouverToutParUn ::: {e}")

    def trouverToutParUnLike(self, val) -> list[Managers]:       
        try: 
            query = '''SELECT * from managers WHERE nom_manager LIKE %s && prenom_manager LIKE %s;'''
            self.cur.execute(query, (val,))
            res = self.cur.fetchall()

            liste_managers = []

            if len(res) > 0:
                for r in res:
                    m = Managers()
                    m.setManagerId(r[0])
                    m.setNomManager(r[1])
                    m.setPrenomManager(r[2])
                    m.setEquipe(r[3])
                    m.setPosteManager(r[4])

                    liste_managers.append(m)
                
                return liste_managers
            
            else:

                return None
        except Exception as e:
            print(f"Erreur_ManagersDAO.trouverToutParUn ::: {e}")

    def modifierUn(self, cleAnc, objModif:Managers) -> int:
        try:
            query = '''UPDATE managers SET nom_manager = %s, prenom_managers = %s  WHERE manager_id = %s;'''
            self.cur.execute(query, (objModif.getNomManager(), objModif.getPrenomManager(), cleAnc))
            #подтверждает операцию
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount!=0 else 0
        except Exception as e:
            print(f"Erreur_ManagersDAO.modifierUn() ::: {e}")
            self.cur.connection.rollback()
        finally: 
            self.cur.close()

    def supprimerUn(self, cleSup) -> int:
        try:
            query = '''DELETE FROM managers WHERE manager_id = %s;'''
            self.cur.execute(query, (cleSup,))
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount!=0 else 0
        except Exception as e:
            print(f"Erreur_ManagersDAO.supprimerUn() ::: {e}")
            self.cur.connection.rollback()
        finally:
            self.cur.close()

    def searchPleinText(self, keyword) -> list[Managers]:
        '''
        Effectue une recherche plein texte.

        :param keyword: Le mot-clé de recherche.
        :return: Une liste de résultats de recherche.
        '''
        try:
            query = '''SELECT * FROM managers WHERE nom_manager @@ %s;'''
            self.cur.execute(query, (f"'{keyword}'",))
            res = self.cur.fetchall()

            liste_managers = []

            if len(res) > 0:
                for r in res:
                    manager = Managers()
                    manager.setJoueurID(r[0])
                    manager.setNom(r[1])
                    liste_managers.append(manager)

                return liste_managers

            else:
                return None

        except Exception as e:
            print(f"Erreur_ManagersDAO.searchPleinText() ::: {e}")
        finally:
            self.cur.close()

        
