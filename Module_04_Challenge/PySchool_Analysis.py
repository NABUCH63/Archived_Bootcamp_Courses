# import dependencies

import os
import pandas as pd
import numpy as np

# files to load

school_data = "Input/schools_complete.csv"
student_data = "Input/students_complete.csv"

#dirpath = os.path.dirname(__file__)
school_path = os.path.join(school_data)
student_path = os.path.join(student_data)

school_df = pd.read_csv(school_path)
student_df = pd.read_csv(student_path)

# Clean student data of unwanted prefix/suffix by iterating through the list

clean = ["Dr. ",  "Mr. ","Ms. ", "Mrs. ", "Miss ", " MD", " DDS", " DVM", " PhD"]

for word in clean:
    student_df["student_name"] = student_df["student_name"].str.replace(word, "", regex=True)

# check if the names were cleaned

# student_df.head(20)

# merge datasets on the school_name column

district_df = pd.merge(student_df, school_df, on="school_name")
district_df_adj = pd.merge(student_df, school_df, on="school_name")

# set all reading and math scores for 9th grade Thomas High School to "NaN"

district_df_adj.loc[((district_df["school_name"] == "Thomas High School") & (district_df["grade"] == "9th")), ["reading_score", "math_score"]] = np.nan
district_df_adj = district_df_adj.dropna()

# calculate totals for the district
school_count = len(district_df["school_name"].unique())
all_students = district_df["Student ID"].count()
district_budget = school_df["budget"].sum()
district_math_avg = district_df["math_score"].mean()
district_read_avg = district_df["reading_score"].mean()
District_passing_math = district_df[(district_df["math_score"] >= 70)]
District_passing_reading = district_df[(district_df["reading_score"] >= 70)]

District_passing_math = District_passing_math["student_name"].count()
District_passing_reading = District_passing_reading["student_name"].count()

District_passing_math = District_passing_math / all_students * 100
District_passing_reading = District_passing_reading / all_students * 100

District_math_reading = district_df[(district_df["reading_score"] >= 70) & (district_df["math_score"] >= 70)]
District_math_reading = District_math_reading["student_name"].count()

District_overall_passing_percentage = District_math_reading / all_students * 100

# calculate adjusted district values

adj_district_math_avg = district_df_adj["math_score"].mean()
adj_district_read_avg = district_df_adj["reading_score"].mean()
adj_District_passing_math = district_df_adj[(district_df_adj["math_score"] >= 70)]
adj_District_passing_reading = district_df_adj[(district_df_adj["reading_score"] >= 70)]

adj_District_passing_math = adj_District_passing_math["student_name"].count()
adj_District_passing_reading = adj_District_passing_reading["student_name"].count()

adj_District_passing_math = adj_District_passing_math / all_students * 100
adj_District_passing_reading = adj_District_passing_reading / all_students * 100

adj_District_math_reading = district_df_adj[(district_df_adj["reading_score"] >= 70) & (district_df_adj["math_score"] >= 70)]
adj_District_math_reading = adj_District_math_reading["student_name"].count()

adj_District_overall_passing_percentage = adj_District_math_reading / all_students * 100

# calculate totals for schools
per_school_type = school_df.set_index(["school_name"])["type"]

per_school_counts = district_df["school_name"].value_counts()
per_school_budget = district_df.groupby(["school_name"]).mean()["budget"]
per_school_capita = per_school_budget / per_school_counts

per_school_math = district_df.groupby(["school_name"]).mean()["math_score"]
per_school_reading = district_df.groupby(["school_name"]).mean()["reading_score"]

per_school_passing_math = district_df[(district_df["math_score"] >= 70)]
per_school_passing_reading = district_df[(district_df["reading_score"] >= 70)]

per_school_passing_math = per_school_passing_math.groupby(["school_name"]).count()["student_name"]
per_school_passing_reading = per_school_passing_reading.groupby(["school_name"]).count()["student_name"]

per_school_passing_math = per_school_passing_math / per_school_counts * 100
per_school_passing_reading = per_school_passing_reading / per_school_counts * 100

per_passing_math_reading = district_df[(district_df["reading_score"] >= 70) & (district_df["math_score"] >= 70)]
per_passing_math_reading = per_passing_math_reading.groupby(["school_name"]).count()["student_name"]

per_overall_passing_percentage = per_passing_math_reading / per_school_counts * 100

# create new dataframe for grade_index
school_list = []
for school in school_df["school_name"]:
    school_list.append(school)
    school_list.append(school)
    school_list.append(school)
    school_list.append(school)
