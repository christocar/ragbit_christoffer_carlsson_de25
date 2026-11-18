from lancedb.embeddings import get_registry
from lancedb.pydantic import LanceModel, Vector
from dotenv import load_dotenv

load_dotenv()

# in .env
# COHERE_API_KEY=...
embedding_model = get_registry().get("cohere").create(name="embed-multilingual-v3.0")


class Article(LanceModel):
    doc_id: str
    filepath: str
    filename: str
    content: str = embedding_model.SourceField()
    embedding: Vector(embedding_model.ndims()) = embedding_model.VectorField()  # type: ignore
