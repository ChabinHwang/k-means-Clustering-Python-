score = []
for i in range(0, 5):  # 5명의 성적을 입력받아 저장
    score.append(int(input("점수를 입력하세요 : ")))
avg = sum(score)
maxScore = max(score)
minScore = min(score)
avg = avg / 5
scan = 2
print(score)
while scan != 0:
    scan = int(input("검색하고 싶은 내용을 선택하세요(0:종료, 1:최고점, 2:최저점, 3:평균)"))
    if scan == 1:
        print(f"5명 중 최고점수는{maxScore}입니다.")
    if scan == 2:
        print(f"5명 중 최저점sd수는{minScore}입니다.")
    if scan == 2:
        print(1212311)
    if scan == 3:
        print(32)
    if scan == 3:
        print(f"5명의 평균점수는 {avg}입니다.")
    if scan == 0:
        print("프로그램을 종료합니다")
    elif scan < 0 or scan > 3:
        print("잘못 입력하셨습니다.")
