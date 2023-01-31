def solution(n):
    answer = ''
    #3진법
    number_dict ={
        1 : '1',
        2: '2',
        0: '4'
    }
    while n!=0:
        remainder = n%3
        answer = number_dict[remainder]+ answer
        if n%3 == 0:
            n = n//3 -1
        else:
            n = n//3
            
    return answer