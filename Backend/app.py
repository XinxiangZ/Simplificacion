from flask import Flask, request, jsonify,render_template

app = Flask(__name__)

@app.route('/', methods=['POST', 'OPTIONS'])

def procesar_datos():
    # Si la solicitud es OPTIONS, responde con los encabezados necesarios
    if request.method == 'OPTIONS':
        response = jsonify({'message': 'Preflight Request Handled'})
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Methods', 'POST, OPTIONS')
        return response
    else:
        # Si la solicitud es POST, procesa los datos recibidos
        data = request.json
        text_input = data.get('textInput')
        selected_option = data.get('selectedOption')
       
        respuesta = {'textInput': text_input, 'selectedOption': selected_option}
        print(respuesta)
        # Realiza cualquier procesamiento necesario aquí
        
        # Devuelve la respuesta correspondiente
        return jsonify(respuesta)

if __name__ == '__main__':
    app.run(debug=True)