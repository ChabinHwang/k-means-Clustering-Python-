# 선형대수학 K Mean 클러스터링
import math as mt
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random as rd
from collections import defaultdict

data = pd.read_excel("termDocMatrix.xlsx", engine="openpyxl", header=None)
K = 9                       # K는 임의의 중심 갯수
arr = np.array(data)        # arr는 data배열을 numpy배열로 바꿈
row = len(arr)
col = len(arr[1])

def vector_distance_calculate(vector1,vector2):     #두 백터의 거리를 계산하는 함수
    return np.linalg.norm(vector2-vector1)          # A열이 nan값이므로, col-1이 총 열수라고 볼 수 있음

def new_center(dictionary_value,data_arr):            #가상의 중심 만드는 함수
     for j in range(K):						#j는 몇번째 중심인지 나타냄
        for i in range(len(dictionary_value[j])): #i는 각 딕셔너리 벨류값
            arr_temp=np.add(arr_temp,data_arr[dictionary_value[j]])	#arr_temp에 그룹원들의 벡터값의 합을 저장
            arr3=np.divide(arr_temp,len(dictionary_value[j])#temp를 백터수로나눠서 새로운 중심을 지정(arr3)중요!
                           


data_arr = np.transpose(arr)                # 문서끼리 비교해야 하므로, 한 열의 값을 한번에 불러올 수 없음. 따라서 행과 열을 전치
random_k = rd.sample(range(1, col), K)  # 1~501사이, K개의 중심점의 좌표를 정함.각 중심점과 길이를 비교
dictionary= defaultdict(list)           #중심과 그 집합을 모은 딕셔너리 생성     

for m in range(len(data_arr)-1):                          #500개의 문서를 9개의 중심들과 거리 비교 후, 가장 짧은 곳 키인덱스:문서인덱스 딕셔너리에 넣음
        dist=[vector_distance_calculate(data_arr[i]-data_arr[m+1])for i in range(K)]
        dictionary[np.argmin(dist)].append(m+1)       # 가장 작은 값의 인덱스(0~8중하나), m은 문서번호(배열상의)를 의미함

#위 for문이 끝나면, 딕셔너리는 1:[5,6,86..], 2:[2,3,23,413..]....와 같이 분류됨.
Jclust=0
for m in range(K):                  #중심과 각 그룹의 원소와의 거리를 다 합해서 Jclust값에 더해야 함
     K_dictionary_value=dictionary.get[m]     # m번 중심 그룹을 K_dictionary_value 배열로 받음(인덱스가 모여있음)

     for i in range(len(K_dictionary_value)):	# j클러스트 값 저장
          Jclust=Jclust+vector_distance_calculate(data_arr[m]-data_arr[K_dictionary_value(i)])
      

for j in range(K):						#j는 몇번째 중심인지 나타냄
    for i in range(len(K_dictionary_value[j])): #i는 각 딕셔너리 벨류값
        arr_temp=np.add(arr.temp,data_arr[K_dictionary_value[j]])	#arr_temp에 그룹원들의 벡터값의 합을 저장
        arr3=np.divide(arr_temp,len(K_dictionary_value[j])#temp를 백터수로나눠서 새로운 중심을 지정(arr3)중요!





group_list.append(np.argmin(dist))


def k_means_klustering(data, center_arr):

dist = np.linalg.norm(data_arr[k+1]-data_arr[random_k[i]])
# 각 벡터와 기준과 백터거리계산. 원소(두 백터의 차)의 곱의 합의 제곱근.

#J-clust=>그룹의 중심-그룹의 원소 거리norm한것들의 총합.