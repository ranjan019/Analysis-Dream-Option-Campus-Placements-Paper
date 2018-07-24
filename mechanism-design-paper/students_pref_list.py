import numpy as np 
from random import shuffle



#import company_final_ranklist from ranking_companies
#for i in company_final_ranklist:
	#company_order[i] = company_final_ranklist[i][0]

#testing
company_order=[]
for i in range(0,200):
	company_order.append(i)	
shuffle(company_order)

student_pref_list=[]
company_order_1=[]
company_order_2=[]
company_order_3=[]
company_order_4=[]
company_order_5=[]
company_order_1=company_order[0:40]
company_order_2=company_order[40:80]
company_order_3=company_order[80:120]
company_order_4=company_order[120:160]
company_order_5=company_order[160:200]



print company_order_1
student_pref_list=[]
for i in range(0,1000):
	shuffle(company_order_1)
	shuffle(company_order_2)
	shuffle(company_order_3)
	shuffle(company_order_4)
	shuffle(company_order_5)
	student_pref_list.append(company_order_1+company_order_2+company_order_3+company_order_4+company_order_5)

for i in range(0,2):
	print(i," : ", student_pref_list[i])
	print
	print



