from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
import os
import time

app = Flask(__name__)

DB_HOST = os.getenv("DB_HOST", "mysql-service")
DB_NAME = os.getenv("DB_NAME", "pets")
DB_USER = os.getenv("DB_USER", "aluno")
DB_PASSWORD = os.getenv("DB_PASSWORD", "alunos")


def conectar_bd():
    tentativas = 10

    while tentativas > 0:
        try:
            conexao = mysql.connector.connect(
                host=DB_HOST,
                database=DB_NAME,
                user=DB_USER,
                password=DB_PASSWORD
            )

            return conexao

        except mysql.connector.Error as erro:
            print(f"Erro ao conectar: {erro}")

            tentativas -= 1
            time.sleep(3)

    return None


@app.route("/clientes")
def listar_clientes():
    conexao = conectar_bd()

    cursor = conexao.cursor(dictionary=True)

    cursor.execute("SELECT * FROM clientes")

    clientes = cursor.fetchall()

    cursor.close()
    conexao.close()

    return render_template(
        "clientes.html",
        clientes=clientes
    )

@app.route("/clientes/cadastrar", methods = ["GET", "POST"])
def cadastrar_clientes():

    if request.method == "POST":

        name = request.form["nome"]
        telefone = request.form["telefone"]
        email = request.form["email"]

        conexao = conectar_bd()
        cursor = conexao.cursor()

        conexao.commit()

        cursor.close()
        conexao.close()

        return redirect(url_for("listar_clientes"))
    
    return render_template("cadastrar_clientes.html")




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)