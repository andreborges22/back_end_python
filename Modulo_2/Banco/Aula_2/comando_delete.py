# importa a biblioteca sqlite
import sqlite3
# faz o tratamento de excecao
try:
    # cria o objeto conexao (con)
    con = sqlite3.Connection("cliente.db")
    # cria o cursor com a conexao (envia comandos)
    cursor = con.cursor()
    # cria a variavel que armazena o resultado do sql
    res = cursor.execute("select name from sqlite_master ")
    # imprime o resultado: fetchone para uma linha, fetchall para varias
    print(f"Tabelas do banco cliente.db: {res.fetchone()}")
    # select diretamente
    # res = cursor.execute("select * from cliente")
    # res = cursor.execute("select nome,idade from cliente"
    #                     " where sexo like 'M'"
    #                     " and idade > 40"
    #                     " order by nome"
    #                     " limit 3"
    #                     )

    # select usando o for
    cursor.execute("DELETE FROM cliente where id_cliente = 20")
    # print(res.fetchall())
except Exception as e:
    print(f"Erro: {e}")
else:
    con.commit()
finally:
    # fechando o cursor
    cursor.close()
    # fechando a conexão
    con.close()
