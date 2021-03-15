from validare.validatori import ValidatorStudent,ValidatorDisciplina,ValidatorNota
from infrastructura.repos import RepositoryStudenti,RepositoryDiscipline,RepositoryNote
from infrastructura.repos import FileRepoStudenti,FileRepoDiscipline,FileRepoNote
from business.servicii import ServiceStudenti,ServiceDiscipline,ServiceNota
from prezentare.consola import UI


class AppCoord(object):

    
    def __init__(self):
        pass
    
    
    
    
    def start(self):
        while True:
        
            metoda=input("alegeti metoda de persistenta: memorie sau fisier\n>>>")
            if metoda == "memorie":
                repo = RepositoryStudenti()
                repo_dis=RepositoryDiscipline()
                repo_nota=RepositoryNote() 
            elif metoda == "fisier":
                repo=FileRepoStudenti("studenti.txt")
                repo_dis=FileRepoDiscipline("discipline.txt")
                repo_nota=FileRepoNote("note.txt",repo,repo_dis) 
            else:
                print("Comanda invalida!")
                continue
    
            valid = ValidatorStudent()
            valid_dis=ValidatorDisciplina()
            valid_nota=ValidatorNota()
            srv = ServiceStudenti(valid,repo)
            srv_dis=ServiceDiscipline(valid_dis,repo_dis)
            srv_nota=ServiceNota(valid_nota,repo_nota,repo,repo_dis)
            cons= UI(srv,srv_dis,srv_nota)
            cons.run()
    
   



