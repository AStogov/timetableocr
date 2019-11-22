import time
import st_day
l = st_day.s.split('/')
#print(l)
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
o_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def calc():
    if int(l[0]) % 4 != 0 or (int(l[0]) % 4 == 0 and int(l[0]) % 400 != 0):
	    pas_days = 0
	    for i in range(1, int(l[1])):
		    pas_days = pas_days + days[i - 1]
	    pas_days = pas_days + int(l[2])
    else:
	    pas_days = 0
	    for i in range(1, int(l[1])):
		    pas_days = pas_days + o_days[i - 1]
	    pas_days = pas_days + int(l[2])
    return int((time.localtime().tm_yday - pas_days) / 7)