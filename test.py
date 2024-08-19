# Without streamlit
# get input (student's 3 subject marks, roll no and name) and output (apply grading and print report card)

# ////////function to find grades/////////////////////
def grades(num):
    if num >= 90:
        return('A+')
    elif num >=80 and num <90:
        return('A')
    elif num >=70 and num <80:
        return('B')    
    elif num >=60 and num <70:
        return('C')
    elif num >=50 and num <60:
        return('D')
    else:
        return('F')

#//////get input ///////////////////////////////////// 
name : str = input("Enter Student's name: ")
roll_no : int = int(input("Enter Roll No: "))
subjects : list = ["English", "Maths", "Urdu", "science"]
marks : list = []
for s in subjects:
    m = float(input(f"Enter Marks of.. {s}...="))
    marks.append(m)

#/////////////calculate agregate/average grades///////
average_marks = sum(marks)/len(marks)
average_grade = grades(average_marks)

#/////////Print Report Card//////// 
print("...........Report Card...............")
print(f"Name:\t {name}")
print(f"Roll No:\t {roll_no}")
print("Subject \t Grade")

for i in range(len(subjects)):
    print(f"{subjects[i]} \t {grades(marks[i])}")


    
print(f"Average Grade = {average_grade}")    
