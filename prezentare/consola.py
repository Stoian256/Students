from erori.exceptii import ValidError,RepoError
import random
import string
class UI(object):
        
    def __ui_adauga_student(self,element):
        if len(element)!=3:
            raise ValidError("numar invalid de parametrii!\n")
        id_stud=int(element[1])
        nume=(element[2])
        self.__srv.adauga_student(id_stud,nume)
        print("Student adaugat cu succes!\n")
    
    def __ui_stegre_student(self,element):
        if len(element)!=2:
            raise ValidError("numar invalid de parametrii!\n")
        id_stud=int(element[1])
        self.__srv_nota.sterge_nota_si_student_dupa_id(id_stud)
        print("Student sters cu succes!\n")
        
    def __ui_modifica_student(self,element):
        if len(element)!=3:
            raise ValidError("numar invalid de parametrii!\n")
        id_stud=int(element[1])
        nume=element[2]
        self.__srv.modifica_student(id_stud,nume)
        print("Student modificat cu succes!\n")
    
    def __ui_cauta_dupa_id(self,element):
        if len(element)!=2:
            raise ValidError("numar invalid de parametrii!\n")
        id_stud=int(element[1])
        print(self.__srv.cauta_dupa_id(id_stud))
    
    def __ui_print_studenti(self,element):
        if len(element)!=1:
            raise ValidError("numar invalid de parametrii!\n")
        studenti=self.__srv.get_studenti()
        if len(studenti)==0:
            print("nu exista studenti in lista!\n")
            return 
        for student in studenti:
            print(student)
        print("")
        
    
    def __ui_adauga_disciplina(self,element):
        if len(element)!=4:
            raise ValidError("numar invalid de parametrii!\n")
        id_dis=int(element[1])
        nume=element[2]
        profesor=element[3]
        self.__srv_dis.adauga_disciplina(id_dis,nume,profesor)
        print("Disciplina adaugata cu succes!\n")
    
    def __ui_stegre_disciplina(self,element):
        if len(element)!=2:
            raise ValidError("numar invalid de parametrii!\n")
        id_dis=int(element[1])
        self.__srv_nota.sterge_nota_si_disciplina_dupa_id(id_dis)
        print("Disciplina stearsa cu succes!\n")
        
    def __ui_modifica_disciplina(self,element):
        if len(element)!=4:
            raise ValidError("numar invalid de parametrii!\n")
        id_dis=int(element[1])
        nume=element[2]
        profesor=element[3]
        self.__srv_dis.modifica_disciplina(id_dis,nume,profesor)
        print("Disciplina modificata cu succes!\n")
    
    def __ui_cauta_dis_dupa_id(self,element):
        if len(element)!=2:
            raise ValidError("numar invalid de parametrii!\n")
        id_dis=int(element[1])
        print(self.__srv_dis.cauta_dupa_id(id_dis))
    
    def __ui_print_discipline(self,element):
        if len(element)!=1:
            raise ValidError("numar invalid de parametrii!\n")

        discipline=self.__srv_dis.get_discipline()
        if len(discipline)==0:
            print("nu exista discipline in lista!\n")
            return 
        for disciplina in discipline:
            print(disciplina)
        print("")


    def __ui_add_nota(self,element):
        if len(element)!=5:
            raise ValidError("numar invalid de parametrii!\n")
        id_nota=int(element[1])
        id_student=int(element[2])
        id_dis=int(element[3])
        valoare=float(element[4])
        self.__srv_nota.adauga_nota(id_nota,id_student,id_dis,valoare)
        print("Nota adaugata cu succes!\n")
    
    def __ui_sterge_nota(self,element):
        if len(element)!=2:
            raise ValidError("numar invalid de parametrii!\n")
        id_nota=int(element[1])
        self.__srv_nota.sterge_nota(id_nota)
        print("Nota stearsa cu succes!\n")
        
    def __ui_print_note(self,element):
        if len(element)!=1:
            raise ValidError("numar invalid de parametrii!\n")

        note= self.__srv_nota.get_all_note()
        if len(note)==0:
            print("nu exista note in lista!\n")
            return 
        for nota in note:
            print(nota)
        print("")
    
    def __ui_lista_ordonata(self,element):
        if len(element)!=2:
            raise ValidError("numar invalid de parametrii!\n")
        lista=self.__srv_nota.ordoneaza_lista(element[1])
        if lista==[]:
            print("Nu sunt premianti!")
            return
        print("Lista sortata de note la materia "+element[1]+" este:")
        print ("____________________________")
        print ("Nume".ljust(7)+"Nota")
        for el in lista:
            print (el.getStudentName().ljust(7)+" "+str(el.getGrade()))
        print ("____________________________")
    def __ui_premianti(self,element):
        if(len(element)!=1):
            raise ValidError("numar invalid de parametrii!\n")
        lista=self.__srv_nota.premianti()
        nr=1
        if lista==[]:
            print("Nu sunt premianti!")
            return
        print("Premiantii sunt:")
        print ("Premiu".ljust(7)+"Nume".ljust(7)+"Medie")
         
        for elem in lista:
            nota=elem.getGrade()/elem.getNumar()
            #print(str(nr)+". "+str(elem[0])+" "+str(elem[1])+" "+str(elem[2]))
            print(str(nr)+". ".ljust(5)+elem.getStudentName().ljust(7)+" "+str(nota))
            nr=nr+1
    
    def __ui_numar_note(self,element):
        if(len(element)!=1):
            raise ValidError("numar invalid de parametrii!\n")
        lista=self.__srv_nota.numar_note()
        nr=1

        print ("Pozitie".ljust(7)+"Nume".ljust(7)+"Nr. note")
         
        for elem in lista:
            #print(str(nr)+". "+str(elem[0])+" "+str(elem[1])+" "+str(elem[2]))
            print(str(nr)+". ".ljust(5)+elem.getStudentName().ljust(7)+" "+str(elem.getNumar()))
            nr=nr+1
        
    def __main(self):
        
        print("Se pot da mai multe comenzi separate prin ;")
        print("Meniu Studnet:                                   Meniu Disciplina:                                 Meniu Catalog:")
        print("1. add stud,id_stud,nume                         1. add dis,id_dis,nume,nume profesor              1. add nota,id_nota,id_stud,id_dis,valoare")
        print("2. mod stud,id_stud,nume                         2. mod dis,id_dis,nume,nume profesor              2. print note")
        print("3. sterge stud,id_stud                           3. sterge dis,id_dis                              3. sterge note,id_nota")
        print("4. cauta stud,id_stud                            4. cauta dis,id_dis                               4. ord,nume_materie")                             
        print("5. print studenti                                5. print dis                                      5. premii")
       
    def __get_random_student(self,lungime):
        for i in range(int(lungime[1])):
            id_stud=random.randint(1,500)
            nume=''.join(random.choices(string.ascii_letters,k=random.randint(4,9)))
            prenume=''.join(random.choices(string.ascii_letters,k=random.randint(4,9)))
            nume+=" "+prenume
            self.__srv.adauga_student(id_stud,nume)
                                
    def __init__(self, srv,srv_dis,srv_nota):
        self.__srv = srv
        self.__srv_dis=srv_dis
        self.__srv_nota=srv_nota
        self.__comenzi={
            "add stud":self.__ui_adauga_student,
            "print studenti":self.__ui_print_studenti,
            "sterge stud":self.__ui_stegre_student,
            "mod stud":self.__ui_modifica_student,
            "cauta stud":self.__ui_cauta_dupa_id,
            "add dis":self.__ui_adauga_disciplina,
            "print dis":self.__ui_print_discipline,
            "sterge dis":self.__ui_stegre_disciplina,
            "mod dis":self.__ui_modifica_disciplina,
            "cauta dis":self.__ui_cauta_dis_dupa_id,
            "add nota":self.__ui_add_nota,
            "print note":self.__ui_print_note,
            "sterge note":self.__ui_sterge_nota,
            "random":self.__get_random_student,
            "ord":self.__ui_lista_ordonata,
            "premii":self.__ui_premianti,
            "nr note":self.__ui_numar_note
            
            }
    
        
    
    def run(self):
        while True:
            self.__main()
            cmd=input(">>>")
            lista_comenzi=cmd.split(";")
            
            
            for c in lista_comenzi:
                element=c.split(",")
                if element[0] == "Exit":
                    print ("Exiting...")
                    return
                if element[0]=="random":
                    self.__comenzi[element[0]](element)
                
                elif element[0] in self.__comenzi:
                    try:
                        self.__comenzi[element[0]](element)
                    except ValueError:
                        print("valoare numeric invalida!")
                    except ValidError as ve:
                        print(ve)
                    except RepoError as re:
                        print(re)
                    except Exception as ex:
                        print(ex)
                else:
                    print("Comanda invalida!")
                
                    
                
            
    
    
    
    



