import numpy as np

import scipy.stats as stats
import pylab as pl
import sys
import random
from random import shuffle
#import numpy as np
import matplotlib
import matplotlib.pyplot as plt
fig_size = plt.rcParams["figure.figsize"]
fig_size[0] = 8
fig_size[1] = 5
plt.rcParams["figure.figsize"] = fig_size

#import plotly.plotly as py
from matplotlib.ticker import NullFormatter  # useful for `logit` scale
from matplotlib.ticker import FuncFormatter


def make_company_ranklist(type_of_rl):
	company_db={}
	company_db_aggr_1=[] #only salary
	company_db_aggr_2=[] #salary plus reputation (0.6,0.4)
	company_db_aggr_3=[] #salary plus reputation plus difficulty of interview (0.5,0.35,0.15)

	for i in range(0,400):
		#salary(<10,10-15,15-20,20-25,25-30,30-35,35-40)
		company_db[i]=[np.random.choice(np.arange(1,8),p=(0.05,0.3,0.2,0.2,0.15,0.05,0.05)),np.random.choice(np.arange(1,6),p=(0.2,0.2,0.3,0.25,0.05)),np.random.choice(np.arange(1,6),p=(0.1,0.1,0.5,0.2,0.1))]

	for key, value in company_db.items():
		#printing the database
	    #print(key," : ",value)
	    #finding aggragate by normalizing
	    company_db_aggr_1.append((key,value[0]))
	    company_db_aggr_2.append((key,0.6*(value[0]*5)+0.4*(value[1]*7)))
	    company_db_aggr_3.append((key,0.5*(value[0]*5)+0.35*(value[1]*7)+0.15*(value[2]*7)))

	#sorting the list of companies based on final aggregate to prepare ranklist
	final_ranklist_1=sorted(company_db_aggr_1, key=lambda x: x[1], reverse=True)
	final_ranklist_2=sorted(company_db_aggr_2, key=lambda x: x[1], reverse=True)
	final_ranklist_3=sorted(company_db_aggr_3, key=lambda x: x[1], reverse=True)

	if type_of_rl==1:
		company_final_ranklist=final_ranklist_1
	elif type_of_rl==2:
		company_final_ranklist=final_ranklist_2
	else:
		company_final_ranklist=final_ranklist_3


	# for i in company_final_ranklist:
	# 	print i

	return company_final_ranklist


def make_student_ranklist():
	students_db={}
	students_db_aggr=[]
	for i in range(0,1000):
		#cgpa(5,10),publications(0,2),algorithmic(1,5),dev(1,5),presentation(1,5),x-factor(0,2)
		students_db[i]=[np.random.choice(np.arange(5,11),p=[0.05,0.1,0.15,0.4,0.2,0.1]), np.random.choice(np.arange(0,3),p=[0.5,0.4,0.1]),np.random.choice(np.arange(1,6),p=[0.1,0.2,0.4,0.2,0.1]),np.random.choice(np.arange(1,6),p=[0.1,0.2,0.4,0.2,0.1]),np.random.choice(np.arange(1,6),p=[0.1,0.2,0.4,0.2,0.1]),np.random.choice(np.arange(0,2),p=[0.8,0.2])]

	for key, value in students_db.items():
		#printing the database
	    #print(key," : ",value)
	    #finding aggragate by normalizing 
	    students_db_aggr.append((key,(0.15*value[0]+0.2*(value[1]*5)+0.35*(value[2]*2)+0.1*(value[3]*2)+0.1*(value[4]*2)+0.1*(value[5]*5))))
	    #printing the aggregate
	    # print(key," : ",students_db_aggr[key][1])
	    # print
	    # print

	#sorting the list of students based on final aggregate to prepare ranklist
	student_final_ranklist=sorted(students_db_aggr, key=lambda x: x[1], reverse=True)
	# for i in student_final_ranklist:
	# 	print i

	return student_final_ranklist



def def_happiness_point(student_final_ranklist,company_final_ranklist):
	happiness_point=[]
	#for i in range(0,25):
		#happiness_point.append((student_final_ranklist[i][0],company_final_ranklist[9][0]))

	for i in range(0,50):
		happiness_point.append((student_final_ranklist[i][0],company_final_ranklist[19][0]))



	for i in range(1,17):
		for j in range(0,50):
			happiness_point.append((student_final_ranklist[50*i+j][0],company_final_ranklist[19+i*20][0]))

	for i in range(850,1000):
		happiness_point.append((student_final_ranklist[i][0],company_final_ranklist[399][0]))

	
	# for i in happiness_point:
	# 	print ("happiness-unsorted:::::",i)


	happiness_point_list_sorted=sorted(happiness_point, key=lambda x: x[0])

	# print "happiness point list"
	# print "----------------------"
	# for i in happiness_point_list_sorted:
	# 	print i
	return happiness_point_list_sorted

def make_expected_stud_pref_list(company_final_ranklist):
	#import company_final_ranklist from ranking_companies
	company_order=[]
	for i in company_final_ranklist:
		company_order.append(i[0])

	#testing
	#company_order=[]
	#for i in range(0,200):
	#	company_order.append(i)	
	#shuffle(company_order)

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
	company_order_6=company_order[200:240]
	company_order_7=company_order[240:280]
	company_order_8=company_order[280:320]
	company_order_9=company_order[320:360]
	company_order_10=company_order[360:400]




	#print company_order_1
	student_pref_list=[]
	for i in range(0,1000):
		# company_order_i=list(company_order)
		shuffle(company_order_1)
		shuffle(company_order_2)
		shuffle(company_order_3)
		shuffle(company_order_4)
		shuffle(company_order_5)
		shuffle(company_order_6)
		shuffle(company_order_7)
		shuffle(company_order_8)
		shuffle(company_order_9)
		shuffle(company_order_10)
		# shuffle(company_order_i)
		student_pref_list.append(company_order_1+company_order_2+company_order_3+company_order_4+company_order_5+company_order_6+company_order_7+company_order_8+company_order_9+company_order_10)
		# student_pref_list.append(company_order_i)
	# for i in range(0,10):
	# 	print(i," :::this is the normal (non SPC) preference list of",i, "::: ", student_pref_list[i])
	# 	print
	# 	print
	return student_pref_list

