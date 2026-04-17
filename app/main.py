from fastapi import FastAPI, File, UploadFile
from services.embedding_service import EmbeddingService

app = FastAPI()

@app.post("/embedding_one_face_image")
async def get_embedding_from_one_face_image(file: UploadFile = File(...)):
    return await EmbeddingService.embedding_one_face_image(file)

@app.post("/embedding_multiple_face_image")
async def get_embedding_from_multiple_face_image(file: UploadFile = File(...)):
    return await EmbeddingService.embedding_multiple_face_image(file)