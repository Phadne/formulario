class Livro:
    def __init__(self, id, nome, autor, paginas):
        self._id = ID_Livro
        self._nome= nome_Livro
        self._autor = autor
        self._paginas = paginas

    
    def imprimirLivro(self):

        print(f'''
        ID - {self._ID_Livro}
        Nome - {self._nome}
        Autor - {self._autor}
        Número de Páginas: {self._paginas}
        ''')

     def imprimirLivroDeletado(self):
        return f'''
        O Livro selecionado foi excluído!
        '''

   def listarLivros(self):
        
        sql = f'''
        SELECT * FROM "Livros" 
        WHERE "ID" = {self._id}
        
        '''
        return sql
    
    def DeletarLivros(self):

        sql = f'''
        DELETE FROM "Livros"
        WHERE "ID" = {self._id}
        
        '''
        return sql
    
    def alterarLivros(self):

        sql = f'''
        UPDATE "Livros"
        SET "NomeLivro" = '{self._nome}', "Autor" = '{self._autor}', "NumeroPaginas" = '{self._paginas}'
        WHERE "ID" = '{self._id}'
        '''
        return sql
        
    def consultarLivroPorID(self):
        sql = f'''
        SELECT * FROM "Livros"
        WHERE "ID" = '{self._id}'
        '''
        return sql

    def consultarAlugueis(self):
        sql = f'''
        SELECT * FROM "Aluguel"
        WHERE "ID" = '{self._id}'
        '''
        return sql

    def inserirLivro(self):
        sql = f'''
        INSERT INTO "Livros"
        VALUES(default, '{self._nome}', '{self._autor}')
        
        '''

        return sql