from flask import Flask, flash, request, render_template
from spotipy_client import *

# DATOS REQUERIDOS PARA LA AUTENTICACIÓN
REDIRECT_URI = "http://127.0.0.1:5000/api_callback"
SCOPE = 'playlist-modify-private,playlist-modify-public,user-top-read'

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/', methods=["GET","POST"])
def client_auth_form():
	if request.method == "POST":
		CLI_ID = request.form['cl_id']
		CLI_SEC = request.form['cl_secret']
		USERNAME = request.form['username']

		# Realizar autenticación
		sp = SpotipyClient(CLI_ID, CLI_SEC, USERNAME, REDIRECT_URI, SCOPE)

		# Generar Playlist y redireccionar
		sp.create_recommended_playlist()
		flash('¡Playlist creada en Spotify!')
	return render_template('home.html')

if __name__ == "__main__":
	app.run()