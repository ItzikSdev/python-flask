from flask import Flask

helloworld = Flask(__name__)

@helloworld.route("/")
def run():
    return "{\"message\":\"Hey python\"}"

if __name__ == "__main__":
    helloworld.run(host='0.0.0.0', port=443, ssl_context=('cert.pem', 'key.pem'))