# 선형대수학 K Mean 클러스터링


import math
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import random as rd

data = pd.read_excel('termDocMatrix.xlsx')  # 4423*500
data.head()


D = data.iloc[:, 0:500].values  # 데이터에서 배열가져오기
D = data.values.T  # 행과 열 변경, 500행 4423열
word_n = D.shape[1]  # 4423 1차원배열
title_n = D.shape[0]  # 500 1차원배열


K = 16  # 집합 수
iteration_n = 20  # 클러스터링
rep = np.empty((0, word_n), float)
# 각 집합의 중심점   word_n-1크기의 빈 배열 rep 생성(float형)


# 각 집합의 중심점 무작위로 설정
for i in range(K):
    rand = rd.randint(0, title_n-1)
    # 무작위값 0~title_n-1까지 중에 하나 반환
    rep = np.append(rep, [D[rand]], axis=0)
    # rep배열에, D[]의 rand행을 가로로 쭉 rep배열에 추가
# 을 K번 반복. 결과는, rep배열에 rand번째 행의 모든 값을 행으로 rep에 추가
# 한번 반복할 때 마다 1행씩 추가. rep는 16행 4423열
# Numpy는 배열을 [행,열]과 같이 입력받는다

JClust = np.array([])
for i in range(iteration_n):  # JClust라는 배열을 선언
    distance = np.array([])
    # 무작위로 설정된 각 집합의 중심점과 다른 모든 점과의 거리 구하기
    for j in range(K):  # j = 0~K-1 16번
        for k in range(title_n):  # k = 0~499 500번
            dis_sum = 0
            for l in range(word_n):  # l = 0~4422
                dis_sum = dis_sum + ((D[k, l]-rep[j, l])**2)
                # j,1과 k,1의거리인데, D의 k,l과 ,rep의 j,l의 거리 비교
                # 16개의 j행 기준과 k행 과의 값(coefficient) 차이의 제곱을 다더함
                # 이게 의미하는바는 한 문서와 단어와의 차이값과, 다른문서와 단어와의 차이값의 차이?
            temp_dis = math.sqrt(dis_sum)  # 다 더한거 제곱근 반환
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
