from flask import Flask, render_template

app = Flask(__name__) #Define a instância do Flask.

@app.route('/') #Definição de rota na barra de pesquisa#
def index(): #Definição de função#
    return render_template('index.html') #Renriza o html "index.html "

app.run(host='127.0.0.1', port=80, debug=True) #Executa o servidor usando os parametros host, porta e debug
