from flask import Flask, request, send_file
from rembg import remove
from PIL import Image
from io import BytesIO

# For Standalone api usage
app = Flask(__name__)

@app.route('/api/rmbg', methods=['POST'])
def remove_background():
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
    app.run(debug=False, port=5000)
