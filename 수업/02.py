def solution(id_list,report,k):
    e_ed_dict = {}
    mail_dict = {}
    answer = []
    for i in id_list:
        e_ed_dict[i] = set()
        mail_dict[i] = 0

    for i in report:
        report, reported = i.split(' ')
        e_ed_dict[reported].add(report)
    
    for key in e_ed_dict:
        if len(e_ed_dict[key]) >= k:
            for user in e_ed_dict[key]:
                mail_dict[user] += 1
    
    for user in mail_dict:
        answer.append(mail_dict[user])

    return answer