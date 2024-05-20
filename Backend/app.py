from flask import Flask, request, jsonify
import requests
from flask_cors import CORS
import asyncio


async def query_mt5(payload):
    API_URL = "https://api-inference.huggingface.co/models/oskrmiguel/mt5-simplification-spanish"
    headers = {"Authorization": "Bearer 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"}
    
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()
	

async def query_Clmt5(payload):
    API_URL = "https://api-inference.huggingface.co/models/CLARA-MeD/mt5-small"
    headers = {"Authorization": "Bearer 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"}
    
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()
	



async def query_Cross(payload):
    API_URL = "https://api-inference.huggingface.co/models/csebuetnlp/mT5_m2m_crossSum"
    headers = {"Authorization": "Bearer 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"}
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()
	

app = Flask(__name__)
CORS(app)

@app.route('/open', methods=['POST', 'OPTIONS'])

async def iniciar_modelo():

    if request.method == 'OPTIONS':
        response = jsonify({'message': 'Preflight Request Handled'})
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Methods', 'POST, OPTIONS')
        return response
    else:

        data = request.json
        text_input = data.get('textInput')
        
        
        respuesta = {"fallo": 1,"generated_text":text_input}
        print("open")
        
        output1 =await query_Cross({
        "inputs": text_input,
        "parameters": {"max_length":84,"no_repeat_ngram_size":2,"num_beams":4,"decoder_start_token_id":250003},
        })
                    
                    
        output3 =await query_mt5({
        "inputs": text_input,
        "parameters": {"max_length": 100,"num_beams" : 4},
        })
                    
        output4 =await query_Clmt5({
        "inputs": text_input,
        "parameters": {"max_length": 100,"num_beams" : 4},
        })

        return jsonify(respuesta)

@app.route('/api', methods=['POST', 'OPTIONS'])

async def procesar_datos():

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
        
        respuesta = {"fallo": 1,"generated_text":text_input}
        i=0
        if selectedOptionSintactica == True and selectedOptionLexica == False and selectedOptionResumen == False:
            try:
                output = await query_mt5({
                "inputs": text_input,
                "parameters": {"max_length": 100,"num_beams" : 4},
                })

                
                respuesta = {"fallo": 0,"num_res":1,"generated_text": output[0]["generated_text"]}
            except KeyError:
                print("Error")
                
            print(1)
             
        elif selectedOptionSintactica == False and selectedOptionLexica == True and selectedOptionResumen == False:
            try:
                output = await query_Clmt5({
                "inputs": text_input,
                "parameters": {"max_length": 100,"num_beams" : 4,"no_repeat_ngram_size":2},
                })
            
                respuesta = {"fallo": 0,"num_res":1,"generated_text": output[0]["generated_text"]}
            except KeyError:
                print("Error")
            print(2)
            
        elif selectedOptionSintactica == False and selectedOptionLexica == False and selectedOptionResumen == True:
            try:
                output = await query_Cross({
                "inputs": text_input,
                "parameters": {"max_length":84,"no_repeat_ngram_size":2,"num_beams":4,"decoder_start_token_id":250003},
                })
            
            
            
            
                respuesta = {"fallo": 0,"num_res":1,"generated_text": output[0]["summary_text"]}
            except KeyError:
                print("Error")
            print(3)
            
        elif selectedOptionSintactica == True and selectedOptionLexica == True and selectedOptionResumen == False:
            try:
                output1 =await query_mt5({
                "inputs": text_input,
                "parameters": {"max_length": 100,"num_beams" : 4},
                }) 
                
                
                output =await query_Clmt5({
                "inputs": output1[0]["generated_text"],
                "parameters": {"max_length": 100,"num_beams" : 4},
                })
                
                output2 =await query_Clmt5({
                "inputs": text_input,
                "parameters": {"max_length": 100,"num_beams" : 4},
                })
            
            
            
                respuesta = {"fallo": 0,"num_res":2,"generated_text": output[0]["generated_text"],"text_1":output1[0]["generated_text"],"text_2":output2[0]["generated_text"]}
            except KeyError:
                print("Error")
            print(4)
            
        elif selectedOptionSintactica == True and selectedOptionLexica == False and selectedOptionResumen == True:
            try:
                output1 =await query_Cross({
                "inputs": text_input,
                "parameters": {"max_length":84,"no_repeat_ngram_size":2,"num_beams":4,"decoder_start_token_id":250003},
                })


                output =await query_mt5({
                "inputs": output1[0]["summary_text"],
                "parameters": {"max_length": 100,"num_beams" : 4},
                })

                
                output2 =await query_mt5({
                "inputs": text_input,
                "parameters": {"max_length": 100,"num_beams" : 4},
                })

           
            
                respuesta = {"fallo": 0,"num_res":2,"generated_text": output[0]["generated_text"],"text_1":output1[0]["summary_text"],"text_2":output2[0]["generated_text"]}
            except KeyError:
                print("Error")
            print(5)
      
        elif selectedOptionSintactica == False and selectedOptionLexica == True and selectedOptionResumen == True:
            
            
            
           
            try:
                output1 =await query_Cross({
                "inputs": text_input,
                "parameters": {"max_length":84,"no_repeat_ngram_size":2,"num_beams":4,"decoder_start_token_id":250003},
                })
                            
                output =await query_Clmt5({
                "inputs": output1[0]["summary_text"],
                "parameters": {"max_length": 100,"num_beams" : 4},
                })
                
                output2 =await query_Clmt5({
                "inputs": text_input,
                "parameters": {"max_length": 100,"num_beams" : 4},
                })
                respuesta = {"fallo": 0,"num_res":2,"generated_text": output[0]["generated_text"],"text_1":output1[0]["summary_text"],"text_2":output2[0]["generated_text"]}
            except KeyError:
                print("Error")
            print(6)
            
        elif selectedOptionLexica == True and selectedOptionSintactica ==True and selectedOptionResumen == True:
        
            
            try:
                output1 =await query_Cross({
                "inputs": text_input,
                "parameters": {"max_length":84,"no_repeat_ngram_size":2,"num_beams":4,"decoder_start_token_id":250003},
                })
                
                
                output2 =await query_mt5({
                "inputs": output1[0]["summary_text"],
                "parameters": {"max_length": 100,"num_beams" : 4},
                })
                
                output =await query_Clmt5({
                "inputs": output2[0]["generated_text"],
                "parameters": {"max_length": 100,"num_beams" : 4},
                })
                
                output3 =await query_mt5({
                "inputs": text_input,
                "parameters": {"max_length": 100,"num_beams" : 4},
                })
                
                output4 =await query_Clmt5({
                "inputs": text_input,
                "parameters": {"max_length": 100,"num_beams" : 4},
                })
               
                respuesta = {"fallo": 0,"num_res":3,"generated_text": output[0]["generated_text"],"text_1":output1[0]["summary_text"],"text_2":output3[0]["generated_text"],"text_3":output4[0]["generated_text"]}
            except KeyError:
                print("Error")
            print(7)
       
        

        return jsonify(respuesta)

if __name__ == '__main__':
    asyncio.run(app.run())