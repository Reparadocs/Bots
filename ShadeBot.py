from flask import flask

app = Flask(__name__)

@app.route('/webhook', methods=['GET'])
def webhook():
  print request

if __name__ == '__main__':
  app.run()