''''''
'''
open cmd:-- pip install streamlit
open pycharm :- python packages :-search for (streamlit)--->> install
TO RUN THE STREAMLIT 
----------------------
to change the directory :-- cd folder_name
to go back : cd..
streamlit run file_name.py
'''



# import streamlit as st
# st.title('WELCOME TO THE NUMBER PROGRAMS')
# st.header('I AM A HEADER')
# st.subheader('I AM A SUB HEADER')
# name=st.text_input('NAME')
# phno=st.number_input('PHNO',min_value=0)
# submit=st.button('SUBMIT')
# if submit:
#     st.write(f'hey {name} your phno is:{phno}')
#     st.success(f'hey {name} your phno is:{phno}')
#     st.warning(f'hey {name} your phno is:{phno}')
#     st.error(f'hey {name} your phno is:{phno}')

import streamlit as st
st.title('NUMBER PROGRAMS')
# st.image('python.jpg')
# st.video('https://youtu.be/-pvt6tQsOqQ?si=xWNTaqoEzs9lCYK-')
no=st.number_input('ENTER THE NUMBER:',min_value=0)
factorial =st.button('FACTORIAL OF A NUMBER',type='primary')
prime=st.button('PRIME NUMBER',type='primary')
strong=st.button('STRONG NUMBER',type='primary')
if factorial:
    temp=no
    fact=1
    while no >0:
        fact=fact*no
        no=no-1
    st.success(f'FACTORIAL OF {temp} is {fact}')
elif prime:
    for i in range(2,no):
        if no%i==0:
                st.error(f'{no} is not a prime number')
                break
    else:
        st.success(f'{no} is  a prime number')
        st.balloons()
elif strong:
    temp = no
    sum=0
    while no>0:
        fact = 1
        r=no%10
        while r>0:
            fact=fact*r
            r=r-1
        sum=sum+fact
        print(fact)
        no=no//10
    if temp==sum:
        st.success('strong number')
        st.balloons()
    else:
        st.error('not a strong number')




