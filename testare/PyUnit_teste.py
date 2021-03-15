import unittest
from domeniu.entitati import Student,Disciplina,Nota,StudentGrade,Premianti,\
    NotaDTO
from validare.validatori import ValidatorStudent, ValidatorDisciplina,ValidatorNota
from erori.exceptii import ValidError,RepoError
from infrastructura.repos import RepositoryStudenti, RepositoryDiscipline ,RepositoryNote,\
    FileRepoStudenti, FileRepoDiscipline, FileRepoNote
from business.servicii import ServiceStudenti, ServiceDiscipline ,ServiceNota

class TestServiceStudenti(unittest.TestCase):
    def setUp(self):
        val=ValidatorStudent()
        self.srv=ServiceStudenti(val,RepositoryStudenti())
        self.srv.adauga_student(1,"A")
    def tearDown(self):
        pass
     
    def testeGetStud(self):
        stud=self.srv.get_studenti()
        self.assertEqual(stud[0].get_id_stud(), 1)
        self.assertTrue(stud[0].get_nume()=="A")
           
    def testAdauga(self):
        self.assertTrue(len(self.srv.get_studenti())==1)
        
        with self.assertRaises(RepoError) as re:
            self.srv.adauga_student(1,"A")
        err=re.exception
        self.assertEqual(str(err),"elem existent!\n")
        
        with self.assertRaises(ValidError) as ve:
            self.srv.adauga_student(-1,"A")
        err=ve.exception
        self.assertEqual(str(err),"id invalid!\n")
        
        self.srv.adauga_student(2,"B")
        stud=self.srv.get_studenti()
        self.assertTrue(len(stud)==2)
        self.assertEqual(stud[1].get_id_stud(), 2)
        self.assertTrue(stud[1].get_nume()=="B")
        
    
    def testModifica(self):
        with self.assertRaises(ValidError) as ve:
            self.srv.modifica_student(-1,"C")
        err=ve.exception
        self.assertEqual(str(err),"id invalid!\n")
    
        with self.assertRaises(RepoError) as re:
            self.srv.modifica_student(3,"C")
        err=re.exception
        self.assertEqual(str(err),"elem inexistent!\n")
            
        self.srv.modifica_student(1,"C")
        stud=self.srv.get_studenti()
        self.assertTrue(len(stud)==1)
        self.assertEqual(stud[0].get_id_stud(), 1)
        self.assertTrue(stud[0].get_nume()=="C")
    def testSterge(self):
        with self.assertRaises(ValidError) as ve:
            self.srv.sterge_student(-1)
        err=ve.exception
        self.assertEqual(str(err),"id invalid!\n")
    
        with self.assertRaises(RepoError) as re:
            self.srv.sterge_student(3)
        err=re.exception
        self.assertEqual(str(err),"elem inexistent!\n")
            
        self.srv.sterge_student(1)
        self.assertTrue(len(self.srv.get_studenti())==0)              
    
    def testCauta(self):
        gasit=self.srv.cauta_dupa_id(1)
        self.assertEqual(gasit.get_nume(),"A")
                
        with self.assertRaises(RepoError) as re:
            self.srv.cauta_dupa_id(3)
        err=re.exception
        self.assertEqual(str(err),"elem inexistent!\n")
        
        with self.assertRaises(ValidError) as ve:
            self.srv.cauta_dupa_id(-1)
        err=ve.exception
        self.assertEqual(str(err),"id invalid!\n")    
        
