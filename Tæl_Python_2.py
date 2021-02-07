# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 08:54:13 2021

@author: UDB

"""

"""
Funktioner kaldes også subprocedures,og subprocedures (funktionmoduler)
kan gemmes separat, så de kan genbruges. Ydtrykkene 'function call'
og 'call a function' er forkortelser for 'call subprocedure into function'
"""
# Funktioner
## Funktioner skrives altid navn(argument)
## Funktioner er udtryk der dækker over kompleks funktionalitet
## Python har mange prædefinerede funktioner
## Vi kan også selv definere funktioner, hvis vi har brug for at genbruge funktionalitet
## Funktioner kan kendes på de runde parenteser
### print() - printer til konsollen
### input() - konverterer inputtet fra prompten (>>>) til en string
### len() - giver os antallet (som integer) af tegn i en string
### str() - ændrer argumentet datatype til string
### int() - ændrer argumentets datatype til integer
### float() - ændrer argumentets datatype til float
#### Function eller method?? Same but different!!

# Læg mærke til hvordan det er nødvendigt at ændre datatype med str() og int()
# Læg mærke til hvorden operatoren + skifter funktion afhængigt af datatypen

# Læg mærke til at Python ignorerer tomme linjer

#Dette er et program/script dvs. en kodesekvens med en bestemt funtionalitet

print('Hvad hedder du?') #print funktion
mitNavn = input() # variablen mitNavn tilskrives den værdi, der indtastes i konsollen
print('Dejligt at se dig, ' + mitNavn)
print('Dit navn har ' + str(len(mitNavn)) + ' bogstaver')

print('Hvor gammael er du?')
minAlder = input()
print('Så bliver du ' + str(int(minAlder) + 1) + ' til næste år')

