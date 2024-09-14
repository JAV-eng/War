from fastapi import FastAPI
from app.banca import Banca

app = FastAPI()

# Inicialize a aplicação com as rotas da classe Banca
banca_instance = Banca(app)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
