class Student:
    
    
    def __init__(self, id_stud, nume):
        self.__id_stud = id_stud
        self.__nume = nume

    def get_id_stud(self):
#metoda getter pentru a accesa id-ul studentului
#returneaza id-ul studentului
        return self.__id_stud


    def get_nume(self):
#metoda getter pentru a accesa numele studentului
#returneaza id-ul studentului
        return self.__nume


    def set_nume(self, value):
#metoda setter pentru a accesasi modifica numele studentului
        self.__nume = value
    
    def __str__(self):
#metoda care returneza un string cu id-ul si numele studentului
        return str(self.__id_stud)+" "+self.__nume 
    def __eq__(self,other):
#metoda care verifica daca doi studenti sunt identici,au acelasi id
        return self.__id_stud==other.__id_stud 

class Disciplina:
    
    
    def __init__(self, id_dis, nume,profesor):
        self.__id_dis = id_dis
        self.__nume = nume
        self.__profesor = profesor

    def get_id_dis(self):
#metoda getter pentru a accesa id-ul diciplinei
#returneaza id-ul diciplinei
        return self.__id_dis


    def get_nume(self):
#metoda getter pentru a accesa numele diciplinei
#returneaza numele diciplinei
        return self.__nume

    def get_profesor(self):
#metoda getter pentru a accesa numele profesorului
#returneaza numele profesorului
        return self.__profesor
    
    def set_nume(self, value):
#metoda setter pentru a accesasi modifica numele disciplinei
        self.__nume = value
        
    def set_profesor(self, value):
#metoda setter pentru a accesasi modifica numele profesorului
        self.__profesor = value
    
    def __str__(self):
#metoda care returneza un string cu id-ul , numele disciplinei, nuleme profesorului
        return str(self.__id_dis)+" "+self.__nume +" "+self.__profesor
    
    def __eq__(self,other):
#metoda care verifica daca doua dscipline sunt identici,au acelasi id
        return self.__id_dis==other.__id_dis 

class Nota:
    
    
    def __init__(self, id_nota, student, disciplina, valoare):
        self.__id_nota = id_nota
        self.__student = student
        self.__disciplina = disciplina
        self.__valoare = valoare
      
    def cauta_dupa_id_nota(self):
#metoda getter pentru a accesa id-ul notei
#returneaza id-ul notei
        return self.__id_nota


    def get_student(self):
#metoda getter pentru a accesa studentul
#returneaza studentul
        return self.__student

    def get_disciplina(self):
#metoda getter pentru a accesa disciplina
#returneaza disciplina
        return self.__disciplina
    
    def get_valoare(self):
#metoda getter pentru a accesa valoarea notei
#returneaza valoarea notei
        return self.__valoare
    
    def set_valoare(self, value):
#metoda setter pentru a accesa si modifica valoarea notei
        self.__valoare = value
    
    def __eq__(self,other):
#metoda care verifica daca doua note sunt identice,au acelasi id
        return self.__id_nota==other.__id_nota
    


class NotaDTO(object):

    
    def __init__(self, id_nota, nume_student, disciplina, valoare):
        self.__id_nota = id_nota
        self.__nume_student = nume_student
        self.__disciplina = disciplina
        self.__valoare = valoare

    def __str__(self):
#returneaza un string cu id-ul notei ,id-ul studentului,id-ul disciplinei si valoarea notei
        return str(self.__id_nota)+" "+self.__nume_student+" "+self.__disciplina+" "+str(self.__valoare)

class StudentGrade:
    """
      Obiect de transfer
    """
    def __init__(self,stId,nume, discipline, grade):
        self.__stID = stId
        self.__name = nume
        self.__discipline = discipline
        self.__grade = grade
        

    def getStudentID(self):
        """
         metoda getter
        """
        return self.__stID
    def getGrade(self):
        """
         metoda getter
        """
        return self.__grade
    def getDiscipline(self):
        """
         metoda getter
        """
        return self.__discipline

    def getStudentName(self):
        """
         metoda getter
        """
        return self.__name

    def setStudentName(self,n):
        self.__name = n
        

class Premianti:
    """
      Obiect de transfer
    """
    def __init__(self,stId,nume,grade,numar):
        self.__stID = stId
        self.__grade = grade
        self.__name = nume
        self.__numar=numar

    def getStudentID(self):
        """
         metoda getter
        """
        return self.__stID
    def getGrade(self):
        """
         metoda getter
        """
        return self.__grade
    def setGrade(self,g):
        """
         metoda setter
        """
        self.__grade=self.__grade+g
        return self.__grade
    
    def getStudentName(self):
        """
         metoda getter
        """
        return self.__name

    def setStudentName(self,n):
        """
        metoda setter
        """
        self.__name = n
        
    def getNumar(self):
        """
         metoda getter
        """
        return self.__numar

    def setNumar(self,n):
        """
        metoda setter
        """
        self.__numar = n
        
                    
