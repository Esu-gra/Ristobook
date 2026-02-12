
class Cliente:
    _nome:str   # noto alla nascita
    _cognome:str #noto alla nascita
    _email:email #noto alla nascita


    def __init__(self,nome:str,cognome:str,email:email):
        self.set_nome(nome)
        self.set_cognome(cognome)
        self.set_email(email)


    def getnome(self)->str:
        return self._nome
    
    def getcognome(self)->str:
        return self._cognome
    
    def getemail(self)->email:
        return self._email
    
    def set_nome(self,nome:str)->None:
        self._nome=nome

    def set_cognome(self,cognome:str)->None:
        self._cognome=cognome

    def setemail(self,email:email)->None:
        self._email=email
    