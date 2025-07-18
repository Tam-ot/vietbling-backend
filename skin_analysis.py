from io import BytesIO
from PIL import Image

def analyze_skin_image(image_bytes):
    try:
        image = Image.open(BytesIO(image_bytes))
        width, height = image.size
        return {
            "status": "success",
            "width": width,
            "height": height,
            "mode": image.mode
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}