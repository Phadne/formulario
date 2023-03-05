class Aluguel:

    def __init__(self, id, id_Cliente, id_Livro, data_Aluguel, nome_Cliente, nome_Livro):
        self._id = id
        self._id_Cliente = id_Cliente
        self._id_Livro = id_Livro
        self._data_Aluguel = data_Aluguel
        self._nome_Cliente = nome_Cliente
        self._nome_Livro = nome_Livro


    def imprimirAluguel(self):
        return f'''
    Aluguel:
    ID do Aluguel: {self._id}
    ID do Cliente: {self.id_Cliente}
    Nome do Cliente: {self._nome_Cliente}
    ID do Livro: {self._id_Livro}
    Nome do Livro: {self._nome_Livro}
    Data do Aluguel: {self._data_Alguel}
    '''

    def cadastrarAluguel(self):
        sql = f'''
        INSERT INTO "Aluguel"
        VALUES({self._id}, '{self.id_Cliente}', '{self._id_Livro}', '{self._data_Alguel}')
        '''
        return sql

    def consultarAluguel(self):
        sql = f'''
        SELECT * FROM "Aluguel"
        WHERE "ID" = '{self._id}'
        '''
        return sql
    
    def consultarAluguelporid_Cliente(self):
        sql = f'''
        SELECT * FROM "Aluguel"
        WHERE "ID_Clientes" = '{self.id_Cliente}'
        '''
        return sql
    
    def consultarAluguelporid_Livro(self):
        sql = f'''
        SELECT * FROM "Aluguel"
        WHERE "ID_Livros" = '{self._id_Livro}'
        '''
        return sql

   

    