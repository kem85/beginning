import numpy as np
np.random.seed()
npc=np.random.randint(1,4)
print("one for paper,two for scissors,three for rock")
print(npc)
x=input()
if npc==1 and x=='3':
     print("npc wins")
elif npc==1 and x=='2':
     print("player wins")
elif npc==2 and x=='1':
     print("npc wins")
elif npc==2 and x=='3':
     print("Player wins")