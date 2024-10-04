from flask import Flask, render_template, request
import sqlite3
import webbrowser
import threading

# Criação da instância da aplicação Flask
app = Flask(__name__)

# Função para abrir o navegador automaticamente
def open_browser():
    webbrowser.open('http://127.0.0.1:5000')

@app.route("/")
def home():
    # Renderiza o template sem resultado inicialmente
    return render_template("index.html", resultado=None)

@app.route("/código_fonte")
def codigo():
    return render_template("codigo.html")
# Define a rota para lidar com o formulário enviado (com método POST)
@app.route('/button', methods=['POST'])
def submit():
    # Pega os valores do formulário
    numero1 = request.form['numero1']
    numero2 = request.form['numero2']
    operacao = request.form['operacao']
    
    # Inicializa uma variável para o resultado
    resultado = None
    
    # Realiza a operação de soma
    if operacao == "+":
        resultado = f'{numero1} + {numero2} = {float(numero1) + float(numero2)}'
    elif operacao == "-":
        resultado = f'{numero1} - {numero2} = {float(numero1) - float(numero2)}'
    elif operacao == "*":
        resultado = f'{numero1} * {numero2} = {float(numero1) * float(numero2)}'
    elif operacao == "//":
        resultado = f'{numero1} // {numero2} = {float(numero1) // float(numero2)}'
    elif operacao == "/":
        resultado = f'{numero1} / {numero2} = {float(numero1) / float(numero2)}'
    elif operacao == "**":
        resultado = f'{numero1} ** {numero2} = {float(numero1) ** float(numero2)}'
    elif operacao == "%":
        resultado = f'{numero1} % {numero2} = {float(numero1) % float(numero2)}'
    else:
        resultado = f'ERRO: o sinal "{operacao}", não existe!'
    
    # Renderiza o template passando o resultado
    return render_template("index.html", resultado=resultado)

if __name__ == "__main__":
    # Inicia o servidor e abre o navegador em uma nova thread
    threading.Timer(0.1, open_browser).start()
    app.run(debug=True)
