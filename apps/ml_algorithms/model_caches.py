from django.conf import settings
from joblib import Memory
from ml_algorithms.knn_algorithms import sort_via_knn

cachedir = settings.BASE_DIR / 'apps/model_caches/'
mem = Memory(cachedir)


def save_caches():
    """Train qilingan model ni keshlaydi"""
    sort_via_knn_trained = mem.cache(sort_via_knn)
