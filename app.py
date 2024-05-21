from flask import Flask,request,jsonify
import json
import requests
import os


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
    
    # Retrieve the Pexels API key from an environment variable
    my_pex_k = os.environ.get('PEXELS_API_KEY')
    
    pex_url = 'https://api.pexels.com/v1/search'
    headers = {
        "Authorization": my_pex_k
    }
    params = {
        "query": data,
        "per_page": 1,
        "page": 1
    }
    
    try:
        response = requests.get(pex_url, headers=headers, params=params)
        
        if response.status_code == 200:
            # Return the photo data as JSON
            return jsonify({'photo': response.json()})
        else:
            # Return a generic error message if the response is not successful
            return jsonify({'photo': 'Error: Unable to fetch data from Pexels API'})
    
    except Exception as e:
        # Log the error (if necessary)
        print(f"Error fetching data from Pexels API: {e}")
        
        # Return a generic error message
        return jsonify({'photo': 'Error fetching data from Pexels API'})



@app.route('/writeJSON', methods=['GET'])
def writefile():
    data = request.args.get('data')
    
    if not data:
        return jsonify({'error': 'No data provided'}), 400

    try:
        with open('j.txt', 'w') as j:
            j.write(data)
        return "<h1>JSON file written successfully</h1>"
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    