class TestServiceDiscipline(unittest.TestCase):
    def setUp(self):
        val=ValidatorDisciplina()
        self.srv=ServiceDiscipline(val,RepositoryDiscipline())
        self.srv.adauga_disciplina(1, "Mate", "Pop")
    def tearDown(self):
        pass
     
    def testeGetDis(self):
        dis=self.srv.get_discipline()
        self.assertEqual(dis[0].get_id_dis(), 1)
        self.assertTrue(dis[0].get_nume()=="Mate")
        self.assertTrue(dis[0].get_profesor()=="Pop")
           
    def testAdauga(self):
        self.assertTrue(len(self.srv.get_discipline())==1)
        
        with self.assertRaises(RepoError) as re:
            self.srv.adauga_disciplina(1,"Mate", "Pop")
        err=re.exception
        self.assertEqual(str(err),"elem existent!\n")
        
        with self.assertRaises(ValidError) as ve:
            self.srv.adauga_disciplina(-1, "Mate", "Pop")
        err=ve.exception
        self.assertEqual(str(err),"id invalid!\n")
        
        self.srv.adauga_disciplina(2,"Rom","Ana")
        dis=self.srv.get_discipline()
        self.assertTrue(len(dis)==2)
        self.assertEqual(dis[1].get_id_dis(), 2)
        self.assertTrue(dis[1].get_nume()=="Rom")
        self.assertTrue(dis[1].get_profesor()=="Ana")
        
    
    def testModifica(self):
        with self.assertRaises(ValidError) as ve:
            self.srv.modifica_disciplina(-1,"Fizica","Mircea")
        err=ve.exception
        self.assertEqual(str(err),"id invalid!\n")
    
        with self.assertRaises(RepoError) as re:
            self.srv.modifica_disciplina(3,"Geografie","Alin")
        err=re.exception
        self.assertEqual(str(err),"elem inexistent!\n")
            
        self.srv.modifica_disciplina(1,"Fizica","Sergiu")
        dis=self.srv.get_discipline()
        self.assertTrue(len(dis)==1)
        self.assertEqual(dis[0].get_id_dis(), 1)
        self.assertTrue(dis[0].get_nume()=="Fizica")
        self.assertTrue(dis[0].get_profesor()=="Sergiu")
        
    def testSterge(self):
        with self.assertRaises(ValidError) as ve:
            self.srv.sterge_disciplina(-1)
        err=ve.exception
        self.assertEqual(str(err),"id invalid!\n")
    
        with self.assertRaises(RepoError) as re:
            self.srv.sterge_disciplina(3)
        err=re.exception
        self.assertEqual(str(err),"elem inexistent!\n")
            
        self.srv.sterge_disciplina(1)
        self.assertTrue(len(self.srv.get_discipline())==0)              
    
    def testCauta(self):
        gasit=self.srv.cauta_dupa_id(1)
        self.assertEqual(gasit.get_nume(),"Mate")
        self.assertEqual(gasit.get_profesor(),"Pop")
                
        with self.assertRaises(RepoError) as re:
            self.srv.cauta_dupa_id(3)
        err=re.exception
        self.assertEqual(str(err),"elem inexistent!\n")
        
        with self.assertRaises(ValidError) as ve:
            self.srv.cauta_dupa_id(-1)
        err=ve.exception
        self.assertEqual(str(err),"id invalid!\n")  
        
