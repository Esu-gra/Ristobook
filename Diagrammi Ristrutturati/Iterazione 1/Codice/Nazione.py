from __future__ import annotations

class _reg_naz:

    class _link:
        _nazione: Nazione # immutabile, sempre noto alla nascita
        _regione: Regione # immutabile, sempre noto alla nascita

        def __init__(self, naz: Nazione, reg: Regione):
            self._nazione = naz
            self._regione = reg
        
        def regione(self) -> Regione:
            return self._regione
        
        def nazione(self) -> Nazione:
            return self._nazione
        
        def __eq__(self, other) -> bool:
            if type(self) != type(other) or hash(self) != hash(other):
                return False
            return (self.nazione(), self.regione()) == (other.nazione(), other.regione())
        
        def __hash__(self) -> int:
            return hash((self.regione(), self.nazione()))   

class Nazione:
    _nome: str
    _regioni: dict[Regione, _reg_naz._link] # non noti alla nascita

    def __init__(self, nome: str) -> None:
        self.set_nome(nome)
        self._regioni = dict()
    
    def nome(self) -> str:
        return self._nome
    
    def regioni(self) -> frozenset[_reg_naz._link]:
        return frozenset(link for link in self._regioni.values())
    
    def regione(self, regione: Regione) -> _reg_naz._link:
        return self._regioni[regione]
    
    def add_link_reg_naz(self, naz: Nazione, reg: Regione) -> None:
        link = _reg_naz._link(self, naz, reg)
        if link.nazione() is not self:
            raise ValueError("Questo link non coinvolge me")
        
        if link.regione() in self._regioni:
            raise KeyError(f"Link duplicato '({self}, {link.regione()})' non consentito")
        
        self._regioni[reg] = link
        reg._add_link_reg_naz(link)
    
    def remove_link_reg_naz(self, link: _reg_naz._link) -> None:
        if link.nazione() is not self:
            raise ValueError("Questo link non coinvolge me")
 
        del self._regioni[link.regione()]
        link.reg()._remove_link_reg_naz(link)

        del link
    
    def set_nome(self, nome: str) -> None:
        if not isinstance(nome, str) or not nome.strip():
            raise ValueError(f"Errore, '{nome}' non valido")
        self._nome = nome

class Regione:
    _nome: str
    _link_reg_naz: _reg_naz._link # [1..1] noto alla nascita

    def __init__(self, nome: str, naz: Nazione) -> None:
        self.set_nome(nome)
        naz.add_regione(self)
        # self.set_link_reg_naz(reg_naz) lo fa nazione

    def nome(self):
        return self._nome
    
    def nazione(self) -> Nazione:
        return self._link_reg_naz.nazione()
    
    def link(self) -> _reg_naz._link:
        return self._link_reg_naz
    
    def set_nome(self, nome: str):
        if not isinstance(nome, str) or not nome.strip():
            raise ValueError(f"Errore, '{nome}' non valido")
        self._nome = nome
    
    def set_link_reg_naz(self, link: _reg_naz._link):
        if link.regione() is not self:
            raise ValueError("Questo link non coinvolge me")
        
        if self._link_reg_naz is not None:
            raise ValueError("Il link è già stato impostato")
        self._link_reg_naz = link
    
    def _remove_link_reg_naz(self):
        del self._link_reg_naz






























class Citta:
    _nome: str

    def __init__(self, nome: str) -> None:
        self.set_nome(nome)
    
    def nome(self) -> str:
        return self._nome
    
    def set_nome(self, nome: str) -> None:
        if not isinstance(nome, str) or not nome.strip():
            raise ValueError(f"Errore, '{nome}' non valido") 
        self._nome = nome



        
        

        