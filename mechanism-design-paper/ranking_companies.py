import numpy as np

company_db={}
company_db_aggr_1=[] #only salary
company_db_aggr_2=[] #salary plus reputation (0.6,0.4)
company_db_aggr_3=[] #salary plus reputation plus difficulty of interview (0.5,0.35,0.15)

for i in range(0,200):
	#salary(<10,10-15,15-20,20-25,25-30,30-35,35-40)
	company_db[i]=[np.random.choice(np.arange(1,8),p=(0.05,0.3,0.2,0.2,0.15,0.05,0.05)),np.random.choice(np.arange(1,6),p=(0.2,0.2,0.3,0.25,0.05)),np.random.choice(np.arange(1,6),p=(0.1,0.1,0.5,0.2,0.1))]

for key, value in company_db.items():
	#printing the database
    print(key," : ",value)
    #finding aggragate by normalizing
    company_db_aggr_1.append((key,value[0]))
    company_db_aggr_2.append((key,0.6*(value[0]*5)+0.4*(value[1]*7)))
    company_db_aggr_3.append((key,0.5*(value[0]*5)+0.35*(value[1]*7)+0.15*(value[2]*7)))

#sorting the list of companies based on final aggregate to prepare ranklist
final_ranklist_1=sorted(company_db_aggr_1, key=lambda x: x[1], reverse=True)
final_ranklist_2=sorted(company_db_aggr_2, key=lambda x: x[1], reverse=True)
final_ranklist_3=sorted(company_db_aggr_3, key=lambda x: x[1], reverse=True)

company_final_ranklist=final_ranklist_3
for i in final_ranklist_3:
	print i