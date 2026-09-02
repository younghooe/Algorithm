'''
문제 분석
풀기 위한 전략
슈도코드
'''
# 평탄화 작업을 하는데, 가장 효율적으로 해라.
# 횟수는 정해져있다.
# 횟수 종료 후.
# answer = 최고점 - 최저점의 차이
#
# 가로 = 100
# 1<= 높이 <= 100
# 1<= 덤프 횟수 <= 1000
#
# * 주어진 덤프 횟수 이내에 평탄화 done =>
# 그 때의 return 최고점 - 최저점. (0 or 1)
#
# max값 - min 값 in all boundry
#
# 옮기는 메커니즘.
# 가장 높은 곳 찾기.
# 가장 낮은 곳 찾기.
# 가장 높은 곳 - 1
# 가장 낮은 곳 + 1
#
# if max == min
# break

test_case = 10
for tc in range(1, test_case+1):
    dumps = int(input())
    W = 100
    H = list(map(int, input().split()))
    for dump in range(dumps):
        h_max = max(H)
        h_min = min(H)
        if h_max != h_min:
            H[H.index(h_max)] -= 1
            H[H.index(h_min)] += 1
        else:
            break

    result = max(H) - min(H)
    print(f"#{tc} {result}")