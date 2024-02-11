from flask import Flask

app = Flask(__name__)

@app.route('/')
def main():
    return "HELLO WORLD!!!"



if __name__ == '__main__':
    print("Hello World!!")
