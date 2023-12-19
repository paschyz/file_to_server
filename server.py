from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    try:
        if 'file' not in request.files:
            print("no file part")
            return jsonify({'error': 'No file part'})

        file = request.files['file']

        if file.filename == '':
            print("no selected file")
            return jsonify({'error': 'No selected file'})
        
        file.save('uploads/' + file.filename)

        print("uploaded successfully")
        return jsonify({'message': 'File uploaded successfully'})

    except Exception as e:
        print( f'{"error" + str(e)}')
        return jsonify({'error': f'Error uploading file: {str(e)}'})

if __name__ == '__main__':
    app.run(debug=True)
