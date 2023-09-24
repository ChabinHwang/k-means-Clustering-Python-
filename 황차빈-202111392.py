# 선형대수학 K Mean 클러스터링


import math
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import random as rd

data = pd.read_excel('termDocMatrix.xlsx')
data.head()


D = data.iloc[:, 0:500].values
D = data.values.T
word_n = D.shape[1]  # 4423
title_n = D.shape[0]  # 500


K = 16  # 집합 수
iteration_n = 20  # 클러스터링
rep = np.empty((0, word_n), float)  # 각 집합의 중심점


# 각 집합의 중심점 무작위로 설정
for i in range(K):
    rand = rd.randint(0, title_n-1)
    rep = np.append(rep, [D[rand]], axis=0)


JClust = np.array([])
for i in range(iteration_n):  # JClust라는 배열을 선언
    distance = np.array([])
    # 무작위로 설정된 각 집합의 중심점과 다른 모든 점과의 거리 구하기
    for j in range(K):  # j = 0~K-1 16번
        for k in range(title_n):  # k = 0~499 500번
            dis_sum = 0
            for l in range(word_n):  # l = 0~4422
                dis_sum = dis_sum + ((D[k, l]-rep[j, l])**2)
            temp_dis = math.sqrt(dis_sum)  # 제곱근 반환
            distance = np.append(distance, temp_dis)
            # distance에 temp_dis를 추가하고, distance배열에 반환
    JClust = np.append(JClust, distance.sum()/title_n)
    # JClust배열에 distance값들의 평균을 배열에 추가함
    distance = distance.reshape(K, 500)
    # 'K행 500열'로 distance 배열을 재정의함
    C = np.argmin(distance, axis=0)+1
    # 인덱스값+1을 반환해서 배열C에 저장, axis가 0이면 행을 따라 연산, 1이면 열을 따라 연산
    Y = {}
    for m in range(K):
        Y[m+1] = np.empty((0, word_n), float)
    for n in range(title_n):
        Y[C[n]] = np.append(Y[C[n]], [D[n]], axis=0)
        ddd = np.array([])
    for o in range(K):
        for p in range(word_n):
            t = 0
            for q in range(Y[o+1].shape[0]):
                t = t+Y[o+1][q][p]
            if (Y[o+1].shape[0] != 0):
                t = t/Y[o+1].shape[0]
            ddd = np.append(ddd, t)
    rep = np.empty((0, word_n), float)
    rep = ddd.reshape(4422, K).T


iter = np.array([])
for i in range(iteration_n):
    iter = np.append(iter, i+1)
plt.plot(iter, JClust)
plt.xlabel('iteration')
plt.ylabel('JClust')
plt.xlim(0, 22)
plt.show()
