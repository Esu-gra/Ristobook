
class Ristorante:

    _nome:str
    _indirizzo:indirizzo
    _partita_iva: partita_iva # immutabile 
    _periodo_chiusura:periodo # noto alla nascita 1..*

    def __init__(self,nome:str,indirizzo:indirizzo,partita_iva:partita_iva,periodo_chiusura:periodo)->None:
        self.set_nome(nome)
        self.set_indirizzo(indirizzo)
        self.partita_iva=partita_iva
        self.set_periodo_chiusura(periodo_chiusura)

    def getNome(self)->str:
        return self._nome
    
    def getInidirizzo(self)->indirizzo:
        return self._indirizzo
    
    def getPartita_iva(self)->partita_iva:
        return self.partita_iva
    
    def getPeriodo_chiusura(self)->periodo:
        return self._periodo_chiusura
    
    def set_nome(self,nome:str)->None:
        self._nome=nome

    def set_indirizzo(self,indirizzo:indirizzo)->None:
        self._indirizzo=indirizzo

    def set_periodo_chiusura(self,periodo_chiusura:periodo)->None:
        self._periodo_chiusura=periodo_chiusura


class Tipocucina:
    nome:str

    def __init__(self,nome:str)->None:

        self.set_nome(nome)


    def set_nome(self,nome:str)->None:
        self.nome=nome
        

    def get_nome(self)->str:
        return self.nome

        
    

        

    