"""
f = open("E:\website\class.json", "r",encoding='utf-8')
s = f.read()
#print(s)
f.close()
#print(s)
"""
import json
import operator
# Regex
# (?<=节\)).+
import re
import time


from app.weekcalc import calc

# print(data)
def is_Chinese(word):
    for ch in word:
        if '\u4e00' <= ch <= '\u9fff':
            return True
    return False


def delc(lst):
    for i in range(len(lst)):
        a = re.findall('[\u4e00-\u9fa5a-zA-Z0-9\-]+', lst[i])
        lst[i] = "".join(a)
    lst[1] = re.sub(r'^(.+?)原', "", lst[1])


def judge(lst):
    if int(lst[0]) >= 100:
        lst[0] = lst[0][1:]
    if int(lst[1]) >= 100:
        lst[1] = lst[1][1:]

def handle(data):
    now_week = weekcalc.calc()
    classes = [[], [], [], [], [], [], [], []]
    hanja = ['', '一', '二', '三', '四', '五', '六', '日']
    #data = open("E:\\website\\timetableocr\\class.json", encoding='utf-8').read()
    data = json.loads(data)
    for i in data['TextDetections']:
        for key, value in i.items():
            if key == "Text" and value != "" and is_Chinese(value):
                value = re.sub(r'[,\._\|\/\\]+', "", value)
                # print(value)
                #print(i["ColTl"], i["RowTl"])
                lst = list(value.split("@"))
                # print(lst)
                if (len(lst) <= 1):
                    continue
                if (len(lst) > 3):
                    value1 = value[:re.search('节\)', value).span()[0] + 2]
                    value2 = value[re.search('节\)', value).span()[0] + 2:]
                    lst1 = list(value1.split("@"))
                    lst2 = list(value2.split("@"))
                    delc(lst1), delc(lst2)
                    #print(lst1, lst2)
                    #print("星期{}第{} 或 第{}".format(i["ColTl"],re.findall(r'(?<=周).*', lst1[2])[0], re.findall(r'(?<=周).*', lst2[2])[0]))
                    week1, week2 = re.findall(
                        r'.*(?=周)', lst1[2])[0], re.findall(r'.*(?=周)', lst2[2])[0]
                    #print(week1, week2)
                    w1 = list(week1.split("-"))
                    w2 = list(week2.split("-"))
                    judge(w1), judge(w2)
                    if int(w1[0]) <= now_week and now_week <= int(w1[1]):
                        # print("former")
                        classes[i["ColTl"]].append(
                            {"Index": i["RowTl"], "Lesson": lst1[0], "Location": lst1[1], "Period": re.findall(r'(?<=周).*', lst1[2])[0]})
                    elif int(w2[0]) <= now_week and now_week <= int(w2[1]):
                        # print("latter")
                        classes[i["ColTl"]].append(
                            {"Index": i["RowTl"], "Lesson": lst2[0], "Location": lst2[1], "Period": re.findall(r'(?<=周).*', lst2[2])[0]})
                    #print(w1, w2)
                else:
                    delc(lst)
                    week = re.findall(r'.*(?=周)', lst[2])[0]
                    w = list(week.split("-"))
                    judge(w)
                    if int(w[0]) <= now_week and now_week <= int(w[1]):
                        #print("in week")
                        classes[i["ColTl"]].append(
                            {"Index": i["RowTl"], "Lesson": lst[0], "Location": lst[1], "Period": re.findall(r'(?<=周).*', lst[2])[0]})
                    # print(w)
                    # print(lst)
    for i in range(1, len(classes)):
        classes[i] = sorted(classes[i], key=operator.itemgetter('Index'))
    #print(classes)
    classes = json.dumps(classes)
    return classes
"""
for i in range(1, len(classes)):
    classes[i].sort()
    print("周{}：".format(hanja[i]))
    for j in range(len(classes[i])):
        for k in range(len(classes[i][j])):
            if k == 3 and classes[i][j][0] == 4 and classes[i][j][k] == '':
                print("9-10节", end = ' ')
            elif k == 3 and classes[i][j][0] == 5 and classes[i][j][k] == '':
                print("11-13节", end = ' ')
            else:
                print(classes[i][j][k], end = ' ')
        print()
"""
