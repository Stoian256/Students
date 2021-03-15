from domeniu.entitati import Student,Disciplina,Nota,NotaDTO,StudentGrade,Premianti
from erori.exceptii import ValidError
from test.sortperf import doit
from Tools.demo.sortvisu import bubblesort
class ServiceStudenti(object):
    
    
    def __init__(self, valid, repo):
        self.__valid = valid
        self.__repo = repo

    
    def adauga_student(self, id_stud, nume):
#construieste un student pe baza unui id si unui nume 
#verifica daca studentul construit este valid si incearca sa il adauge 
#date de intrare:id_stud- id-ul studentului care trebuie adaugat
#                nume - numele studentului care trebuie adaugat
#date de iesire: -, daca studentul este adaugat cu succes
#ridica exceptie de tipul ValidError cu textul :
#           -id invalid! , daca id-ul dat este < 0
#           -nume invalid , daca numele este gol sau contine cifre
#ridica exceptie de tipul RepoError cu textul :
#           -elem existent! , daca exista deja un student cu acelasi id
        student = Student(id_stud,nume)
        self.__valid.valideaza(student)
        self.__repo.adauga(student)

    def sterge_student(self, id_stud):
#sterge un student pe baza unui id 
#verifica daca id-ul studentului este valid si incearca sa il stearga
#date de intrare:id_stud- id-ul studentului care trebuie sters
#date de iesire: -, daca studentul este sters cu succes
#ridica exceptie de tipul ValidError cu textul :
#           -id invalid! , daca id-ul dat este < 0
#ridica exceptie de tipul RepoError cu textul :
#           -elem inexistent! , daca nu exista  un student cu  id-ul dat
        if id_stud<0:
            raise ValidError("id invalid!\n")
        self.__repo.sterge_dupa_id(id_stud)
    
    def cauta_dupa_id(self, id_stud):
#cauta un student pe baza unui id 
#verifica daca id-ul studentului este valid si incearca sa il caute
#date de intrare:id_stud- id-ul studentului care trebuie sters
#date de iesire: -, daca studentul este gasit cu succes
#ridica exceptie de tipul ValidError cu textul :
#           -id invalid! , daca id-ul dat este < 0
#ridica exceptie de tipul RepoError cu textul :
#           -elem inexistent! , daca nu exista  un student cu  id-ul dat
        if id_stud<0:
            raise ValidError("id invalid!\n")
        return self.__repo.cauta_dupa_id(id_stud)
        
    def modifica_student(self, id_stud, nume):
#modifica un student pe baza unui id si unui nume 
#verifica daca studentul construit este valid si incearca sa modifice studentul cu acelasi id 
#date de intrare:id_stud- id-ul studentului care trebuie modificat
#                nume - numele pe care studentul trebuie sa il aiba
#date de iesire: -, daca studentul este modificat cu succes
#ridica exceptie de tipul ValidError cu textul :
#           -id invalid! , daca id-ul dat este < 0
#           -nume invalid , daca numele este gol sau contine cifre
#ridica exceptie de tipul RepoError cu textul :
#           -elem existent! , daca nu exista deja un student cu acelasi id
        student = Student(id_stud,nume)
        self.__valid.valideaza(student)
        self.__repo.modifica(student)
        
    def get_studenti(self):
#returneaza studentii
        return self.__repo.get_all()
    
    
    
class ServiceDiscipline(object):
    
    
    def __init__(self, valid_dis, repo_dis):
        self.__valid_dis = valid_dis
        self.__repo_dis= repo_dis

    
    def adauga_disciplina(self, id_dis, nume,profesor):
#construieste o disciplina pe baza unui id si unui nume si unui nume de profesor
#verifica daca diciplina construita este valida si incearca sa o adauge 
#date de intrare:id_dis- id-ul disciplinei care trebuie adaugata
#                nume - numele diciplinei care trebuie adaugata
#                profesor - numele profesrului 
#date de iesire: -, daca diciplina este adaugata cu succes
#ridica exceptie de tipul ValidError cu textul :
#           -id invalid! , daca id-ul dat este < 0
#           -nume invalid , daca numele este gol sau contine cifre
#           -nume profesor invalid , daca numele profesorului este gol sau contine cifre
#ridica exceptie de tipul RepoError cu textul :
#           -elem existent! , daca exista deja o diciplina cu acelasi id
        disciplina = Disciplina(id_dis,nume,profesor)
        self.__valid_dis.valideaza(disciplina)
        self.__repo_dis.adauga(disciplina)

    def sterge_disciplina(self, id_dis):
