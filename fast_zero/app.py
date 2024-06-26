from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def read_root():
    msg = {'msg': 'Olá! Mundo'}
    return msg
