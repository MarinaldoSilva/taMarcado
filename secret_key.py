from django.core.management.utils import get_random_secret_key

print(get_random_secret_key())


"""random secret key, gera uma chave nova para ser adicionado no nosso .env
cria uma variável com o nome SECRET_KEY='sua chave' e rode o migrate para subir o banco"""