#sterge o disicplina pe baza unui id 
#verifica daca id-ul disciplinei este valid si incearca sa o stearga
#date de intrare:id_dis- id-ul disciplinei care trebuie sterse
#date de iesire: -, daca disciplina este stersa cu succes
#ridica exceptie de tipul ValidError cu textul :
#           -id invalid! , daca id-ul dat este < 0
#ridica exceptie de tipul RepoError cu textul :
#           -elem inexistent! , daca nu exista  o disiciplina cu  id-ul dat
        if id_dis<0:
            raise ValidError("id invalid!\n")
        self.__repo_dis.sterge_dupa_id(id_dis)
    
    def cauta_dupa_id(self, id_dis):
#cauta o diciplina pe baza unui id 
#verifica daca id-ul diciplinei este valid si incearca sa caute diciplina
#date de intrare:id_dis- id-ul diciplinei care trebuie sterse
#date de iesire: -, daca diciplina este gasita cu succes
#ridica exceptie de tipul ValidError cu textul :
#           -id invalid! , daca id-ul dat este < 0
#ridica exceptie de tipul RepoError cu textul :
#           -elem inexistent! , daca nu exista o disciplina cu  id-ul dat
        if id_dis<0:
            raise ValidError("id invalid!\n")
        return self.__repo_dis.cauta_dupa_id(id_dis)
        
    def modifica_disciplina(self, id_dis, nume,profesor):
#modifica o diciplina pe baza unui id , unui nume si unui nume de profesor
#verifica daca diciplina construita este valida si incearca sa modifice diciplina cu acelasi id 
#date de intrare:id_dis- id-ul disciplinei care trebuie modificata
#                nume - numele diciplinei care trebuie modificata
#                profesor - numele profesrului 
#date de iesire: -, daca diciplina este modificata cu succes
#ridica exceptie de tipul ValidError cu textul :
#           -id invalid! , daca id-ul dat este < 0
#           -nume invalid , daca numele este gol sau contine cifre
#ridica exceptie de tipul RepoError cu textul :
#           -elem existent! , daca nu exista deja un student cu acelasi id
        disciplina = Disciplina(id_dis,nume,profesor)
        self.__valid_dis.valideaza(disciplina)
        self.__repo_dis.modifica(disciplina)
        
    def get_discipline(self):
#returneaza diciplinele
        return self.__repo_dis.get_all_dis()
    
    
    
class ServiceNota(object):
    
    
    def __init__(self, valid_nota, repo_nota, repo_stud,repo_dis):
        self.__valid_nota = valid_nota
        self.__repo_nota = repo_nota
        self.__repo_stud = repo_stud
        self.__repo_dis = repo_dis
       

    
    def adauga_nota(self, id_nota,id_stud,id_dis,valoare):
#construieste o nota pe baza urmatoarelor: id_nota,id_stud,id_dis,valoare 
#verifica daca nota construita este valida si incearca sa o adauge 
#date de intrare:id_nota- id-ul notei
#                id_stud- id-ul studentului 
#                id_dis- id-ul disciplinei
#                valoare- valoarea notei
#date de iesire: -, daca nota este adaugata cu succes
#ridica exceptie de tipul ValidError cu textul :
#           -id invalid! , daca id-ul notei dat este < 0
#           -valoare invalida! , daca valoarea notei este este <0 sau >10
#ridica exceptie de tipul RepoError cu textul :
#           -elem existent! , daca exista deja o nota cu acelasi id
        student=self.__repo_stud.cauta_dupa_id(id_stud)
        materie=self.__repo_dis.cauta_dupa_id(id_dis)
        nota= Nota(id_nota,student,materie,valoare)
        self.__valid_nota.valideaza(nota)
        self.__repo_nota.adauga(nota)
    def get_all_note(self):
#preia catalogul cu note si afiseaza returneaza nota sub forma : id-ul notei ,id-ul studentului,id-ul disciplinei si valoarea notei
        self.__repo_dis.get_all_dis()
        self.__repo_stud.get_all()
        note=self.__repo_nota.get_all_note()
    
        note_dtos=[]
        for nota in note:
            id_nota=nota.cauta_dupa_id_nota()
            nume_student=nota.get_student().get_nume()
            #nume_student=self.__repo_stud.cauta_dupa_id(nota.get_student().get_id_stud()).get_nume()
            disciplina=nota.get_disciplina().get_nume()
            valoare=nota.get_valoare()
            nota_dto=NotaDTO(id_nota,nume_student,disciplina,valoare)
            note_dtos.append(nota_dto) 
        return note_dtos   


    def sterge_nota_si_student_dupa_id(self,id_stud):
