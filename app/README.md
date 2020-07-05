# Mega-Tutorial-Flask

 No Python, um subdiretório que inclui um arquivo __init__.py é considerado um pacote e pode ser importado. 
 Quando você importa um pacote, o __init__.py executa e define quais símbolos o pacote expõe ao mundo externo.

 O script dentro do arquivo __init__.py simplesmente cria o objeto de aplicativo como uma instância da classe Flask importada do pacote do Flask. 
 A variável __name__ passada para a classe Flask é uma variável predefinida do Python, definida como o nome do módulo no qual é usada.

 Um aspecto que pode parecer confuso a princípio é que existem duas entidades nomeadas app. 
 O pacote app é definido pelo diretório do aplicativo e pelo script __init__.py, e é mencionado na declaração from app import routes. 
 A variável app é definida como uma instância da classe Flask no script __init__.py, o que a torna um membro do pacote app.

 Outra peculiaridade é que o módulo routes é importado na parte inferior e não na parte superior do script, como sempre. A importação inferior é uma solução alternativa para importações "circulares", um problema comum com aplicativos Flask.
 É necessário que saibamos que o módulo routes precisa importar a variável app definida neste script, portanto, colocar uma das importações recíprocas na parte inferior evita o erro resultante das referências mútuas entre esses dois arquivos.
 
 As rotas (que estarão descritas dentro de routes.py) são os diferentes URLs que o aplicativo implementa. No Flask, os manipuladores das rotas de aplicativos são escritos como funções Python, chamadas funções de exibição. As funções de exibição são mapeadas para um ou mais URLs de rota, para que o Flask saiba qual lógica executar quando um cliente solicitar um determinado URL.

 As linhas "@app.route..." estranhas acima das funções são decoradores, um recurso exclusivo da linguagem Python. Um decorador modifica a função que segue. Um padrão comum com os decoradores é usá-los para registrar funções como retornos de chamada para determinados eventos.
 Nesse caso, o decorador @app.route cria uma associação entre a URL fornecida como argumento e a função.

 Para concluir o aplicativo, você precisa de um script Python no nível superior que defina a instância do aplicativo Flask. Vamos chamar esse script de microblog.py.

 Quando estamos no início do desenvolvimento, o Flask precisa saber como importá-lo, definindo a variável de ambiente FLASK_APP:

 (venv) $ set FLASK_APP=microblog.py

 Com o comando: flask run, nossa aplicação começa a ser executada em http://127.0.0.1:5000/. Que também pode ser acessado por http://localhost:5000/.

 