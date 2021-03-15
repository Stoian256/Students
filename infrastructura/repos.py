from erori.exceptii import RepoError
from domeniu.entitati import Student,Disciplina,Nota
class RepositoryStudenti(object):
    
    
    def __init__(self):
        self._elems= []
    
    def __len__(self):
# returneaza lungimea 
        return len(self._elems)

    
    def adauga(self, student):
#adauga un student
#date de intrare :student ,un student valid
#ridica exceptie de tipul RepoError cu textul:
#       -elem existent , daca esxista deja un student cu acelasi id
        if student in self._elems:
            raise RepoError("elem existent!\n")
        self._elems.append(student)

    
    def cauta_dupa_id(self, id_stud):
#cauta un student pe baza unu id
#date de intrare: -id_stud ,id-ul studentului care trebuie cautat
#returneaza exceptie de tipul RepoError cu textul:
#       -elem inexistent!, daca nu exista un student cu id-ul dat
        for el in self._elems:
            if el.get_id_stud()==id_stud:
                return el 
        raise RepoError("elem inexistent!\n")
    
    def modifica(self, student_nou):
#modifica un student pe baza studentului nou
#date de intrare :student_nou ,cum arata noul student
#ridica exceptie de tipul RepoError cu textul:
#      -elem inexistent , daca nu exista un student cu acelasi id
        if student_nou not in self._elems:
            raise RepoError("elem inexistent!\n")
        for i in range(len(self._elems)):
            if self._elems[i]==student_nou:
                self._elems[i].set_nume(student_nou.get_nume())
                return 
    
        

    
    def get_all(self):
#returneza studentii
        return self._elems[:]

    
    def sterge_dupa_id(self, id_stud):
#sterge un student pe baza id-ului
#date de intrare:id_stud ,id-ul studentului
#ridica exceptie de tipul RepoError cu textul:
#         -elem inexistent ,daca nu exista un student cu acelasi id
        for i in range(len(self._elems)):
            if self._elems[i].get_id_stud()==id_stud:
                del  self._elems[i]
                return 
        raise RepoError("elem inexistent!\n")
                        
class RepositoryDiscipline(object):
    
    
    def __init__(self):
        self._elems= []
    
    def __len__(self):
#returneza lungimea(nr de discipline)
        return len(self._elems)

    
    def adauga(self,disciplina):
#adauga o disciplina
#date de intrare: disciplina,o disciplina valida
#ridica exceptie de tipul RepoError cu textul:
#       -elem existent , daca esxista deja o diciplina cu acelasi id
        if disciplina in self._elems:
            raise RepoError("elem existent!\n")
        self._elems.append(disciplina)

    
    def cauta_dupa_id(self, id_dis):
#cauta o diciplina pe baza unu id
#date de intrare: -id_dis ,id-ul diciplinei care trebuie cautata
#returneaza exceptie de tipul RepoError cu textul:
#       -elem inexistent!, daca nu exista o diciplina cu id-ul dat
        for el in self._elems:
            if el.get_id_dis()==id_dis:
                return el 
        raise RepoError("elem inexistent!\n")
    
    def cauta_dupa_id_rec(self,id_dis,nr=0):
        if nr>=len(self._elems):
            raise RepoError("elem inexistent!\n")
        if self._elems[nr].get_id_dis()==id_dis:
            return self._elems[nr]
        return self.cauta_dupa_id_rec(id_dis,nr+1)
        
    
    def modifica(self, disciplina_noua):
#modifica o disciplina pe baza diciplinei noi
#date de intrare :diciplina_noua ,cum arata noua diciplina
#ridica exceptie de tipul RepoError cu textul:
#      -elem inexistent , daca nu exista o diciplina cu acelasi id
        if disciplina_noua not in self._elems:
            raise RepoError("elem inexistent!\n")
        for i in range(len(self._elems)):
            if self._elems[i]==disciplina_noua:
                self._elems[i].set_nume(disciplina_noua.get_nume())
                self._elems[i].set_profesor(disciplina_noua.get_profesor())
                return 
    
        

    
    def get_all_dis(self):