grade_list = ["9th", "10th", "11th", "12th", "9th", "10th", "11th", "12th", "9th", "10th", "11th", "12th", "9th", "10th", "11th", "12th", "9th", "10th", "11th", "12th", "9th", "10th", "11th", "12th", "9th", "10th", "11th", "12th", "9th", "10th", "11th", "12th", "9th", "10th", "11th", "12th", "9th", "10th", "11th", "12th", "9th", "10th", "11th", "12th", "9th", "10th", "11th", "12th", "9th", "10th", "11th", "12th", "9th", "10th", "11th", "12th", "9th", "10th", "11th", "12th"]

# calculate totals per grade
per_grade_counts = district_df["grade"].value_counts()
total_students_per_grade = district_df.groupby(["school_name", "grade"]).size()

Average_read_score_per_grade = district_df.groupby(["school_name", "grade"]).mean()["reading_score"]
Average_math_score_per_grade = district_df.groupby(["school_name", "grade"]).mean()["math_score"]
per_grade_passing_math = district_df[(district_df["math_score"] >= 70)]
per_grade_passing_reading = district_df[(district_df["reading_score"] >= 70)]

per_grade_passing_math = per_grade_passing_math.groupby(["school_name", "grade"]).count()["student_name"]
per_grade_passing_reading = per_grade_passing_reading.groupby(["school_name", "grade"]).count()["student_name"]

per_grade_passing_math = per_grade_passing_math / total_students_per_grade * 100
per_grade_passing_reading = per_grade_passing_reading / total_students_per_grade * 100

per_passing_grade_math_reading = district_df[(district_df["reading_score"] >= 70) & (district_df["math_score"] >= 70)]
per_passing_grade_math_reading = per_passing_grade_math_reading.groupby(["school_name", "grade"]).count()["student_name"]

per_grade_overall_passing_percentage = per_passing_grade_math_reading / total_students_per_grade * 100

# create district dataframe
District_total_df = pd.DataFrame(
    [{"Schools": school_count,
    "Total Students": all_students,
    "Total Budget": district_budget,
    "Average Math Score": district_math_avg,
    "Average Reading Score": district_read_avg,
    "Percent Passing Math": District_passing_math,
    "Percent Passing Reading": District_passing_reading,
    "Percent Passing Overall": District_overall_passing_percentage}])

# create schools dataframe
school_summary_df = pd.DataFrame({
    "School_Type": per_school_type,
    "Total_Students": per_school_counts,
    "Total_School_Budget": per_school_budget,
    "Per_Student_Budget": per_school_capita,
    "Average_Math_Score": per_school_math,
    "Average_Reading_Score": per_school_reading,
    "%_Passing_Math": per_school_passing_math,
    "%_Passing_Reading": per_school_passing_reading,
    "%_Overall_Passing": per_overall_passing_percentage})
school_summary_df.reset_index(inplace=True)
school_summary_df.rename(columns={"index": "School"}, inplace=True)

# create grade level dataframe
grade_summary_df = pd.DataFrame({
    "Total_Students": total_students_per_grade,
    "Average_Math_Score": Average_math_score_per_grade,
    "Average_Reading_Score": Average_read_score_per_grade,
    "%_Passing_Math": per_grade_passing_math,
    "%_Passing_Reading": per_grade_passing_reading,
    "%_Overall_Passing": per_grade_overall_passing_percentage})
grade_summary_df.reindex([school_list, grade_list])

# recalc Thomas High School grades 10-12 to remove effect of missing 9th grade scores
per_school_counts_adj = district_df["school_name"].value_counts()

Average_read_score_per_school_adj = district_df_adj.groupby(["school_name"]).mean()["reading_score"]
Average_math_score_per_school_adj = district_df_adj.groupby(["school_name"]).mean()["math_score"]

per_school_passing_math_adj = district_df_adj[(district_df_adj["math_score"] >= 70)]
per_school_passing_reading_adj = district_df_adj[(district_df_adj["reading_score"] >= 70)]

per_school_passing_math_adj = per_school_passing_math_adj.groupby(["school_name"]).count()["student_name"]
per_school_passing_reading_adj = per_school_passing_reading_adj.groupby(["school_name"]).count()["student_name"]

per_school_passing_math_adj = per_school_passing_math_adj / per_school_counts_adj * 100
per_school_passing_reading_adj = per_school_passing_reading_adj / per_school_counts_adj * 100
THS_math_pass = per_school_passing_math_adj["Thomas High School"]
per_passing_school_math_reading_adj = district_df_adj[(district_df_adj["reading_score"] >= 70) & (district_df_adj["math_score"] >= 70)]
per_passing_school_math_reading_adj = per_passing_school_math_reading_adj.groupby(["school_name"]).count()["student_name"]

per_school_overall_passing_percentage_adj = per_passing_school_math_reading_adj / per_school_counts_adj * 100

# create new dataframe with updated values for Thomas High School, removing 9th grade
school_summary_adj_df = school_summary_df.copy()
district_total_adj_df = District_total_df.copy()
district_total_adj_df.reset_index(inplace=True)

