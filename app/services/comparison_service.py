import numpy as np
from fastapi import HTTPException, UploadFile
from services.embedding_service import EmbeddingService # Assurez-vous du chemin

class ComparisonService:
    def __init__(self):
        # On peut injecter le service d'embedding ici si nécessaire
        self.embedding_service = EmbeddingService()

    @staticmethod
    def compare_vectors(vector_one: list, vector_two: list) -> float:
        """
        Calcule la similarité cosinus entre deux vecteurs.
        Retourne un score entre -1 (opposés) et 1 (identiques).
        En reconnaissance faciale, un score > 0.4 ou 0.5 indique généralement la même personne.
        """
        if len(vector_one) != len(vector_two):
            raise HTTPException(
                status_code=400, 
                detail=f"Les dimensions des vecteurs ne correspondent pas: {len(vector_one)} vs {len(vector_two)}"
            )

        # Conversion en tableaux numpy pour le calcul vectoriel
        v1 = np.array(vector_one)
        v2 = np.array(vector_two)

        # Calcul de la similarité cosinus : (A . B) / (||A|| * ||B||)
        dot_product = np.dot(v1, v2)
        norm_v1 = np.linalg.norm(v1)
        norm_v2 = np.linalg.norm(v2)

        if norm_v1 == 0 or norm_v2 == 0:
            return 0.0

        similarity = dot_product / (norm_v1 * norm_v2)
        return float(similarity)

    async def compare_two_images(self, image_one: UploadFile, image_two: UploadFile) -> dict:
        """
        Prend deux images brutes, génère leurs embeddings et les compare.
        """
        # 1. Extraire l'embedding de la première image
        # On suppose que votre embedding_service a une méthode pour traiter les bytes
        feat1 = await self.embedding_service.embedding_one_face_image(image_one)
        
        # 2. Extraire l'embedding de la deuxième image
        feat2 = await self.embedding_service.embedding_one_face_image(image_two)

        if feat1["embedding"] is None or feat2["embedding"] is None:
            raise HTTPException(
                status_code=404, 
                detail="Impossible de détecter un visage dans l'une des images."
            )

        # 3. Comparer
        score = self.compare_vectors(feat1["embedding"], feat2["embedding"])

        # 4. Décision (Seuil souvent fixé à 0.4 pour Buffalo_L)
        is_same = score > 0.4

        return {
            "similarity_score": round(score, 4),
            "is_same_person": is_same
        }