import sys
sys.path.insert(0, 'C:/Users/ahmed/OneDrive/Bureau/AHMED/PremiereLeague-main')
from dao import ModelDAO
from model.MatchsM import Matchs


class MatchsDAO(ModelDAO.modeleDAO):
    def __init__(self):
        params = ModelDAO.modeleDAO.connect_objet
        self.cur = params.cursor()

    def insererUn(self, objIns: Matchs) -> int:
        try:
            query = '''INSERT INTO matchs (manager_id, match_id, stade, resultat) VALUES(%s, %s, %s, %s);'''
            self.cur.execute(query,( objIns.getMatchId(), objIns.getDate(), objIns.getStade(), objIns.getResultat(),))
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount != 0 else 0
        except Exception as e:
            print(f"Erreur_MatchsDAO.insererUn() ::: {e}")
            self.cur.connection.rollback()
            return 0
        
    def insererToutList(self, objInsList: list[Matchs] = []) -> int:
        try:
            query = '''INSERT INTO matchs (manager_id, match_id, stade, resultat) VALUES(%s, %s, %s, %s);'''
            self.cur.execute(query,[(obj.getMatchId(), obj.getDate(), obj.getStade(), obj.getResultat()) for obj in objInsList])
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount != 0 else 0
        except Exception as e:
            print(f"Erreur_MatchsDAO.insererUn() ::: {e}")
            self.cur.connection.rollback()
            return 0

    def trouverUn(self, cleTrouv) -> Matchs:
        try:
            query = '''SELECT * FROM matchs WHERE match_id = %s;'''
            self.cur.execute(query, (cleTrouv,))
            res = self.cur.fetchone()

            if res:
                m = Matchs()
                m.setMatchId(res[0])
                m.setDate(res[1])
                m.setStade(res[2])
                m.setResultat(res[3])

                return m
            else: 
                return None
            
        except Exception as e:
            print(f"Erreur_MatchsDAO.trouverUn() ::: {e}")

        
    def trouverTout(self) -> list[Matchs]:
        try: 
            query = '''SELECT * FROM matchs;'''
            self.cur.execute(query)
            res = self.cur.fetchall()

            liste_matchs = []

            if len(res) > 0:

                for r in res:
                    m = Matchs()
                    m.setMatchId(r[0])
                    m.setDate(r[1])
                    m.setStade(r[2])
                    m.setResultat(r[3])

                    liste_matchs.append(m)
                return liste_matchs
                
            else: 
                return None
        
        except Exception as e:
            print(f"Erreur_MatchsDAO.trouverTout() ::: {e}")
        finally:
            self.cur.close()
            return None
        
    def trouverToutParUn(self, cleTrouv) -> list[Matchs]:
        try: 
            query = '''SELECT * from matchs WHERE date = %s;'''
            self.cur.execute(query, (cleTrouv,))
            res = self.cur.fetchall()

            liste_matchs = []

            if len(res) > 0:
                for r in res:
                    m = Matchs()
                    m.setMatchId(r[0])
                    m.setDate(r[1])
                    m.setStade(r[2])
                    m.setResultat(r[3])

                    liste_matchs.append(m)
                
                return liste_matchs
            
            else:

                return None
        except Exception as e:
            print(f"Erreur_MatchsDAO.trouverToutParUn ::: {e}")

    def trouverToutParUnLike(self, val) -> list[Matchs]:       
        try: 
            query = '''SELECT * from matchs WHERE date LIKE %s;'''
            self.cur.execute(query, (val,))
            res = self.cur.fetchall()

            liste_matchs = []

            if len(res) > 0:
                for r in res:
                    m = Matchs()
                    m.setMatchId(r[0])
                    m.setDate(r[1])
                    m.setStade(r[2])
                    m.setResultat(r[3])

                    liste_matchs.append(m)
                
                return liste_matchs
            
            else:

                return None
        except Exception as e:
            print(f"Erreur_ManagersDAO.trouverToutParUn ::: {e}")

    def modifierUn(self, cleAnc, objModif:Matchs) -> int:
        try:
            query = '''UPDATE matchs SET date = %s WHERE match_id = %s;'''
            self.cur.execute(query, (objModif.getNomManager(), objModif.getPrenomManager(), cleAnc))
            #подтверждает операцию
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount!=0 else 0
        except Exception as e:
            print(f"Erreur_MatchsDAO.modifierUn() ::: {e}")
            self.cur.connection.rollback()
        finally: 
            self.cur.close()

    def supprimerUn(self, cleSup) -> int:
        try:
            query = '''DELETE FROM matchs WHERE match_id = %s;'''
            self.cur.execute(query, (cleSup,))
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount!=0 else 0
        except Exception as e:
            print(f"Erreur_MatchsDAO.supprimerUn() ::: {e}")
            self.cur.connection.rollback()
        finally:
            self.cur.close()

    def searchPleinText(self, keyword) -> list[Matchs]:
        '''
        Effectue une recherche plein texte.

        :param keyword: Le mot-clé de recherche.
        :return: Une liste de résultats de recherche.
        '''
        try:
            query = '''SELECT * FROM matchs WHERE date_match @@ %s;'''
            self.cur.execute(query, (f"'{keyword}'",))
            res = self.cur.fetchall()

            liste_matchs = []

            if len(res) > 0:
                for r in res:
                    match = Matchs()
                    match.setMatchID(r[0])
                    match.setDate(r[1])
                    liste_matchs.append(match)

                return liste_matchs

            else:
                return None

        except Exception as e:
            print(f"Erreur_MatchsDAO.searchPleinText() ::: {e}")
        finally:
            self.cur.close()
        
