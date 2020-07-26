#!/usr/bin/env python
# coding: utf-8

# In[30]:


#pyplot绘制复杂区域图
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
get_ipython().run_line_magic('matplotlib', 'inline')

gs = gridspec.GridSpec(3,3) #分成9等分

ax1 = plt.subplot(gs[0, :]) #第一排占三列
ax2 = plt.subplot(gs[1, :-1]) #第二排占一个，占第一第二列，但‘-1’什么意思暂时不清楚
ax3 = plt.subplot(gs[1:, -1]) #占第二第三排，占第三列
ax4 = plt.subplot(gs[2, 0]) #第三排第一个
ax5 = plt.subplot(gs[2, 1]) #第三排第二个
plt.show()


# In[16]:


#pyplot绘制扇形图
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = [15, 30, 45, 10]
explode = (0, 0.1, 0, 0)

plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=False, startangle=90)
plt.axis('equal')
plt.show()


# In[25]:


#pyplot绘制直方图
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

np.random.seed(0)
mu, sigma = 100, 20 #均值和标准差
a = np.random.normal(mu, sigma, size = 100)

plt.hist(a, 40, density = 1, histtype = 'stepfilled', facecolor = 'b', alpha = 0.75)
plt.title('Histogram')

plt.show()


# In[32]:


#pyplot绘制极坐标图
import numpy as np
import matplotlib.pyplot as ple
get_ipython().run_line_magic('matplotlib', 'inline')

N = 20 #20个数
theta = np.linspace(0.0, 2 * np.pi, N, endpoint=False)
radii = 10 * np.random.rand(N)
width = np.pi / 4 * np.random.rand(N)

ax = plt.subplot(111, projection = 'polar')
bars = ax.bar(theta, radii, width=width, bottom=0.0) #theta对应left, radii对应height, width对应width
#核心函数ax.bar

for r, bar in zip(radii, bars):
    bar.set_facecolor(plt.cm.viridis(r / 10.))
    bar.set_alpha(0.75)
    
plt.show()


# In[33]:


#pyplot绘制散点图
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

fig, ax = plt.subplots()
ax.plot(10*np.random.randn(100), 10*np.random.randn(100), 'o')
ax.set_title('Simple Scatter')

plt.show()


# In[ ]:




