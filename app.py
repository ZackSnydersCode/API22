from flask import Flask,request,jsonify
import json

app = Flask("__name__")

@app.route("/")
def render_index():
    return "<H1>Hello world</H1>"

@app.route('/search',methods=['GET'])
def renderAPI():
    result = []
    queryData = request.args.get('data')
    with open('searchTemplates.json','r') as file:
        loader = json.load(file)
        for i in loader:
            if i['category'].lower() == queryData.lower():
                result.append(i)
        return jsonify({'result':result})
@app.route('/applyRequest',methods=['GET'])
def Desire():
    queryData = int(request.args.get('id'))
    with open('TaskTemplates.json','r') as file:
        loader = json.load(file)
        for i in loader:
            print(i['id'],queryData)
            if i['id'] == queryData:
                return jsonify({'Template':i})
            return jsonify({'Template':2})
        return jsonify({'Template':3})

@app.route('/customTmp', methods=['GET'])
def customTmpl():
    data = request.args.get('data')
    return f"Hello Custome POrno {data}"