#sterge o nota si un student pe baza unui id 
#date de intrare:id_stud- id-ul studentului a carui nota trebuie stersa
#date de iesire: -, daca nota este stearsa cu succes
#ridica exceptie de tipul ValidError cu textul :
#           -id invalid! , daca id-ul dat este < 0
#ridica exceptie de tipul RepoError cu textul :
#           -elem inexistent! , daca nu exista  o nota cu  id-ul dat
        if id_stud<0:
            raise ValidError("id invalid!\n")
        note=self.__repo_nota.get_all_note()
        for nota in note:
            if nota.get_student().get_id_stud()==id_stud:
                self.__repo_nota.sterge_dupa_id(nota.cauta_dupa_id_nota())
        self.__repo_stud.sterge_dupa_id(id_stud)

    def sterge_nota_si_disciplina_dupa_id(self,id_dis):
#sterge o nota si o disciplina pe baza unui id 
#date de intrare:id_dis- id-ul disciplinei a carui nota trebuie stersa
#date de iesire: -, daca nota este stearsa cu succes
#ridica exceptie de tipul ValidError cu textul :
#           -id invalid! , daca id-ul dat este < 0
#ridica exceptie de tipul RepoError cu textul :
#           -elem inexistent! , daca nu exista  o nota cu  id-ul dat
        if id_dis<0:
            raise ValidError("id invalid!\n")
        note=self.__repo_nota.get_all_note()
        for nota in note:
            if nota.get_disciplina().get_id_dis()==id_dis:
                self.__repo_nota.sterge_dupa_id(nota.cauta_dupa_id_nota())
        self.__repo_dis.sterge_dupa_id(id_dis)
                
    
    def sterge_nota(self,id_nota):
#sterge o nota pe baza unui id 
#date de intrare:id_nota- id-ul notei care trebuie stersa
#date de iesire: -, daca nota este stearsa cu succes
#ridica exceptie de tipul ValidError cu textul :
#           -id invalid! , daca id-ul dat este < 0
#ridica exceptie de tipul RepoError cu textul :
#           -elem inexistent! , daca nu exista  o nota cu  id-ul dat
        if id_nota<0:
            raise ValidError("id invalid!\n")
        self.__repo_nota.sterge_dupa_id(id_nota)
   
    def crteriu_note_materie(self,x,y):
        if x.getStudentName() == y.getStudentName():
            return x.getGrade() > y.getGrade()
        else:
            return x.getStudentName() < y.getStudentName()
    def bubbleSort(self,l,n=None,cmp=None,reverse=False):
        sort=False 
        while not sort:
            sort=True 
            for i in range (len(l)-1):
                if reverse==False:
                    if cmp(l[i+1],l[i]):
                        l[i],l[i+1]=l[i+1],l[i]
                        sort=False
                    
                        
                elif reverse==True:
                    if cmp(l[i+1],l[i]):
                        l[i],l[i+1]=l[i+1],l[i]
                        sort=False 
            
        return l
    
    def bubbleSortRec(self,l,n=None,key=None,reverse=False):
 
        if n is None:
            n = len(l)-1
 
        if n == 0:
            return l
        
        for i in range(n):
            if reverse==False:
                if key(l[i+1])<key(l[i]):
                    l[i],l[i+1]=l[i+1],l[i]
            elif reverse==True:
                if key(l[i+1])>key(l[i]):
                    l[i],l[i+1]=l[i+1],l[i]
        
        return self.bubbleSortRec(l, n-1, key, reverse)             
            

        
    def shellSort(self,array,key,reverse):

    
        n=len(array)
        interval = n // 2
        while interval > 0:
            for i in range(interval, n):
                temp = array[i]
                j = i
                if reverse==True:
                    while j >= interval and key(array[j - interval]) < key(temp):
                        array[j] = array[j - interval]
                        j -= interval
                elif reverse==False:
                    while j >= interval and key(array[j - interval]) > key(temp):
                        array[j] = array[j - interval]
                        j -= interval

                array[j] = temp
            interval //= 2
        return array
    
    def ordoneaza_lista(self,materie):
