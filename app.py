from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista para armazenar as tarefas
tarefas = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/editor')
def editor():
    return render_template('editor.html')

@app.route('/portifolio')
def portifolio():
    return render_template('portifolio.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/aninhaysz')
def aninha():
    return render_template('aninhaysz.html')

@app.route('/todo')
def todo():
    return render_template('todo.html', tarefas=tarefas)

@app.route('/adicionar', methods=['POST'])
def adicionar_tarefa():
    nova_tarefa = request.form['novaTarefa']
    if nova_tarefa:
        tarefas.append(nova_tarefa)
    return redirect(url_for('todo'))  # Redireciona para a página de tarefas

@app.route('/remover/<int:indice>')
def remover_tarefa(indice):
    if 0 <= indice < len(tarefas):
        tarefas.pop(indice)  # Remove a tarefa pelo índice
    return redirect(url_for('todo'))

if __name__ == '__main__':
    app.run(debug=True)
