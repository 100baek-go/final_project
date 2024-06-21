f=open("mileage_list.csv",encoding='utf-16')
text=f.read()
text=text.split('\n')
text_final=[]
for i in text[1:]:
    i=i.split('\t')
    for j in range(len(i)):
        if "0." in i[j]:
            i[j]=int(float(i[j])*1000)
        else: i[j]=int(i[j])
    text_final.append(i)

soph_list=[]
jun_list=[]
sen_list=[]

soph_num = 22
jun_num = 22
sen_num = 22

print("========수강신청========\n")

for k in range(len(text_final)):
        grade=text_final[k][4]
        if grade==2:
            soph_list.append(text_final[k])
        elif grade==3:
            jun_list.append(text_final[k])
        else:
            sen_list.append(text_final[k])

i = 0

while i == 0 :

    from operator import itemgetter

    my_List = []
    mil = int(input("신청 과목에 넣을 마일리지를 입력하시오 : "))
    num_S = int(input("신청 과목 수를 입력하시오 : "))
    rate_T = float(input("총이수학점비율을 입력하시오 : "))
    rate_B = float(input("직전학기 이수학점 비율을 입력하시오 : "))
    my_Grade = int(input("학년을 입력하시오 : "))

    my_List.append(mil)
    my_List.append(num_S)
    my_List.append(rate_T)
    my_List.append(rate_B)
    my_List.append(my_Grade)

    if mil < 0 or mil > 36 :
        print("잘못된 마일리지 값입니다.")
    
    if my_Grade == 2 :
        i = 1
        soph_list.append(my_List)
        soph_list=sorted(soph_list, key=itemgetter(0,1,2,3), reverse=True)
    elif my_Grade == 3 :
        i = 1
        jun_list.append(my_List)
        jun_list=sorted(jun_list, key=itemgetter(0,1,2,3), reverse=True)
    elif my_Grade == 4 :
        i = 1
        sen_list.append(my_List)
        sen_list=sorted(sen_list, key=itemgetter(0,1,2,3), reverse=True)
    else:
        print("학년이 잘못 입력되었습니다.")


if my_Grade == 2 :
    for m in range(len(soph_list)):
        if soph_list[m] == my_List :
            R = m + 1
    v = soph_num - R
    if v < 0 :
        res = 'Fail'
        wai = -v
    else:
        res = 'Success'
elif my_Grade == 3 :
    for m in range(len(jun_list)):
        if jun_list[m] == my_List :
            R = m
    v = jun_num - R
    if v < 0 :
        res = 'Fail'
        wai = -v
    else:
        res = 'Success'
elif my_Grade == 4 :
    for m in range(len(sen_list)):
        if sen_list[m] == my_List :
            R = m
    v = sen_num - R
    if v < 0 :
        res = 'Fail'
        wai = -v
    else:
        res = 'Success'

print("=======수강신청 결과=======\n")
if res == 'Success' :
    print(f"순위 : {R}")
    print("수강 신청에 성공하셨습니다.\n")
elif res == 'Fail' :
    print(f"순위 : {R}")
    print("수강 신청에 실패하셨습니다.")
    print(f"대기번호 : {wai}\n")