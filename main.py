'''
Created on Nov 7, 2020

@author: silvi
'''
from testare.teste import Teste
from coordonare.appcoord import AppCoord

if __name__ == '__main__':
    teste=Teste()
    teste.ruleaza_teste()
    appCoord=AppCoord()
    appCoord.start()

    

# Exemplu:
#add stud,1,Alex Andrei;print studenti;add stud,1,Pop Ioan;add stud,2,Pop Ioan;print studenti;add dis,1,Matematica,Popescu George;print dis
#add nota,1,1,1,8.99;print note;add nota,2,2,1,13;add nota,2,2,1,10;print note;sterge stud,1;print studenti;print not
#add stud,1,Alex;add stud,2,Marian;add stud,3,Eu;add stud,4,Gras;add stud,5,Eru;add dis,1,Mate,Pop;add dis,2,Rom,Ana;add dis,3,Fizica,Jol;add nota,1,1,1,7;add nota,2,1,2,9;add nota,3,1,3,10;add nota,4,2,1,10;add nota,5,2,2,10;add nota,6,2,3,10;add nota,7,3,1,5;add nota,8,3,2,1;add nota,9,3,3,3;add nota,10,4,2,7;add nota,11,5,1,3;ord,Mate
#add stud,1,A;add stud,2,M;add stud,3,Eu;add stud,4,Gras;add stud,5,Eru;add dis,1,Mate,Pop;add dis,2,Rom,Ana;add dis,3,Fizica,Jol;add nota,1,1,1,10;add nota,2,1,2,10;add nota,3,1,3,10;add nota,4,2,1,10;add nota,5,2,2,10;add nota,6,2,3,10;add nota,7,3,1,5;add nota,8,3,2,1;add nota,9,3,3,3;add nota,10,4,2,7;add nota,11,5,1,3;premii
#add stud,1,Alex;add stud,2,Marian;add stud,3,Eu;add stud,4,Gras;add stud,5,Eru;add dis,1,Mate,Pop;add dis,2,Rom,Ana;add dis,3,Fizica,Jol;add nota,1,1,1,7;add nota,2,1,2,9;add nota,3,1,3,10;add nota,4,2,1,5;add nota,5,2,2,5;add nota,6,2,3,10;add nota,7,3,1,5;add nota,8,3,2,1;add nota,9,3,3,3;add nota,10,4,2,7;add nota,11,5,1,3;premii