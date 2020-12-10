
# Bronze V
### 1000번 
문제 :  두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성
```python 
a,b=map(int,input().split())
print(a+b)
```

### 1001번 
문제 : 두 정수 A와 B를 입력받은 다음, A-B를 출력하는 프로그램을 작성
```python
a,b=map(int,input().split())
print(a-b)
```
### 1271번 
문제: 갑부 최백준 조교는 동전을 최소로 바꾸는데 성공했으나 김재홍 조교가 그 돈을 발견해서 최백준 조교에게 그 돈을 나누자고 따진다.
그 사실이 전 우주로 알려지자 우주에 있던 많은 생명체들이 자신들에게 돈을 분배해 달라고 당장 달려오기 시작했다.
프로토스 중앙 우주 정부의 정책인, ‘모든 지적 생명체는 동등하다’라는 규칙에 입각해서 돈을 똑같이 분배하고자 한다.
한 생명체에게 얼마씩 돈을 줄 수 있는가?
또, 생명체들에게 동일하게 분배한 후 남는 돈은 얼마인가?
```python
money, living = map(int, input('').split(' '))
m_changes = money//living
n_changes =  money % living
print(m_changes,n_changes)
```

### 1550번 
문제 : 16진수 수를 입력받아서 10진수로 출력하는 프로그램을 작성
```python
print(int(input(), 16)) 
```

### 2338번
문제 : 두 수 A, B를 입력받아, A+B, A-B, A×B를 구하는 프로그램을 작성
```python 
a=int(input())
b=int(input())
print(a+b)
print(a-b)
print(a*b)
```
