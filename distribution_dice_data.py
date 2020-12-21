import random
import plotly.express as px
import plotly.figure_factory  as pff
randomList=[]
countList=[]
for i in range(0,100):
    random1 = random.randint(1,6)
    random2 = random.randint(1,6)
    random3 = random1+random2
    randomList.append(random3)
    countList.append(i)
print(randomList)
dis_plot1 = pff.create_distplot([randomList],["Dice Data Distribution"])
dis_plot1.show()