from lancedb.embeddings import get_registry
from lancedb.pydantic import LanceModel, Vector

class Article(LanceModel):
    doc_id: str 
    filepath: str 
    filename: str 
    content: str 
    embedding: Vector