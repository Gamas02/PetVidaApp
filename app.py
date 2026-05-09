from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
import os
import time

app = Flask(__name__)

DB_HOST = os.getenv("DB_HOST", "mysql-service")
DB_NAME = os.getenv("DB_NAME", "pets") #mudar depois
DB_USER = os.getenv("DB_USER", "aluno")
DB_PASSWORD = os.getenv("DB_PASSWORD", "alunos")

@app.route("/")
def home():
    return "Olá"