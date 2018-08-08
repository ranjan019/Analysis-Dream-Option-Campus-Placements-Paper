miport numpy as np
import sys
import random
from random import shuffle
#import numpy as np
import matplotlib
import matplotlib.pyplot as plt

#import plotly.plotly as py
from matplotlib.ticker import NullFormatter  # useful for `logit` scale
from matplotlib.ticker import FuncFormatter


def make_company_ranklist(type_of_rl):
	company_db={}
	company_db_aggr_1=[] #only salary
	company_db_aggr_2=[] #salary plus reputation (0.6,0.4)
	company_db_aggr_3=[] #salary plus reputation plus difficulty of interview (0.5,0.35,0.15)

	for i in range(0,200):
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
	for i in range(0,50):
		happiness_point.append((student_final_ranklist[i][0],company_final_ranklist[9][0]))

	for i in range(1,17):
		for j in range(0,50):
			happiness_point.append((student_final_ranklist[50*i+j][0],company_final_ranklist[9+i*10][0]))

	for i in range(850,1000):
		happiness_point.append((student_final_ranklist[i][0],company_final_ranklist[199][0]))

	
	# for i in happiness_point:
	# 	print ("happiness-unsorted:::::",i)


	happiness_point_list_sorted=sorted(happiness_point, key=lambda x: x[0])

	# print "happiness point list"
	# print "----------------------"
	# for i in happiness_point_list_sorted:
	# 	print i
	return happiness_point_list_sorted


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

	student_pref_list=[]
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
		seq_part=company_order[i/5:len(company_order)]
		non_seq_part=company_order[0:i/5]

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
		for k in range(0,5):
			
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
			#print student_index
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
		if len(addd) > 4 :
			shuffle(addd)				
			full_list_for_this_company=addd[0:4]+full_list_for_this_company
			#dream+=1
			#print "adding dream guys (more than 5 options)"
		else:
			full_list_for_this_company=addd+full_list_for_this_company
			#dream+=1
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
				dream+=1
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

def cal_rank_efficiency(student_selected_list,stud_pref_list,l):
	total_students_placed=len(student_selected_list)
	sum_ranks=0
	for i in student_selected_list[0:l]:
		student_index=i[0]
		company_alloted=i[2]
		sum_ranks+=stud_pref_list[student_index].index(company_alloted)
		print ("student_no::",student_index,":::company_alloted::",company_alloted,":::index in pref list:::",stud_pref_list[student_index].index(company_alloted),":::summing:::",sum_ranks)

	print "done------------done-----------------done"
	return float(float(sum_ranks)/float(l))

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
	return float(float(above_hp)/float(total_students_placed))

def find_companies_lost(oldies_placement):
	people_leftoffer_list=list(oldies_placement)
	company_recruits=[]
	for i in range(0,200):
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
# 	cd=[]
# 	sd=[]
# 	company_f_ranklist= make_company_ranklist(3)
# 	student_f_ranklist= make_student_ranklist()


# 	for i in company_f_ranklist:
# 		cd.append(i[1])
# 	for i in student_f_ranklist:
# 		sd.append(i[1])

