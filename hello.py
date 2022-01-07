from flask import Flask
from markupsafe import escape
# Biblioteca request implementada pelo Flask
from flask import request

# Iniciando uma aplicação FLASK
# --> >> $env:FLASK_APP = "hello"
# --> >> $env:FLASK_ENV = "development"
# --> >> flask run
app = Flask(__name__)


# Rota básica
# ---------------
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


# Rota básica com variável
# ---------------
@app.route("/<name>")
def hello(name):
    return f"Hello, {name}!"


# Rota com variável username (string) e sanitização (escape())
# ---------------
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'


# Rota com variável e tipo esperado (int)
# ---------------
@app.route('/post/<int:post_id>')
def show_post(post_id):
    # exibe um post com id específica, do tipo int
    return f'Post {post_id}'

# Rota implementando variável methods e tratamento conforme tipo da requisição
@app.route('/login', methods=['GET', 'POST'])
def login():
    # SE O MÉTODO DA REQUISIÇÃO FOR POST
    # if request.method == 'POST':
        # return do_the_login()
    # else:
        # return show_the_login_form()



# Executa a aplicação em modo DEBUG.
# ---------------
if __name__ == '__main__':
    app.run(debug=True)
