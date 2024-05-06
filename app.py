from flask import Flask,request,jsonify
import json
import requests

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
    my_pex_k = '3F5Q1kY3jFYMs27tFm0bh6EEHlJfvVOAEcK8do9QKHVaQUcIJNajlPDM'
    pex_url = 'https://api.pexels.com/v1/search'
    headers={
        "Authorization":my_pex_k
    }
    params={
        "query":data,
        "per_page":1,
        "page":1
    }
    try:
        response = requests.get(pex_url, headers=headers, params=params)
        if response.status_code == 200:
            return jsonify({'photo':response.json()})
        else:
            return jsonify({'photo':'err'})
    except Exception as e:
        return jsonify({'photo':e})



