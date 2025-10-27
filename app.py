import streamlit as st
import pandas as pd
import functions


## TITLE
st.title(":blue[Draft Order Maker]")
st.divider()


## SIDEBAR
st.sidebar.title("League Settings")
st.sidebar.divider()
st.sidebar.subheader("Fill out form")
members = st.sidebar.pills("Number of League Members:",("8", "10", "12"), selection_mode="single", default="8")
draft_type = st.sidebar.radio("Pick a draft style:", ("Snake", "Linear"))


## BODY
st.subheader("Choose the number of participants and enter their names")
if not members:
    members = "8"

members = int(members)
half = int(members / 2)
my_dict = {}

# Making symmetrical player slots
col1, col2 = st.columns(2)
with col1:
    for player in range(1, half + 1):
        name = st.text_input(f"Player {player}", placeholder=None, key=f'{player}')
        if name:
            
            my_dict.update({player: name.strip()})
        
with col2:
    for player in range(half + 1, members + 1):
        name = st.text_input(f"Player {player}", placeholder=None, key=f'{player}')
        my_dict.update({player: name.strip()})

# Button condition
button = False
for name in my_dict.values():
    if name == '':
        button = False
        break
    else:
        button = True

st.divider()

# Instructions and Submit/Clear buttons
stack1, stack2, stack3 = st.columns(3)
with stack1:
    if button == False:
        st.write("\*\*\*All player slots must be filled in to create a randomized order")
    else:
        st.write(":green[READY TO CREATE DRAFT ORDER]")
    
with stack2:
    if button == True:
        randomize = st.button("Randomize Order", use_container_width=True, type="primary")
        if randomize:
            new_dict = functions.assign_draft_nums(list(my_dict.values()))
            print(new_dict)
            df = pd.DataFrame.from_dict([my_dict])
            st.table(df)
            
with stack3:
    if st.button("Clear", on_click=functions.clear_players(members)):
        st.badge("Cleared", icon=":material/check:", color="green")

#st.table()