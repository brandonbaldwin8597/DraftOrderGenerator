import streamlit as st
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

col1, col2 = st.columns(2)
with col1:
    for player in range(1, half + 1):
        name = st.text_input(f":green[Player {player}:]", placeholder=None, key=f'{player}')
        if name:
            
            my_dict.update({player: name.strip()})
        
with col2:
    for player in range(half + 1, members + 1):
        name = st.text_input(f":green[Player {player}:]", placeholder=None, key=f'{player}')
        my_dict.update({player: name.strip()})

print(my_dict.values())
button = False
for name in my_dict.values():
    if name == '':
        button = False
        break
    else:
        button = True

st.divider()

stack1, stack2, stack3 = st.columns(3)
with stack1:
    st.write("_All players must be filled in to randomize order_")
with stack2:
    if button == True:
        randomize = st.button("Randomize Order", use_container_width=True)
with stack3:
    if st.button("Clear"):
        st.badge("Cleared", icon=":material/check:", color="green")

if randomize:
    print(my_dict.keys())
#st.table()