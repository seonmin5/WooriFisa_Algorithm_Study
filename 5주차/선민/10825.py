import sys
input = sys.stdin.readline

# 반 학생의 수
n = int(input().strip())

# 학생의 이름, 국어, 영어, 수학점수
student = []
for _ in range(n):
    name, ko, eng, math = map(str, input().strip().split())
    student.append([name, ko, eng, math])
    
# 국어 점수가 감소하는 순서로 => 국어 내림차순
# 국어 점수가 같으면 영어 점수가 증가하는 순서로 => 영어 오름차순
# 국어 점수와 영어 점수가 같으면 수학 점수가 감소하는 순서로 => 수학 내림차순
# 모든 점수가 같으면 이름이 사전 순으로 증가하는 순서로 (단, 아스키 코드에서 대문자는 소문자보다 작으므로 사전순으로 앞에 온다.)
# => 이름 오름차순
student.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in student:
    print(i[0])