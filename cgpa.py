import streamlit as st

st.title("CGPA Calculator")

# Input number of semesters
num_sems = st.number_input("Enter number of semesters", min_value=1, step=1)

sgpas = []
for i in range(1, num_sems + 1):
    sgpa = st.number_input(f"Enter SGPA for Semester {i}", min_value=0.0, max_value=10.0, step=0.01, key=i)
    sgpas.append(sgpa)

if sgpas:
    cgpa = sum(sgpas) / len(sgpas)
    st.success(f"Your CGPA is: {cgpa:.2f}")