def make_stud_pref_list(company_final_ranklist):
	#import company_final_ranklist from ranking_companies
	company_order=[]
	for i in company_final_ranklist:
		company_order.append(i[0])

	#testing
	#company_order=[]
	#for i in range(0,200):
	#	company_order.append(i)	
	#shuffle(company_order)

	# company_order_1=[]
	# company_order_2=[]
	# company_order_3=[]
	# company_order_4=[]
	# company_order_5=[]
	# company_order_1=company_order[0:40]
	# company_order_2=company_order[40:80]
	# company_order_3=company_order[80:120]
	# company_order_4=company_order[120:160]
	# company_order_5=company_order[160:200]



	#print company_order_1
	student_pref_list=[]
	for i in range(0,1000):
		company_order_i=list(company_order)
		# shuffle(company_order_1)
		# shuffle(company_order_2)
		# shuffle(company_order_3)
		# shuffle(company_order_4)
		# shuffle(company_order_5)
		shuffle(company_order_i)
		#student_pref_list.append(company_order_1+company_order_2+company_order_3+company_order_4+company_order_5)
		student_pref_list.append(company_order_i)
	# for i in range(0,10):
	# 	print(i," :::this is the normal (non SPC) preference list of",i, "::: ", student_pref_list[i])
	# 	print
	# 	print
	return student_pref_list

def make_seq_stud_pref_list(company_final_ranklist, student_final_ranklist):

	temp_stud_pref_list=[]
	company_order=[]
	for i in company_final_ranklist:
		company_order.append(i[0])
	for i in range(0,len(student_final_ranklist)):
		
		seq_part=[]
		non_seq_part=[]
		seq_part=company_order[int(i/(2.5)):len(company_order)]
		non_seq_part=company_order[0:int(i/(2.5))]

		for j in non_seq_part:
			seq_part.insert(random.randint(0, len(seq_part)), j)

		temp_stud_pref_list.append((student_final_ranklist[i][0],seq_part))

	# print "printing sequential preference ordering"
	# print "---------------------------------------"
	# print "---------------------------------------"

	# for i in temp_stud_pref_list:
	# 	print i

		
	seq_stud_pref_list=[]
	temp2=[]	
	temp2=sorted(temp_stud_pref_list, key=lambda x: x[0])

	for i in temp2:
		#print i[0]
		seq_stud_pref_list.append(i[1])

	return seq_stud_pref_list







def match_normal(student_final_ranklist,company_final_ranklist):
	student_left_list=list(student_final_ranklist)
	student_selected_list=[]
	for i in company_final_ranklist:
		#when company i comes
		shortlist=[]
		shortlist=student_left_list[0:10]
		shuffle(shortlist)
		selected=[]
		selected=shortlist[0:5]
		# for z in selected:
		# 	print("normalselected",":::student:::",z,":::company:::",i)
		for j in selected:
			student_left_list.remove(j)
			#print("removed",":::student:::",j)
		new_selected=[]	
		for k in range(0,len(selected)):
			
			l=list(selected[k])
			p=list(i)
			cct=[]
			cct=l+p
			tuple(cct)
			new_selected.append(cct) #appending company information to selected students

		for m in new_selected:
			student_selected_list.append(m)
			#print("new_selected:::",m)

	return student_selected_list

def match_dream(student_final_ranklist,company_final_ranklist,stud_pref_list):
	student_left_list=list(student_final_ranklist)
	dream_chances=[]
	for p in range(0,1000):
		#t=(p,3)
		dream_chances.append(3)
	people_dreamt=[] #all people who got their dream option
	dream=0
	oldies_placement=[] #old placements of people who got dream options
	student_selected_list=[]
	for i in company_final_ranklist:
		#when company i comes
		addd=[]
		full_list_for_this_company=[]
		full_list_for_this_company=list(student_left_list)
		#total_dream_for_this_company=5
		#in the below written function we are finding the people who want to use dream option
		for y in student_selected_list:
			company_alloted=y[2]
			current_company=i[0]
			student_index=y[0]
			# print student_index
			# print("stud_pref_list[student_index].index(company_alloted)",stud_pref_list[student_index].index(company_alloted))
			# print("stud_pref_list[student_index].index(current_company)",stud_pref_list[student_index].index(current_company))
			# print student_index
			dream_option_already_used=0
			for p in oldies_placement:
				if p[0]==y[0]:
					dream_option_already_used=1
			if ((stud_pref_list[student_index].index(company_alloted)> stud_pref_list[student_index].index(current_company)) and dream_chances[student_index]>0 and dream_option_already_used==0  ):
				extract_student=[]
				extract_student.append(y[0])
				extract_student.append(y[1])
				dream_chances[y[0]]-=1
				addd.append(tuple(extract_student))

				
		#if addd not in people_dreamt:
		if len(addd) > 5:
			shuffle(addd)				
			full_list_for_this_company=addd[0:5]+full_list_for_this_company
			#print "adding dream guys (more than 5 options)"
		else:
			full_list_for_this_company=addd+full_list_for_this_company
			#print "adding dream guys (<=5 options)"

		
		#total_dream_for_this_company-=1
		#dream+=1
		#print("dreeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeam:::",dream)

		shortlist=[]
		shortlist=full_list_for_this_company[0:10]
		shuffle(shortlist)
		selected=[]
		selected=shortlist[0:5]
		people_dreamt_this_company=[]
		for z in selected:
			#print("dreamselected",":::student:::",z,":::company:::",i)
			if z in student_left_list:
				student_left_list.remove(z)
				#print("removed",":::student:::",z)
			else:
				people_dreamt_this_company.append(z)
				#print(z,":::dreamt and got selected:::appended to people_dreamt:::")

		for m in people_dreamt_this_company:
			for n in student_selected_list:
				if m[0] == n[0]:
					oldies_placement.append(n)
					student_selected_list.remove(n)




		new_selected=[]	
		for k in selected:
			
			l=list(k)
			p=list(i)
			cct=[]
			cct=l+p
			tuple(cct)
			new_selected.append(cct) #appending company information to selected students
			if k in people_dreamt_this_company:
				people_dreamt.append(cct)

		for m in new_selected:
			student_selected_list.append(m)
			#print("new_selected:::",m)
	total_dream_count=0

	# for p in oldies_placement:
	# 	print ("left placements:::",p)
	# for p in people_dreamt:
	# 	print ("new placements:::",p)



	for i in range(0,1000):
		#print(i,":::::",dream_chances[i])
		total_dream_count=total_dream_count+ 3- dream_chances[i]

	# print total_dream_count
	# print ("total --- dream --- options --- utilised",len(people_dreamt))
	# print ("total---placed-----", len(student_selected_list))
	return (oldies_placement, people_dreamt, student_selected_list)

