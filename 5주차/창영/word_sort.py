import sys
input = sys.stdin.readline
print = sys.stdout.write

word_set = set()
for _ in range(int(input().strip())):
    word_set.add(input().strip())

word_list =list(word_set)

for i in sorted(word_list, key=lambda x: (len(x), x)):
    print(i + '\n')