#returneza disciplinele
        return self._elems[:]

    
    def sterge_dupa_id(self, id_dis):
#sterge o diciplina pe baza id-ului
#date de intrare:id_dis ,id-ul diciplinei
#ridica exceptie de tipul RepoError cu textul:
#         -elem inexistent ,daca nu exista o diciplina cu acelasi id
        for i in range(len(self._elems)):
            if self._elems[i].get_id_dis()==id_dis:
                del  self._elems[i]
                return 
        raise RepoError("elem inexistent!\n")
                            
        
class RepositoryNote(object):
    
    
    def __init__(self):
        self._elems= []
        self.__repo_stud=RepositoryStudenti
        #repo_dis=RepositoryDiscipline
    
    def __len__(self):
#returneza lungimea
        return len(self._elems)

    
    def adauga(self,nota):
#adauga o nota
#date de intrare: nota,o nota valida
#ridica exceptie de tipul RepoError cu textul:
#       -elem existent , daca esxista deja o nota cu acelasi id
        if nota in self._elems:
            raise RepoError("elem existent!\n")
        self._elems.append(nota)

    
  
    def get_all_note(self):
#returneza notele
        return self._elems[:]

    def sterge_dupa_id(self,id_nota):
#sterge o nota  pe baza id-ului
#date de intrare:id_nota ,id-ul notei
#ridica exceptie de tipul RepoError cu textul:
#         -elem inexistent ,daca nu exista o nota cu acelasi id
        for i in range(len(self._elems)):
            if self._elems[i].cauta_dupa_id_nota()==id_nota:
                del self._elems[i]
                return 
        raise RepoError("elem inexistent!\n")
            
    def cauta_dupa_id(self, id_nota):
#cauta o nota pe baza unu id
#date de intrare: -id_dis ,id-ul notei care trebuie cautata
#returneaza exceptie de tipul RepoError cu textul:
#       -elem inexistent!, daca nu exista o nota cu id-ul dat
        for el in self._elems:
            if el.cauta_dupa_id_nota()==id_nota:
                return el 
        raise RepoError("elem inexistent!\n")
    
             
class FileRepoStudenti(RepositoryStudenti):
    
    
    def __init__(self, txt):
        self.__txt = txt
        RepositoryStudenti.__init__(self)
    

    def __citeste_student_din_fisier(self):
#metoda care citeste studentii din fisier si ii incarca in memorie
        with open(self.__txt,"r") as f:
            self._elems=[]
            lines=f.readlines()
            for line in lines:
                line=line.strip()
                if line !="":
                    parts=line.split(",")
                    student=Student(int(parts[0]),parts[1])
                    self._elems.append(student)
                    
                    
    
    
    def __append_student_in_fisier(self, student):
#metoda care adauga la finalul fisierului de studenti studentul 
#date de intrre:student-studentul care trebuie adaugat in fisier
        with open(self.__txt,"a") as f:
            f.write(str(student.get_id_stud())+","+student.get_nume()+"\n")
    
    
    def adauga(self, student):
#metoda care primeste un sudent si il adauga atat in lista din memori cat si in fisier daca nu exista deja un student cu acelasi id
#date de intrare:student-studentul care trebuie adaugat
#date de iesire:,daca studentul este adaugat cu succes
#ridica exceptie de tipul RepoError cu textul:
#       -elem existent , daca esxista deja un student cu acelasi id
        self.__citeste_student_din_fisier()
        RepositoryStudenti.adauga(self, student)
        self.__append_student_in_fisier(student)
    
    def cauta_dupa_id(self, id_stud):
#cauta un student pe baza unu id
#date de intrare: -id_stud ,id-ul studentului care trebuie cautat
#returneaza exceptie de tipul RepoError cu textul:
#       -elem inexistent!, daca nu exista un student cu id-ul dat
        self.__citeste_student_din_fisier()
        return RepositoryStudenti.cauta_dupa_id(self, id_stud)
    
    def __len__(self):