class TestServiceNote(unittest.TestCase):
    def setUp(self):     
        
        val=ValidatorNota()
        repo_nota = RepositoryNote()
        self.repo_dis = RepositoryDiscipline()
        self.repo_stud = RepositoryStudenti()
        self.srv_nota=ServiceNota(val,repo_nota,self.repo_stud,self.repo_dis)
        student=Student(1,"A")
        self.repo_stud.adauga(student)
        student=Student(2,"B")
        self.repo_stud.adauga(student)
        disciplina=Disciplina(1,"Mate","Pop")
        self.repo_dis.adauga(disciplina)
        self.srv_nota.adauga_nota(1,1,1,8.99)
        
    def tearDown(self):
        pass
     
    def testeGetNote(self):
        note=self.srv_nota.get_all_note()
        nota=note[0]
        self.assertEqual(str(nota),"1 A Mate 8.99")
        
           
    def testAdauga(self):
        self.assertTrue(len(self.srv_nota.get_all_note())==1)
        
        with self.assertRaises(RepoError) as re:
            self.srv_nota.adauga_nota(1,1,1,9)
        err=re.exception
        self.assertEqual(str(err),"elem existent!\n")
        
        with self.assertRaises(ValidError) as ve:
            self.srv_nota.adauga_nota(-1, 1, 1,11)
        err=ve.exception
        self.assertEqual(str(err),"id invalid!\nvaloare invalida!\n")
        
        with self.assertRaises(ValidError) as ve:
            self.srv_nota.adauga_nota(-1, 1, 1,-11)
        err=ve.exception
        self.assertEqual(str(err),"id invalid!\nvaloare invalida!\n")
        
        self.srv_nota.adauga_nota(2,2,1,10)
        note=self.srv_nota.get_all_note()
        self.assertTrue(len(note)==2)
        nota=note[1]
        self.assertEqual(str(nota),"2 B Mate 10")
        
    
    def testStergeNota(self):
        with self.assertRaises(ValidError) as ve:
            self.srv_nota.sterge_nota(-1)
        err=ve.exception
        self.assertEqual(str(err),"id invalid!\n")
    
        with self.assertRaises(RepoError) as re:
            self.srv_nota.sterge_nota(4)
        err=re.exception
        self.assertEqual(str(err),"elem inexistent!\n")
            
        self.srv_nota.sterge_nota(1)
        note=self.srv_nota.get_all_note()
        self.assertTrue(len(note)==0)
    def testStergeNota_Student(self):
        with self.assertRaises(ValidError) as ve:
            self.srv_nota.sterge_nota_si_student_dupa_id(-1)
        err=ve.exception
        self.assertEqual(str(err),"id invalid!\n")
    
        with self.assertRaises(RepoError) as re:
            self.srv_nota.sterge_nota_si_student_dupa_id(4)
        err=re.exception
        self.assertEqual(str(err),"elem inexistent!\n")
        
        self.srv_nota.sterge_nota_si_student_dupa_id(1)
        note=self.srv_nota.get_all_note()
        self.assertTrue(len(note)==0)
        stud=self.repo_stud.get_all()
        self.assertTrue(len(stud)==1)
        
        self.assertEqual(stud[0].get_id_stud(), 2)
        self.assertTrue(stud[0].get_nume()=="B")
    
    def testStergeNota_Disciplina(self):
        with self.assertRaises(ValidError) as ve:
            self.srv_nota.sterge_nota_si_disciplina_dupa_id(-1)
        err=ve.exception
        self.assertEqual(str(err),"id invalid!\n")
    
        with self.assertRaises(RepoError) as re:
            self.srv_nota.sterge_nota_si_disciplina_dupa_id(4)
        err=re.exception
        self.assertEqual(str(err),"elem inexistent!\n")
        
        self.srv_nota.sterge_nota_si_disciplina_dupa_id(1)
        note=self.srv_nota.get_all_note()
        self.assertTrue(len(note)==0)
        dis=self.repo_dis.get_all_dis()
        self.assertTrue(len(dis)==0)  
    
class TestServiceNote1(unittest.TestCase):
    
    def setUp(self):     
        
        val=ValidatorNota()
        repo_nota = RepositoryNote()
        self.repo_dis = RepositoryDiscipline()
        self.repo_stud = RepositoryStudenti()
        self.srv_nota=ServiceNota(val,repo_nota,self.repo_stud,self.repo_dis)
        student=Student(1,"A")
        self.repo_stud.adauga(student)
        student=Student(3,"C")
        self.repo_stud.adauga(student)
        student=Student(4,"D")
        self.repo_stud.adauga(student)
        student=Student(5,"D")
        self.repo_stud.adauga(student)
        student=Student(6,"O")
        self.repo_stud.adauga(student)
        disciplina=Disciplina(1,"Mate","Pop")
        self.repo_dis.adauga(disciplina)
        disciplina=Disciplina(2,"Rom","Ana")
        self.repo_dis.adauga(disciplina)
        self.srv_nota.adauga_nota(1,1,1,8.99)
        self.srv_nota.adauga_nota(3,3,1,10)
        self.srv_nota.adauga_nota(4,4,1,7)
        self.srv_nota.adauga_nota(5,5,1,6)
        
        self.srv_nota.adauga_nota(6,3,2,10)
        self.srv_nota.adauga_nota(7,4,2,7)
        self.srv_nota.adauga_nota(8,5,2,6)
        self.srv_nota.adauga_nota(9,6,2,5)
    
    def tearDown(self):
        pass                  
    
    def testOrdoneaza(self):
        materie="Mat77"
        with self.assertRaises(ValidError) as ve:
            self.srv_nota.ordoneaza_lista(materie)
        err=ve.exception
        self.assertEqual(str(err),"materie invalida!\n")
        
        materie=""
        with self.assertRaises(ValidError) as ve:
            self.srv_nota.ordoneaza_lista(materie)
        err=ve.exception
        self.assertEqual(str(err),"materie invalida!\n")
        
        materie="Fizica"
        with self.assertRaises(Exception) as re:
            self.srv_nota.ordoneaza_lista(materie)
        err=re.exception
        self.assertEqual(str(err),"Nu exista o astfel de disciplina!")
        
        rez=self.srv_nota.ordoneaza_lista("Mate")
        self.assertEqual(rez[0].getStudentName(), "A")
        self.assertTrue(rez[0].getGrade()==8.99)
        
        self.assertEqual(rez[1].getStudentName(), "C")
        self.assertTrue(rez[1].getGrade()==10)
        
        self.assertEqual(rez[2].getStudentName(), "D")
        self.assertTrue(rez[2].getGrade()==6)
       
        self.assertEqual(rez[3].getStudentName(), "D")
        self.assertTrue(rez[3].getGrade()==7) 
        
        
    def testPremii(self):
    
        
        rez=self.srv_nota.premianti()
        self.assertEqual(rez[0].getStudentName(), "C")
        self.assertTrue(rez[0].getGrade()/rez[0].getNumar()==10)

