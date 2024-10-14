A simple flask app to remove the background of an image with [Rembg](https://github.com/danielgatis/rembg)

Watch the [tutorial](https://youtu.be/cw34KMPSt4k) on YouTube

## Run it

```bash
pip install -r requirements.txt
python3 app.py
```

## API Usage

This app provides a simple API for removing backgrounds.

**Endpoint:** `/api/rmbg`

**Method:** `POST`

**Request Body:**  A multipart/form-data request with a file named `file` containing the image.

**Response:** The image with the background removed (as a PNG).  The response is a binary image file, so you may need to handle it appropriately (e.g., save it to a file using curl's `--output` option).

**Example using curl:**

```bash
curl -X POST -F "file=@path/to/your/image.jpg" http://127.0.0.1:5100/api/rmbg --output output.png
```

Replace `path/to/your/image.jpg` with the actual path to your image file.

## Usage

To use the web interface, simply run the application and open your browser to `http://127.0.0.1:5100`. You can then upload an image to remove its background.  The processed image will be downloaded automatically.

## Build a Docker Image

1. **Download the u2net model:** Download `u2net.onnx` from [this link](https://github.com/danielgatis/rembg/releases/download/v0.0.0/u2net.onnx) and place it in the project's root directory.
2. **Build the image:**
   ```bash
   docker build -t rembg-app .
   ```
3. **Run the container:**
   ```bash
   docker run -p 5100:5100 rembg-app
   ```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Credits

This project was inspired by Fireship's tutorial: [https://github.com/codediodeio/rembg-webapp-tutorial](https://github.com/codediodeio/rembg-webapp-tutorial)
