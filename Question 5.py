import pandas

students_dataframe = pandas.read_csv("student.csv") # load the dataset
students_dataframe["grade"] = students_dataframe["grade"].astype(int) # convert grade column to integers

def assign_grade_band(grade): # define function to categorize grade bands
    if grade <= 9: # check for low band
        return "Low"
    elif 10 <= grade <= 14: # check for medium band
        return "Medium"
    else:
        return "High" # otherwise assign high band

students_dataframe["grade_band"] = students_dataframe["grade"].apply(assign_grade_band) # apply banding function

grouped_summary_table = students_dataframe.groupby("grade_band").agg( # group by grade band and summarize
    num_students=('grade', 'count'),
    avg_absences=('absences', 'mean'),
    internet_percentage=('internet', lambda x: 100 * x.sum() / len(x))
).reset_index() # convert grouped result back to a dataframe

grouped_summary_table.to_csv("student_bands.csv") # save summary table to CSV

print(grouped_summary_table) # display the summary table
