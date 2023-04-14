from flask import Flask

# Déclarer le serveur web via Flask
app = Flask(__name__)

# 
# Mapper l'appel du navigateur à l'url ../ à la réponse : Hello from Flask! 
# 
@app.route('/')
def index():
  return 'Hello from Flask!'

# Démarrer le erveur web
app.run(host='0.0.0.0', port=81)
