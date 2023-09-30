import numpy as np

data_arr = [
    {1, 2, 3, 4, 5}, {6, 7, 8, 9, 10}, {
        1, 2, 3, 4, 5}, {6, 7, 8, 9, 10}, {1, 2, 3, 4, 5}
]

dictionary = {
    "1": [1, 2, 3],
    "2": [4, 5, 6]
}


def Calculate_Jclust(dictionary, data_arr,  K):  # J클러스트값 계산
    clust = 0
    for m in range(K):
        K_dictionary_value = dictionary.get(m)
        for i in range(len(K_dictionary_value)):
            clust = clust + \
                vector_distance_calculate(
                    data_arr[m], data_arr[K_dictionary_value[i]])
    return clust


def vector_distance_calculate(vector1, vector2):
    return np.linalg.norm(np.array(vector2)-np.array(vector1))


print(vector_distance_calculate(dictionary.get("a"), dictionary.get("b")))
print(dictionary.get("a"))
print(Calculate_Jclust(dictionary, data_arr, 2))
