from insightface.app import FaceAnalysis

class ModelConfig:
    def __init__(self):
        self.model = FaceAnalysis(
            name="buffalo_l",
            root="./"
        )
        self.model.prepare(ctx_id=-1)


# instance globale (singleton)
model_config = ModelConfig()