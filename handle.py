"""
f = open("E:\website\class.json", "r",encoding='utf-8')
s = f.read()
#print(s)
f.close()
#print(s)
"""
#Regex
#(?<=节\)).+
import re
import time
import json
from weekcalc import calc
data = open("E:\website\timetableocr\class.json").read()
print(data)
now_week = calc()
classes = [[],[],[],[],[],[],[],[]]
hanja = ['','一','二','三','四','五','六','日']
def is_Chinese(word):
    for ch in word:
        if '\u4e00' <= ch <= '\u9fff':
            return True
    return False
def delc(lst):
    for i in range(len(lst)):
        a = re.findall('[\u4e00-\u9fa5a-zA-Z0-9\-]+',lst[i])
        lst[i] = "".join(a)
    lst[1] = re.sub(r'^(.+?)原', "", lst[1])
def judge(lst):
    if int(lst[0]) >= 100:
        lst[0] = lst[0][1:]
    if int(lst[1]) >= 100:
        lst[1] = lst[1][1:]
data={
    "TextDetections": [
        {
            "ColTl": 6,
            "RowTl": 4,
            "ColBr": 7,
            "RowBr": 5,
            "Text": "",
            "Type": "body",
            "Confidence": 0,
            "Polygon": [
                {
                    "X": 926,
                    "Y": 1541
                },
                {
                    "X": 1083,
                    "Y": 1541
                },
                {
                    "X": 1083,
                    "Y": 1840
                },
                {
                    "X": 926,
                    "Y": 1840
                }
            ],
            "AdvancedInfo": "{}"
        },
        {
            "ColTl": 4,
            "RowTl": 3,
            "ColBr": 5,
            "RowBr": 4,
            "Text": "",
            "Type": "body",
            "Confidence": 0,
            "Polygon": [
                {
                    "X": 616,
                    "Y": 954
                },
                {
                    "X": 773,
                    "Y": 954
                },
                {
                    "X": 773,
                    "Y": 1541
                },
                {
                    "X": 618,
                    "Y": 1541
                }
            ],
            "AdvancedInfo": "{}"
        },
        {
            "ColTl": 5,
            "RowTl": 3,
            "ColBr": 6,
            "RowBr": 4,
            "Text": "大数据管理与安全导论@博学西楼(原新3)-204@10-14周(6-7节)大数据管.理与安全导论@博学西楼(原新3)-204@06-08周(6-7节)",
            "Type": "body",
            "Confidence": 98,
            "Polygon": [
                {
                    "X": 773,
                    "Y": 954
                },
                {
                    "X": 926,
                    "Y": 954
                },
                {
                    "X": 926,
                    "Y": 1541
                },
                {
                    "X": 773,
                    "Y": 1541
                }
            ],
            "AdvancedInfo": "{}"
        },
        {
            "ColTl": 6,
            "RowTl": 3,
            "ColBr": 7,
            "RowBr": 4,
            "Text": "大学英语A1@博学北楼(原新4)-412@06-06周(6-7节)",
            "Type": "body",
            "Confidence": 98,
            "Polygon": [
                {
                    "X": 926,
                    "Y": 954
                },
                {
                    "X": 1083,
                    "Y": 954
                },
                {
                    "X": 1083,
                    "Y": 1541
                },
                {
                    "X": 926,
                    "Y": 1541
                }
            ],
            "AdvancedInfo": "{}"
        },
        {
            "ColTl": 7,
            "RowTl": 3,
            "ColBr": 8,
            "RowBr": 4,
            "Text": "",
            "Type": "body",
            "Confidence": 0,
            "Polygon": [
                {
                    "X": 1083,
                    "Y": 954
                },
                {
                    "X": 1238,
                    "Y": 954
                },
                {
                    "X": 1238,
                    "Y": 1541
                },
                {
                    "X": 1083,
                    "Y": 1541
                }
            ],
            "AdvancedInfo": "{}"
        },
        {
            "ColTl": 0,
            "RowTl": 4,
            "ColBr": 1,
            "RowBr": 5,
            "Text": "9-1016:45N18:20",
            "Type": "body",
            "Confidence": 99,
            "Polygon": [
                {
                    "X": 0,
                    "Y": 1541
                },
                {
                    "X": 152,
                    "Y": 1541
                },
                {
                    "X": 152,
                    "Y": 1840
                },
                {
                    "X": 0,
                    "Y": 1840
                }
            ],
            "AdvancedInfo": "{}"
        },
        {
            "ColTl": 1,
            "RowTl": 4,
            "ColBr": 2,
            "RowBr": 5,
            "Text": "",
            "Type": "body",
            "Confidence": 0,
            "Polygon": [
                {
                    "X": 152,
                    "Y": 1541
                },
                {
                    "X": 307,
                    "Y": 1541
                },
                {
                    "X": 307,
                    "Y": 1840
                },
                {
                    "X": 152,
                    "Y": 1840
                }
            ],
            "AdvancedInfo": "{}"
        },
        {
            "ColTl": 2,
            "RowTl": 4,
            "ColBr": 3,
            "RowBr": 5,
            "Text": "中国近现代史纲要@博学东楼(原新2)-402@06-16周", "Type": "body", "Confidence": 98, "Polygon": [{"X": 307, "Y": 1541}, {"X": 460, "Y": 1541}, {"X": 460, "Y": 1840}, {"X": 307, "Y": 1840}], "AdvancedInfo": "{}"}, {"ColTl": 3, "RowTl": 4, "ColBr": 4, "RowBr": 5, "Text": "", "Type": "body", 
"Confidence": 0,
            "Polygon": [
                {
                    "X": 460,
                    "Y": 1541
                },
                {
                    "X": 618,
                    "Y": 1541
                },
                {
                    "X": 618,
                    "Y": 1840
                },
                {
                    "X": 460,
                    "Y": 1840
                }
            ],
            "AdvancedInfo": "{}"
        },
        {
            "ColTl": 4,
            "RowTl": 4,
            "ColBr": 5,
            "RowBr": 5,
            "Text": "",
            "Type": "body",
            "Confidence": 0,
            "Polygon": [
                {
                    "X": 618,
                    "Y": 1541
                },
                {
                    "X": 773,
                    "Y": 1541
                },
                {
                    "X": 773,
                    "Y": 1840
                },
                {
                    "X": 618,
                    "Y": 1840
                }
            ],
            "AdvancedInfo": "{}"
        },
        {
            "ColTl": 5,
            "RowTl": 4,
            "ColBr": 6,
            "RowBr": 5,
            "Text": "",
            "Type": "body",
            "Confidence": 0,
            "Polygon": [
                {
                    "X": 773,
                    "Y": 1541
                },
                {
                    "X": 926,
                    "Y": 1541
                },
                {
                    "X": 926,
                    "Y": 1840
                },
                {
                    "X": 773,
                    "Y": 1840
                }
            ],
            "AdvancedInfo": "{}"
        },
        {
            "ColTl": 3,
            "RowTl": 3,
            "ColBr": 4,
            "RowBr": 4,
            "Text": "",
            "Type": "body",
            "Confidence": 0,
            "Polygon": [
                {
                    "X": 460,
                    "Y": 954
                },
                {
                    "X": 616,
                    "Y": 954
                },
                {
                    "X": 618,
                    "Y": 1541
                },
                {
                    "X": 460,
                    "Y": 1541
                }
            ],
            "AdvancedInfo": "{}"
        },
        {
            "ColTl": 7,
            "RowTl": 4,
            "ColBr": 8,
            "RowBr": 5,
            "Text": "",
            "Type": "body",
            "Confidence": 0,
            "Polygon": [
                {
                    "X": 1083,
                    "Y": 1541
                },
                {
                    "X": 1238,
                    "Y": 1541
                },
                {
                    "X": 1238,
                    "Y": 1840
                },
                {
                    "X": 1083,
                    "Y": 1840
                }
            ],
            "AdvancedInfo": "{}"
        },
        {
            "ColTl": 0,
            "RowTl": 5,
            "ColBr": 1,
            "RowBr": 6,
            "Text": "",
            "Type": "body",
            "Confidence": 0,
            "Polygon": [
                {
                    "X": 0,
                    "Y": 1840
                },
                {
                    "X": 152,
                    "Y": 1840
                },
                {
                    "X": 152,
                    "Y": 1960
                },
                {
                    "X": 0,
                    "Y": 1960
                }
            ],
            "AdvancedInfo": "{}"
        },
        {
            "ColTl": 1,
            "RowTl": 5,
            "ColBr": 2,
            "RowBr": 6,
            "Text": "",
            "Type": "body",
            "Confidence": 0,
            "Polygon": [
                {
                    "X": 152,
                    "Y": 1840
                },
                {
                    "X": 307,
                    "Y": 1840
                },
                {
                    "X": 307,
                    "Y": 1960
                },
                {
                    "X": 152,
                    "Y": 1960
                }
            ],
            "AdvancedInfo": "{}"
        },
        {
            "ColTl": 2,
            "RowTl": 5,
            "ColBr": 3,
            "RowBr": 6,
            "Text": "",
            "Type": "body",
            "Confidence": 0,
            "Polygon": [
                {
                    "X": 307,
                    "Y": 1840
                },
                {
                    "X": 460,
                    "Y": 1840
                },
                {
                    "X": 460,
                    "Y": 1960
                },
                {
                    "X": 307,
                    "Y": 1960
                }
            ],
            "AdvancedInfo": "{}"
        },
        {
            "ColTl": 3,
            "RowTl": 5,
            "ColBr": 4,
            "RowBr": 6,
            "Text": "",
            "Type": "body",
            "Confidence": 0,
            "Polygon": [
                {
                    "X": 460,
                    "Y": 1840
                },
                {
                    "X": 618,
                    "Y": 1840
                },
                {
                    "X": 618,
                    "Y": 1960
                },
                {
                    "X": 460,
                    "Y": 1960
                }
            ],
            "AdvancedInfo": "{}"
        },
        {
            "ColTl": 4,
            "RowTl": 5,
            "ColBr": 5,
            "RowBr": 6,
            "Text": "",
            "Type": "body",
            "Confidence": 0,
            "Polygon": [
                {
                    "X": 618,
                    "Y": 1840
                },
                {
                    "X": 773,
                    "Y": 1840
                },
                {
                    "X": 773,
                    "Y": 1960
                },
                {
                    "X": 618,
                    "Y": 1960
                }
            ],
            "AdvancedInfo": "{}"
        },
        {
            "ColTl": 5,
            "RowTl": 5,
            "ColBr": 6,
            "RowBr": 6,
            "Text": "",
            "Type": "body",
            "Confidence": 0,
            "Polygon": [
                {
                    "X": 773,
                    "Y": 1840
                },
                {
                    "X": 926,
                    "Y": 1840
                },
                {
                    "X": 926,
                    "Y": 1960
                },
                {
                    "X": 773,
                    "Y": 1960
                }
            ],
            "AdvancedInfo": "{}"
        },
        {
            "ColTl": 6,
            "RowTl": 5,
            "ColBr": 7,
            "RowBr": 6,
            "Text": "",
            "Type": "body",
            "Confidence": 0,
            "Polygon": [
                {
                    "X": 926,
                    "Y": 1840
                },
                {
                    "X": 1083,
                    "Y": 1840
                },
                {
                    "X": 1083,
                    "Y": 1960
                },
                {
                    "X": 926,
                    "Y": 1960
                }
            ],
            "AdvancedInfo": "{}"
        },
        {
            "ColTl": 7,
            "RowTl": 5,
            "ColBr": 8,
            "RowBr": 6,
            "Text": "",
            "Type": "body",
            "Confidence": 0,
            "Polygon": [
                {
                    "X": 1083,
                    "Y": 1840
                },
                {
                    "X": 1238,
                    "Y": 1840
                },
                {
                    "X": 1238,
                    "Y": 1960
                },
                {
                    "X": 1083,
                    "Y": 1960
                }
            ],
            "AdvancedInfo": "{}"
        },
        {
            "ColTl": 1,
            "RowTl": 2,
            "ColBr": 2,
            "RowBr": 3,
            "Text": "数学分析1@博学西楼(原新3)-304@18-18周(3-5节)数学分析1@博学西楼(原新3)-413@07-16周(3-4节)",
            "Type": "body",
            "Confidence": 99,
            "Polygon": [
                {
                    "X": 152,
                    "Y": 490
                },
                {
                    "X": 301,
                    "Y": 490
                },
                {
                    "X": 303,
                    "Y": 955
                },
                {
                    "X": 152,
                    "Y": 954
                }
            ],
            "AdvancedInfo": "{}"
        },
        {
            "ColTl": 0,
            "RowTl": 1,
            "ColBr": 1,
            "RowBr": 2,
            "Text": "1-208:0009:35",
            "Type": "body",
            "Confidence": 99,
            "Polygon": [
                {
                    "X": 0,
                    "Y": 187
                },
                {
                    "X": 152,
                    "Y": 187
                },
                {
                    "X": 152,
                    "Y": 490
                },
                {
                    "X": 0,
                    "Y": 488
                }
            ],
            "AdvancedInfo": "{}"
        },
        {
            "ColTl": 1,
            "RowTl": 1,
            "ColBr": 2,
            "RowBr": 2,
            "Text": "形势与政策@博学东楼(原新2)-109@10-13周(1-2节)",
            "Type": "body",
            "Confidence": 99,
            "Polygon": [
                {
                    "X": 152,
                    "Y": 187
                },
                {
                    "X": 301,
                    "Y": 187
                },
                {
                    "X": 301,
                    "Y": 490
                },
                {
                    "X": 152,
                    "Y": 490
                }
            ],
            "AdvancedInfo": "{}"
        },
        {
            "ColTl": 2,
            "RowTl": 1,
            "ColBr": 3,
            "RowBr": 2,
            "Text": "-1)",
            "Type": "body",
            "Confidence": 70,
            "Polygon": [
                {
                    "X": 301,
                    "Y": 187
                },
                {
                    "X": 458,
                    "Y": 187
                },
                {
                    "X": 460,
                    "Y": 488
                },
                {
                    "X": 301,
                    "Y": 490
                }
            ],
            "AdvancedInfo": "{}"
        },
        {
            "ColTl": 3,
            "RowTl": 1,
            "ColBr": 4,
            "RowBr": 2,
            "Text": "数学分析1@博学西楼(原新3)-3 04@06-16周(1-2节)", "Type": "body", "Confidence": 99, "Polygon": [{"X": 458, "Y": 187}, {"X": 614, "Y": 187}, {"X": 616, "Y": 488}, {"X": 460, "Y": 488}], "AdvancedInfo": "{}"}, {"ColTl": 4, "RowTl": 1, "ColBr": 5, "RowBr": 2, "Text": "大学英语A1@博学北楼(原新4)-412@06-1) 7周(1-2节)", "Type": "body", "Confidence": 99, "Polygon": [{"X": 614, "Y": 187}, {"X": 773, "Y": 187}, {"X": 773, "Y": 488}, {"X": 616, "Y": 488}], "AdvancedInfo": "{}"}, {"ColTl": 5, "RowTl": 1, "ColBr": 6, "RowBr": 2, "Text": "", "Type": "body", "Confidence": 0, "Polygon": [{"X": 773, "Y": 187}, {"X": 924, "Y": 187}, {"X": 926, "Y": 488}, {"X": 773, "Y": 488}], "AdvancedInfo": "{}"}, {"ColTl": 6, "RowTl": 1, "ColBr": 7, "RowBr": 2, "Text": "", "Type": "body", "Confidence": 0, "Polygon": [{"X": 924, "Y": 187}, {"X": 1083, "Y": 187}, {"X": 1083, "Y": 488}, {"X": 926, "Y": 488}], "AdvancedInfo": "{}"}, {"ColTl": 7, "RowTl": 1, "ColBr": 8, "RowBr": 2, "Text": "", "Type": "body", "Confidence": 0, "Polygon": [{"X": 1083, "Y": 187}, {"X": 1238, "Y": 187}, {"X": 1238, "Y": 488}, {"X": 1083, "Y": 488}], "AdvancedInfo": "{}"}, {"ColTl": 0, "RowTl": 2, "ColBr": 1, "RowBr": 3, "Text": "3-509: 55N'12: 20", "Type": "body", "Confidence": 85, "Polygon": [{"X": 0, "Y": 488}, {"X": 152, "Y": 490}, {"X": 152, "Y": 954}, {"X": 0, "Y": 954}], "AdvancedInfo": "{}"}, {"ColTl": 0, "RowTl": 0, "ColBr": 8, "RowBr": 1, "Text": "周一周二周三周四周五周六周日11-1811-1911-2011-2111-2211-2311-24", "Type": "body", "Confidence": 99, "Polygon": [{"X": 0, "Y": 2}, {"X": 1238, "Y": 2}, {"X": 1238, "Y": 187}, {"X": 0, "Y": 187}], "AdvancedInfo": "{}"}, {"ColTl": 2, "RowTl": 2, "ColBr": 3, "RowBr": 3, "Text": "基础体育@南湖校区@06-15周(3-5节)基础体育@南湖校区@116-16周(3-4节)", "Type": "body", "Confidence": 97, "Polygon": [{"X": 301, "Y": 490}, {"X": 460, "Y": 488}, {"X": 460, "Y": 954}, {"X": 303, "Y": 955}], "AdvancedInfo": "{}"}, {"ColTl": 3, "RowTl": 2, "ColBr": 4, "RowBr": 3, "Text": ")微观经济学C@博学北楼(原新4)-609@0) 6-17周(3-5节)", "Type": "body", "Confidence": 99, "Polygon": [{"X": 460, "Y": 488}, {"X": 616, "Y": 488}, {"X": 616, "Y": 954}, {"X": 460, "Y": 954}], "AdvancedInfo": "{}"}, {"ColTl": 4, "RowTl": 2, "ColBr": 5, "RowBr": 3, "Text": "中国近现代史纲要@博学东楼()原新2)-401@06-15周(3-4节)", "Type": "body", "Confidence": 99, "Polygon": [{"X": 616, "Y": 488}, 
{
                "X": 773,
                "Y": 488
            },
            {
                "X": 773,
                "Y": 954
            },
            {
                "X": 616,
                "Y": 954
            }
        ],
        "AdvancedInfo": "{}"
    },
    {
        "ColTl": 5,
        "RowTl": 2,
        "ColBr": 6,
        "RowBr": 3,
        "Text": "数学分析1@博学西楼(原新3)-304@06-08周(3-5节)数学分析1@博学西楼(原新3)-304@10-17周(3-5节)",
        "Type": "body",
        "Confidence": 99,
        "Polygon": [
            {
                "X": 773,
                "Y": 488
            },
            {
                "X": 926,
                "Y": 488
            },
            {
                "X": 926,
                "Y": 954
            },
            {
                "X": 773,
                "Y": 954
            }
        ],
        "AdvancedInfo": "{}"
    },
    {
        "ColTl": 6,
        "RowTl": 2,
        "ColBr": 7,
        "RowBr": 3,
        "Text": "数学分析1@博学西楼(原新3)-205@06-06周(3-4节)",
        "Type": "body",
        "Confidence": 99,
        "Polygon": [
            {
                "X": 926,
                "Y": 488
            },
            {
                "X": 1083,
                "Y": 488
            },
            {
                "X": 1083,
                "Y": 954
            },
            {
                "X": 926,
                "Y": 954
            }
        ],
        "AdvancedInfo": "{}"
    },
    {
        "ColTl": 7,
        "RowTl": 2,
        "ColBr": 8,
        "RowBr": 3,
        "Text": "",
        "Type": "body",
        "Confidence": 0,
        "Polygon": [
            {
                "X": 1083,
                "Y": 488
            },
            {
                "X": 1238,
                "Y": 488
            },
            {
                "X": 1238,
                "Y": 954
            },
            {
                "X": 1083,
                "Y": 954
            }
        ],
        "AdvancedInfo": "{}"
    },
    {
        "ColTl": 0,
        "RowTl": 3,
        "ColBr": 1,
        "RowBr": 4,
        "Text": "6-814:00N'16:25",
        "Type": "body",
        "Confidence": 85,
        "Polygon": [
            {
                "X": 0,
                "Y": 954
            },
            {
                "X": 152,
                "Y": 954
            },
            {
                "X": 152,
                "Y": 1541
            },
            {
                "X": 0,
                "Y": 1541
            }
        ],
        "AdvancedInfo": "{}"
    },
    {
        "ColTl": 1,
        "RowTl": 3,
        "ColBr": 2,
        "RowBr": 4,
        "Text": "大学英语A1@博学北楼(原新4)-412@07-17周(6-7节)",
        "Type": "body",
        "Confidence": 99,
        "Polygon": [
            {
                "X": 152,
                "Y": 954
            },
            {
                "X": 303,
                "Y": 955
            },
            {
                "X": 307,
                "Y": 1541
            },
            {
                "X": 152,
                "Y": 1541
            }
        ],
        "AdvancedInfo": "{}"
    },
    {
        "ColTl": 2,
        "RowTl": 3,
        "ColBr": 3,
        "RowBr": 4,
        "Text": "微观经济学C@博学-北楼(原新4)-208@06-07周(6-7节)",
        "Type": "body",
        "Confidence": 97,
        "Polygon": [
            {
                "X": 303,
                "Y": 955
            },
            {
                "X": 460,
                "Y": 954
            },
            {
                "X": 460,
                "Y": 1541
            },
            {
                "X": 307,
                "Y": 1541
            }
        ],
        "AdvancedInfo": "{}"
    }
]
}
for i in data['TextDetections']:
    for key, value in i.items():
        if key == "Text" and value != "" and is_Chinese(value):
            #print(value)
            #print(i["ColTl"], i["RowTl"])
            lst = list(value.split("@"))
            #print(lst)
            if (len(lst) <= 1): continue
            if (len(lst) > 3):
                value1 = value[:re.search('节\)', value).span()[0] + 2]
                value2 = value[re.search('节\)', value).span()[0] + 2:]
                lst1 = list(value1.split("@"))
                lst2 = list(value2.split("@"))
                delc(lst1), delc(lst2)
                #print(lst1, lst2)
                #print("星期{}第{} 或 第{}".format(i["ColTl"],re.findall(r'(?<=周).*', lst1[2])[0], re.findall(r'(?<=周).*', lst2[2])[0]))
                week1, week2 = re.findall(r'.*(?=周)', lst1[2])[0], re.findall(r'.*(?=周)', lst2[2])[0]
                #print(week1, week2)
                w1 = list(week1.split("-"))
                w2 = list(week2.split("-"))
                judge(w1), judge(w2)
                if int(w1[0]) <= now_week and now_week <= int(w1[1]):
                    #print("former")
                    classes[i["ColTl"]].append([i["RowTl"], lst1[0], lst1[1], re.findall(r'(?<=周).*', lst1[2])[0]])
                elif int(w2[0]) <= now_week and now_week <= int(w2[1]):
                    #print("latter")
                    classes[i["ColTl"]].append([i["RowTl"], lst2[0], lst2[1], re.findall(r'(?<=周).*', lst2[2])[0]])
                #print(w1, w2)
            else:
                delc(lst)
                week = re.findall(r'.*(?=周)', lst[2])[0]
                w = list(week.split("-"))
                judge(w)
                if int(w[0]) <= now_week and now_week <= int(w[1]):
                    #print("in week")
                    classes[i["ColTl"]].append([i["RowTl"], lst[0], lst[1], re.findall(r'(?<=周).*', lst[2])[0]])
                #print(w)
                #print(lst)
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