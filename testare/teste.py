from domeniu.entitati import Student,Disciplina,Nota,StudentGrade,Premianti,\
    NotaDTO
from validare.validatori import ValidatorStudent, ValidatorDisciplina,ValidatorNota
from erori.exceptii import ValidError,RepoError
from infrastructura.repos import FileRepoStudenti,RepositoryStudenti, RepositoryDiscipline ,RepositoryNote,FileRepoDiscipline,FileRepoNote
from business.servicii import ServiceStudenti, ServiceDiscipline ,ServiceNota

class Teste(object):
    
    
    def __ruleaza_teste_domeniu(self):
        id_stud=2
        nume="Sergiu"
        student=Student(id_stud,nume)
        assert(student.get_id_stud()==id_stud)
        assert(student.get_nume()==nume)
        assert(str(student)=="2 Sergiu")
        student.set_nume("Andrei")
        assert(student.get_nume()=="Andrei")
        alt_student = Student(id_stud,"")
        assert (student == alt_student)
        
        id_dis=2
        nume="Mate"
        profesor="Maria"
        disciplina=Disciplina(id_dis,nume,profesor)
        assert(disciplina.get_id_dis()==id_dis)
        assert(disciplina.get_nume()==nume)
        assert(disciplina.get_profesor()==profesor)
        assert(str(disciplina)=="2 Mate Maria")
        disciplina.set_nume("Rom")
        disciplina.set_profesor("Pop")
        assert(disciplina.get_nume()=="Rom")
        assert(disciplina.get_profesor()=="Pop")
        alta_dis = Disciplina(id_dis,"","")
        assert (disciplina == alta_dis)
        
        id_nota=1
        student=Student(1,"Vlad")
        disciplina=Disciplina(1,"mate","popescu")
        nota=Nota(1,student,disciplina,10)
        assert(nota.cauta_dupa_id_nota()==id_nota)
        assert(nota.get_student()==student)
        assert(nota.get_disciplina()==disciplina)
        assert(nota.get_valoare()==10)
        nota.set_valoare(7)
        assert(nota.get_valoare()==7)
        alta_nota = Nota(id_nota,student,disciplina,7)
        assert (nota == alta_nota)
        nota.set_valoare(9)
        assert(nota.get_valoare()==9)
        
        notaDTO=NotaDTO(id_nota,student.get_nume(),disciplina.get_nume(),7)
        assert(str(notaDTO)=="1 Vlad mate 7")
        
        
        id_stud=1
        nume="Alex"
        disciplina="Mate"
        valoare=9.55
        studentGrade=StudentGrade(id_stud,nume,disciplina,valoare)
        assert(studentGrade.getStudentID()==id_stud)
        assert(studentGrade.getGrade()==valoare)
        assert(studentGrade.getDiscipline()==disciplina)
        assert(studentGrade.getStudentName()==nume)
        studentGrade.setStudentName("Marian")
        assert(studentGrade.getStudentName()=="Marian")
        
        id_stud=1
        nume="Alex"
        valoare=26.8
        numar=3
        premiant=Premianti(id_stud,nume,valoare,numar)
        assert(premiant.getStudentID()==id_stud)
        assert(premiant.getGrade()==valoare)
        premiant.setGrade(4)
        assert(premiant.getGrade()==valoare+4)
        assert(premiant.getStudentName()==nume)
        premiant.setStudentName("Marian")
        assert(premiant.getStudentName()=="Marian")
        assert(premiant.getNumar()==numar)
        premiant.setNumar(5)
        assert(premiant.getNumar()==5)
        
    
    
    def __ruleaza_teste_validare(self):
        valid=ValidatorStudent()
        student_rau=Student(-34,"")
        try:
            valid.valideaza(student_rau)
            assert(False)
        except Exception as ve:
            assert(str(ve)=="id invalid!\nnume invalid!\n")
        student_rau=Student(3,"Ana7")
        try:
            valid.valideaza(student_rau)
            assert(False)
        except Exception as ve:
            assert(str(ve)=="nume invalid!\n")
            
        
        valid=ValidatorDisciplina()
        disciplina_rea=Disciplina(-34,"","")
        try:
            valid.valideaza(disciplina_rea)
            assert(False)
        except Exception as ve:
            assert(str(ve)=="id invalid!\nnume invalid!\nprofesor invalid!\n")
        disciplina_rea=Disciplina(-34,"Ma5","Pop7")
        try:
            valid.valideaza(disciplina_rea)
            assert(False)
        except Exception as ve:
            assert(str(ve)=="id invalid!\nnume invalid!\nprofesor invalid!\n")
        
         
        valid=ValidatorNota()
        student=Student(1,"Vlad")
        disciplina=Disciplina(1,"mate","popescu")
        nota_rea=Nota(-34,student,disciplina,11)
        try:
            valid.valideaza(nota_rea)
            assert(False)
        except Exception as ve:
            assert(str(ve)=="id invalid!\nvaloare invalida!\n")
        nota_rea=Nota(-34,student,disciplina,-11)
        try:
            valid.valideaza(nota_rea)
            assert(False)
        except Exception as ve:
            assert(str(ve)=="id invalid!\nvaloare invalida!\n")
    
    def __ruleaza_teste_repo(self):
        repo = RepositoryStudenti()
        assert(len(repo)==0)
        id_stud=2
        nume="Sergiu"
        student=Student(id_stud,nume)
        repo.adauga(student)
        assert(len(repo)==1)
        gasit= repo.cauta_dupa_id(id_stud)
        assert(gasit.get_nume()==nume)
        try:
            repo.adauga(student)
            assert(False)
        except RepoError as re:
            assert(str(re)=="elem existent!\n")
        try:
            repo.cauta_dupa_id(id_stud+3)
            assert(False)
        except RepoError as re:
            assert(str(re)=="elem inexistent!\n")
        student_nou=Student(id_stud,"Andrei")
        repo.modifica(student_nou)
        gasit= repo.cauta_dupa_id(id_stud)
        assert(gasit.get_nume()=="Andrei")
        student_nou_rau=Student(id_stud+3,"Andrei")
        try:
            repo.modifica(student_nou_rau)
            assert(False)
        except RepoError as re:
            assert(str(re)=="elem inexistent!\n")
        all = repo.get_all()
        assert(len(all)==1)
        assert(all[0].get_nume()=="Andrei")
        repo.sterge_dupa_id(id_stud)
        assert(len(repo)==0)
        try:
            repo.sterge_dupa_id(id_stud)
            assert(False)
        except RepoError as re:
            assert(str(re)=="elem inexistent!\n")
        
        
        repo = RepositoryDiscipline()
        assert(len(repo)==0)
        id_dis=2
        nume="Mate"
        profesor="Maria"
        disciplina=Disciplina(id_dis,nume,profesor)
        repo.adauga(disciplina)
        assert(len(repo)==1)
        gasit= repo.cauta_dupa_id(id_dis)
        assert(gasit.get_nume()==nume)
        assert(gasit.get_profesor()==profesor)
        try:
            repo.adauga(disciplina)
            assert(False)
        except RepoError as re:
            assert(str(re)=="elem existent!\n")
        try:
            repo.cauta_dupa_id(id_dis+3)
            assert(False)
        except RepoError as re:
            assert(str(re)=="elem inexistent!\n")
        disciplina_noua=Disciplina(id_dis,"Mate","Lelcu")
        repo.modifica(disciplina_noua)
        gasit= repo.cauta_dupa_id(id_dis)
        assert(gasit.get_nume()=="Mate")
        assert(gasit.get_profesor()=="Lelcu")
        disciplina_noua_rea=Disciplina(id_dis+3,"Mate","Andrei")
        try:
            repo.modifica(disciplina_noua_rea)
            assert(False)
        except RepoError as re:
            assert(str(re)=="elem inexistent!\n")
        all = repo.get_all_dis()
        assert(len(all)==1)
        assert(all[0].get_nume()=="Mate")
        assert(all[0].get_profesor()=="Lelcu")
        repo.sterge_dupa_id(id_dis)
        assert(len(repo)==0)
        try:
            repo.sterge_dupa_id(id_dis)
            assert(False)
        except RepoError as re:
            assert(str(re)=="elem inexistent!\n")
    
        
        
        repo = RepositoryNote()
        assert(len(repo)==0)
        id_nota=1
        val=8
        student=Student(2,"Sergiu")
        disciplina=Disciplina(1,"Mate","Popescu")
        nota=Nota(id_nota,student,disciplina,val)
        repo.adauga(nota)
        gasit= repo.cauta_dupa_id(id_nota)
        assert(gasit.get_student()==student)
        assert(gasit.get_disciplina()==disciplina)
        assert(gasit.get_valoare()==val)
        
        try:
            repo.cauta_dupa_id(id_nota+3)
            assert(False)
        except RepoError as re:
            assert(str(re)=="elem inexistent!\n")
            
        assert(len(repo)==1)
        try:
            repo.adauga(nota)
            assert(False)
        except RepoError as re:
            assert(str(re)=="elem existent!\n")
        all = repo.get_all_note()
        assert(len(all)==1)
        repo.sterge_dupa_id(id_nota)
        assert(len(repo)==0)
        try:
            repo.sterge_dupa_id(id_nota)
            assert(False)
        except RepoError as re:
            assert(str(re)=="elem inexistent!\n")
        
            
    def __ruleaza_teste_service(self):
        with open("test_studenti.txt","w") as f:
            f.write("")
        valid=ValidatorStudent()
        repo = FileRepoStudenti("test_studenti.txt")
        srv=ServiceStudenti(valid,repo)
        id_stud = 21
        nume = "Alex"
        srv.adauga_student(id_stud,nume)
        studenti = srv.get_studenti()
        assert(len(studenti)==1)
        try:
            srv.adauga_student(id_stud,nume)
            assert(False)
        except RepoError as re:
            assert(str(re)=="elem existent!\n")
        nume=""
        try:
            srv.adauga_student(-id_stud,nume)
            assert(False)
        except ValidError as ve:
            assert(str(ve)=="id invalid!\nnume invalid!\n")
        
        nume="Ale7"
        try:
            srv.adauga_student(-id_stud,nume)
            assert(False)
        except ValidError as ve:
            assert(str(ve)=="id invalid!\nnume invalid!\n")
        
        try:
            srv.modifica_student(-id_stud,nume)
            assert(False)
        except ValidError as ve:
            assert(str(ve)=="id invalid!\nnume invalid!\n")
        
        nume=""
        try:
            srv.modifica_student(-id_stud,nume)
            assert(False)
        except ValidError as ve:
            assert(str(ve)=="id invalid!\nnume invalid!\n")
        nume="ALex"   
        try:
            srv.modifica_student(id_stud+3,nume)
            assert(False)
        except RepoError as re:
            assert(str(re)=="elem inexistent!\n")
        
        srv.modifica_student(id_stud, "Sergiu")
        studenti = srv.get_studenti()
        assert(len(studenti)==1)
        gasit=srv.cauta_dupa_id(id_stud)
        assert(gasit.get_nume()=="Sergiu")   
        try:
            srv.sterge_student(-id_stud)
            assert(False)
        except ValidError as ve:
            assert(str(ve)=="id invalid!\n")
        
        try:
            srv.sterge_student(id_stud+3)
            assert(False)
        except RepoError as re:
            assert(str(re)=="elem inexistent!\n")
        srv.sterge_student(id_stud)
        studenti = srv.get_studenti()
        assert(len(studenti)==0)
        
        
        
        with open("test_discipline.txt","w") as f:
            f.write("")
        repo = FileRepoDiscipline("test_discipline.txt")
        valid=ValidatorDisciplina()

        srv=ServiceDiscipline(valid,repo)
        id_dis = 12
        nume = "Matematica"
        profesor="Popescu Ioan"
        srv.adauga_disciplina(id_dis, nume, profesor)
        discipline = srv.get_discipline()
        assert(len(discipline)==1)
        try:
            srv.adauga_disciplina(id_dis,nume,profesor)
            assert(False)
        except RepoError as re:
            assert(str(re)=="elem existent!\n")
        nume_rau=""
        prof_rau=""
        try:
            srv.adauga_disciplina(-id_dis,nume_rau,prof_rau)
            assert(False)
        except ValidError as ve:
            assert(str(ve)=="id invalid!\nnume invalid!\nprofesor invalid!\n")
        
        nume_rau="Ma7"
        prof_rau="An7"
        try:
            srv.adauga_disciplina(-id_dis,nume_rau,prof_rau)
            assert(False)
        except ValidError as ve:
            assert(str(ve)=="id invalid!\nnume invalid!\nprofesor invalid!\n")
            
        try:
            srv.modifica_disciplina(-id_stud,nume_rau,prof_rau)
            assert(False)
        except ValidError as ve:
            assert(str(ve)=="id invalid!\nnume invalid!\nprofesor invalid!\n")
        nume_rau=""
        prof_rau=""
        try:
            srv.modifica_disciplina(-id_stud,nume_rau,prof_rau)
            assert(False)
        except ValidError as ve:
            assert(str(ve)=="id invalid!\nnume invalid!\nprofesor invalid!\n")
        
        try:
            srv.modifica_disciplina(id_dis+3,nume,profesor)
            assert(False)
        except RepoError as re:
            assert(str(re)=="elem inexistent!\n")
        
        srv.modifica_disciplina(id_dis, "Analiza","Popescu Ioan")
        discipline = srv.get_discipline()
        assert(len(discipline)==1)
        gasit=srv.cauta_dupa_id(id_dis)
        assert(gasit.get_nume()=="Analiza")   
        assert(gasit.get_profesor()=="Popescu Ioan") 
        try:
            srv.sterge_disciplina(-id_dis)
            assert(False)
        except ValidError as ve:
            assert(str(ve)=="id invalid!\n")
        
        try:
            srv.sterge_disciplina(id_dis+3)
            assert(False)
        except RepoError as re:
            assert(str(re)=="elem inexistent!\n")
        srv.sterge_disciplina(id_dis)
        discipline = srv.get_discipline()
        assert(len(discipline)==0)
        
       
        with open("test_note.txt","w") as f:
            f.write("")
        
        valid=ValidatorNota()
        repo_dis = FileRepoDiscipline("test_discipline.txt")
        repo_stud = FileRepoStudenti("test_studenti.txt")
        repo = FileRepoNote("test_note.txt",repo_stud,repo_dis)
        srv=ServiceNota(valid,repo,repo_stud,repo_dis)
        id_nota=1
        val=8
        student=Student(2,"Sergiu")
        repo_stud.adauga(student)
        disciplina=Disciplina(1,"Mate","Popescu")
        repo_dis.adauga(disciplina)
        srv.adauga_nota(id_nota,2,1,val)
        
        note = srv.get_all_note()
        assert(len(note)==1)
        try:
            srv.adauga_nota(id_nota,2,1,val)
            assert(False)
        except RepoError as re:
            assert(str(re)=="elem existent!\n")
        val=11
        try:
            srv.adauga_nota(-id_nota,2,1,val)
            assert(False)
        except ValidError as ve:
            assert(str(ve)=="id invalid!\nvaloare invalida!\n")
        
        val=-11
        try:
            srv.adauga_nota(-id_nota,2,1,val)
            assert(False)
        except ValidError as ve:
            assert(str(ve)=="id invalid!\nvaloare invalida!\n")
            
        id_nota=2
        val=8
        student=Student(3,"Sergiu")
        repo_stud.adauga(student)
        srv.adauga_nota(id_nota,2,1,val)
        
        id_nota=3
        val=8
        student=Student(2,"Sergiu")
        disciplina=Disciplina(2,"Rom","Popescu")
        repo_dis.adauga(disciplina)
        srv.adauga_nota(id_nota,2,2,val)
        lista=srv.ordoneaza_lista("Mate")
        note = srv.get_all_note()
        assert(len(note)==3)
        assert(len(lista)==2)
        lista=srv.premianti()
        assert(len(lista)==1)

        
    def ruleaza_teste(self):
        self.__ruleaza_teste_domeniu()
        self.__ruleaza_teste_validare()
        self.__ruleaza_teste_repo()
        self.__ruleaza_teste_service()
        
    



