import sys
sys.path.insert(0, 'C:/Users/ahmed/OneDrive/Bureau/AHMED/PremiereLeague-main')
from dao import ModelDAO
from model.ButsM import Buts

class ButsDAO(ModelDAO.modeleDAO):

    def __init__(self):
        '''
        Initialise l'objet ButsDAO en établissant une connexion à la base de données.
        '''
        params = ModelDAO.modeleDAO.connect_objet
        self.cur = params.cursor()

    def insererUn(self, objIns: Buts) -> int:
        '''
        Insère un objet dans la table Buts.

        :param objIns: L'objet à insérer dans la table.
        :return: Le nombre de lignes affectées.
        '''
        try:
            query = '''INSERT INTO buts (but_id, minute, buteur, passeur)
              VALUES(%s, %s, %s, %s);'''
            self.cur.execute(query,(objIns.getButId(), objIns.getMinute(), objIns.getButeur(), objIns.getPasseur(),))
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount != 0 else 0
        except Exception as e:
            print(f"Erreur_ButsDAO.insererUn() ::: {e}")
            self.cur.connection.rollback()  
            return 0

    def insererToutList(self, objInsList: list[Buts] = []) -> int:
        try:
            query = '''INSERT INTO buts (but_id, minute, buteur, passeur)
              VALUES(%s, %s, %s, %s);'''
            self.cur.execute(query, [(obj.getButId(), obj.getMinute(), obj.getButeur(), obj.getPasseur()) for obj in objInsList])
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount != 0 else 0
        except Exception as e:
            print(f"Erreur_ButsDAO.insererUn() ::: {e}")
            self.cur.connection.rollback()  
            return 0       

    def trouverUn(self, cleTrouv) -> Buts:
        '''
        Trouve un objet dans la table Buts par clé.

        :param cleTrouv: La clé de recherche.
        :return: L'objet trouvé.
        '''
        try: 
            query = '''SELECT * FROM buts WHERE but_id = %s;'''
            self.cur.execute(query, (cleTrouv,))
            #возвращает первую запись
            res = self.cur.fetchone()

            if res: 
                but = Buts()
                but.setButId(res[0])
                but.setMinute(res[0])
                but.setButeur(res[0])
                but.setPasseur(res[0])
                return but
            else:
                return None
        except Exception as e:
            print(f"Erreur_ButsDAO.trouverUn() ::: {e}")

    def trouverTout(self) -> list[Buts]:
        '''
        Récupère tous les enregistrements de la table Buts.

        :return: Une liste d'objets Buts.
        '''        
        try:
            query = '''SELECT * FROM buts;'''
            self.cur.execute(query)
            # возвращает все записи
            res = self.cur.fetchall()

            liste_buts = []

            if len(res) > 0:

                for r in res:
                    but = Buts()

                    but.setButId(r[0])
                    but.setMinute(r[1])
                    but.setButeur(r[2])
                    but.setPasseur(r[3])

                    liste_buts.append(but)
                
                return liste_buts
            
            else: 
                return None
            
        except Exception as e:
            print(f"Erreur_ButsDAO.trouverTout() ::: {e}")

    def trouverToutParUn(self, cleTrouv) -> list:
        return super().trouverToutParUn(cleTrouv)
    
    def trouverToutParUnLike(self, cleTrouv) -> list[Buts]:
        '''
        Récupère tous les enregistrements de la table BodyParts par une clé similaire.

        :param cleTrouv: La clé de recherche similaire.
        :return: Une liste d'objets BodyParts.
        '''
        try:
            query = '''SELECT * FROM buts WHERE buteur LIKE %s;'''
            self.cur.execute(query, (cleTrouv,))
            res = self.cur.fetchall()

            liste_buts = []

            if len(res) > 0:

                for r in res:
                    but = Buts()
                    but.setButId(r[0])
                    but.setMinute(r[1])
                    but.setButeur(r[2])
                    but.setPasseur(r[3])

                    liste_buts.append(but)

                return liste_buts
            
            else: 
                return None
            
        except Exception as e:
            print(f"Erreur_ButsDAO.trouverToutParUnLike ::: {e}")

    def modifierUn(self, cleAnc, objModif: Buts) -> int:
        '''
        Modifie un enregistrement dans la table Buts.

        :param cleAnc: La clé de l'enregistrement à
        :param cleAnc: La clé de l'enregistrement à modifier.
        :param objModif: Les nouvelles données à mettre à jour.
        :return: Le nombre de lignes affectées.
        '''
        try: 
            query = '''UPDATE buts SET buteur = %s, passeur = %s WHERE but_id = %s;'''
            self.cur.execute(query, (objModif.getButeur(), cleAnc), (objModif.getPasseur(), cleAnc))
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount != 0 else 0
        
        except Exception as e:
            print(f"Erreur_ButsDAO.modifierUn() ::: {e}")
            self.cur.connection.rollback()
            return 0
        
    def supprimerUn(self, cleSup) -> int:
        '''
        Supprime un enregistrement de la table Buts.

        :param cleSup: La clé de l'enregistrement à supprimer.
        :return: Le nombre de lignes affectées.
        '''
        try: 
            query = f'''DELETE FROM buts WHERE but_id = %s;'''
            self.cur.execute(query, (cleSup,))
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount != 0 else 0
        except Exception as e:
            print(f"Erreur_ButsDAO.supprimerUn() ::: {e}")
            self.cur.connection.rollback()
            return 0
    
    def searchPleinText(self) -> list:
        pass

    def creerUser(self, pwd, usr) -> object:
        pass

    def creerRole(self, role) -> int:
        pass

    def attribuerRole(self, usr, role) -> int:
        pass        


                  


    

