from flask import Flask

# No Python, um subdiretório que inclui um arquivo __init__.py é considerado um pacote 
# e pode ser importado. 
# Quando você importa um pacote, o __init__.py executa e define quais símbolos o pacote 
# expõe ao mundo externo.
app = Flask(__name__)


from app import routes