# returneaza lungimea  (numarul de studenti)
        self.__citeste_student_din_fisier()
        return RepositoryStudenti.__len__(self)
    
    def get_all(self):
#returneaza studentii
        self.__citeste_student_din_fisier()
        return RepositoryStudenti.get_all(self)
        
    def modifica(self, student_nou):
#modifica un student pe baza studentului nou
#date de intrare :student_nou ,cum arata noul student
#ridica exceptie de tipul RepoError cu textul:
#      -elem inexistent , daca nu exista un student cu acelasi id
        self.__citeste_student_din_fisier() 
        RepositoryStudenti.modifica(self, student_nou)
        with open(self.__txt,"w") as f:
            f.write("")
        for el in self._elems:
            self.__append_student_in_fisier(el)
    
    def sterge_dupa_id(self, id_stud):
#sterge un student pe baza id-ului
#date de intrare:id_stud ,id-ul studentului
#ridica exceptie de tipul RepoError cu textul:
#         -elem inexistent ,daca nu exista un student cu acelasi id
        self.__citeste_student_din_fisier()
        RepositoryStudenti.sterge_dupa_id(self, id_stud)
        with open(self.__txt,"w") as f:
            f.write("")
        for el in self._elems:
            self.__append_student_in_fisier(el)


class FileRepoDiscipline(RepositoryDiscipline):
    
    
    def __init__(self, txt):
        self.__txt = txt
        RepositoryDiscipline.__init__(self)
    

    def __citeste_disciplina_din_fisier(self):
#metoda care citeste disciplinele din fisier si le incarca in memorie
        with open(self.__txt,"r") as f:
            self._elems=[]
            lines=f.readlines()
            for line in lines:
                line=line.strip()
                if line !="":
                    parts=line.split(",")
                    disciplina=Disciplina(int(parts[0]),parts[1],parts[2])
                    self._elems.append(disciplina)
                    
                    
    
    
    def __append_disciplina_in_fisier(self, disciplina):
#metoda care adauga la finalul fisierului de discipline disciplina
#date de intrre:disciplina-disciplina care trebuie adaugat in fisier
        with open(self.__txt,"a") as f:
            f.write(str(disciplina.get_id_dis())+","+disciplina.get_nume()+","+disciplina.get_profesor()+"\n")
    
    
    def adauga(self, disciplina):
#adauga o disciplina atat in fisier cat si in lista din memorie
#date de intrare: disciplina,o disciplina valida
#ridica exceptie de tipul RepoError cu textul:
#       -elem existent , daca esxista deja o diciplina cu acelasi id
        self.__citeste_disciplina_din_fisier()
        RepositoryDiscipline.adauga(self, disciplina)
        self.__append_disciplina_in_fisier(disciplina)
    
    def cauta_dupa_id(self, id_dis):
#cauta o diciplina pe baza unu id
#date de intrare: -id_dis ,id-ul diciplinei care trebuie cautata
#returneaza exceptie de tipul RepoError cu textul:
#       -elem inexistent!, daca nu exista o diciplina cu id-ul dat
        self.__citeste_disciplina_din_fisier()
        return RepositoryDiscipline.cauta_dupa_id_rec(self, id_dis)
    
    def __len__(self):
#returneaza lungimea (nr de discipline)
        self.__citeste_disciplina_din_fisier()
        return RepositoryDiscipline.__len__(self)
    
    def get_all_dis(self):
#returneaza disciplinele
        self.__citeste_disciplina_din_fisier()
        return RepositoryDiscipline.get_all_dis(self)
    
    def modifica(self, disciplina_noua):
