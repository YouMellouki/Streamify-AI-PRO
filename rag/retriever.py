import faiss
import numpy as np
from rag.embedder import embed

class Retriever:
    def __init__(self, documents):
        self.docs = documents
        self.embeddings = embed(documents)
        dim = self.embeddings.shape[1]
        self.index = faiss.IndexFlatL2(dim)
        self.index.add(np.array(self.embeddings))

    def search(self, query, k=3):
        q_vec = embed([query])
        distances, indices = self.index.search(np.array(q_vec), k)
        return [self.docs[i] for i in indices[0]]
