#!/usr/bin/env python
# coding: utf-8

# In[4]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

plt.plot([3, 1, 4, 5, 2])
plt.ylabel("Grade")
plt.savefig('test', dpi=800) #默认PNG文件
plt.show()


# In[7]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

plt.plot([0, 2, 4, 6, 8], [3, 1, 4, 5, 2])
plt.ylabel("Grade")
plt.axis([-1,10,0,6])
plt.show()


# In[16]:


import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

a = np.arange(0.0, 5.0, 0.02)

plt.subplot(211) #两行，一列， 两个区域中的第一个区域
plt.plot(a,f(a))

plt.subplot(2,1,2) #两行，一列，两个区域中的第二个区域，加不加“，”都可以
plt.plot(a, np.cos(2*np.pi*a), 'r--') #'r--'代表颜色和线段形式，同理 'g'表示绿色，--代表虚线
plt.show()


# In[24]:


import matplotlib.pyplot as plt
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')

a = np.arange(10)
plt.plot(a, a*1.5, 'go-', a, a*2.5, 'rx', a, a*3.5, '*', a, a*4.5, 'b-.')
plt.show()


# In[29]:


#pyplot的中文显示：第一种方法

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
get_ipython().run_line_magic('matplotlib', 'inline')

matplotlib.rcParams['font.family']='SimHei' #负号显示不出来不知道原因
matplotlib.rcParams['font.size']=15

a = np.arange(0.0, 5.0, 0.02)

plt.xlabel('横轴：时间')
plt.ylabel('纵轴：振幅')
plt.plot(a, np.cos(2*np.pi*a), 'r--')
plt.show()


# In[32]:


#pyplot的中文显示：第二种方法
#增加fontproperties

import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

a = np.arange(0.0, 5.0, 0.02)

plt.xlabel('横轴：时间', fontproperties='SimHei',fontsize=15)
plt.ylabel('纵轴：振幅', fontproperties='SimHei',fontsize=15)
plt.plot(a, np.cos(2*np.pi*a), 'r--')
plt.show()


# In[33]:


import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

a = np.arange(0.0, 5.0, 0.02)
plt.plot(a, np.cos(2*np.pi*a), 'r--')

plt.xlabel('横轴：时间', fontproperties='SimHei', fontsize=15, color='green')
plt.ylabel('纵轴：振幅', fontproperties='SimHei', fontsize=15)
plt.title(r'正弦波实例 $y=cos(2\pi x)$', fontproperties='SimHei', fontsize=20)
plt.text(2, 1, r'$\mu=100$', fontsize=15)

plt.axis([-1, 6, -2, 2])
plt.grid(True)
plt.show()


# In[36]:


import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

a = np.arange(0.0, 5.0, 0.02)
plt.plot(a, np.cos(2*np.pi*a), 'r--')

plt.xlabel('横轴：时间', fontproperties='SimHei', fontsize=25, color='green')
plt.ylabel('纵轴：振幅', fontproperties='SimHei', fontsize=25)
plt.title(r'正弦波实例 $y=cos(2\pi x)$', fontproperties='SimHei', fontsize=25)
plt.annotate(r'$\mu=100$', xy=(2, 1), xytext=(3, 1.5), arrowprops=dict(facecolor='black', shrink=0.1, width=2))
#加数字引用箭头，数字出现在(3, 1.5), 箭头在(2,1)

plt.axis([-1, 6, -2, 2])
plt.grid(True)
plt.show()


# In[ ]:


#3：22：00