# 	cd.sort()
# 	sd.sort()

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
	

	companies_disappointed_normal_sum=0
	companies_disappointed_normal_spc_sum=0
	companies_disappointed_dream_sum=0
	companies_disappointed_dream_spc_sum=0

	rank_eff_normal_sum=0
	rank_eff_normal_spc_sum=0
	rank_eff_dream_sum=0
	rank_eff_dream_spc_sum=0

	blocking_pairs_normal_sum=0
	blocking_pairs_normal_spc_sum=0
	blocking_pairs_dream_sum=0
	blocking_pairs_dream_spc_sum=0

	happiness_index_normal_sum=0
	happiness_index_normal_spc_sum=0
	happiness_index_dream_sum=0
	happiness_index_dream_spc_sum=0

	total_st_placed_normal_sum=0
	total_st_placed_normal_spc_sum=0
	total_st_placed_dream_sum=0
	total_st_placed_dream_spc_sum=0

	oldies_placement_sum=0
	oldies_placement_spc_sum=0

	avg_gain_normal_sum=0
	avg_gain_normal_spc_sum=0
	avg_gain_dream_sum=0
	avg_gain_dream_spc_sum=0

	highest_gain_normal_sum=0
	highest_gain_normal_spc_sum=0
	highest_gain_dream_sum=0
	highest_gain_dream_spc_sum=0

	highest_loss_normal_sum=0
	highest_loss_normal_spc_sum=0
	highest_loss_dream_sum=0
	highest_loss_dream_spc_sum=0


	#for i in range (0,1000):

		#print ("iteration ::::: ",i)

	company_f_ranklist= make_company_ranklist(3)
	student_f_ranklist= make_student_ranklist()
	happiness_point_list= def_happiness_point(student_f_ranklist,company_f_ranklist)
	stud_pref_list= make_stud_pref_list(company_f_ranklist)
	seq_stud_pref_list=make_seq_stud_pref_list(company_f_ranklist,student_f_ranklist)


	
	
	f_normal_match= match_normal(student_f_ranklist, company_f_ranklist)
	f_normal_match_spc=list(f_normal_match)
	(oldies_placement, people_dreamt, f_dream_match)=match_dream(student_f_ranklist,company_f_ranklist,stud_pref_list)
	(oldies_placement_spc, people_dreamt_spc, f_dream_match_spc)=match_dream(student_f_ranklist,company_f_ranklist,seq_stud_pref_list)

	(avg_gain_normal,highest_gain_normal,highest_loss_normal) =  fairness(f_normal_match, student_f_ranklist)
	(avg_gain_normal_spc,highest_gain_normal_spc,highest_loss_normal_spc) =  fairness(f_normal_match_spc, student_f_ranklist)
	(avg_gain_dream,highest_gain_dream,highest_loss_dream) =  fairness(f_dream_match, student_f_ranklist)
	(avg_gain_dream_spc,highest_gain_dream_spc,highest_loss_dream_spc) =  fairness(f_dream_match_spc, student_f_ranklist)


	companies_disappointed_normal=0
	companies_disappointed_normal_spc=0
	companies_disappointed_dream = find_companies_lost(oldies_placement)
	companies_disappointed_dream_spc = find_companies_lost(oldies_placement_spc)



	

	


	blocking_pairs_normal=find_stability(f_normal_match,stud_pref_list)
	blocking_pairs_normal_spc=find_stability(f_normal_match_spc,seq_stud_pref_list)
	blocking_pairs_dream=find_stability(f_dream_match,stud_pref_list)
	blocking_pairs_dream_spc=find_stability(f_dream_match_spc,seq_stud_pref_list)


	happiness_index_normal=calc_happiness_index(f_normal_match,happiness_point_list,stud_pref_list)
	happiness_index_normal_spc=calc_happiness_index(f_normal_match_spc,happiness_point_list,seq_stud_pref_list)
	happiness_index_dream=calc_happiness_index(f_dream_match,happiness_point_list,stud_pref_list)
	happiness_index_dream_spc=calc_happiness_index(f_dream_match_spc,happiness_point_list,seq_stud_pref_list)

	total_st_placed_normal=len(f_normal_match)
	total_st_placed_normal_spc=len(f_normal_match_spc)
	total_st_placed_dream=len(f_dream_match)
	total_st_placed_dream_spc=len(f_dream_match_spc)

	rank_eff_normal=cal_rank_efficiency(f_normal_match,stud_pref_list,total_st_placed_dream)
	rank_eff_normal_spc=cal_rank_efficiency(f_normal_match_spc,seq_stud_pref_list,total_st_placed_normal_spc)
	rank_eff_dream=cal_rank_efficiency(f_dream_match,stud_pref_list,total_st_placed_dream)
	rank_eff_dream_spc=cal_rank_efficiency(f_dream_match_spc,seq_stud_pref_list,total_st_placed_dream_spc)

	print total_st_placed_dream
	print ("rank_eff_normal::",rank_eff_normal)
	print
	print ("rank_eff_dream::",rank_eff_dream)


	#
	#
	#	
	# #summation of all simulations
	companies_disappointed_normal_sum+=companies_disappointed_normal
	companies_disappointed_normal_spc_sum+=companies_disappointed_normal_spc
	companies_disappointed_dream_sum+=companies_disappointed_dream
	companies_disappointed_dream_spc_sum+=companies_disappointed_dream_spc

	rank_eff_normal_sum+=rank_eff_normal
	rank_eff_normal_spc_sum+=rank_eff_normal_spc
	rank_eff_dream_sum+=rank_eff_dream
	rank_eff_dream_spc_sum+=rank_eff_dream_spc

	blocking_pairs_normal_sum+=blocking_pairs_normal
	blocking_pairs_normal_spc_sum+=blocking_pairs_normal_spc
	blocking_pairs_dream_sum+=blocking_pairs_dream
	blocking_pairs_dream_spc_sum+=blocking_pairs_dream_spc

	happiness_index_normal_sum+=happiness_index_normal
	happiness_index_normal_spc_sum+=happiness_index_normal_spc
	happiness_index_dream_sum+=happiness_index_dream
	happiness_index_dream_spc_sum+=happiness_index_dream_spc

	total_st_placed_normal_sum+=total_st_placed_normal
	total_st_placed_normal_spc_sum+=total_st_placed_normal_spc
	total_st_placed_dream_sum+=total_st_placed_dream
	total_st_placed_dream_spc_sum+=total_st_placed_dream_spc

	oldies_placement_sum+=len(oldies_placement)
	oldies_placement_spc_sum+=len(oldies_placement_spc)

	avg_gain_normal_sum+=avg_gain_normal
	avg_gain_normal_spc_sum+=avg_gain_normal_spc
	avg_gain_dream_sum+=avg_gain_dream
	avg_gain_dream_spc_sum+=avg_gain_dream_spc

	highest_gain_normal_sum+=highest_gain_normal
	highest_gain_normal_spc_sum+=highest_gain_normal_spc
	highest_gain_dream_sum+=highest_gain_dream
	highest_gain_dream_spc_sum+=highest_gain_dream_spc

	highest_loss_normal_sum+=highest_loss_normal
	highest_loss_normal_spc_sum+=highest_loss_normal_spc
	highest_loss_dream_sum+=highest_loss_dream
	highest_loss_dream_spc_sum+=highest_loss_dream_spc




	#Graph comparison rank efficiency

	N = 1
	ind = np.arange(N)  # the x locations for the groups
	width = 0.2      # the width of the bars

	fig, ax = plt.subplots()
	rects1 = ax.bar(ind + width, rank_eff_normal_sum, width, color='dimgray')
	rects2 = ax.bar(ind + 2*width, rank_eff_dream_sum, width, color='darkgray')
	rects3 = ax.bar(ind + 3.5*width, rank_eff_normal_spc_sum, width, color='lightgray')
	rects4 = ax.bar(ind + 4.5*width, rank_eff_dream_spc_sum, width, color='tan')

	# add some text for labels, title and axes ticks
	ax.set_ylabel('Rank Efficiency')
	ax.set_title('Rank Efficiency Comparison')
	ax.set_xticks(ind + width / 2)
	ax.set_xticklabels((''))

	ax.legend((rects1[0], rects2[0], rects3[0], rects4[0]), ('Normal Match',  'Dream Match', 'Normal Match with SPC', 'Dream Match with SPC'))

	def autolabel(rects):
	    """
	    Attach a text label above each bar displaying its height
	    """
	    for rect in rects:
	        height = rect.get_height()
	        ax.text(rect.get_x() + rect.get_width()/2., 1.03*height,
	                '%d' % int(height),
	                ha='center', va='bottom')

	autolabel(rects1)
	autolabel(rects2)
	autolabel(rects3)
	autolabel(rects4)
	plt.show()

	#Fairness
	N = 4
	avggain=(avg_gain_normal_sum, avg_gain_dream_sum, avg_gain_normal_spc_sum, avg_gain_dream_spc_sum)
	highestgain=(highest_gain_normal_sum, highest_gain_dream_sum, highest_gain_normal_spc_sum, highest_gain_dream_spc_sum)
	highestloss=(-highest_loss_normal_sum, -highest_loss_dream_sum, -highest_loss_normal_spc_sum, -highest_loss_dream_spc_sum)
	ind = np.arange(N)  # the x locations for the groups
	width = 0.35      # the width of the bars

	fig, ax = plt.subplots()
	rects1 = ax.bar(ind + width, avggain, width, color='dimgray')
	rects2 = ax.bar(ind + 2*width, highestgain, width, color='darkgray')
	rects3 = ax.bar(ind + 3*width, highestloss, width, color='lightgray')
	#rects4 = ax.bar(ind + 4.5*width, rank_eff_dream_spc, width, color='tan')

	# add some text for labels, title and axes ticks
	ax.set_ylabel('Score')
	ax.set_title('Fairness Comparison')
	ax.set_xticks(ind + width / 2)
	ax.set_xticklabels((''))

	ax.legend((rects1[0], rects2[0], rects3[0], rects4[0]), ('Avg Gain', 'Highest Gain in Rank', 'Greatest Loss in Rank'))

	def autolabel(rects):
	    """
	    Attach a text label above each bar displaying its height
	    """
	    for rect in rects:
	        height = rect.get_height()
	        ax.text(rect.get_x() + rect.get_width()/2., 1.03*height,
	                '%d' % int(height),
	                ha='center', va='bottom')

	autolabel(rects1)
	autolabel(rects2)
	autolabel(rects3)
	#autolabel(rects4)
	plt.show()


	#Happiness Index

	N = 1
	ind = np.arange(N)  # the x locations for the groups
	width = 0.2      # the width of the bars

	fig, ax = plt.subplots()
	rects1 = ax.bar(ind + width, (happiness_index_normal_sum)*100, width, color='dimgray')
	rects2 = ax.bar(ind + 2*width, happiness_index_dream_sum*100, width, color='darkgray')
	rects3 = ax.bar(ind + 3.5*width, happiness_index_normal_spc_sum*100, width, color='lightgray')
	rects4 = ax.bar(ind + 4.5*width, happiness_index_dream_spc_sum*100, width, color='tan')

	# add some text for labels, title and axes ticks
	ax.set_ylabel('Happiness Index')
	ax.set_title('Happiness Index Comparison')
	ax.set_xticks(ind + width / 2)
	ax.set_xticklabels((''))

	ax.legend((rects1[0], rects2[0], rects3[0], rects4[0]), ('Normal Match',  'Dream Match', 'Normal Match with SPC', 'Dream Match with SPC'))

	def autolabel(rects):
	    """
	    Attach a text label above each bar displaying its height
	    """
	    for rect in rects:
	        height = rect.get_height()
	        ax.text(rect.get_x() + rect.get_width()/2., 0.5*height,
	                '%d' % int(height),
	                ha='center', va='bottom')

	autolabel(rects1)
	autolabel(rects2)
	autolabel(rects3)
	autolabel(rects4)
	plt.show()


	#Blocking Pairs

	N = 1
	ind = np.arange(N)  # the x locations for the groups
	width = 0.2      # the width of the bars

	fig, ax = plt.subplots()
	rects1 = ax.bar(ind + width, blocking_pairs_normal_sum, width, color='dimgray')
	rects2 = ax.bar(ind + 2*width, blocking_pairs_dream_sum, width, color='darkgray')
	rects3 = ax.bar(ind + 3.5*width, blocking_pairs_normal_spc_sum, width, color='lightgray')
	rects4 = ax.bar(ind + 4.5*width, blocking_pairs_dream_spc_sum, width, color='tan')

	# add some text for labels, title and axes ticks
	ax.set_ylabel('Blocking Pairs')
	ax.set_title('Stability Comparison')
	ax.set_xticks(ind + width / 2)
	ax.set_xticklabels((''))

	ax.legend((rects1[0], rects2[0], rects3[0], rects4[0]), ('Normal Match',  'Dream Match', 'Normal Match with SPC', 'Dream Match with SPC'))

	def autolabel(rects):
	    """
	    Attach a text label above each bar displaying its height
	    """
	    for rect in rects:
	        height = rect.get_height()
	        ax.text(rect.get_x() + rect.get_width()/2., 0.5*height,
	                '%d' % int(height),
	                ha='center', va='bottom')

	autolabel(rects1)
	autolabel(rects2)
	autolabel(rects3)
	autolabel(rects4)
	plt.show()

	#Companies Disappointed

	N = 1
	ind = np.arange(N)  # the x locations for the groups
	width = 0.2      # the width of the bars

	fig, ax = plt.subplots()
	rects1 = ax.bar(ind + width, companies_disappointed_normal_sum, width, color='dimgray')
	rects2 = ax.bar(ind + 2*width, companies_disappointed_dream_sum, width, color='darkgray')
	rects3 = ax.bar(ind + 3.5*width, companies_disappointed_normal_spc_sum, width, color='lightgray')
	rects4 = ax.bar(ind + 4.5*width, companies_disappointed_dream_spc_sum, width, color='tan')

	# add some text for labels, title and axes ticks
	ax.set_ylabel('No. of Companies Disappointed')
	ax.set_title('Company Satisfaction Comparison')
	ax.set_xticks(ind + width / 2)
	ax.set_xticklabels((''))

	ax.legend((rects1[0], rects2[0], rects3[0], rects4[0]), ('Normal Match',  'Dream Match', 'Normal Match with SPC', 'Dream Match with SPC'))

	def autolabel(rects):
	    """
	    Attach a text label above each bar displaying its height
	    """
	    for rect in rects:
	        height = rect.get_height()
	        ax.text(rect.get_x() + rect.get_width()/2., 0.5*height,
	                '%d' % int(height),
	                ha='center', va='bottom')

	autolabel(rects1)
	autolabel(rects2)
	autolabel(rects3)
	autolabel(rects4)
	plt.show()

	#Total Students Placed
	N = 1
	ind = np.arange(N)  # the x locations for the groups
	width = 0.2      # the width of the bars

	fig, ax = plt.subplots()
	rects1 = ax.bar(ind + width, total_st_placed_normal_sum, width, color='dimgray')
	rects2 = ax.bar(ind + 2*width, total_st_placed_dream_sum, width, color='darkgray')
	rects3 = ax.bar(ind + 3.5*width, total_st_placed_normal_spc_sum, width, color='lightgray')
	rects4 = ax.bar(ind + 4.5*width, total_st_placed_dream_spc_sum, width, color='tan')

	# add some text for labels, title and axes ticks
	ax.set_ylabel('Total Student Placed')
	ax.set_title('Total Students Placed Comparison')
	ax.set_xticks(ind + width / 2)
	ax.set_xticklabels((''))

	ax.legend((rects1[0], rects2[0], rects3[0], rects4[0]), ('Normal Match',  'Dream Match', 'Normal Match with SPC', 'Dream Match with SPC'))

	def autolabel(rects):
	    """
	    Attach a text label above each bar displaying its height
	    """
	    for rect in rects:
	        height = rect.get_height()
	        ax.text(rect.get_x() + rect.get_width()/2., 0.5*height,
	                '%d' % int(height),
	                ha='center', va='bottom')

	autolabel(rects1)
	autolabel(rects2)
	autolabel(rects3)
	autolabel(rects4)
	plt.show()


	#No of dream options utlised to get better offers
	N = 1
	ind = np.arange(N)  # the x locations for the groups
	width = 0.2      # the width of the bars

	fig, ax = plt.subplots()
	rects1 = ax.bar(ind + width, 0, width, color='dimgray')
	rects2 = ax.bar(ind + 2*width, oldies_placement_sum, width, color='darkgray')
	rects3 = ax.bar(ind + 3.5*width, 0, width, color='lightgray')
	rects4 = ax.bar(ind + 4.5*width, oldies_placement_spc_sum, width, color='tan')

	# add some text for labels, title and axes ticks
	ax.set_ylabel('Total Dream Options Utilised')
	ax.set_title('Total Dream Options Utilised to Get Better Offers')
	ax.set_xticks(ind + width / 2)
	ax.set_xticklabels((''))

	ax.legend((rects1[0], rects2[0], rects3[0], rects4[0]), ('Normal Match',  'Dream Match', 'Normal Match with SPC', 'Dream Match with SPC'))

	def autolabel(rects):
	    """
	    Attach a text label above each bar displaying its height
	    """
	    for rect in rects:
	        height = rect.get_height()
	        ax.text(rect.get_x() + rect.get_width()/2., 0.5*height,
	                '%d' % int(height),
	                ha='center', va='bottom')

	autolabel(rects1)
	autolabel(rects2)
	autolabel(rects3)
	autolabel(rects4)
	plt.show()
	#done
	# print ("total placed dream:::",total_st_placed_dream)
	# print ("happiness_index_normal:::",happiness_index_normal)
	# print ("happiness_index_dream:::",happiness_index_dream)
	#for i in f_normal_match:
		#print ("normal",i)

	#for i in f_dream_match:
		#print ("dream",i)
	# print companies_disappointed
	# print avg_gain
	# print highest_gain
	# print highest_loss
	# print blocking_pairs
	# print rank_eff
	# print happiness_index
	# print blocking_pairs_dream
	# print rank_eff_dream
	# print happiness_index_dream

	# r.append(rank_eff)
	# b.append(blocking_pairs)
	# h.append(happiness_index)
	# rd.append(rank_eff_dream)
	# bd.append(blocking_pairs_dream)
	# hd.append(happiness_index_dream)

	# plt.plot(r)
	# plt.ylabel("rank_efficiency-normal-normal")
	# plt.show()

	# plt.plot(rd)
	# plt.ylabel("rank_efficiency-dream-normal")
	# plt.show()

	# plt.plot(b)
	# plt.ylabel("blocking_pairs-normal-normal")
	# plt.show()

	# plt.plot(bd)
	# plt.ylabel("blocking_pairs-dream-normal")
	# plt.show()

	# plt.plot(h)
	# plt.ylabel("happiness_index-normal-normal")
	# plt.show()

	# plt.plot(hd)
	# plt.ylabel("happiness_index-dream-normal")
	# plt.show()

if __name__=="__main__":
	main()