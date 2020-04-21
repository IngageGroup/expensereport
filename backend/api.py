from flask_cors import CORS
import flask


app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config["HOST"] = "0.0.0.0"
CORS(app)


@app.route('/', methods=['GET'])
def home():
    data = {
        "userId": 1,
        "id": 1,
        "title": "delectus aut autem",
        "completed": "false"
    }
    response = app.response_class(
        response=flask.json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
