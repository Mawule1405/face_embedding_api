from fastapi import FastAPI, File, UploadFile, HTTPException
from typing import List
from services.embedding_service import EmbeddingService
from services.comparison_service import ComparisonService # Assurez-vous du nom du fichier

app = FastAPI(title="Face Embedding & Comparison API")

# Instanciation des services
embedding_service = EmbeddingService()
comparison_service = ComparisonService()


@app.post("/embedding_one_face_image")
async def get_embedding_from_one_face_image(file: UploadFile = File(...)):
    return await embedding_service.embedding_one_face_image(file)



@app.post("/embedding_multiple_face_image")
async def get_embedding_from_multiple_face_image(file: UploadFile = File(...)):
    return await embedding_service.embedding_multiple_face_image(file)



@app.post("/compare_vectors")
async def compare_two_vectors(vector_one: List[float], vector_two: List[float]):
    """
    Compare deux listes de nombres (embeddings) et retourne le score de similarité.
    """
    score = comparison_service.compare_vectors(vector_one, vector_two)
    return {
        "score": round(score, 4),
        "is_same_person": score > 0.4 # Seuil recommandé pour Buffalo_L
    }

@app.post("/compare_images")
async def compare_two_images(file1: UploadFile = File(...), file2: UploadFile = File(...)):
    """
    Prend deux fichiers images, extrait les visages et compare leur identité.
    """
    
    # Appel au service de comparaison
    result = await comparison_service.compare_two_images(file1, file2)
    return result