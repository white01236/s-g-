import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter

size=100

x=np.linspace(1,size,size)
data=np.random.randint(1,size,size)
plt.plot(x, data,labal='original')
#plt.show()

#此处为用scipy库的savgol_filter验证
y=savgol_filter(data,5,3,mode='nearest')

plt.plot(x,y,'b',label='savgol')
plt.show()
#下面自己编写代码验证
arr=[]
window_size=5
order=3
step=int((window_size-1)/2)

for i in range(window_size):
    a=[]
    for j in range(order):
        y_val=np.power(-step+i,j)
        a.append(y_val)
    arr.append(a)
#print(arr)
#矩阵运算
arr=np.mat(arr)
arr=arr*(arr.T*arr).I*arr.T
a=np.array(arr[step])
a=a.reshape(window_size)
#print(a)
print(data)
data=np.insert(data,0,[data[0] for i in range(step)])
print(data)

data=np.append(data,[data[-1] for i in range(step)])

list=[]
for i in range(step,data.shape[0]-step):
    arr=[]
    for j in range(-step,step+1):
        arr.append(data[i+j])

    b=np.sum(np.array(arr)*a)
    list.append(b)
#print(list)
plt.plot(x,np.array(list),'r',label='result')

plt.legend()
plt.show()
