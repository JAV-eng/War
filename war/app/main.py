from fastapi import FastAPI
from war.app.jogo import Jogo

app = FastAPI()


banca_instance = Jogo(app)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
