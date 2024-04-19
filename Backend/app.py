from flask import Flask, request, jsonify,render_template
import requests



def query_mt5(payload):
    API_URL = "https://api-inference.huggingface.co/models/oskrmiguel/mt5-simplification-spanish"
    headers = {"Authorization": "Bearer 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"}
    
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()
	

def query_Clmt5(payload):
    API_URL = "https://api-inference.huggingface.co/models/CLARA-MeD/mt5-small"
    headers = {"Authorization": "Bearer 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"}
    
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()
	



def query(payload):
    API_URL = "https://api-inference.huggingface.co/models/csebuetnlp/mT5_m2m_crossSum"
    headers = {"Authorization": "Bearer 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"}
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()
	

app = Flask(__name__)

@app.route('/', methods=['POST', 'OPTIONS'])

def procesar_datos():

    if request.method == 'OPTIONS':
        response = jsonify({'message': 'Preflight Request Handled'})
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Methods', 'POST, OPTIONS')
        return response
    else:

        data = request.json
        text_input = data.get('textInput')
        selected_option = data.get('selectedOption')
        
        output = query_mt5({
	    "inputs": text_input,
        "parameters": {"max_length": 100,"num_beams" : 4},
        })
        
        output1 = query_Clmt5({
	    "inputs": text_input,
        "parameters": {"max_length": 100,"num_beams" : 4},
        })
        
        output2 = query({
	    "inputs": text_input,
        "parameters": {"max_length":84,"no_repeat_ngram_size":2,"num_beams":4,"decoder_start_token_id":250003},
        })

        
        print(output)
        print(output1)
        print(output2)



       
        respuesta = {'textInput': text_input, 'selectedOption': selected_option}

        return jsonify(respuesta)

if __name__ == '__main__':
    app.run(debug=True)