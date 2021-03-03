# Se importan los métodos
from Metodos3 import check_char
from Metodos3 import caps_switch

import string  # Importa string para poder hacer las listas con letras

Alfabeto = list(string.ascii_letters)  # Lista letras en minúscula y mayúscula
AlfabetoM = list(string.ascii_uppercase)  # Lista con las letras en mayúscula
Alfabetom = list(string.ascii_lowercase)  # Lista con las letras en minúscula


def test_checkchar():  # Caso de éxito check_char evaluando todas las letras
    for i in Alfabeto:  # Recorre todo el alfabeto en mayúscula y minúscula
        assert check_char(i) == 0


def test_capsswitch():  # Prueba de la funcion Caps_switch
    n = 0
    h = 0
    for i in AlfabetoM:  # Recorre todo el alfabeto en mayúscula
        assert caps_switch(i) == Alfabetom[n]
        n = n + 1
    for i in Alfabetom:  # Recorre todo el alfabeto en minúscula
        assert caps_switch(i) == AlfabetoM[h]
        h = h + 1


def test_checkcharB2():  # Prueba ERROR#3
    assert check_char("AbCd") == "ERROR #3: Mas de un caracter en el rango A-Z"
    print("AbCd", " : ", check_char("AbCd"))


def test_checkcharC2():  # Prueba ERROR#2
    assert check_char("e.p[") == "ERROR #2: Caracteres fuera del rango A-Z"
    print("e.p[", " : ", check_char("e.p["))


def test_checkcharD2():  # Prueba ERROR#1
    assert check_char(2345) == "ERROR #1: no es un carácter o string"
    print(2345, " : ", check_char(2345))
