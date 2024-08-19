# Assignment with streamlit
# get input (student's 3 subject marks, roll no and name) and output (apply grading and print report card)

import streamlit as st

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

st.title("Students Report Card")
col1, col2 = st.columns(2)
name : str = col1.text_input("Enter Student's name: ")
roll_no : int = int(col2.number_input("Enter Roll No: ", 0))

col1, col2 = st.columns(2)
with col1:
    subjects : list = ["English", "Maths", "Urdu", "science"]
    marks : list = []
    for s in subjects:
        m = float(col1.number_input(f"Marks in {s}", 0, 100))
        marks.append(m)

    #/////////////calculate agregate/average grades///////
    average_marks = sum(marks)/len(marks)
    average_grade = grades(average_marks)

#/////////Print Report Card//////// 
with col2:
    if col2.button("Print Report"):
        col2.write(".......................Report Card........................")
        
        sub_col1, sub_col2 = st.columns(2)
        sub_col1.write(f"Name:\t {name}")
        sub_col2.write(f"Roll No:\t {roll_no}")
        
        col2.write(".........................................................")
        
        sub_col1, sub_col2 = st.columns(2)
        sub_col1.write("Subject")
        sub_col2.write("Grade")

        for i in range(len(subjects)):
            sub_col1.write(f"{subjects[i]}")
            sub_col2.write(f"{grades(marks[i])}")


            
        col2.write(f"Average Grade = {average_grade}")    
