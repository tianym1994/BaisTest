import  numpy as np
#存储学生的各科成绩并计算最大值，最小值，方差，总和等
persontype=np.dtype({'names':['name','chinese','math','english','Total'],'formats':['S32','f','f','f','f']})
people=np.array([("Zhangsan",66,65,30,0),("Lisi",95,85,98,0),("Mrwang",90,88,77,0),("GuanYu",80,90,90,0)],dtype=persontype)
name=people[:]['name']
chinese=people[:]['chinese']
math=people[:]['math']
english=people[:]['english']
people[:]['Total']=people[:]['chinese']+people[:]['english']+people[:]['math']
print(np.mean(chinese))
#1代表横轴，0代表竖轴
print(np.amin(chinese,axis=1))
print(np.amax(math,axis=0))
#std 标准差，var 方差
print(np.std(english))
print(np.var(english))
