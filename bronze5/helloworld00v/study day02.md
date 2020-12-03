백준 [#2475] 검증수       

검증수는 고유번호의 처음 5자리에 들어가는 5개의 숫자를 각각 제곱한 수의 합을 10으로 나눈 나머지이다. 
예를 들어, 고유번호의 처음 5자리의 숫자들이 04256이면,  
각 숫자를 제곱한 수들의 합 0+16+4+25+36 = 81을 10으로 나눈 나머지인 1이 검증수.

[입력] 
첫째 줄에 고유번호의 처음 5자리의 숫자들이 빈칸을 사이에 두고 하나씩 주어진다. 
0 4 2 5 6

[출력]
첫째 줄에 검증수를 출력한다 



```python
lst = list(map(int,input().split()))
sum=0
for e in lst:
    sum += e**2
    print(sum%10)
```

백준 [#2557] Hello world! 를 출력하시오


```python
print("hello world!")
```

백준 [#2558] 두 정수 A과 B를 입력받은 다음 A+B를 출력하는 프로그램을 작성하시오.


```python
a = int(input())
b = int(input())
print(a+b)
```

백준 [#2845] 파티가 끝나고 난 뒤 

첫째 줄에 1m2당 사람의 수 L(1<=L<=10)과 파티가 열렸던 곳의 넓이 P(1<=P<=1000)가 주어진다.     
둘째 줄에는 각 기사에 실려있는 참가자의 수가 주어진다. 10의 6제곱보다 작은 양의 정수 5개가 주어진다,      

[출력] 
출력은 첫째 줄에 다섯 개의 숫자를 출력해야 한다. 이 숫자는 상근이가 게산한 참가자의 수와 각 기사에 적혀있는 참가자의 수의 차이이다. 

5 20 
99 101 1000 0 97 



```python
L, P = map(int, input().split())  
news=list(map(int, input().split()))
for i in news:
    print(i-L*P, end='')
```


```python
p,s = map(int, input().split())
people = p*s 
L=[str(i-(p*s))for i in list(map(int().split()))]      
''.join(L)
```


```python
L, P = map(int, input().split())
posted_people = [int(people) for people in input().split()]

real = L*P     

diff = [int(posted)-real for posted in posted_people]
print(''.join(map(str,diff)))
```

백준 [#2914] 저작권

적어도 몇 곡이 저작권이 있는 멜로디인지 구하는 프로그램 


Q. 첫째 줄에 앨범이 수록된 곡의 개수 A와 평균값 I가 주어진다(1<=A,I<=100)  
첫째 줄에 적어도 몇 곡이 저작권이 있는 멜로디인지 출력
A : 저작권이 있는 멜로디의 총 개수 
B : 앨범에 수록된 곡의 개수 
C : 평균을 올림한 값으로 하면
A/B = (올림)C 가 된다. 

만약 (올린 후의)평균이 24가 나왔다면, 올림을 안했을 때의 평균이 23일 때의 저작권 곡에서 딱 
1권을 더했을 때의 곡의 평균은 23.xxx가 될 것이고, 이것을 올림하면 24가 될 것이므로, 
이 때 곡의 개수가 평균이 24인 곡의 갯수에서 최소가 될 것임. 

따라서 첫째줄에 map을 통해 a,b를 각각 받아와 
둘째줄에 (b-1)을 넣어주었을때의 총 멜로디의 갯수를 구한다음 1을 더하여 출력


```python
A, I = input().split()  # 수록된 곡의 개수 A와 평균값 I
A = int(A)    
I = int(I)

print(A*(I-1)+1)
```


```python
A, I = map(int, input().split())
print(A*(I-1)+1)
```
