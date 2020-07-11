# Mega-Tutorial-Flask

 Tutorial Flask para desenvolvimento de aplicação Web criado e orientado por Miguel Grinberg.

 Neste tutorial ele irá explicar várias ferramentas ligadas ao Framework Flask, e outras ferramentas de desenvolvimento Web, para que possamos iniciar criações de sistemas de aplicação para Web. 

 Link do tutorial: https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world


Arquivo de Requisitos
Neste ponto, instalei um número razoável de pacotes no ambiente virtual Python. Se você precisar regenerar seu ambiente em outra máquina, terá problemas em lembrar quais pacotes você deve instalar, portanto, a prática geralmente aceita é gravar um arquivo requirements.txt na pasta raiz do seu projeto, listando todas as dependências , junto com suas versões. Produzir esta lista é realmente fácil:

(venv) $ pip freeze > requirements.txt
O pip freezecomando fará o dump de todos os pacotes instalados no seu ambiente virtual no formato correto para o arquivo requirements.txt . Agora, se você precisar criar o mesmo ambiente virtual em outra máquina, em vez de instalar pacotes um por um, poderá executar:

(venv) $ pip install -r requirements.txt