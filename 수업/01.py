def solution(lottos, win_nums):
    lottodict = {0:6, 1:6, 2:5, 3:4, 4:3,5:2, 6:1}
    zero = lottos.count(0)
    count = 0
    for i in lottos:
        if i in win_nums:
            count += 1
    return [lottodict[count+zero],lottodict[count]]

solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25])