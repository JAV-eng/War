class InsertStrategy:
    async def inserir(self, db, table_name, cartas):
        # Certifique-se de que a lista de campos que você deseja ignorar seja relevante para a tabela
        campos_ignorar = ['vizinhos']  # Adicione mais campos conforme necessário

        # Prepare a consulta, excluindo os campos a serem ignorados
        campos_validos = [field for field in cartas[0].keys() if field not in campos_ignorar]
        query = f"INSERT OR IGNORE INTO {table_name} ({', '.join(campos_validos)}, selecionado) VALUES ({', '.join(['?'] * len(campos_validos))}, 0)"

        for carta in cartas:
            # Obtenha os valores apenas dos campos que não estão na lista de ignorar
            valores = tuple(carta[field] for field in campos_validos)
            await db.execute_query(query, valores)


class SelectStrategy:
    async def selecionar(self, db, table_name, quantidade):
        sql = f"SELECT * FROM {table_name} ORDER BY RANDOM() LIMIT {quantidade}"
        async with db.execute(sql) as cursor:
            return await cursor.fetchall()
