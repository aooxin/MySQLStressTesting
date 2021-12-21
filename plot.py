import matplotlib.pyplot as plt
import csv
import numpy
import matplotlib.ticker as ticker

fCsv2 = csv.reader(open('record.csv', 'r'))
fcsv = csv.reader(open('record_select.csv', 'r'))
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set(title='select time-time pic',
       ylabel='second', xlabel='the X 100 times')

x = []
y = []
xs = []
ys = []
i = 1
for row in fcsv:
    i = i + 1
    if i % 10:
        xs.append(row[0])
        ys.append(row[1])
# for row in fCsv2:
#     x.append(row[0])
#     y.append(row[1])

# 设置坐标轴精度
# ax.set_ylim(0, 1)
# ax.set_xlim(0, 5100)
# my_y1 = numpy.arange(0, 1, 0.1)
# my_x1 = numpy.arange(0, 5100, 500)
# plt.xticks(my_x1)
# plt.yticks(my_y1)
# print(x, y)
# ax.plot(x, y, color='red')
# 设置刻度不可见
# plt.xticks([])
# plt.yticks([])
ax.yaxis.set_major_locator(ticker.MultipleLocator())
ax.xaxis.set_major_locator(ticker.MultipleLocator(base=500))
ax.plot(xs, ys, color='blue')
plt.show()