def cal_rank_efficiency(student_selected_list,stud_pref_list):
	total_students_placed=len(student_selected_list)
	sum_ranks=0
	for i in student_selected_list:
		student_index=i[0]
		company_alloted=i[2]
		sum_ranks+=stud_pref_list[student_index].index(company_alloted)

	return float(float(sum_ranks)/float(len(student_selected_list)))

def find_stability(student_selected_list,stud_pref_list):
	blocking_pairs=0
	company_order=[]
	for i in student_selected_list:
		company_order.append(i[2])
	for i in range(0,len(student_selected_list)):
		student_index=student_selected_list[i][0]
		company_alloted=student_selected_list[i][2]
		for j in range(i+1,len(company_order)):
			if(stud_pref_list[student_index].index(company_alloted)>stud_pref_list[student_index].index(company_order[j])):
				blocking_pairs+=1
				break

	return float(float(blocking_pairs*100)/float(len(student_selected_list)))

def calc_happiness_index(student_selected_list,happiness_point_list,stud_pref_list):
	total_students_placed=len(student_selected_list)
	#print ("in cal_happiness_index",":::total students placed:::",total_students_placed)
	above_hp=0
	#count=0
	happiness_point_list_sorted=list(happiness_point_list)
	for i in student_selected_list:
		student_index=i[0]
		company_alloted=i[2]
		#count+=1
		happiness_point=happiness_point_list_sorted[student_index][1]
		if(stud_pref_list[student_index].index(happiness_point)>=stud_pref_list[student_index].index(company_alloted) ):
			above_hp+=1
			
	#print ("above hp::::",above_hp)
	return float(float(above_hp)/1000)

def find_companies_lost(oldies_placement):
	people_leftoffer_list=list(oldies_placement)
	company_recruits=[]
	for i in range(0,400):
		company_recruits.append(5)

	for i in people_leftoffer_list:
		company_recruits[i[2]]-=1
	
	companies_disappointed=0	
	for i in company_recruits:
		if(i<3):
			companies_disappointed+=1

	return companies_disappointed

def fairness(student_selected_list, student_final_ranklist):
	placed_ranklist=[]

	for i in student_selected_list:
		placed_ranklist.append(i[0])

	diff_places=[]

	for i in range(0,len(placed_ranklist)):
		for j in range(0,len(student_final_ranklist)):
			if(student_final_ranklist[j][0]==placed_ranklist[i]):
				diff_places.append((placed_ranklist[i],i-j))

	highest_gain=0
	highest_loss=0
	avg_gain=0			
	for i in diff_places:
		if(i[1]>=highest_gain):
			highest_gain=i[1]
		if(i[1]<=highest_loss):
			highest_loss=i[1]
		avg_gain+=i[1]

	avg_gain=float(float(avg_gain)/float(len(diff_places)))

	return (avg_gain,highest_gain,highest_loss)






def main():

	# r=[]
	# b=[]
	# h=[]
	# rd=[]
	# bd=[]
	# hd=[]
# 	company_distribution=[]
# 	student_distribution=[]
	cd=[]
	sd=[]
	company_f_ranklist= make_company_ranklist(3)
	student_f_ranklist= make_student_ranklist()


	for i in company_f_ranklist:
		cd.append(i[1])
	for i in student_f_ranklist:
		sd.append(i[1])

	cd.sort()
	sd.sort()
	fit = stats.norm.pdf(cd, np.mean(cd), np.std(cd))
	pl.plot(cd,fit,'-o', color='b')

	pl.hist(cd,normed=True, color='cyan') 
	pl.xlabel('Company Aggregate Quality Value')
	pl.ylabel('Probability of Occurence')
	pl.title('Company Distribution')     #use this to draw histogram of your data

	pl.show()



	fit = stats.norm.pdf(sd, np.mean(sd), np.std(sd))
	pl.plot(sd,fit,'-o', color='b')

	pl.hist(sd,normed=True, color='cyan')
	plt.xlabel('Student Aggregate Quality Value')
	plt.ylabel('Probability of Occurence')
	plt.title('Student Distribution')
	      #use this to draw histogram of your data

	pl.show()   

# 	company_distribution = cd
# 	student_distribution = sd
# 	n, bins, patches = plt.hist(company_distribution, facecolor='lightgrey', alpha=0.5)