#modifica o disciplina pe baza diciplinei noi
#date de intrare :diciplina_noua ,cum arata noua diciplina
#ridica exceptie de tipul RepoError cu textul:
#      -elem inexistent , daca nu exista o diciplina cu acelasi id
        self.__citeste_disciplina_din_fisier()     
        RepositoryDiscipline.modifica(self, disciplina_noua)
        with open(self.__txt,"w") as f:
            f.write("")
        for el in self._elems:
            self.__append_disciplina_in_fisier(el)
            
    def sterge_dupa_id(self, id_dis):
#sterge o diciplina pe baza id-ului
#date de intrare:id_dis ,id-ul diciplinei
#ridica exceptie de tipul RepoError cu textul:
#         -elem inexistent ,daca nu exista o diciplina cu acelasi id
        self.__citeste_disciplina_din_fisier()        
        RepositoryDiscipline.sterge_dupa_id(self, id_dis)
        with open(self.__txt,"w") as f:
            f.write("")
        for el in self._elems:
            self.__append_disciplina_in_fisier(el)


class FileRepoNote(RepositoryNote,RepositoryDiscipline,RepositoryStudenti):
    
    
    def __init__(self, txt,FileRepoStudenti,FileRepoDiscipline):
        self.__txt = txt
        RepositoryNote.__init__(self)
        RepositoryDiscipline.__init__(self)
        RepositoryStudenti.__init__(self)
        self.__repo_stud=FileRepoStudenti
        self.__repo_dis=FileRepoDiscipline
                    
                    
    def __citeste_nota_din_fisier(self):
#metoda care citeste notele din fisier si le incarca in memorie
        with open(self.__txt,"r") as f:
            self._elems=[]
            lines=f.readlines()
            for line in lines:
                line=line.strip()
                if line !="":
                    parts=line.split(",")
                    nota=Nota(int(parts[0]),self.__repo_stud.cauta_dupa_id( int(parts[1])),self.__repo_dis.cauta_dupa_id( int(parts[2])),float(parts[3]))
                    self._elems.append(nota)
    
    def __append_nota_in_fisier(self, nota):
#metoda care adauga la finalul fisierului de note nota data
#date de intrre:nota - nota care trebuie adaugat in fisier
        with open(self.__txt,"a") as f:
            f.write(str(nota.cauta_dupa_id_nota())+","+str(nota.get_student().get_id_stud())+","+str(nota.get_disciplina().get_id_dis())+","+str(nota.get_valoare())+"\n")
    
    
    def adauga(self, nota):
#adauga o nota atat in fisier cat si in lista din memorie
#date de intrare: nota,o nota valida
#ridica exceptie de tipul RepoError cu textul:
#       -elem existent , daca esxista deja o nota cu acelasi id
        self.__citeste_nota_din_fisier()
        RepositoryNote.adauga(self, nota)
        self.__append_nota_in_fisier(nota)
    
    def cauta_dupa_id(self, id_nota):
#sterge o nota  pe baza id-ului
#date de intrare:id_nota ,id-ul notei
#ridica exceptie de tipul RepoError cu textul:
#         -elem inexistent ,daca nu exista o nota cu acelasi id
        self.__citeste_nota_din_fisier()
        return RepositoryNote.cauta_dupa_id(self, id_nota)
    
    def __len__(self):
        self.__citeste_nota_din_fisier()
        return RepositoryNote.__len__(self)
    
    def get_all_note(self):
#returneaza notele
        self.__citeste_nota_din_fisier()
        return RepositoryNote.get_all_note(self)
    
    def sterge_dupa_id(self, id_nota):
#cauta o nota pe baza unu id
#date de intrare: -id_dis ,id-ul notei care trebuie cautata
#returneaza exceptie de tipul RepoError cu textul:
#       -elem inexistent!, daca nu exista o nota cu id-ul dat
        self.__citeste_nota_din_fisier()   
        RepositoryNote.sterge_dupa_id(self, id_nota)
        with open(self.__txt,"w") as f:
            f.write("")
        for el in self._elems:
            self.__append_nota_in_fisier(el)