class TestDomeniu(unittest.TestCase):
    def setUp(self):     
        self.student=Student(2,"A")   
        self.alt_student = Student(2,"")
        self.disciplina=Disciplina(1,"Mate","Pop")
        self.alta_dis = Disciplina(1,"","")
        self.nota=Nota(1,self.student,self.disciplina,10)
        self.alta_nota = Nota(1,self.student,self.disciplina,7)
        self.studentGrade=StudentGrade(2,"A",self.disciplina,10)
        self.premiant=Premianti(2,"A",26.8,3)
        self.notaDTO=NotaDTO(1,"A","Mate",7)
        
    
    def tearDown(self):
        pass                  
    
    
    def testStudent(self):
        self.assertTrue(self.student.get_id_stud()==2)
        self.assertTrue(self.student.get_nume()=="A")
        self.assertTrue(str(self.student)=="2 A") 
        self.student.set_nume("B")
        self.assertTrue(self.student.get_nume()=="B")  
        self.assertTrue(self.student==self.alt_student)     
    
    def testDisciplina(self):
        self.assertTrue(self.disciplina.get_id_dis()==1)
        self.assertTrue(self.disciplina.get_nume()=="Mate")
        self.assertTrue(self.disciplina.get_profesor()=="Pop")
        self.assertTrue(str(self.disciplina)=="1 Mate Pop")  
        self.disciplina.set_nume("Fizica")
        self.disciplina.set_profesor("Lelcu")
        self.assertTrue(self.disciplina.get_nume()=="Fizica")
        self.assertTrue(self.disciplina.get_profesor()=="Lelcu")
        self.assertTrue(self.disciplina==self.alta_dis)  
    
    def testNota(self):
        self.assertTrue(self.nota.cauta_dupa_id_nota()==1)
        self.assertTrue(self.nota.get_student()==self.student)
        self.assertTrue(self.nota.get_disciplina()==self.disciplina)
        self.assertTrue(self.nota.get_valoare()==10)
        self.nota.set_valoare(7)
        self.assertTrue(self.nota.get_valoare()==7)
        self.assertTrue(self.nota==self.alta_nota)  
    
    def notaDTO(self):
        self.assertTrue(str(self.notaDTO)=="1 Vlad mate 7")
        
        
    def testStudentGrade(self):
        self.assertTrue(self.studentGrade.getStudentID()==2)
        self.assertTrue(self.studentGrade.getGrade()==10)
        self.assertTrue(self.studentGrade.getDiscipline()==self.disciplina)
        self.assertTrue(self.studentGrade.getStudentName()=="A")
        self.studentGrade.setStudentName("M")
        self.assertTrue(self.studentGrade.getStudentName()=="M")  
        
    def testPremianti(self):
        self.assertTrue(self.premiant.getStudentID()==2)
        self.assertTrue(self.premiant.getGrade()==26.8)
        self.premiant.setGrade(4)
        self.assertTrue(self.premiant.getGrade()==30.8)
        self.assertTrue(self.premiant.getStudentName()=="A")
        self.premiant.setStudentName("M")
        self.assertTrue(self.premiant.getStudentName()=="M") 
        self.assertTrue(self.premiant.getNumar()==3)
        self.premiant.setNumar(5)
        self.assertTrue(self.premiant.getNumar()==5)
         
        
