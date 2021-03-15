# Students
Cerinte 
Folosiți dezvoltarea iterativă bazat pe funcționalități
 Identificați și planificați funcționalități pe 3 iterații
 Folosiți dezvoltare dirijate de teste. Toate funcțiile trebuie testate și specificate
 Folosiți arhitectură stratificată (UI, Controller, Domain, Repository)
 Validați datele – pentru intrări invalide, aplicația sa tipărescă mesaje de eroare corespunzătoare – folosiți
excepții.
 Documentația conține: Enunț, lista de funcționalități, planul de iterații. Pentru fiecare funcționalitate: scenariu de
rulare

P1. Catalog studenți
Facultatea stochează informații despre:
 studenți: <IDStudent>,<nume>
 discipline: <idDisciplină>, <nume>, <profesor>
Creați o aplicație care permite:
 gestionarea listei de studenți si listei de discipline.
 adaugă, șterge, modifică, lista de studenți, listă de discipline
 căutare student, cautarea de disciplină.
 Asignare de note la un student și o disciplină
 Creare de statistici:
 lista de studenți și notele lor la o disciplină dată, ordonat: alfabetic după nume, după notă.
 Primi 20% din studenți ordonat dupa media notelor la toate disciplinele (nume și notă)
  
 Adaugați posibilitatea de a salva datele în fișiere text:
• creați clase repository care salvează în fișier
• modificând în application coordinator aplicația poate funcționa cu
date salvate în memorie sau date salvate în fișiere
Folosiți frameworkul PyUnit pentru testare:
• creați clase TestCase de test (transformați funcțiile de test existente)
• faceți white-box texting pentru fiecare metodă, la o metodă la alegere
faceți black-box testing
