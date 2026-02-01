number = input()
set_ = []#필요한 숫자 = index, index의 값 = 각 숫자가 필요한 수
for i in range(10):
    set_.append(0)
for i in number:
    if int(i) != 6 and int(i) != 9:
        set_[int(i)]+=1
    else:#6과9는 같이 쓰일 수 있으므로 6인덱스만 사용
        set_[6] += 1
if set_[6]%2:#짝수개가 아니면
    set_[6] //= 2
    set_[6] += 1#하나더 추가
else:#짝수개면 그냥 절반
    set_[6] //=2
print(max(set_))#세트의 수 = 각 숫자가 최대로 필요한 수