#ordoneaza lista de note de la o materie 
#sortarea se face dupa numele studentului astfel incat sa fie crescator lexicografic ,iar in caz de egalitatea al doilea criterieu esyte nota
#date de intrare:materie - materea dupa care se va sorta lista
#date de iesire: -lista, lista de note de la materia materie sortata
#ridica exceptie de tipul ValidError cu textul :
#           -id invalid! , daca id-ul dat este < 0
#ridica exceptie de tipul ValodError cu textul :
#           -materie invalida , daca materia contine cifre
#ridica exceptie de tipul Exception cu textul :
#           -Nu exista o astfel de disciplina! , daca disciplina nu este in lista de discipline
        if materie=="":
            raise ValidError("materie invalida!\n")
            
        for ind in range(0,len(materie)):
            if materie[ind]>='0'and materie[ind]<='9':
                raise ValidError("materie invalida!\n")
        dis=self.__repo_dis.get_all_dis()
        ok=0
        for el in dis:
            if el.get_nume()==materie:
                ok=1
        if ok==0:
            raise Exception("Nu exista o astfel de disciplina!")
        note=self.__repo_nota.get_all_note()
        rez = []
        for el in note:
            if str(el.get_disciplina().get_nume())==str(materie):
                el = StudentGrade(el.get_student().get_id_stud(),el.get_student().get_nume(),el.get_disciplina(),el.get_valoare())
                rez.append(el)
        
        #ls=sorted(rez,key=lambda studentGrade: studentGrade.getGrade(),reverse=False)
        #ls=sorted(ls,key=lambda studentGrade: studentGrade.getStudentName(),reverse=False)
        
        ls=self.bubbleSort(rez,cmp =lambda x,y:self.crteriu_note_materie(x, y),reverse=False)
        
        #ls=self.bubbleSortRec(rez,key =lambda studentGrade: studentGrade.getGrade(),reverse=False)
        #ls=self.bubbleSortRec(ls,key = lambda studentGrade: studentGrade.getStudentName(),reverse=False)
        
        #ls=self.shellSort(rez,key =lambda studentGrade: studentGrade.getGrade(),reverse=False)
        #ls=self.shellSort(ls,key = lambda studentGrade: studentGrade.getStudentName(),reverse=False)
        
        return ls

    def premianti(self):
#returneaza lista premiantiilor: primii 20% dintre studentii din lista cu media la toate materiile ordonati descrescator dupa nota
#date de intrare: ,
#date de iesire: -lista, lista celor 20% (premiantii)

        note=self.__repo_nota.get_all_note()
        rez = []
        
        for el in note:
                el = Premianti(el.get_student().get_id_stud(),el.get_student().get_nume(),el.get_valoare(),1)
                #el=Premianti(el.get_student(),self.__repo_stud.cauta_dupa_id(1).get_nume(),repo_stud.cauta_dupa_id(el.get_student()).get_valoare())
                gasit=0
                for elem in rez:
                
                    if elem.getStudentID()==el.getStudentID():
                        elem.setGrade(el.getGrade())
                        elem.setNumar(elem.getNumar()+1)
                        gasit=1
                if gasit==0:
                    rez.append(el)
        
        #ls=sorted(rez,key=lambda Premianti: Premianti.getStudentName(),reverse=False)
        #ls=sorted(ls,key=lambda Premianti: Premianti.getGrade()/Premianti.getNumar(),reverse=True)

        ls=self.bubbleSortRec(rez,key=lambda Premianti: Premianti.getStudentName(),reverse=False)
        ls=self.bubbleSortRec(ls,key=lambda Premianti: Premianti.getGrade()/Premianti.getNumar(),reverse=True)
        
        #ls=self.shellSort(rez,key=lambda Premianti: Premianti.getStudentName(),reverse=False)
        #ls=self.shellSort(ls,key=lambda Premianti: Premianti.getGrade()/Premianti.getNumar(),reverse=True)
        
        #numar=int(len(ls)/5)
        #ls=ls[:numar]
        return ls
    
    
            
    def numar_note(self):

        note=self.__repo_nota.get_all_note()
        rez = []
        
        for el in note:
                el = Premianti(el.get_student().get_id_stud(),el.get_student().get_nume(),el.get_valoare(),1)
                #el=Premianti(el.get_student(),self.__repo_stud.cauta_dupa_id(1).get_nume(),repo_stud.cauta_dupa_id(el.get_student()).get_valoare())
                gasit=0
                for elem in rez:
                
                    if elem.getStudentID()==el.getStudentID():
                        elem.setGrade(el.getGrade())
                        elem.setNumar(elem.getNumar()+1)
                        gasit=1
                if gasit==0:
                    rez.append(el)
        ls=sorted(rez,key=lambda Premianti: Premianti.getStudentName(),reverse=False)
        ls=sorted(ls,key=lambda Premianti: Premianti.getNumar(),reverse=True)
        if len(ls)>5:
            ls=ls[:5]
        return ls
                     
            