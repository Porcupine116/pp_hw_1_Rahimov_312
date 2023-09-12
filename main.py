from random import randint


massiv = []

for i in range(12):
    massiv.append(randint(100, 1000))

max_s = 0
min_s = 999999999
per_max = ''
per_min = ''
zima = massiv[0:4]
vesna = massiv[4:7]
leto = massiv[7:10]
osen = massiv[10:13]

max_s = max(sum(zima), sum(vesna), sum(osen), sum(leto))
for i in range(4):


sr_znch = round((max_s / 3), 2)

print(per_max)
print(sr_znch)
print(per_min)