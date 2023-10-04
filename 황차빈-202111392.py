import math as mt
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random as rd
from collections import defaultdict
import matplotlib.pyplot as plt

data = pd.read_excel("termDocMatrix.xlsx", engine="openpyxl", header=None)
K = 9                      # K는  중심 갯수
arr = np.array(data)        # arr는 data배열을 numpy배열로 바꿈
row = len(arr)
col = len(arr[1])


def cluster_represent_print(Cluster_arr, data_arr, K, dictionary, docTitle):
    for j in range(K):         # 그룹원들과 그 클러스터중심과 비교
        print(str(j+1), "번째 클러스터", "\n", center_arr[j], "\n")
        print("클러스터를 대표하는 문서명")
        dist = [vector_distance_calculate(
            Cluster_arr[j], data_arr[dictionary.get(j)[i]])for i in range(len(dictionary.get(j)))]
        indices = np.argsort(dist)  # 오름차순했을때, 인덱스반환
        if len(dictionary.get(j)) < 5:  # 가장작은 문서 인덱스 반환
            # 가장 작은 값들의 딕셔너리 벨류 안 리스트의 인덱스
            smallist_indices = indices[:len(dictionary.get(j))]
        else:
            smallist_indices = indices[:5]
        for i in range(len(smallist_indices)):
            print(docTitle[dictionary.get(j)[smallist_indices[i]]])
        print("\n")


def vector_distance_calculate(vector1, vector2):  # 두 백터의 거리를 계산하는 함수
    return np.linalg.norm(np.array(vector2)-np.array(vector1))


def Calculate_Jclust(dictionary, data_arr,  K, center_arr):  # J클러스트값 계산
    clust = 0
    for m in range(K):  # 중심과 각 그룹의 원소와의 거리를 다 합해서 clust값에 더해야 함
        # m번 중심 그룹을 K_dictionary_value 배열로 받음(data_arr의 인덱스)
        K_dictionary_value = dictionary.get(m)
        for i in range(len(K_dictionary_value)):     	# j클러스트 값 저장
            clust = clust + \
                vector_distance_calculate(
                    center_arr[m], data_arr[K_dictionary_value[i]])
    return clust  # clust값은 K개의 중심에서 나온 모든 값들의 합


def new_center_K(dictionary, data_arr, K):  # 그룹 중심들 다시 잡기
    arr_center = []
    for a in range(K):  # K까지 중심에 대해 중심 재정의
        arr_temp = np.zeros_like(data_arr[3])  # 배열의 열의 수만큼 0으로 초기화
        for i in range(len(dictionary[a])):  # i는 각 딕셔너리 벨류값
            # arr_temp에 그룹원들의 벡터값의 합을 저장,a는 키값(중심)i는 원소
            arr_temp = np.add(arr_temp, data_arr[dictionary[a][i]])
        # temp를 백터수로나눠서 새로운 중심을 지정(arr)중요
        arr = np.divide(arr_temp, len(dictionary[a]))
        arr_center.append(arr)  # np.append보다 append가 메모리가 덜 쓰임
    return np.array(arr_center)  # 2차원배열로 중심 백터들 반환


def printGraph(array):  # 그래프 출력
    plt.plot(array)
    plt.scatter(range(len(array)), array)
    plt.title("Jclust Alteration of K-Mean Clustering")
    plt.show()


# 엑셀 속 A열이 완전히 비어있는걸 의식해야함
# 문서끼리 비교해야 하므로, 한 열의 값을 한번에 불러올 수 없음. 따라서 행과 열을 전치
# 1~501사이, K개의 중심점의 좌표를 정함.각 중심점과 길이를 비교
data_arr = np.transpose(arr)
random_k = rd.sample(range(1, col), K)
dictionary = defaultdict(list)          # 중심과 그 집합을 모은 딕셔너리 생성

# 500개의 문서를 9개의 중심들과 거리 비교 후, 가장 짧은 곳 키인덱스:문서인덱스 딕셔너리에 넣음
for m in range(len(data_arr)-1):
    dist = [vector_distance_calculate(
        data_arr[random_k[i]], data_arr[m+1])for i in range(K)]  # 가장 작은 값의 인덱스를 딕셔너리 벨류 리스트에 추가
    dictionary[np.argmin(dist)].append(m+1)

Jclust = []
center = []
center = [data_arr[random_k[i]] for i in range(K)]
center_arr = np.array(center)  # 중심의 배열을 새로 지정해줌


for fin in range(19):
    Jclust.append(Calculate_Jclust(dictionary, data_arr, K, center_arr))
    center = new_center_K(dictionary, data_arr, K)
    center_arr = np.array(center)
    dictionary = defaultdict(list)
    for m in range(len(data_arr)-1):  # 500개의 문서를 K개의 중심들과 거리 비교 후, 가장 짧은 키값의 벨류에 지정
        dist = [vector_distance_calculate(
            center_arr[i], data_arr[m+1])for i in range(K)]
        dictionary[np.argmin(dist)].append(m+1)

for i in range(len(Jclust)):  # J클러스트값을 문서수로 나누기
    Jclust[i] = Jclust[i]/(len(data_arr)-1)
# 문서명 들어있는 txt파일 읽기
title = "word-docTitle.txt"
start = 4428
with open(title, "r") as file:
    for _ in range(start-1):
        file.readline()
    docTitle = [file.readline().strip() for _ in range(len(data_arr)-1)]

# 클러스터의 위치에 따라, 문서명이 5개가 안될수도 있음
# dictionary에 그룹원들이 정리되어 있음. 그룹원들사이에 중심과의 거리를 계산해 상위5개 문서명 출력
print("-------클러스터(가상의 벡터값)와 클러스터를 대표하는 문서명-------\n\n")
cluster_represent_print(center_arr, data_arr, K, dictionary, docTitle)

# 15개의 클러스터(가상의 중심 벡터 출력), 대표 5개 문서
printGraph(Jclust)

#JClust값 n번째값:뭐다 이렇게 출력
