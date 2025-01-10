### 1학년 2학기 선형대수학 과제 1

## K-Means Clustering - Python Implementation 🚀  


<img alt="Untitled 5" src="https://github.com/user-attachments/assets/d9703c1f-4b38-480a-bdb4-ad834a139427" />


# 📌 프로젝트 개요  

K-Means 클러스터링은 데이터 포인트를 **K개의 클러스터**로 그룹화하는 대표적인 비지도 학습 알고리즘입니다.  
랜덤으로 선택된 중심점에서 시작하여, 반복적으로 클러스터 중심을 재계산하면서 최적의 분류를 찾아갑니다.  

<img  alt="Untitled" src="https://github.com/user-attachments/assets/76c51d64-64a5-4300-8832-9e533e331b40" />

- **목표**: 클러스터링 과정에서 **Jclust 값(클러스터 내 거리의 합)**이 최소가 되는 지점을 찾아내는 것입니다.  
- **결과**: 최적의 클러스터 중심이 정해지면 각 그룹의 대표적인 데이터를 도출합니다.  



# 📊 실행 예시  

### 🔹 Jclust 변화 그래프  
![Untitled 6](https://github.com/user-attachments/assets/f46ec345-1ff4-46ed-a630-95822eed4b42) 

### 🔹 클러스터별 대표 문서 출력  
![Untitled 7](https://github.com/user-attachments/assets/1cbcaed3-93c3-4d9f-a04f-88d209d974d4)



# 🛠 프로젝트 계획  

1️⃣ **초기 중심 선정**  
- 중심은 임의의 문서로 지정하며, numpy 라이브러리를 활용하여 계산 속도를 최적화합니다.  

2️⃣ **반복적인 클러스터링**  
- 중심점은 각 클러스터에 속한 데이터 포인트의 평균값으로 재계산됩니다.  
- 반복 횟수는 19회로 고정하며, 반복 시 **Jclust 값**을 계산하여 저장합니다.  

3️⃣ **결과 출력**  
- 최적화된 중심 벡터와 각 중심에 가까운 상위 5개의 문서명을 출력합니다.  


# 🧑‍💻 코드 구성  

### 🔑 주요 변수  
| 변수명        | 설명                                      |
|---------------|------------------------------------------|
| `K`           | 클러스터의 개수                         |
| `data_arr`    | 엑셀 데이터를 numpy 배열로 변환한 2차원 배열 |
| `Jclust`      | 반복마다 계산된 Jclust 값을 저장하는 리스트 |
| `center_arr`  | 클러스터 중심을 저장하는 numpy 배열       |
| `dictionary`  | 각 클러스터의 중심과 데이터 인덱스를 저장 |

### 📋 주요 함수  
1️⃣ **`vector_distance_calculate(vector1, vector2)`**  
> 두 벡터 간의 유클리드 거리를 계산합니다.  

2️⃣ **`Calculate_Jclust(dictionary, data_arr, K, center_arr)`**  
> 각 클러스터 내 데이터 포인트와 중심 간 거리를 계산하여 Jclust 값을 반환합니다.  

3️⃣ **`new_center_K(dictionary, data_arr, K)`**  
> 각 클러스터의 중심을 재계산합니다.  

4️⃣ **`cluster_represent_print(center_arr, data_arr, K, dictionary, docTitle)`**  
> 각 클러스터의 중심과 가까운 문서명을 출력합니다.  

5️⃣ **`printGraph(array)`**  
> Jclust 값을 시각화하여 그래프로 출력합니다.  



# 📂 실행 방법  

1️⃣ **필요한 패키지 설치**  
```bash
pip install numpy pandas matplotlib openpyxl
```  

2️⃣ **데이터 준비**  
- `termDocMatrix.xlsx`: 클러스터링에 사용할 데이터 파일  
- `word-docTitle.txt`: 문서 제목이 저장된 파일  

3️⃣ **코드 실행**  
```python
python k_means_clustering.py
```  

4️⃣ **결과 확인**  
- Jclust 변화 그래프  
- 클러스터별 대표 문서명  



# 🧩 학습 및 적용한 개념  

### 🔹 `collections.defaultdict` 활용  
- 기본값을 가지는 딕셔너리를 통해 클러스터 그룹화 관리  

### 🔹 `numpy` 배열 연산  
- 데이터 크기, 벡터 연산, 평균 계산 등을 효율적으로 처리  

### 🔹 리스트 컴프리헨션  
- 클러스터링 과정에서 간결하고 직관적인 코드 작성  
