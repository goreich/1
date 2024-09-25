import os
import math
import matplotlib.pyplot as plt

x=[110,120,130,140,150,160,170,180,190,200,210,220,230,240,250,260,270,280,290,300,310,320,330,340,350,360,370,380,390,400]#伤害
y=[20,15,10,5]#弹匣

for u in x:#伤害
    for v in y:#弹匣
        if v==20:
            z1=u*0.25+v*2#拟合函数
            print(z1)
            plt.plot(u,z1,color='blue',linestyle='--',marker='*')# 离散点linestyle不生效
        elif v==15:
            z2=u*0.25+v*2#拟合函数
            plt.plot(u,z2,color='yellow',linestyle='--',marker='*')
        elif v==10:
            z3=u*0.25+v*2#拟合函数
            plt.plot(u,z3,color='green',linestyle='--',marker='*')
        elif v==5:
            z4=u*0.25+v*2#拟合函数
            plt.plot(u,z4,color='red',linestyle='--',marker='*')


plt.title('AWP analysis')   #添加图标题
plt.xlabel('damage')             #添加x轴名
plt.ylabel('effort')           #添加y轴名
plt.tight_layout()  #tight_layout() 函数来自动调整子图间距,从而避免部分内容（标题等）被遮住
plt.show()