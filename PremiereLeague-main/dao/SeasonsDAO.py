import sys
sys.path.insert(0, 'C:/Users/ahmed/OneDrive/Bureau/AHMED/PremiereLeague-main')
from dao import ModelDAO
from model.SeasonsM import Seasons


class SeasonsDAO(ModelDAO.modeleDAO):
    def __init__(self):
        params = ModelDAO.modeleDAO.connect_objet
        self.cur = params.cursor()

    def insererUn(self, objIns: Seasons) -> int:
        try:
            query = '''INSERT INTO seasons season_id VALUES %s;'''
            self.cur.execute(query,( objIns.getSeasonId(),objIns.getAnnee(),))
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount != 0 else 0
        except Exception as e:
            print(f"Erreur_SeasonsDAO.insererUn() ::: {e}")
            self.cur.connection.rollback()
            return 0
        
    def insererToutList(self, objInsList: list[Seasons] = []) -> int:
        try:
            query = '''INSERT INTO seasons season_id VALUES %s;'''
            self.cur.execute(query,[(obj.getSeasonId(), obj.getAnnee()) for obj in objInsList])
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount != 0 else 0
        except Exception as e:
            print(f"Erreur_SeasonsDAO.insererUn() ::: {e}")
            self.cur.connection.rollback()
            return 0

    def trouverUn(self, cleTrouv) -> Seasons:
        try:
            query = '''SELECT * FROM seasons WHERE season_id = %s;'''
            self.cur.execute(query, (cleTrouv,))
            res = self.cur.fetchone()

            if res:
                s = Seasons()
                s.setSeasonId(res[0])
                s.setAnnee(res[1])
                return s
            else: 
                return None
            
        except Exception as e:
            print(f"Erreur_SeasonsDAO.trouverUn() ::: {e}")

        
    def trouverTout(self) -> list[Seasons]:
        try: 
            query = '''SELECT * FROM seasons;'''
            self.cur.execute(query)
            res = self.cur.fetchall()

            liste_seasons = []

            if len(res) > 0:

                for r in res:
                    s = Seasons()
                    s.setSeasonId(r[0])
                    s.setAnnee(r[1])


                    liste_seasons.append(s)
                return liste_seasons
                
            else: 
                return None
        
        except Exception as e:
            print(f"Erreur_SeasonsDAO.trouverTout() ::: {e}")
        finally:
            self.cur.close()
            return None
        
    def trouverToutParUn(self, cleTrouv) -> list[Seasons]:
        try: 
            query = '''SELECT * from seasons WHERE season_id = %s;'''
            self.cur.execute(query, (cleTrouv,))
            res = self.cur.fetchall()

            liste_seasons = []

            if len(res) > 0:
                for r in res:
                    s = Seasons()
                    s.setMatchId(r[0])
                    liste_seasons.append(s)
                
                return liste_seasons
            
            else:

                return None
        except Exception as e:
            print(f"Erreur_SeasonsDAO.trouverToutParUn ::: {e}")

    def trouverToutParUnLike(self, val) -> list[Seasons]:       
        try: 
            query = '''SELECT * from season WHERE annee LIKE %s;'''
            self.cur.execute(query, (val,))
            res = self.cur.fetchall()

            liste_seasons = []

            if len(res) > 0:
                for r in res:
                    s = Seasons()
                    s.setSeasonId(r[0])


                    liste_seasons.append(s)
                
                return liste_seasons
            
            else:

                return None
        except Exception as e:
            print(f"Erreur_SeasonsDAO.trouverToutParUn ::: {e}")


    def searchPleinText(self) -> list:
        '''
        Effectue une recherche plein texte.

        :return: Une liste de résultats de recherche.
        '''
        pass

        
