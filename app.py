from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    message = "Hello, Flask! This message is displayed in the browser."
    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run()
