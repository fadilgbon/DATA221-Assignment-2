import pandas

students_dataframe = pandas.read_csv("student.csv") # load the dataset
filtered_students_dataframe = students_dataframe[(students_dataframe["studytime"]>=3) # filter for high study time
& (students_dataframe["internet"]==1) # filter for students with internet access
& (students_dataframe["absences"]<=5)] # filter for low absences

filtered_students_dataframe.to_csv("high engagement.csv") # save filtered data to CSV

number_of_students = len(filtered_students_dataframe) # count number of filtered students
print(f"Number of students saved: {number_of_students}") # print count

average_grade = filtered_students_dataframe["grade"].mean() # compute average grade
print(f"Average grade of filtered students: {average_grade:.2f}") # print formatted average
