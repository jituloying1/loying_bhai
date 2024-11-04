import streamlit as st 
# title
import pandas as pd
st.title("python Staion")

# header 
st.header('hello jitu loying ')

#subheader
st.subheader("jitu loying 123")
# text 
st.text(" hello everyone wellcome back to my chenal ")
# write 
st.write(" please like my page ")

# image
from PIL import Image
img = Image.open('MUNU4.jpg')
st.image(img,width=200,caption='hello munu') 
#colorfulll text
#success
st.success('jitu 7896220943')
# error 
st.error('error')
#warning 
st.warning("warning message")
#info
st.info('note: you have to know this...')
st.exception("name error(name is not define)")
#help
st.help(help)
# video 
vid=open('neyhe.mp4','rb').read()
st.video(vid)
# sidebar
st.sidebar.header('WELLCOME TO MY NEW WEBSITE LOYINGWEB.COME')
st.sidebar.header('about')
st.sidebar.text(''' hey i am jitu loying  i am a students of 
                information technology of software level o 
                and now i am going to learn about of python streamlit''')
#widgets
#chackbox
if st.checkbox('Show/Hide'):
  st.write('if you love to do python cooding then learn to python programing  ')
  #radio 
  status = st.radio('what is your status',('Active','Inactive'))
  if status is "Active":
    st.success('Active')
  else:
    st.warning('you are inactive')
#selectbox
occupation = st.selectbox('what you do for living ',['engineer','programer','teacher'])
st.write('you are a ',occupation)
#multiselect
location = st.multiselect('where did you live',('India','America','japan','netherland'))
st.write('you selected',len(location),'location')
st.slider('What is your age ',12,70)
#button
if st.button('About me'):
  st.write(' hello everyone i am jitu loying  i am from assam i am a students of information technology in nielit ')
  
# text_input
gmail=st.text_input('Enter your name id:')
if '@gmail.com'in gmail:
  st.write(f"confirm your gmail id{gmail}")
#text area
message=st.text_area('give your experience about streamlit')
#date time
#date
import datetime
st.date_input('Today is',datetime.datetime.now())
import time
st.time_input('time is',datetime.time())
# display raw code
st.text('how to install streamlit')
st.code('pip install streamlit')
#echo
with st.echo():
  # how to import streamlit un your python script
  import streamlit
  # display json
  st.json({'name':'jitu loying','gender':'male'})
  #spiner
with st.spinner('wait a second...'):
    time.sleep(6)
    st.success('success')
    
import time
my_bar=st.progress(0)
for p in range(10):
  my_bar.progress(p+1)
  # ballons 
  st.balloons()
  st.sidebar.header('hello jitu loying ')
  st.sidebar.button('about of Jitu Loying')
  st.sidebar.checkbox("active")
  name=st.text_input("Enter your name:")