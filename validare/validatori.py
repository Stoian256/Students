from erori.exceptii import ValidError
class ValidatorStudent(object):
    
    
    def valideaza(self, student):
#valideaza un studet
#date de intrare:student ,un student construit
#date de iesire ,daca studentul este valid 
#ridica exceptie de tipul ValidError cu textul :
#           -id invalid! , daca id-ul dat este < 0
#           -nume invalid , daca numele este gol sau contine cifre
        erori=""
        if student.get_id_stud()<1:
            erori+="id invalid!\n"
        if student.get_nume()=="":
            erori+="nume invalid!\n"
        name=student.get_nume()
        for ind in range(0,len(name)):
            if name[ind]>='0'and name[ind]<='9':
                erori+="nume invalid!\n"
                break
        if len(erori)>0:
            raise ValidError(erori)
        
    
class ValidatorDisciplina(object):
    
    
    def valideaza(self, disciplina):
#valideaza o disciplina
#date de intrare:diciplina , o disciplina construita
#date de iesire:, daca disciplina este valida
#ridica exceptie de tipul ValidError cu textul :
#           -id invalid! , daca id-ul dat este < 0
#           -nume invalid , daca numele este gol sau contine cifre
#           -nume profesor invalid , daca numele profesorului este gol sau contine cifre
        erori=""
        if disciplina.get_id_dis()<0:
            erori+="id invalid!\n"
        if disciplina.get_nume()=="":
            erori+="nume invalid!\n"
        name=disciplina.get_nume()
        for ind in range(0,len(name)):
            if name[ind]>='0'and name[ind]<='9':
                erori+="nume invalid!\n"
                break
        if disciplina.get_profesor()=="":
            erori+="profesor invalid!\n"
        prof=disciplina.get_profesor()
        for ind in range(0,len(prof)):
            if prof[ind]>='0'and prof[ind]<='9':
                erori+="profesor invalid!\n"
                break
        if len(erori)>0:
            raise ValidError(erori)

class ValidatorNota(object):
    
    
    def valideaza(self, nota):
#valideaza o nota
#date de intrare:nota , o nota construita
#date de iesire:, daca nota este valida
#ridica exceptie de tipul ValidError cu textul :
#           -id invalid! , daca id-ul dat este < 0
#           -valoare invalida! , daca valoarea notei este <0 sau >10

        erori=""
        if nota.cauta_dupa_id_nota()<0 :
            erori+="id invalid!\n"
        if nota.get_valoare()<0 or nota.get_valoare()>10:
            erori+="valoare invalida!\n"
        
        if len(erori)>0:
            raise ValidError(erori)


