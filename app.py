from flask import Flask, render_template, request


# Criar a aplicação Flask
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def teste():
    return "teste"

if __name__ == '__main__':
    app.run(debug=True)