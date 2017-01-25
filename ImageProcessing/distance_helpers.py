import pickle
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def getDistances(coefficients):
    similarities = cosine_similarity(coefficients)
    return similarities

def getAvgDistance(similarities):
    total = np.sum(similarities)
    trace = np.trace(similarities)
    correctedTotal = (total - trace) / 2.0
    n = similarities.shape[0]
    nDistances = n * n - n
    avg = float(correctedTotal) / float(nDistances)
    return avg