district_total_adj_df.loc[district_total_adj_df["index"] == 0, "Average Math Score"] = adj_district_math_avg
district_total_adj_df.loc[district_total_adj_df["index"] == 0, "Average Reading Score"] = adj_district_read_avg
district_total_adj_df.loc[district_total_adj_df["index"] == 0, "Percent Passing Math"] = adj_District_passing_math
district_total_adj_df.loc[district_total_adj_df["index"] == 0, "Percent Passing Reading"] = adj_District_passing_reading
district_total_adj_df.loc[district_total_adj_df["index"] == 0, "Percent Passing Overall"] = adj_District_overall_passing_percentage


school_summary_adj_df.loc[school_summary_adj_df["School"] == "Thomas High School", "Total_Students"] = per_school_counts_adj["Thomas High School"]
school_summary_adj_df.loc[school_summary_adj_df["School"] == "Thomas High School", "Average_Math_Score"] = Average_math_score_per_school_adj["Thomas High School"]
school_summary_adj_df.loc[school_summary_adj_df["School"] == "Thomas High School", "Average_Reading_Score"] = Average_read_score_per_school_adj["Thomas High School"]
school_summary_adj_df.loc[school_summary_adj_df["School"] == "Thomas High School", "%_Passing_Math"] = per_school_passing_math_adj["Thomas High School"]
school_summary_adj_df.loc[school_summary_adj_df["School"] == "Thomas High School", "%_Passing_Reading"] = per_school_passing_reading_adj["Thomas High School"]
school_summary_adj_df.loc[school_summary_adj_df["School"] == "Thomas High School", "%_Overall_Passing"] = per_school_overall_passing_percentage_adj["Thomas High School"]

# output dataframes as csv for review
school_summary_adj_df.to_csv("Output/adj_school_summary_output.csv", index=True)
school_summary_df.to_csv("Output/school_summary_output.csv", index=True)
District_total_df.to_csv("Output/district_summary_output.csv", index=True)
district_total_adj_df.to_csv("Output/adj_district_summary_output.csv", index=True)
grade_summary_df.to_csv("Output/grade_summary_output.csv", index=True)

# Sort schools for top performance based on overall testing before and after adjusting the scores
budget_per_schooltype = school_summary_df.sort_values(by=["School_Type", "Per_Student_Budget"], ascending=False)
score_per_studentcapita = school_summary_df.sort_values(by=["%_Overall_Passing", "Per_Student_Budget"], ascending=False)
score_per_studentcount = school_summary_df.sort_values(by=["%_Overall_Passing", "Total_Students"], ascending=False)
score_per_schooltype = school_summary_df.sort_values(by=["%_Overall_Passing", "School_Type"], ascending=False)
performance = school_summary_df.sort_values(by=["%_Overall_Passing"], ascending=False)

adj_budget_per_schooltype = school_summary_adj_df.sort_values(by=["School_Type", "Per_Student_Budget"], ascending=False)
adj_score_per_studentcapita = school_summary_adj_df.sort_values(by=["%_Overall_Passing", "Per_Student_Budget"], ascending=False)
adj_score_per_studentcount = school_summary_adj_df.sort_values(by=["%_Overall_Passing", "Total_Students"], ascending=False)
adj_score_per_schooltype = school_summary_adj_df.sort_values(by=["%_Overall_Passing", "School_Type"], ascending=False)
adj_performance = school_summary_adj_df.sort_values(by=["%_Overall_Passing"], ascending=False)

# score per student capita
print("Score per Student Capita")
print(score_per_studentcapita[["School", "%_Overall_Passing", "Per_Student_Budget"]])
print("Adjusted score per Student Capita")
print(adj_score_per_studentcapita[["School", "%_Overall_Passing", "Per_Student_Budget"]])
# score per student count
print("Score per Student Count")
print(score_per_studentcount[["School", "%_Overall_Passing", "Total_Students"]])
print("Adjusted_score per Student Count")
print(adj_score_per_studentcount[["School", "%_Overall_Passing", "Total_Students"]])
# score per school type
print("Score per School Type")
print(score_per_schooltype[["School", "%_Overall_Passing", "School_Type"]])
print("Adjusted_score per School Type")
print(adj_score_per_schooltype[["School", "%_Overall_Passing", "School_Type"]])
# top 5 performing
print("Top 5 Schools")
print(performance[["School", "%_Overall_Passing"]].head(5))
print("Adjusted top 5 Schools")
print(adj_performance[["School", "%_Overall_Passing"]].head(5))
# bottom 5 performing
print("Bottom 5 Schools")
print(performance[["School", "%_Overall_Passing"]].tail(5))
print("Adjusted bottom 5 Schools")
print(adj_performance[["School", "%_Overall_Passing"]].tail(5))


