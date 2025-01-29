import os
import dotenv

dotenv.load_dotenv()

# a "URL DO FRONT" é o localhost fornecido pelo front-end. ( Ex: http://localhost:5173 )
config = {
    "client_url": "http://localhost:5173" if os.getenv("ENVIRONMENT") == "dev" else "",
    "mongo_user": os.getenv("MONGO_USER"),
    "mongo_pwd": os.getenv("MONGO_PWD"),
    "user_jwt_secret": os.getenv("USER_JWT_SECRET"),
    "director_jwt_secret": os.getenv("DIRECTOR_JWT_SECRET"),
}

if not config["director_jwt_secret"]:
    raise ValueError("Erro: Variável 'DIRECTOR_JWT_SECRET' não foi carregada do .env")