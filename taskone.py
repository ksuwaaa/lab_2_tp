import requests
import matplotlib.pyplot as plt


def func(s):
    data = s.split(',')[1:]
    return data

f = requests.get("https://raw.githubusercontent.com/dm-fedorov/python_basic/master/data/opendata.stat")
lst = list(map(func, str(f.text).split('\n')[1:]))

pens = []
for s in lst:
    try:
        if s[0] == 'Забайкальский край' and s[1][:4] == '2018':
            pens.append([s[1], int(s[2])])
    except:
        pass

date_groups = {}

for date, value in pens:
    if date not in date_groups:
        date_groups[date] = []
    date_groups[date].append(value)
averaged_pens = []
sorted_dates = sorted(date_groups.keys())
for date in sorted_dates:
    values = date_groups[date]
    count = len(values)
    total = sum(values)
    average = total / count
    averaged_pens.append([date, round(average)])

summ = sum([i[1] for i in averaged_pens])
print(f"Срендий размер пенсии в 2018: {summ/len(averaged_pens):.2f}")


dates = [item[0] for item in averaged_pens]
values = [item[1] for item in averaged_pens]


plt.figure(figsize=(12, 6))
plt.plot(dates, values)

plt.title('Средний размер пенсии по месяцам в Забайкальском крае в 2018')
plt.xlabel('Дата')
plt.ylabel('Средний размер пенсии')
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
