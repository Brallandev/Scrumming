import os

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

clear()

def titulo():
    TITULO = ( 
    '  __    ___ ____  __ __ ___  ___ ___  ___ __ __  __   ___ '+"\n"
    ' (( \  //   || \\ || || ||\\//|| ||\\//|| || ||\ ||  // \\'+"\n"
    '  \\  ((    ||_// || || || \/ || || \/ || || ||\\|| (( ___'+"\n"
    ' \_))  \\__ || \\ \\_// ||    || ||    || || || \||  \\_||'+"\n"
    )
    
    print(TITULO)
    