# 	plt.xlabel('Company Aggregate Quality Value')
# 	plt.ylabel('Frequency')
# 	plt.title('Company Distribution')
# #	plt.axis([40, 160, 0, 0.03])
# 	plt.grid(True)
# 	plt.show()


# 	n, bins, patches = plt.hist(student_distribution, facecolor='lightgrey', alpha=0.5)


# 	plt.xlabel('Student Aggregate Quality Value')
# 	plt.ylabel('Frequency')
# 	plt.title('Student Distribution')
# #	plt.axis([40, 160, 0, 0.03])
# 	plt.grid(True)
# 	plt.show()
	
	# companies_disappointed_normal_expected_sum=0
	# companies_disappointed_normal_sum=0
	# companies_disappointed_normal_spc_sum=0
	# companies_disappointed_dream_expected_sum=0
	# companies_disappointed_dream_sum=0
	# companies_disappointed_dream_spc_sum=0

	# rank_eff_normal_expected_sum=0
	# rank_eff_normal_sum=0
	# rank_eff_normal_spc_sum=0
	# rank_eff_dream_expected_sum=0
	# rank_eff_dream_sum=0
	# rank_eff_dream_spc_sum=0

	
	# blocking_pairs_normal_expected_sum=0
	# blocking_pairs_normal_sum=0
	# blocking_pairs_normal_spc_sum=0
	# blocking_pairs_dream_expected_sum=0
	# blocking_pairs_dream_sum=0
	# blocking_pairs_dream_spc_sum=0

	# happiness_index_normal_expected_sum=0
	# happiness_index_normal_sum=0
	# happiness_index_normal_spc_sum=0
	# happiness_index_dream_expected_sum=0
	# happiness_index_dream_sum=0
	# happiness_index_dream_spc_sum=0

	
	# total_st_placed_normal_expected_sum=0
	# total_st_placed_normal_sum=0
	# total_st_placed_normal_spc_sum=0
	# total_st_placed_dream_expected_sum=0
	# total_st_placed_dream_sum=0
	# total_st_placed_dream_spc_sum=0

	# oldies_placement_expected_sum=0
	# oldies_placement_sum=0
	# oldies_placement_spc_sum=0

	# avg_gain_normal_expected_sum=0
	# avg_gain_normal_sum=0
	# avg_gain_normal_spc_sum=0
	# avg_gain_dream_expected_sum=0
	# avg_gain_dream_sum=0
	# avg_gain_dream_spc_sum=0

	# highest_gain_normal_expected_sum=0
	# highest_gain_normal_sum=0
	# highest_gain_normal_spc_sum=0
	# highest_gain_dream_expected_sum=0
	# highest_gain_dream_sum=0
	# highest_gain_dream_spc_sum=0

	# highest_loss_normal_expected_sum=0
	# highest_loss_normal_sum=0
	# highest_loss_normal_spc_sum=0
	# highest_loss_dream_expected_sum=0
	# highest_loss_dream_sum=0
	# highest_loss_dream_spc_sum=0


	# for i in range (0,1000):

	# 	print ("iteration ::::: ",i)

	# 	company_f_ranklist= make_company_ranklist(3)
	# 	student_f_ranklist= make_student_ranklist()
	# 	happiness_point_list= def_happiness_point(student_f_ranklist,company_f_ranklist)
	# 	stud_expected_pref_list=make_expected_stud_pref_list(company_f_ranklist)
	# 	stud_pref_list= make_stud_pref_list(company_f_ranklist)
	# 	seq_stud_pref_list=make_seq_stud_pref_list(company_f_ranklist,student_f_ranklist)


		
		
	# 	f_normal_match= match_normal(student_f_ranklist, company_f_ranklist)
	# 	f_normal_match_spc=list(f_normal_match)
	# 	f_normal_match_expected=list(f_normal_match)
	# 	(oldies_placement_expected, people_dreamt_expected, f_dream_match_expected)=match_dream(student_f_ranklist,company_f_ranklist,stud_expected_pref_list)
	# 	(oldies_placement, people_dreamt, f_dream_match)=match_dream(student_f_ranklist,company_f_ranklist,stud_pref_list)
	# 	(oldies_placement_spc, people_dreamt_spc, f_dream_match_spc)=match_dream(student_f_ranklist,company_f_ranklist,seq_stud_pref_list)

	# 	(avg_gain_normal_expected,highest_gain_normal_expected,highest_loss_normal_expected) =  fairness(f_normal_match_expected, student_f_ranklist)
	# 	(avg_gain_normal,highest_gain_normal,highest_loss_normal) =  fairness(f_normal_match, student_f_ranklist)
	# 	(avg_gain_normal_spc,highest_gain_normal_spc,highest_loss_normal_spc) =  fairness(f_normal_match_spc, student_f_ranklist)
	# 	(avg_gain_dream_expected,highest_gain_dream_expected,highest_loss_dream_expected) =  fairness(f_dream_match_expected, student_f_ranklist)
	# 	(avg_gain_dream,highest_gain_dream,highest_loss_dream) =  fairness(f_dream_match, student_f_ranklist)
	# 	(avg_gain_dream_spc,highest_gain_dream_spc,highest_loss_dream_spc) =  fairness(f_dream_match_spc, student_f_ranklist)

	# 	companies_disappointed_normal_expected=0
	# 	companies_disappointed_normal=0
	# 	companies_disappointed_normal_spc=0
	# 	companies_disappointed_dream_expected = find_companies_lost(oldies_placement_expected)
	# 	companies_disappointed_dream = find_companies_lost(oldies_placement)
	# 	companies_disappointed_dream_spc = find_companies_lost(oldies_placement_spc)


	# 	rank_eff_normal_expected=cal_rank_efficiency(f_normal_match_expected,stud_expected_pref_list)
	# 	rank_eff_normal=cal_rank_efficiency(f_normal_match,stud_pref_list)
	# 	rank_eff_normal_spc=cal_rank_efficiency(f_normal_match_spc,seq_stud_pref_list)
	# 	rank_eff_dream_expected=cal_rank_efficiency(f_dream_match_expected,stud_expected_pref_list)
	# 	rank_eff_dream=cal_rank_efficiency(f_dream_match,stud_pref_list)
	# 	rank_eff_dream_spc=cal_rank_efficiency(f_dream_match_spc,seq_stud_pref_list)

	# 	# print ("rank_eff_normal::",rank_eff_normal)
	# 	# print
	# 	# print ("rank_eff_dream::",rank_eff_dream)

		

	# 	blocking_pairs_normal_expected=find_stability(f_normal_match_expected,stud_expected_pref_list)
	# 	blocking_pairs_normal=find_stability(f_normal_match,stud_pref_list)
	# 	blocking_pairs_normal_spc=find_stability(f_normal_match_spc,seq_stud_pref_list)
	# 	blocking_pairs_dream_expected=find_stability(f_dream_match_expected,stud_expected_pref_list)
	# 	blocking_pairs_dream=find_stability(f_dream_match,stud_pref_list)
	# 	blocking_pairs_dream_spc=find_stability(f_dream_match_spc,seq_stud_pref_list)


	# 	happiness_index_normal_expected=calc_happiness_index(f_normal_match_expected,happiness_point_list,stud_expected_pref_list)
	# 	happiness_index_normal=calc_happiness_index(f_normal_match,happiness_point_list,stud_pref_list)
	# 	happiness_index_normal_spc=calc_happiness_index(f_normal_match_spc,happiness_point_list,seq_stud_pref_list)
	# 	happiness_index_dream_expected=calc_happiness_index(f_dream_match_expected,happiness_point_list,stud_expected_pref_list)
	# 	happiness_index_dream=calc_happiness_index(f_dream_match,happiness_point_list,stud_pref_list)
	# 	happiness_index_dream_spc=calc_happiness_index(f_dream_match_spc,happiness_point_list,seq_stud_pref_list)

	# 	total_st_placed_normal_expected=len(f_normal_match_expected)
	# 	total_st_placed_normal=len(f_normal_match)
	# 	total_st_placed_normal_spc=len(f_normal_match_spc)
	# 	total_st_placed_dream_expected=len(f_dream_match_expected)
	# 	total_st_placed_dream=len(f_dream_match)
	# 	total_st_placed_dream_spc=len(f_dream_match_spc)


	# 	#
	# 	#
	# 	#	
	# 	#summation of all simulations
	# 	companies_disappointed_normal_expected_sum+=companies_disappointed_normal_expected
	# 	companies_disappointed_normal_sum+=companies_disappointed_normal
	# 	companies_disappointed_normal_spc_sum+=companies_disappointed_normal_spc
	# 	companies_disappointed_dream_expected_sum+=companies_disappointed_dream_expected
	# 	companies_disappointed_dream_sum+=companies_disappointed_dream
	# 	companies_disappointed_dream_spc_sum+=companies_disappointed_dream_spc

	# 	rank_eff_normal_expected_sum+=rank_eff_normal_expected
	# 	rank_eff_normal_sum+=rank_eff_normal
	# 	rank_eff_normal_spc_sum+=rank_eff_normal_spc
	# 	rank_eff_dream_expected_sum+=rank_eff_dream_expected
	# 	rank_eff_dream_sum+=rank_eff_dream
	# 	rank_eff_dream_spc_sum+=rank_eff_dream_spc

	# 	blocking_pairs_normal_expected_sum+=blocking_pairs_normal_expected
	# 	blocking_pairs_normal_sum+=blocking_pairs_normal
	# 	blocking_pairs_normal_spc_sum+=blocking_pairs_normal_spc
	# 	blocking_pairs_dream_expected_sum+=blocking_pairs_dream_expected
	# 	blocking_pairs_dream_sum+=blocking_pairs_dream
	# 	blocking_pairs_dream_spc_sum+=blocking_pairs_dream_spc

	# 	happiness_index_normal_expected_sum+=happiness_index_normal_expected
	# 	happiness_index_normal_sum+=happiness_index_normal
	# 	happiness_index_normal_spc_sum+=happiness_index_normal_spc
	# 	happiness_index_dream_expected_sum+=happiness_index_dream_expected
	# 	happiness_index_dream_sum+=happiness_index_dream
	# 	happiness_index_dream_spc_sum+=happiness_index_dream_spc

	# 	total_st_placed_normal_expected_sum+=total_st_placed_normal_expected
	# 	total_st_placed_normal_sum+=total_st_placed_normal
	# 	total_st_placed_normal_spc_sum+=total_st_placed_normal_spc
	# 	total_st_placed_dream_expected_sum+=total_st_placed_dream_expected
	# 	total_st_placed_dream_sum+=total_st_placed_dream
	# 	total_st_placed_dream_spc_sum+=total_st_placed_dream_spc

	# 	oldies_placement_expected_sum+=len(oldies_placement_expected)
	# 	oldies_placement_sum+=len(oldies_placement)
	# 	oldies_placement_spc_sum+=len(oldies_placement_spc)

	# 	avg_gain_normal_expected_sum+=avg_gain_normal_expected
	# 	avg_gain_normal_sum+=avg_gain_normal
	# 	avg_gain_normal_spc_sum+=avg_gain_normal_spc
	# 	avg_gain_dream_expected_sum+=avg_gain_dream_expected
	# 	avg_gain_dream_sum+=avg_gain_dream
	# 	avg_gain_dream_spc_sum+=avg_gain_dream_spc

	# 	highest_gain_normal_expected_sum+=highest_gain_normal_expected
	# 	highest_gain_normal_sum+=highest_gain_normal
	# 	highest_gain_normal_spc_sum+=highest_gain_normal_spc
	# 	highest_gain_dream_expected_sum+=highest_gain_dream_expected
	# 	highest_gain_dream_sum+=highest_gain_dream
	# 	highest_gain_dream_spc_sum+=highest_gain_dream_spc

		
	# 	highest_loss_normal_expected_sum+=highest_loss_normal_expected
	# 	highest_loss_normal_sum+=highest_loss_normal
	# 	highest_loss_normal_spc_sum+=highest_loss_normal_spc
	# 	highest_loss_dream_expected_sum+=highest_loss_dream_expected
	# 	highest_loss_dream_sum+=highest_loss_dream
	# 	highest_loss_dream_spc_sum+=highest_loss_dream_spc




	# #Graph comparison rank efficiency

	# N = 1
	# ind = np.arange(N)  # the x locations for the groups
	# width = 0.04      # the width of the bars

	# fig, ax = plt.subplots()

	# rects1 = ax.bar(1, rank_eff_normal_expected_sum, align='center', color='white',edgecolor='black', hatch="o")
	# rects2 = ax.bar(2, rank_eff_dream_expected_sum, align='center', color='white',edgecolor='black', hatch="|")
	# rects3 = ax.bar(4, rank_eff_normal_sum, align='center', color='white',edgecolor='black', hatch=".")
	# rects4 = ax.bar(5, rank_eff_dream_sum, align='center', color='white', edgecolor='black', hatch="*")
	# rects5 = ax.bar(7, rank_eff_normal_spc_sum, align='center', color='white',edgecolor='black', hatch="X")
	# rects6 = ax.bar(8, rank_eff_dream_spc_sum, align='center', color='white',edgecolor='black', hatch="+")
	# # add some text for labels, title and axes ticks
	# ax.set_ylim(top=250)
	# ax.set_ylabel('Rank Efficiency')
	# ax.set_title('Rank Efficiency Comparison')
	
	# ax.set_xticks([1,2,4,5,7,8])
	# ax.set_xticklabels(['NE','DE','NR','DR','NSPC','DSPC'])
	# #ax.set_xticklabels((''))
	# ax.yaxis.grid(True)

	# #ax.legend((rects1[0], rects2[0], rects3[0], rects4[0]), ('(a)',  '(b)', '(c)', '(d)'))

	# def autolabel(rects):
	#     """
	#     Attach a text label above each bar displaying its height
	#     """
	#     for rect in rects:
	#         height = rect.get_height()
	#         ax.text(rect.get_x() + rect.get_width()/2., 1.03*height,
	#                 '%d' % int(height),
	#                 ha='center', va='bottom')

	# autolabel(rects1)
	# autolabel(rects2)
	# autolabel(rects3)
	# autolabel(rects4)
	# autolabel(rects5)
	# autolabel(rects6)
	# plt.tight_layout()
	# plt.show()

	# #Fairness
	# #----------
	# # N = 6
	# # avggain=(avg_gain_normal_expected_sum, avg_gain_dream_expected_sum, avg_gain_normal_sum, avg_gain_dream_sum, avg_gain_normal_spc_sum, avg_gain_dream_spc_sum)
	# # highestgain=(highest_gain_normal_expected_sum, highest_gain_dream_expected_sum, highest_gain_normal_sum, highest_gain_dream_sum, highest_gain_normal_spc_sum, highest_gain_dream_spc_sum)
	# # highestloss=(-highest_loss_normal_expected_sum, -highest_loss_dream_expected_sum, -highest_loss_normal_sum, -highest_loss_dream_sum, -highest_loss_normal_spc_sum, -highest_loss_dream_spc_sum)
	# # ind = np.arange(N)  # the x locations for the groups
	# # width = 0.35      # the width of the bars

	# # fig, ax = plt.subplots()
	# # rects1 = ax.bar(1, avggain, align='center', color='white',edgecolor='black', hatch="o")
	# # rects2 = ax.bar(2, highestgain, align='center', color='white',edgecolor='black', hatch="+")
	# # rects3 = ax.bar(3, highestloss, align='center', color='white',edgecolor='black', hatch="*")
	# # #rects4 = ax.bar(ind + 4.5*width, rank_eff_dream_spc, width, color='tan')

	# # #ax.set_ylim(top=1000)
	# # # add some text for labels, title and axes ticks
	# # ax.set_ylabel('Score')
	# # ax.set_title('Fairness Comparison')
	# # # ax.set_xticks(ind + width / 2)
	# # # ax.set_xticklabels((''))
	# # ax.set_xticks([1,2,3])
	# # # ax.legend((rects1[0], rects2[0], rects3[0], rects4[0]), ('Avg Gain', 'Highest Gain in Rank', 'Greatest Loss in Rank'))
	# # ax.yaxis.grid(True)

	# # def autolabel(rects):
	# #     """
	# #     Attach a text label above each bar displaying its height
	# #     """
	# #     for rect in rects:
	# #         height = rect.get_height()
	# #         ax.text(rect.get_x() + rect.get_width()/2., 1.03*height,
	# #                 '%d' % int(height),
	# #                 ha='center', va='bottom')

	# # autolabel(rects1)
	# # autolabel(rects2)
	# # autolabel(rects3)
	# # #autolabel(rects4)
	# # plt.tight_layout()
	# # plt.show()
	# #-------------


	# #Happiness Index

	# N = 1
	# ind = np.arange(N)  # the x locations for the groups
	# width = 0.2      # the width of the bars

	# fig, ax = plt.subplots()
	# rects1 = ax.bar(1, happiness_index_normal_expected_sum*100, align='center', color='white',edgecolor='black', hatch="o")
	# rects2 = ax.bar(2, happiness_index_dream_expected_sum*100, align='center', color='white',edgecolor='black', hatch="|")
	# rects3 = ax.bar(4, happiness_index_normal_sum*100, align='center', color='white',edgecolor='black', hatch=".")
	# rects4 = ax.bar(5, happiness_index_dream_sum*100, align='center', color='white', edgecolor='black', hatch="*")
	# rects5 = ax.bar(7, happiness_index_normal_spc_sum*100, align='center', color='white',edgecolor='black', hatch="X")
	# rects6 = ax.bar(8, happiness_index_dream_spc_sum*100, align='center', color='white',edgecolor='black', hatch="+")

	# # add some text for labels, title and axes ticks
	
	# ax.set_ylabel('"%" of Students Happy (Happiness Index)')
	# ax.set_title('Happiness Index Comparison')
	# ax.set_xticks([1,2,4,5,7,8])
	# ax.set_xticklabels(['NE','DE','NR','DR','NSPC','DSPC'])
	# #ax.set_xticklabels((''))
	# ax.yaxis.grid(True)

	# #ax.legend((rects1[0], rects2[0], rects3[0], rects4[0]), ('(a)',  '(b)', '(c)', '(d)'))

	# def autolabel(rects):
	#     """
	#     Attach a text label above each bar displaying its height
	#     """
	#     for rect in rects:
	#         height = rect.get_height()
	#         ax.text(rect.get_x() + rect.get_width()/2., 1.03*height,
	#                 '%d' % int(height),
	#                 ha='center', va='bottom')

	# autolabel(rects1)
	# autolabel(rects2)
	# autolabel(rects3)
	# autolabel(rects4)
	# autolabel(rects5)
	# autolabel(rects6)
	# plt.tight_layout()
	# plt.show()


	# #Blocking Pairs

	# N = 1
	# ind = np.arange(N)  # the x locations for the groups
	# width = 0.2      # the width of the bars

	# fig, ax = plt.subplots()
	# rects1 = ax.bar(1, blocking_pairs_normal_expected_sum, align='center', color='white',edgecolor='black', hatch="o")
	# rects2 = ax.bar(2, blocking_pairs_dream_expected_sum, align='center', color='white',edgecolor='black', hatch="|")
	# rects3 = ax.bar(4, blocking_pairs_normal_sum, align='center', color='white',edgecolor='black', hatch=".")
	# rects4 = ax.bar(5, blocking_pairs_dream_sum, align='center', color='white', edgecolor='black', hatch="*")
	# rects5 = ax.bar(7, blocking_pairs_normal_spc_sum, align='center', color='white',edgecolor='black', hatch="X")
	# rects6 = ax.bar(8, blocking_pairs_dream_spc_sum, align='center', color='white',edgecolor='black', hatch="+")

	# # add some text for labels, title and axes ticks
	# ax.set_ylim(top=150)
	# ax.set_ylabel('No. of Blocking Pairs')
	# ax.set_title('Stability Comparison')
	# ax.set_xticks([1,2,4,5,7,8])
	# ax.set_xticklabels(['NE','DE','NR','DR','NSPC','DSPC'])
	# #ax.set_xticklabels((''))
	# ax.yaxis.grid(True)

	# #ax.legend((rects1[0], rects2[0], rects3[0], rects4[0]), ('(a)',  '(b)', '(c)', '(d)'))

	# def autolabel(rects):
	#     """
	#     Attach a text label above each bar displaying its height
	#     """
	#     for rect in rects:
	#         height = rect.get_height()
	#         ax.text(rect.get_x() + rect.get_width()/2., 1.03*height,
	#                 '%d' % int(height),
	#                 ha='center', va='bottom')

	# autolabel(rects1)
	# autolabel(rects2)
	# autolabel(rects3)
	# autolabel(rects4)
	# autolabel(rects5)
	# autolabel(rects6)
	# plt.tight_layout()
	# plt.show()

	# #Companies Disappointed

	# N = 1
	# ind = np.arange(N)  # the x locations for the groups
	# width = 0.2      # the width of the bars

	# fig, ax = plt.subplots()
	# rects1 = ax.bar(1, companies_disappointed_normal_expected_sum, align='center', color='white',edgecolor='black', hatch="o")
	# rects2 = ax.bar(2, companies_disappointed_dream_expected_sum, align='center', color='white',edgecolor='black', hatch="|")
	# rects3 = ax.bar(4, companies_disappointed_normal_sum, align='center', color='white',edgecolor='black', hatch=".")
	# rects4 = ax.bar(5, companies_disappointed_dream_sum, align='center', color='white', edgecolor='black', hatch="*")
	# rects5 = ax.bar(7, companies_disappointed_normal_spc_sum, align='center', color='white',edgecolor='black', hatch="X")
	# rects6 = ax.bar(8, companies_disappointed_dream_spc_sum, align='center', color='white',edgecolor='black', hatch="+")

	# # add some text for labels, title and axes ticks
	# ax.set_ylim(top=400)
	# ax.set_ylabel('Companies Lost')
	# ax.set_title('Companies Lost Comparison')
	# ax.set_xticks([1,2,4,5,7,8])
	# ax.set_xticklabels(['NE','DE','NR','DR','NSPC','DSPC'])
	# #ax.set_xticklabels((''))
	# ax.yaxis.grid(True)

	# #ax.legend((rects1[0], rects2[0], rects3[0], rects4[0]), ('(a)',  '(b)', '(c)', '(d)'))

	# def autolabel(rects):
	#     """
	#     Attach a text label above each bar displaying its height
	#     """
	#     for rect in rects:
	#         height = rect.get_height()
	#         ax.text(rect.get_x() + rect.get_width()/2., 1.03*height,
	#                 '%d' % int(height),
	#                 ha='center', va='bottom')

	# autolabel(rects1)
	# autolabel(rects2)
	# autolabel(rects3)
	# autolabel(rects4)
	# autolabel(rects5)
	# autolabel(rects6)
	# plt.tight_layout()
	# plt.show()

	# #Total Students Placed
	# N = 1
	# ind = np.arange(N)  # the x locations for the groups
	# width = 0.2      # the width of the bars

	# fig, ax = plt.subplots()
	# rects1 = ax.bar(1, total_st_placed_normal_expected_sum, align='center', color='white',edgecolor='black', hatch="o")
	# rects2 = ax.bar(2, total_st_placed_dream_expected_sum, align='center', color='white',edgecolor='black', hatch="|")
	# rects3 = ax.bar(4, total_st_placed_normal_sum, align='center', color='white',edgecolor='black', hatch=".")
	# rects4 = ax.bar(5, total_st_placed_dream_sum, align='center', color='white', edgecolor='black', hatch="*")
	# rects5 = ax.bar(7, total_st_placed_normal_spc_sum, align='center', color='white',edgecolor='black', hatch="X")
	# rects6 = ax.bar(8, total_st_placed_dream_spc_sum, align='center', color='white',edgecolor='black', hatch="+")

	# # add some text for labels, title and axes ticks
	# ax.set_ylim(top=1200)
	# ax.set_ylabel('Total Students Placed')
	# ax.set_title('Total Students Placed Comparison')
	# ax.set_xticks([1,2,4,5,7,8])
	# ax.set_xticklabels(['NE','DE','NR','DR','NSPC','DSPC'])
	# #ax.set_xticklabels((''))
	# ax.yaxis.grid(True)

	# #ax.legend((rects1[0], rects2[0], rects3[0], rects4[0]), ('(a)',  '(b)', '(c)', '(d)'))

	# def autolabel(rects):
	#     """
	#     Attach a text label above each bar displaying its height
	#     """
	#     for rect in rects:
	#         height = rect.get_height()
	#         ax.text(rect.get_x() + rect.get_width()/2., 1.03*height,
	#                 '%d' % int(height),
	#                 ha='center', va='bottom')

	# autolabel(rects1)
	# autolabel(rects2)
	# autolabel(rects3)
	# autolabel(rects4)
	# autolabel(rects5)
	# autolabel(rects6)
	# plt.tight_layout()
	# plt.show()


	# #No of dream options utlised to get better offers
	# N = 1
	# ind = np.arange(N)  # the x locations for the groups
	# width = 0.2      # the width of the bars

	# fig, ax = plt.subplots()
	# rects1 = ax.bar(1, 0, align='center', color='white',edgecolor='black', hatch="o")
	# rects2 = ax.bar(2, oldies_placement_expected_sum, align='center', color='white',edgecolor='black', hatch="|")
	# rects3 = ax.bar(4, 0, align='center', color='white',edgecolor='black', hatch=".")
	# rects4 = ax.bar(5, oldies_placement_sum, align='center', color='white', edgecolor='black', hatch="*")
	# rects5 = ax.bar(7, 0, align='center', color='white',edgecolor='black', hatch="X")
	# rects6 = ax.bar(8, oldies_placement_spc_sum, align='center', color='white',edgecolor='black', hatch="+")

	# # add some text for labels, title and axes ticks
	# ax.set_ylim(top=1000)
	# ax.set_ylabel('Dream Options Used')
	# ax.set_title('Comparing # of Dream Options Used')
	# ax.set_xticks([1,2,4,5,7,8])
	# ax.set_xticklabels(['NE','DE','NR','DR','NSPC','DSPC'])
	# #ax.set_xticklabels((''))
	# ax.yaxis.grid(True)

	# #ax.legend((rects1[0], rects2[0], rects3[0], rects4[0]), ('(a)',  '(b)', '(c)', '(d)'))

	# def autolabel(rects):
	#     """
	#     Attach a text label above each bar displaying its height
	#     """
	#     for rect in rects:
	#         height = rect.get_height()
	#         ax.text(rect.get_x() + rect.get_width()/2., 1.03*height,
	#                 '%d' % int(height),
	#                 ha='center', va='bottom')

	# autolabel(rects1)
	# autolabel(rects2)
	# autolabel(rects3)
	# autolabel(rects4)
	# autolabel(rects5)
	# autolabel(rects6)
	# plt.tight_layout()
	# plt.show()
	# #done
	# # print ("total placed dream:::",total_st_placed_dream)
	# # print ("happiness_index_normal:::",happiness_index_normal)
	# # print ("happiness_index_dream:::",happiness_index_dream)
	# #for i in f_normal_match:
	# 	#print ("normal",i)

	# #for i in f_dream_match:
	# 	#print ("dream",i)
	# # print companies_disappointed
	# # print avg_gain
	# # print highest_gain
	# # print highest_loss
	# # print blocking_pairs
	# # print rank_eff
	# # print happiness_index
	# # print blocking_pairs_dream
	# # print rank_eff_dream
	# # print happiness_index_dream

	# # r.append(rank_eff)
	# # b.append(blocking_pairs)
	# # h.append(happiness_index)
	# # rd.append(rank_eff_dream)
	# # bd.append(blocking_pairs_dream)
	# # hd.append(happiness_index_dream)

	# # plt.plot(r)
	# # plt.ylabel("rank_efficiency-normal-normal")
	# # plt.show()

	# # plt.plot(rd)
	# # plt.ylabel("rank_efficiency-dream-normal")
	# # plt.show()

	# # plt.plot(b)
	# # plt.ylabel("blocking_pairs-normal-normal")
	# # plt.show()

	# # plt.plot(bd)
	# # plt.ylabel("blocking_pairs-dream-normal")
	# # plt.show()

	# # plt.plot(h)
	# # plt.ylabel("happiness_index-normal-normal")
	# # plt.show()

	# # plt.plot(hd)
	# # plt.ylabel("happiness_index-dream-normal")
	# # plt.show()

if __name__=="__main__":
	main()