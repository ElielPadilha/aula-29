from flask import Flask, render_template
import pandas as pd
import os

TITULO = os.getenv("TITULO")

app = Flask(__name__)
from flask import Flask, render_template

app = Flask(__name__)

class Livro:
    def __init__(self, titulo, autor, categoria, ano, editora):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.ano = ano
        self.editora = editora
        self.ativo = False
    def ativar(self):
        self.ativo = True
        if self.editora =="":
            return "Livro Sem Editora"

@app.route("/inicio")
def home():
    livro1 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", "Fantasia", 1954, "")
    livro2 = Livro("Dom Casmurro", "Machado de Assis", "Romance", 1899, "Martin Claret")
    livro3 = Livro("O Alquimista", "Paulo Coelho", "Autoajuda", 1988, "Rocco")
    livro3.ativar()
    lista = [livro1, livro2, livro3]
    
    
    df = pd.read_csv("tabela_livros.csv")
    #lista = df["Titulo do Livro"].tolist()
    return render_template("lista.html", titulo=TITULO, lista_de_livros=lista)


@app.route("/curriculo")
def curriculo():
    return render_template("curriculo.html")



if __name__ == "__main__":
    app.run()