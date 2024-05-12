from flask import Flask, request, jsonify
import requests
from flask_cors import CORS


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
	



def query_Cross(payload):
    API_URL = "https://api-inference.huggingface.co/models/csebuetnlp/mT5_m2m_crossSum"
    headers = {"Authorization": "Bearer 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"}
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()
	

app = Flask(__name__)
CORS(app)


@app.route('/api', methods=['POST', 'OPTIONS'])

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
        selectedOptionSintactica = data.get("selectedOptionSintactica")
        selectedOptionLexica = data.get("selectedOptionLexica")
        selectedOptionResumen = data.get("selectedOptionResumen")
        
        respuesta = {"generated_text": text_input}
        
        if selectedOptionSintactica == True and selectedOptionLexica == False and selectedOptionResumen == False:
            output = query_mt5({
	        "inputs": text_input,
            "parameters": {"max_length": 100,"num_beams" : 4},
            })
            respuesta = {"num_res":1,"generated_text": output[0]["generated_text"]}
            
            print(1)
             
        elif selectedOptionSintactica == False and selectedOptionLexica == True and selectedOptionResumen == False:
            output = query_Clmt5({
	        "inputs": text_input,
            "parameters": {"max_length": 100,"num_beams" : 4},
            })
            respuesta = {"num_res":1,"generated_text": output[0]["generated_text"]}
            print(2)
            
        elif selectedOptionSintactica == False and selectedOptionLexica == False and selectedOptionResumen == True:
            output = query_Cross({
	        "inputs": text_input,
            "parameters": {"max_length":84,"no_repeat_ngram_size":2,"num_beams":4,"decoder_start_token_id":250003},
            })
            respuesta = {"num_res":1,"generated_text": output[0]["generated_text"]}
            print(3)
            
        elif selectedOptionSintactica == True and selectedOptionLexica == True and selectedOptionResumen == False:
            output1 = query_mt5({
	        "inputs": text_input,
            "parameters": {"max_length": 100,"num_beams" : 4},
            }) 
            
            output2 = query_Clmt5({
	        "inputs": text_input,
            "parameters": {"max_length": 100,"num_beams" : 4},
            })
            
            output = query_Clmt5({
	        "inputs": output1[0]["generated_text"],
            "parameters": {"max_length": 100,"num_beams" : 4},
            })
            
            respuesta = {"num_res":2,"generated_text": output[0]["generated_text"],"text_1":output1[0]["generated_text"],"text_2":output2[0]["generated_text"]}
            print(4)
            
        elif selectedOptionSintactica == True and selectedOptionLexica == False and selectedOptionResumen == True:
            
            output1 = query_Cross({
	        "inputs": text_input,
            "parameters": {"max_length":84,"no_repeat_ngram_size":2,"num_beams":4,"decoder_start_token_id":250003},
            })
            
            output2 = query_mt5({
	        "inputs": text_input,
            "parameters": {"max_length": 100,"num_beams" : 4},
            })

            output = query_mt5({
	        "inputs": output1[0]["summary_text"],
            "parameters": {"max_length": 100,"num_beams" : 4},
            })

            respuesta = {"num_res":2,"generated_text": output[0]["generated_text"],"text_1":output1[0]["summary_text"],"text_2":output2[0]["generated_text"]}
            print(5)
      
        elif selectedOptionSintactica == False and selectedOptionLexica == True and selectedOptionResumen == True:
            
            output1 = query_Cross({
	        "inputs": text_input,
            "parameters": {"max_length":84,"no_repeat_ngram_size":2,"num_beams":4,"decoder_start_token_id":250003},
            })
            
            output = query_Clmt5({
	        "inputs": text_input,
            "parameters": {"max_length": 100,"num_beams" : 4},
            })
             
            output = query_Clmt5({
	        "inputs": output1[0]["summary_text"],
            "parameters": {"max_length": 100,"num_beams" : 4},
            })
            respuesta = {"num_res":2,"generated_text": output[0]["generated_text"],"text_1":output1[0]["summary_text"],"text_2":output2[0]["generated_text"]}
            print(6)
            
        elif selectedOptionLexica == True and selectedOptionSintactica ==True and selectedOptionResumen == True:
        
            output1 = query_Cross({
	        "inputs": text_input,
            "parameters": {"max_length":84,"no_repeat_ngram_size":2,"num_beams":4,"decoder_start_token_id":250003},
            })
            
            output3 = query_mt5({
	        "inputs": text_input,
            "parameters": {"max_length": 100,"num_beams" : 4},
            })
            
            output4 = query_Clmt5({
	        "inputs": text_input,
            "parameters": {"max_length": 100,"num_beams" : 4},
            })
            
            output2 = query_mt5({
	        "inputs": output1[0]["summary_text"],
            "parameters": {"max_length": 100,"num_beams" : 4},
            })
            
            output = query_Clmt5({
	        "inputs": output2[0]["generated_text"],
            "parameters": {"max_length": 100,"num_beams" : 4},
            })
            respuesta = {"num_res":3,"generated_text": output[0]["generated_text"],"text_1":output1[0]["summary_text"],"text_2":output3[0]["generated_text"],"text_3":output4[0]["generated_text"]}
            print(7)
       
        

        return jsonify(respuesta)

if __name__ == '__main__':
    app.run(debug=True)