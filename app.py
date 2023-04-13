from flask import Flask, request, jsonify

app = Flask("__name__")

@app.route('/api',methods=['GET'])
def hello_world():
    d={}
    d["val"] = request.args["sello"]
    return jsonify(d)


if __name__=="__main__":
    app.run(port=33)
    