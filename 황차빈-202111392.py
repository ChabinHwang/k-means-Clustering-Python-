# 선형대수학 K Mean 클러스터링
import math as mt
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random as rd

data = pd.read_excel("termDocMatrix.xlsx", engine="openpyxl", header=None)
K = 9
# K는 임의의 중심 갯수
arr = np.array(data)
row = len(arr)
col = len(arr[1])

# A열이 nan값이므로, col-1이 총 열수라고 볼 수 있음
arr2 = np.transpose(arr)

print(row, "row 4423임", col, "col 501", arr[3][5])

random_k = rd.sample(range(1, col), K)
# 9개 중심점의 문서를 정함
# 각 중심점과 길이를 비교
tlist = np.empty((K, col-1))  # 9,500배열
# list는 중심과 그 중심 그룹으로 묶인 문서를 저장하는 리스트이다
# list_temp는 최솟값을 구하기 위한 임시 배열
# 이 아래는 클러스터링 행위
for k in range(col-1):  # 소문자k대문자K 헷갈리는거주의
    list_temp = np.empty(K)  # K개 크기의 배열
    for i in range(K):
        dist = np.linalg.norm(arr2[k+1]-arr2[random_k[i]])
        list_temp[i] = dist  # 백터의 거리를list_temp에 저장
    min = np.argmin(list_temp)
    tlist[min].append(k)  # min그룹에k문서넣기
print(dist)
