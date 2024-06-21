# Mileage-based Course Registration System

## Table of Contents
1. [Motivation](#motivation)
2. [Data Acquisition](#data-acquisition)
3. [Model](#model)
4. [Performance](#performance)
5. [Usage](#usage)
6. [Contributors](#contributors)
7. [License](#license)

## Motivation
[Back to Table of Contents](#table-of-contents)

이 프로젝트는 연세대학교 마일리지 수강 신청 시스템의 이해를 돕기 위해 시작되었습니다. 1학년과 달리 마일리지를 사용하여 진행되는 수강 신청 시스템을 학생들이 잘 이해하고 실제 수강 신청에서 적절한 전략을 짤 수 있도록 모의로 실행해 보는 기회를 제공합니다. 

## Data Acquisition
[Back to Table of Contents](#table-of-contents)

데이터는 학생들의 마일리지 정보를 포함하고 있습니다. 데이터는 다음과 같은 특성을 가지고 있습니다:
- 마일리지
- 신청 과목 수
- 총이수학점비율
- 직전학기 이수학점비율
- 학년

데이터는 CSV 형식으로 제공되었으며, 필요한 경우 전처리 과정을 거쳤습니다. (연세대학교 임의의 과목의 전 학기 마일리지 내역을 사용하였습니다.)

## Model
[Back to Table of Contents](#table-of-contents)

마일리지 기반 수강 신청 시스템은 학생들의 마일리지를 우선으로 하여 수강 신청 순위를 결정하는 알고리즘을 사용합니다. 주어진 마일리지 데이터를 기반으로 학생들의 신청 우선순위를 결정합니다. 만약 같은 마일리지를 배당한 경우 데이터 정보를 순차적으로 비교하여 우선 순위를 결정합니다.

사용된 알고리즘:
- 마일리지 순위 기반 배정 알고리즘

## Performance
[Back to Table of Contents](#table-of-contents)

모델의 성능은 시스템의 공정성과 효율성으로 평가됩니다. 실제 운영 데이터를 통해 다음과 같은 지표를 사용하여 평가하였습니다:
- 평균 대기 시간
- 마일리지 사용 효율성
- 학생 만족도

구체적인 성능 평가 결과는 추가 데이터 분석을 통해 제공될 예정입니다.

## Usage
[Back to Table of Contents](#table-of-contents)

프로젝트를 사용하는 방법은 다음과 같습니다:

1. 데이터 파일을 `data` 폴더에 위치시킵니다.

2. 시스템 실행:
    ```bash
    python 마일리지_수강신청.py
    ```
3. 자신의 배당할 마일리지, 신청 과목 수, 총이수학점비율, 직전학기 이수학점비율, 학년 값을 차례로 입력합니다.
    ```bash
    mil = int(input("신청 과목에 넣을 마일리지를 입력하시오 : "))
    num_S = int(input("신청 과목 수를 입력하시오 : "))
    rate_T = float(input("총이수학점비율을 입력하시오 : "))
    rate_B = float(input("직전학기 이수학점 비율을 입력하시오 : "))
    my_Grade = int(input("학년을 입력하시오 : "))
    ```
   마일리지는 0 이상 36 이하의 범위로 입력해야 하며, 학년은 2 - 4 학년까지 입력해야 합니다. (나머지 데이터 값은 faulty input이 없다고 가정함.)
    ```bash
    if mil < 0 or mil > 36 :
        print("잘못된 마일리지 값입니다.")
    ```
    ```bash
    ~ ~ ~
    else:
        print("학년이 잘못 입력되었습니다.")
    ```
  
4. 코드는 주어진 데이터 파일을 학년에 따라 분류하고, 입력받은 이의 데이터를 같은 학년의 list에 추가합니다.
    ```bash
    for k in range(len(text_final)):
        grade=text_final[k][4]
        if grade==2:
            soph_list.append(text_final[k])
        elif grade==3:
            jun_list.append(text_final[k])
        else:
            sen_list.append(text_final[k])
    ```
   
5. 이후 각 학년 별 list를 순차적으로 sort합니다. (3,4학년 코드 생략)
    ```bash
    if my_Grade == 2 :
        i = 1
        soph_list.append(my_List)
        soph_list=sorted(soph_list, key=itemgetter(0,1,2,3), reverse=True)
    ```

6. 입력받은 데이터의 사람이 어느 순위에 있는지 확인하고 수강 신청 성공 여부를 출력합니다. 이때 수강 신청에 실패한 경우, 대기번호를 출력합니다. (3,4학년 코드 생략)
    ```bash
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
    ```
    ```bash
    if res == 'Success' :
        print(f"순위 : {R}")
        print("수강 신청에 성공하셨습니다.\n")
    elif res == 'Fail' :
        print(f"순위 : {R}")
        print("수강 신청에 실패하셨습니다.")
        print(f"대기번호 : {wai}\n")
    ```
