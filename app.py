from flask import Flask, request

app = Flask(__name__)

@app.get("/users/<id>")
def show_string():
    return {}
pass

# This runs the app
if __name__ == "__main__":
    app.run()
