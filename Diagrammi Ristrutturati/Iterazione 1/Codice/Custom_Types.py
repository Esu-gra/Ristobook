import re
from typing import *
from datetime import *
from enum import *

class CodiceFiscale(str):

    def __new__(cls, cf: str | Self) -> Self:

        cff: str = cf.upper().strip()
        
        if re.fullmatch(r"[A-Z]{6}[0-9]{2}[A-Z]{1}[0-9]{2}[A-Z]{1}[0-9]{3}[A-Z]{1}", cf):
            return super().__new__(cls, cff)
        raise ValueError(f"{cff} non è un codice fiscale italiano valido")

class Telefono(str):

    def __new__(cls, tel: str | Self) -> Self:
        
        if re.fullmatch(r"^\d{10}$", tel):
            return super().__new__(cls, tel)
        raise ValueError(f"{tel} non è un numero di telefono italiano valido")
    
class Email:
    def __new__(cls, email: str):

        if not re.fullmatch(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$",email):
              raise ValueError(f"Email '{cls._email}' non valida.")
        
        cls._email = email
    
    def __eq__(self, other):
         raise isinstance(other, Email) and (self._email == other._email)
    
    def __hash__(self):
         return hash(self._email)
    
    def __str__(self):
         return self._email

class Genere(StrEnum):

    uomo = auto()
    donna = auto()

class Voto(int):
    def __new__(cls, voto:int|float|Self)->Self:
        if voto  < 18 or voto > 30:
            raise ValueError(f"Value v == {voto} must be between 18 and 30")
        return int.__new__(cls, voto)

class IntGEZ(int):
    # Tipo di dato specializzato Intero >= 0

    def __new__(cls, v: Self | int | float | str | bool):

        value: int = super().__new__(cls, v)

        if value < 0:
            raise ValueError(f"The value {v} must be greater than zero")
        return value

class IntGZ(int):
    # Tipo di dato specializzato Intero > 0

    def __new__(cls, v: Self | int | float | str | bool):

        value: int = super().__new__(cls, v)

        if value <= 0:
            raise ValueError(f"The value {v} must be greater than zero")
        return value
    
    # Attenzione: in generale la differenza tra interi non dovrebbe essere toccata
    def __sub__(self, other: int | Self) -> Self:
        other_int : int = int(other)
        
        try:
            res: int = int(self) - other_int
            return IntGZ(res)
        except ValueError:
            raise ValueError(f"The difference between {self} and {other} is not an IntGZ")
        
class Indirizzo:
    def __init__(cls, via: str, civico: str, cap: str):
        if not via or not civico:
            raise ValueError(f"Via '{cls.via}' e civico '{cls.civico}' non possono essere vuoti.")
        
        if not (cap.isdigit() and len(cap) == 5):
            raise ValueError(f"CAP '{cls.cap}' deve essere una stringa di 5 cifre numeriche.")

        cls._via = via
        cls._civico = civico
        cls._cap = cap

    def via(self) -> str: 
        return self._via

    def civico(self) -> str: 
        return self._civico

    def cap(self) -> str: 
        return self._cap

    def __eq__(self, other):
        return isinstance(other, Indirizzo) and \
               (self._via, self._civico, self._cap) == (other._via, other._civico, other._cap)

    def __hash__(self):
        return hash((self._via, self._civico, self._cap))

    def __str__(self):
        return f"{self._via}, {self._civico}, {self._cap}"

class PartitaIva:
    def __new__(cls, p_iva:str):
        if not (p_iva.isdigit() and len(p_iva) == 11):
            raise ValueError(f"Partita IVA '{cls._p_iva}' non valida, deve contenere 11 cifre")
        
        cls._p_iva = p_iva

    def __str__(self):
        return self._p_iva
    
    def __eq__(self, other):
        return isinstance(other,PartitaIva) and (self._p_iva == other._p_iva)
    
    def __hash__(self):
        return hash(self._p_iva)


