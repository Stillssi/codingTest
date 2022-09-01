def solution(price, money, count):
    cnt =0 
    for i in range(1,count+1,1):
        cnt += price * i

    if money-cnt > 0:
        return 0
    else:
        return cnt-money 

solution(3,20,4)