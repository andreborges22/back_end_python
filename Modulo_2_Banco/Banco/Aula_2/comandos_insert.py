# importa a biblioteca sqlite
import sqlite3
# faz o tratamento de excecao
try:
    # cria o objeto conexao (con)
    con = sqlite3.Connection("cliente.db")
    # cria o cursor com a conexao (envia comandos)
    cursor = con.cursor()
    # cria uma variavel para armazenar a lista para insercao

    dados_insert = "INSERT INTO cliente (id_cliente,nome,idade) values (8, 'Jose', 20)"
    # dados_insert = "INSERT INTO cliente values (14, 'luigi', 20)"
    cursor.execute(dados_insert)
    #con.commit()
    #dados_insert = "INSERT INTO cliente (id_cliente,nome,idade) values " \
    #               " (9, 'Lucas', 10), "\
    #               " (10, 'Luisa', 5) "
    #cursor.execute(dados_insert)
    #con.commit()

    #dados_insert_placehold = [
    #    (11, 'Mario', 50),
    #    (12, 'Neymar', 30),
    #    (13, 'Messi', 40)
    #]
    # insere no banco via placehold
    #sql_comando_insert = "INSERT INTO cliente (id_cliente,nome,idade) values (?,?,?)"
    #cursor.executemany(sql_comando_insert, dados_insert_placehold)
    # usando o gerenciador de contexto
    # conexão fechada automaticamente
    #with con:
    #    cursor.execute(
    #        "INSERT INTO clientes (id_cliente,nome,idade) values (?,?,?),(14,'Mateus',13)")
except Exception as e:
    con.rollback()
    print(f"Erro: {e}")
else:
    con.commit()
finally:
    # fechando o cursos
    cursor.close()
    # fechando a conexão
    con.close()