class TestValidare(unittest.TestCase):
    def setUp(self):     
        self.val_stud=ValidatorStudent()
        self.stud_rau=Student(-34,"")
        self.stud_rau1=Student(3,"Ana7")
        
        self.val_dis=ValidatorDisciplina()
        self.dis_rea=Disciplina(-34,"","")
        self.dis_rea1=Disciplina(-34,"Ma7","Po7")
        
        self.val_nota=ValidatorNota()
        student=Student(1,"Vlad")
        disciplina=Disciplina(1,"mate","popescu")
        self.nota_rea=Nota(-34,student,disciplina,11)
        self.nota_rea1=Nota(-34,student,disciplina,-11)
        
        
    def tearDown(self):
        pass
     
    def testeValidareStudent(self):
        with self.assertRaises(ValidError) as ve:
            self.val_stud.valideaza(self.stud_rau)
        err=ve.exception
        self.assertEqual(str(err),"id invalid!\nnume invalid!\n")
        
        with self.assertRaises(Exception) as ve:
            self.val_stud.valideaza(self.stud_rau1)
        err=ve.exception
        self.assertEqual(str(err),"nume invalid!\n")
    
    def testeValidareDisciplina(self):    
        with self.assertRaises(Exception) as ve:
            self.val_dis.valideaza(self.dis_rea)
        err=ve.exception
        self.assertEqual(str(err),"id invalid!\nnume invalid!\nprofesor invalid!\n")
        
        with self.assertRaises(Exception) as ve:
            self.val_dis.valideaza(self.dis_rea1)
        err=ve.exception
        self.assertEqual(str(err),"id invalid!\nnume invalid!\nprofesor invalid!\n")
    
    def testeValidareNota(self):    
        with self.assertRaises(Exception) as ve:
            self.val_nota.valideaza(self.nota_rea)
        err=ve.exception
        self.assertEqual(str(err),"id invalid!\nvaloare invalida!\n")
        
        with self.assertRaises(ValidError) as ve:
            self.val_nota.valideaza(self.nota_rea1)
        err=ve.exception
        self.assertEqual(str(err),"id invalid!\nvaloare invalida!\n")
        
