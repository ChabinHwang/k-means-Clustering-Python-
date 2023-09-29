import numpy as np


dictionary = {
    "a": [1, 2, 3],
    "b": [4, 5, 6]
}


def vector_distance_calculate(vector1, vector2):
    # 두 백터의 거리를 계산하는 함수
    return np.linalg.norm(np.array(vector2)-np.array(vector1))


print(vector_distance_calculate(dictionary.get("a"), dictionary.get("b")))
