# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 16:08:37 2021

@author: UDB
"""

"""
Lang kommentar
"""

# Kort kommentar

"""
Topics: 1) Expressions 2) Data types 3) Variables

Brug SHIFT + ENTER for at afvikle scriptet

Hjælp: https://docs.python.org/3/tutorial/

"""
# Expressions - evalueres til en enkelt værdi
## Simpleste instruktionstype
## Værdier + operatorer
## Resultatet vises kun i konsollen, hvis man anvender print()

# Statements - gør noget, fx print() eller =

2+2 #Expression, evalueres, men vises ikke 
print(2+2) # Statement, printergør noget, printer i konsollen

# Data typer 
## Data typer er forskellige kategorier af data med forskellige egenskaber
## Alle værdier har en datatype
## Data typen kan ses i variabelvinduet
### Integers / hele tal
### Float (floating point) / decimaltal - skrives med punktum!!
### Strings / strenge (af bogstaver) - skrives med ´ ´ eller " "
### Lister indeholder mere end et element - skrives [ , , , ]

# Variabler 
## Vilkårligt navn for en værdi af en hvilken som helst datatype
## Variabler til skrives værdi (assignment function) med '='

a = 1
b = 2.5
c = a + b

d = 'Hello'
e = ' '
f = 'world!'

g = d + e + f #string concatenation (sammenføjning) skrives +
h = d + f
print(g)
print(h)

i = [a,b,c,d,e,f,g,h]
print(i)