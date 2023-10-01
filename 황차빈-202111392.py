# 선형대수학 K Mean 클러스터링
import math as mt
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random as rd
from collections import defaultdict
import matplotlib.pyplot as plt

data = pd.read_excel("termDocMatrix.xlsx", engine="openpyxl", header=None)
K = 9                       # K는 임의의 중심 갯수
arr = np.array(data)        # arr는 data배열을 numpy배열로 바꿈
row = len(arr)
col = len(arr[1])


def vector_distance_calculate(vector1, vector2):  # 두 백터의 거리를 계산하는 함수
    return np.linalg.norm(np.array(vector2)-np.array(vector1))


def Calculate_Jclust(dictionary, data_arr,  K, center_arr):  # J클러스트값 계산
    clust = 0
    for m in range(K):  # 중심과 각 그룹의 원소와의 거리를 다 합해서 clust값에 더해야 함
        # m번 중심 그룹을 K_dictionary_value 배열로 받음(인덱스가 모여있음)
        K_dictionary_value = dictionary.get(m)
        for i in range(len(K_dictionary_value)):     	# j클러스트 값 저장
            clust = clust + \
                vector_distance_calculate(
                    center_arr[m], data_arr[K_dictionary_value[i]])
    return clust  # clust값은 K개의 중심에서 나온 모든 값들의 합


def new_center_K(dictionary, data_arr, K):  # 그룹 중심들 다시 잡기
    arr_center = []
    for a in range(K):  # 0~8까지 중심에 대해 중심 재정의
        arr_temp = np.zeros_like(data_arr[3])  # data_arr[3]만큼 0으로 초기화
        for i in range(len(dictionary[a])):  # i는 각 딕셔너리 벨류값
            # arr_temp에 그룹원들의 벡터값의 합을 저장,j는 키값(중심)i는 원소
            arr_temp = np.add(arr_temp, data_arr[dictionary[a][i]])
        # temp를 백터수로나눠서 새로운 중심을 지정(arr3)중요
        arr = np.divide(arr_temp, len(dictionary[a]))
        arr_center.append(arr)  # np.append보다 append가 메모리가 덜 쓰임
    return np.array(arr_center)  # 2차원배열로 중심 백터들 반환(8x4423)


# 문서끼리 비교해야 하므로, 한 열의 값을 한번에 불러올 수 없음. 따라서 행과 열을 전치
# 1~501사이, K개의 중심점의 좌표를 정함.각 중심점과 길이를 비교
data_arr = np.transpose(arr)
random_k = rd.sample(range(1, col), K)
dictionary = defaultdict(list)          # 중심과 그 집합을 모은 딕셔너리 생성

# 500개의 문서를 9개의 중심들과 거리 비교 후, 가장 짧은 곳 키인덱스:문서인덱스 딕셔너리에 넣음
for m in range(len(data_arr)-1):
    dist = [vector_distance_calculate(
        data_arr[random_k[i]], data_arr[m+1])for i in range(K)]  # 가장 작은 값의 인덱스(0~8중하나), m은 문서번호(배열상의)를 의미함
    dictionary[np.argmin(dist)].append(m+1)

# 위 for문이 끝나면, 딕셔너리는 1:[5,6,86..], 2:[2,3,23,413..]....와 같이 분류됨.
Jclust = []
center = []
center = [data_arr[random_k[i]] for i in range(K)]
center_arr = np.array(center)  # 중심의 배열을 새로 지정해줌

# # 1. J클러스터값 더하기
# # 2. 그룹 중심 다시잡기
# # 3. 그룹 묶기(딕셔너리초기화)
# 4. '1>2>3'반복15회
for fin in range(15):
    Jclust.append(Calculate_Jclust(dictionary, data_arr, K, center_arr))
    center = new_center_K(dictionary, data_arr, K)
    center_arr = np.array(center)
    dictionary = defaultdict(list)
    for m in range(len(data_arr)-1):  # 500개의 문서를 9개의 중심들과 거리 비교 후, 가장 짧은 곳 키인덱스:문서인덱스 딕셔너리에 넣음
        dist = [vector_distance_calculate(
            center_arr[i], data_arr[m+1])for i in range(K)]  # i부터 k까지, 거리비교
        dictionary[np.argmin(dist)].append(m+1)

for i in range(len(Jclust)):  # J클러스트값을 문서수로 나누기
    Jclust[i] = Jclust[i]/(len(data_arr)-1)

print(Jclust)
plt.plot(Jclust)  # 함수로 표현
plt.show()
