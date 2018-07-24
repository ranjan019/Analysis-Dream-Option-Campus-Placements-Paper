import numpy as np
students_db={}
students_db_aggr=[]
for i in range(0,1000):
	#cgpa(5,10),publications(0,2),algorithmic(1,5),dev(1,5),presentation(1,5),x-factor(0,2)
	students_db[i]=[np.random.choice(np.arange(5,11),p=[0.05,0.1,0.15,0.4,0.2,0.1]), np.random.choice(np.arange(0,3),p=[0.5,0.4,0.1]),np.random.choice(np.arange(1,6),p=[0.1,0.2,0.4,0.2,0.1]),np.random.choice(np.arange(1,6),p=[0.1,0.2,0.4,0.2,0.1]),np.random.choice(np.arange(1,6),p=[0.1,0.2,0.4,0.2,0.1]),np.random.choice(np.arange(0,2),p=[0.8,0.2])]

for key, value in students_db.items():
	#printing the database
    print(key," : ",value)
    #finding aggragate by normalizing 
    students_db_aggr.append((key,(0.15*value[0]+0.2*(value[1]*5)+0.35*(value[2]*2)+0.1*(value[3]*2)+0.1*(value[4]*2)+0.1*(value[5]*5))))
    #printing the aggregate
    print(key," : ",students_db_aggr[key][1])
    print
    print

#sorting the list of students based on final aggregate to prepare ranklist
student_final_ranklist=sorted(students_db_aggr, key=lambda x: x[1], reverse=True)
for i in student_final_ranklist:
	print i

for i in range(0,50):
	happiness_point.append(student_final_ranklist[i][0],company_final_ranklist[9][0])

for i in range(1,16):
	for j in range(0,50):
		happiness_point.append(student_final_ranklist[50*i+j][0],company_final_ranklist[9+i*10][0])

for i in range(850,1000):
	happiness_point.append(student_final_ranklist[i][0],company_final_ranklist[199][0])




