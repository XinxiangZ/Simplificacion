from flask import Flask, request, jsonify,render_template

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
       
        respuesta = {'textInput': text_input, 'selectedOption': selected_option}
        print(respuesta)

        return jsonify(respuesta)

if __name__ == '__main__':
    app.run(debug=True)