class TestRepo(unittest.TestCase):
    
    def setUp(self):
        self.repo_stud = RepositoryStudenti()
        self.student=Student(1,"A")
        self.student_nou=Student(1,"B")
        self.student_nou_rau=Student(4,"B")
        
        self.repo_dis = RepositoryDiscipline()
        self.disciplina=Disciplina(2,"Mate","Maria")
        self.disciplina_noua=Disciplina(2,"Mate","Lelcu")
        self.disciplina_noua_rea=Disciplina(4,"Mate","Andrei")
        
        self.repo_note = RepositoryNote()
        self.nota=Nota(1,self.student,self.disciplina,10)
    
    def tearDown(self):
        pass
    
    def TestRepoStud(self):
        self.assertTrue(len(self.repo_stud)==0)
        self.repo_stud.adauga(self.student)
        self.assertTrue(len(self.repo_stud)==1)
        gasit= self.repo_stud.cauta_dupa_id(1)
        self.assertTrue(gasit.get_nume()=="A")
        
        with self.assertRaises(RepoError) as re:
            self.repo_stud.adauga(self.student)
        err=re.exception
        self.assertEqual(str(err),"elem existent!\n")
        
        with self.assertRaises(RepoError) as re:
            self.repo_stud.cauta_dupa_id(4)
        err=re.exception
        self.assertEqual(str(err),"elem inexistent!\n")       
        
        self.repo_stud.modifica(self.student_nou)
        gasit= self.repo_stud.cauta_dupa_id(1)
        assert(gasit.get_nume()=="B")
        
        with self.assertRaises(RepoError) as re:
            self.repo_stud.modifica(self.student_nou_rau)
        err=re.exception
        self.assertEqual(str(err),"elem inexistent!\n") 
        
        alll = self.repo_stud.get_all()
        self.assertTrue(len(self.repo_stud)==1)
        self.assertTrue(alll[0].get_nume=="B")
        self.repo_stud.sterge_dupa_id(1)
        self.assertTrue(len(self.repo_stud)==0)
        
        with self.assertRaises(RepoError) as re:
            self.repo_stud.sterge_dupa_id(1)
        err=re.exception
        self.assertEqual(str(err),"elem inexistent!\n") 
    
    def TestRepoDis(self):
                
        self.assertTrue(len(self.repo_dis)==0)
        self.repo_stud.adauga(self.disciplina)
        self.assertTrue(len(self.repo_dis)==1)
        gasit= self.repo_dis.cauta_dupa_id(2)
        self.assertTrue(gasit.get_nume()=="Mate")
        self.assertTrue(gasit.get_profesor()=="Maria")
        
        with self.assertRaises(RepoError) as re:
            self.repo_dis.adauga(self.disciplina)
        err=re.exception
        self.assertEqual(str(err),"elem existent!\n")
        
        with self.assertRaises(RepoError) as re:
            self.repo_dis.cauta_dupa_id(4)
        err=re.exception
        self.assertEqual(str(err),"elem inexistent!\n")       
        
        self.repo_dis.modifica(self.disciplina_noua)
        gasit= self.repo_dis.cauta_dupa_id(1)
        assert(gasit.get_nume()=="Mate")
        assert(gasit.get_profesor()=="Lelcu")
        
        with self.assertRaises(RepoError) as re:
            self.repo_dis.modifica(self.disciplina_noua_rea)
        err=re.exception
        self.assertEqual(str(err),"elem inexistent!\n") 
        
        alll = self.repo_dis.get_all()
        self.assertTrue(len(self.repo_dis)==1)
        self.assertTrue(alll[0].get_nume=="Mate")
        self.assertTrue(alll[0].get_profesor=="Lelcu")
        self.repo_dis.sterge_dupa_id(1)
        self.assertTrue(len(self.repo_dis)==0)
        
        with self.assertRaises(RepoError) as re:
            self.repo_dis.sterge_dupa_id(1)
        err=re.exception
        self.assertEqual(str(err),"elem inexistent!\n") 
     
    def TestRepoNota(self):
        
        self.assertTrue(len(self.repo_note)==0)
        self.repo_note.adauga(self.nota)
        self.assertTrue(len(self.repo_note)==1)
        gasit= self.repo_nota.cauta_dupa_id(1)
        self.assertTrue(gasit.get_student()==self.student)
        self.assertTrue(gasit.get_disciplina()==self.disciplina)
        self.assertTrue(gasit.get_valoare()==10)
        
        with self.assertRaises(RepoError) as re:
            self.repo_note.cauta_dupa_id(3)
        err=re.exception
        self.assertEqual(str(err),"elem inexistent!\n")
        
        alll = self.repo_note.get_all()
        self.assertTrue(len(alll)==1)
        self.assertTrue(alll[0].get_student=="A")
        self.assertTrue(alll[0].get_disciplina=="Mate")
        
        with self.assertRaises(RepoError) as re:
            self.repo_note.adauga(self.nota)
        err=re.exception
        self.assertEqual(str(err),"elem existent!\n")
        
        with self.assertRaises(RepoError) as re:
            self.repo_note.cauta_dupa_id(4)
        err=re.exception
        self.assertEqual(str(err),"elem inexistent!\n")
        
        self.repo_note.sterge_nota_dupa_id(1)
        self.assertTrue(len(self.repo_note)==0)
        
        with self.assertRaises(RepoError) as re:
            self.repo_note.sterge_dupa_id(1)
        err=re.exception
        self.assertEqual(str(err),"elem inexistent!\n")
        
