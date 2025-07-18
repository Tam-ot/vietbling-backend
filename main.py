from fastapi import FastAPI, UploadFile, File
from skin_analysis import analyze_skin_image

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "VietBling API is running!"}

@app.post("/analyze/")
async def analyze_image(file: UploadFile = File(...)):
    contents = await file.read()
    result = analyze_skin_image(contents)
    return result