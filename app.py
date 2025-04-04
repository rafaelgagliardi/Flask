from flask import flask
app = Flask (__name__)
@app.route("/")
def home():
  return "Olá Rafael! Sua API está no ar"

if __name__ == "main":
  app.run(host="0.0.0.0",port=8000)