class TestFileRepo(unittest.TestCase):
    
    def setUp(self):
        with open("test_studenti.txt","w") as f:
            f.write("")
        self.repo_stud =FileRepoStudenti("test_studenti.txt")
        self.student=Student(1,"A")
        self.student_nou=Student(1,"B")
        self.student_nou_rau=Student(4,"B")
        
        with open("test_discipline.txt","w") as f:
            f.write("")
        self.repo_dis = FileRepoDiscipline("test_discipline.txt")
        self.disciplina=Disciplina(2,"Mate","Maria")
        self.disciplina_noua=Disciplina(2,"Mate","Lelcu")
        self.disciplina_noua_rea=Disciplina(4,"Mate","Andrei")
        
        with open("test_note.txt","w") as f:
            f.write("")
        self.repo_note = FileRepoNote("test_note.txt")
        self.nota=Nota(1,self.student,self.disciplina,10)
    
    def tearDown(self):
        pass
    
    def TestFileRepoStud(self):
        self.assertTrue(len(self.repo_stud)==0)
        self.repo_stud.adauga(self.student)
        self.assertTrue(len(self.repo_stud)==1)
        gasit= self.repo_stud.cauta_dupa_id(1)
        self.assertTrue(gasit.get_nume()=="A")
        
        with self.assertRaises(RepoError) as re:
            self.repo_stud.adauga(self.student)
        err=re.exception
        self.assertEqual(str(err),"elem existent!\n")
        
        with self.assertRaises(RepoError) as re:
            self.repo_stud.cauta_dupa_id(4)
        err=re.exception
        self.assertEqual(str(err),"elem inexistent!\n")       
        
        self.repo_stud.modifica(self.student_nou)
        gasit= self.repo_stud.cauta_dupa_id(1)
        assert(gasit.get_nume()=="B")
        
        with self.assertRaises(RepoError) as re:
            self.repo_stud.modifica(self.student_nou_rau)
        err=re.exception
        self.assertEqual(str(err),"elem inexistent!\n") 
        
        alll = self.repo_stud.get_all()
        self.assertTrue(len(self.repo_stud)==1)
        self.assertTrue(alll[0].get_nume=="B")
        self.repo_stud.sterge_dupa_id(1)
        self.assertTrue(len(self.repo_stud)==0)
        
        with self.assertRaises(RepoError) as re:
            self.repo_stud.sterge_dupa_id(1)
        err=re.exception
        self.assertEqual(str(err),"elem inexistent!\n") 
    
    def TestFileRepoDis(self):
                
        self.assertTrue(len(self.repo_dis)==0)
        self.repo_stud.adauga(self.disciplina)
        self.assertTrue(len(self.repo_dis)==1)
        gasit= self.repo_dis.cauta_dupa_id(2)
        self.assertTrue(gasit.get_nume()=="Mate")
        self.assertTrue(gasit.get_profesor()=="Maria")
        
        with self.assertRaises(RepoError) as re:
            self.repo_dis.adauga(self.disciplina)
        err=re.exception
        self.assertEqual(str(err),"elem existent!\n")
        
        with self.assertRaises(RepoError) as re:
            self.repo_dis.cauta_dupa_id(4)
        err=re.exception
        self.assertEqual(str(err),"elem inexistent!\n")       
        
        self.repo_dis.modifica(self.disciplina_noua)
        gasit= self.repo_dis.cauta_dupa_id(1)
        assert(gasit.get_nume()=="Mate")
        assert(gasit.get_profesor()=="Lelcu")
        
        with self.assertRaises(RepoError) as re:
            self.repo_dis.modifica(self.disciplina_noua_rea)
        err=re.exception
        self.assertEqual(str(err),"elem inexistent!\n") 
        
        alll = self.repo_dis.get_all()
        self.assertTrue(len(self.repo_dis)==1)
        self.assertTrue(alll[0].get_nume=="Mate")
        self.assertTrue(alll[0].get_profesor=="Lelcu")
        self.repo_dis.sterge_dupa_id(1)
        self.assertTrue(len(self.repo_dis)==0)
        
        with self.assertRaises(RepoError) as re:
            self.repo_dis.sterge_dupa_id(1)
        err=re.exception
        self.assertEqual(str(err),"elem inexistent!\n") 
     
    def TestFileRepoNota(self):
        
        self.assertTrue(len(self.repo_note)==0)
        self.repo_note.adauga(self.nota)
        self.assertTrue(len(self.repo_note)==1)
        gasit= self.repo_nota.cauta_dupa_id(1)
        self.assertTrue(gasit.get_student()==self.student)
        self.assertTrue(gasit.get_disciplina()==self.disciplina)
        self.assertTrue(gasit.get_valoare()==10)
        
        with self.assertRaises(RepoError) as re:
            self.repo_note.cauta_dupa_id(3)
        err=re.exception
        self.assertEqual(str(err),"elem inexistent!\n")
        
        alll = self.repo_note.get_all()
        self.assertTrue(len(alll)==1)
        self.assertTrue(alll[0].get_student=="A")
        self.assertTrue(alll[0].get_disciplina=="Mate")
        
        with self.assertRaises(RepoError) as re:
            self.repo_note.adauga(self.nota)
        err=re.exception
        self.assertEqual(str(err),"elem existent!\n")
        
        with self.assertRaises(RepoError) as re:
            self.repo_note.cauta_dupa_id(4)
        err=re.exception
        self.assertEqual(str(err),"elem inexistent!\n")
        
        self.repo_note.sterge_nota_dupa_id(1)
        self.assertTrue(len(self.repo_note)==0)
        
        with self.assertRaises(RepoError) as re:
            self.repo_note.sterge_dupa_id(1)
        err=re.exception
        self.assertEqual(str(err),"elem inexistent!\n")     
   
if __name__ == '__main__':
    unittest.main()