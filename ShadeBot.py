from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook', methods=['GET'])
def webhook():
  print request
  return "<h1>Hello World</h1>"

if __name__ == '__main__':
  app.run()