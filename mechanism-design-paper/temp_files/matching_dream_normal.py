import numpy as np 

student_left_list=student_final_ranklist
student_selected_list=[]
for i in company_final_ranklist:
	#when company i comes
	shortlist=[]
	shortlist.append(student_left_list[0:10])
	shuffle(shortlist)
	selected=[]
	selected.append(shortlist[0:5])
	for j in selected:
		student_left_list.remove(j)
	for k in range(0,5):
		selected[k].append(i) #appending company information to selected students

	student_selected_list.append(selected)


if __name__=="__main__":
	main()	

