class CartasRepository:
    def __init__(self, table_name, insert_strategy, select_strategy):
        self.table_name = table_name
        self.insert_strategy = insert_strategy
        self.select_strategy = select_strategy

    async def inserir_cartas(self, db, cartas):
        await self.insert_strategy.inserir(db, self.table_name, cartas)

    async def selecionar_cartas(self, db, quantidade):
        return await self.select_strategy.selecionar(db, self.table_name, quantidade)

    async def set_selecionado(self, db, carta_id):
        async with db.database.cursor() as cursor:
            await cursor.execute(
                f"UPDATE {self.table_name} SET selecionado = 1 WHERE id = ?",
                (carta_id,)
            )
        await db.database.commit()
