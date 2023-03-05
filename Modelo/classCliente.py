class Cliente:
    def __init__(self, id, nome, cpf, telefone):
        self._id = id
        self._nome = nome
        self._cpf = cpf
        self._telefone = telefone
    
    def imprimirCliente(self):

        print(f'''
        ID - {self._id}
        Nome - {self._nome}
        CPF - {self._cpf}
        Telefone - {self._telefone}
        ''')

     def imprimirClienteExcluido(self):
         return f'''
        O Cliente selecionado foi excluído!
        '''

    def listarCliente(self):
        sql = f'''
        SELECT * FROM "Cliente"
        WHERE "ID" = '{self._id}'
        '''
        return sql

    def DeletarCliente(self):
        sql = f'''
        DELETE FROM "Cliente"
        WHERE "ID" = {self._id}
        
        '''
        return sql
    
    def consultarAlugueis(self):
        sql = f'''
        SELECT * FROM "Aluguel"
        WHERE "ID_Cliente" = '{self._id}'
        '''
        return sql

    def alterarCliente(self):
        sql = f'''
        UPDATE "Cliente"
        SET "Nome" = '{self._nome}', "CPF" = '{self._cpf}', "Telefone" = '{self._telefone}'
        WHERE "ID" = '{self._id}'
        '''
        return sql

    def inserirCliente(self):
        sql = f'''
        INSERT INTO "Cliente"
        VALUES(default, '{self._nome}', '{self._cpf}','{self._telefone}' )
        
        '''

        return sql