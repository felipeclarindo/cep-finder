from src.modules.search_cep import search_cep # Importando função de buscar cep do pacote modules
from unittest.mock import patch, Mock

def test_valid_cep():
    valid_cep = "01153000"
    result = search_cep(valid_cep)
    assert type(result) == dict

def test_empty_cep():
    invalid_cep = ""
    result = search_cep(invalid_cep)
    assert result == "O Cep não pode ser vazio!"
    
def test_invalid_cep_length():
    invalid_cep = "123"
    result = search_cep(invalid_cep)
    assert result == "Cep Invalido. \nDigite um CEP com 8 digitos numéricos!"
    
def test_invalid_cep_non_numeric():
    invalid_cep = "12345abcdef"
    result = search_cep(invalid_cep)
    assert result == "Cep Invalido. \nDigite um CEP com 8 digitos numéricos!"
