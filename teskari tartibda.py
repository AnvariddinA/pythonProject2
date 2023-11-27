son = int(input())
rq = 0
while son!= 0:
	qaz = son % 10
	rq = rq * 10 + qaz
	son = son // 10
print(rq)
