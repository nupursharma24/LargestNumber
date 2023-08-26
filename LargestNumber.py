import streamlit as st
st.write("Highest Number")
st.header("Input Numbers")
def user_input():
  n1 = st.number_input("1st Number")
  n2 = st.number_input("2nd Number")
  n3 = st.number_input("3rd Number")
  return n1,n2,n3
a,b,c = user_input()
if a >= b and a >= c:
  st.write(a)
elif b >= a and b >= c:
  st.write(b)
else:
  st.write(c)
