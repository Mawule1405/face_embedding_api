import cv2
import numpy as np
from fastapi import HTTPException, UploadFile

from core.model_config import model_config

class EmbeddingService:

    @staticmethod
    async def embedding_one_face_image(file: UploadFile):
        
        filename = file.filename.lower()

        if not filename.endswith(("png", "jpg", "jpeg", "webp")):
            raise HTTPException(status_code=400, detail="File must be an image")

        contents = await file.read()

        if len(contents) == 0:
            raise HTTPException(status_code=400, detail="Empty file")

        npimg = np.frombuffer(contents, np.uint8)
        img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)

        if img is None:
            raise HTTPException(status_code=400, detail="Invalid image")

        faces = model_config.model.get(img)

        if len(faces) == 0:
            raise HTTPException(status_code=404, detail="No face detected")

        if len(faces) > 1:
            raise HTTPException(
                status_code=400,
                detail="Multiple faces detected. Please provide an image with a single face."
            )

        embedding = faces[0].embedding

        # normalisation (IMPORTANT)
        embedding = embedding / np.linalg.norm(embedding)

        return {
            "embedding": embedding.tolist(),
            "dimension": len(embedding)
        }
    

    @staticmethod
    async def embedding_multiple_face_image(file: UploadFile):
        
        filename = file.filename.lower()

        if not filename.endswith(("png", "jpg", "jpeg", "webp")):
            raise HTTPException(status_code=400, detail="File must be an image")

        contents = await file.read()

        if len(contents) == 0:
            raise HTTPException(status_code=400, detail="Empty file")

        npimg = np.frombuffer(contents, np.uint8)
        img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)

        if img is None:
            raise HTTPException(status_code=400, detail="Invalid image")

        faces = model_config.model.get(img)

        if len(faces) == 0:
            raise HTTPException(status_code=404, detail="No face detected")

        # normalisation (IMPORTANT)
        embeddings = [
                (face.embedding / np.linalg.norm(face.embedding)).tolist()
                    for face in faces
                ]

        return {
                "nb_faces": len(embeddings),
                "embeddings": embeddings
                }