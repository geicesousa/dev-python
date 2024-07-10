from Cliente import Cliente

class PessoaFisica(Cliente):
    
    def __init__(self, cpf, nome, nascimento, endereco):
        super().__init__(endereco)
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = nascimento