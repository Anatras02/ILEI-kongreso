import os
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
from pyrogram import Client, filters


app = Client("KongresoGDrive", config_file="config/config.ini")
gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

@app.on_message(filters.command("start"))
def start(_,message):
    app.send_message(f"Benvenuto {message.from_user.username}, questo è un bot di utilizzo esclusivo del gruppo di organizazzione del Congresso 2023 a Massa per la gestione dei file")

@app.on_message(filters.document)
def documento(_,message):
    #MI SALVO I NOMI IN VARIABILI
    nome_documento = message.document.file_name
    nome_file = f"file_locali/{nome_documento}"
    #SCARICO IL FILE IN LOCALE
    message.download(nome_file)
    #LO CARICO SU GOOGLE DRIVE
    file = drive.CreateFile({'title': nome_documento})
    file.SetContentFile(nome_file)
    file.Upload()
    #RIMUOVO IL FILE IN LOCALE
    os.remove(nome_file)



app.run()
