import requests
import matplotlib.pyplot as plt


def func(s):
    data = s.split(',')
    return data

f = requests.get("https://raw.githubusercontent.com/dm-fedorov/python_basic/master/data/opendata.stat")
lst = list(map(func, str(f.text).split('\n')[1:]))
 
pens = []
for s in lst:
    try:
        if s[0] == 'Средняя пенсия' and s[1] == 'Забайкальский край' and s[2][:4] == '2018':
            pens.append([s[2], int(s[3])])
    except:
        pass

summ = sum([i[1] for i in pens])
print(f"Срендий размер пенсии в 2018: {summ/len(pens)}")


dates = [item[0] for item in pens]
values = [item[1] for item in pens]


plt.figure(figsize=(12, 6))
plt.plot(dates, values)

plt.title('Средний размер пенсии по месяцам в Забайкальском крае в 2018')
plt.xlabel('Дата')
plt.ylabel('Средний размер пенсии')
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
