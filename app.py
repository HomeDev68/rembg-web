from flask import Flask, render_template, request, send_file
from rembg import remove
from PIL import Image
from io import BytesIO
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file uploaded', 400
        file = request.files['file']
        if file.filename == '':
            return 'No file selected', 400
        if file:
            try:
                input_image = Image.open(file.stream)
                output_image = remove(input_image, post_process_mask=True)
                img_io = BytesIO()
                output_image.save(img_io, 'PNG')
                img_io.seek(0)
                filename, file_extension = os.path.splitext(file.filename)
                download_name = filename + '_rmbg.png'
                return send_file(img_io, mimetype='image/png', as_attachment=True, download_name=download_name)
            except Exception as e:
                return f"Error processing image: {e}", 500
    else:
        return render_template('index.html')

@app.route('/api/rmbg', methods=['POST'])
def api_remove_background():
    if 'file' not in request.files:
        return 'No file part', 400
    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400
    if file:
        try:
            input_image = Image.open(file.stream)
            output_image = remove(input_image, post_process_mask=True)
            img_io = BytesIO()
            output_image.save(img_io, 'PNG')
            img_io.seek(0)
            return send_file(img_io, mimetype='image/png')
        except Exception as e:
            return f"Error processing image: {e}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5100) # Change debug to false in a Prod Environment
