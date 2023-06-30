import streamlit as st


st.title('User Data Collection Form')

# Part One: Text Elements:
##########################
st.write("#")

first_name = st.text_input(label='First Name')

### ADD A SECTION FOR LAST NAME HERE ###








# Part Two: Other types of inputs:
##########################
st.write("#")
st.write("#")
st.write("#")
st.write("#")

dob = st.date_input(label='Date of Birth')

### GO TO THE PAGE BELOW AND ADD TWO INPUT WIDGETS ###
# https://docs.streamlit.io/library/api-reference/widgets




# Part Three: If statements:
##########################
st.write("#")
st.write("#")
st.write("#")
st.write("#")

if st.checkbox(label='Check if you are a student'):

    year = st.selectbox(label='What year are you in?', options=['Freshman', 'Sophomore', 'Junior', 'Senior'])

st.write("#")
st.write("#")

genre = st.radio(
    "What is your major",
    ('STEM', 'ARTS/HUMANITIES', 'BUSINESS/FINANCE', 'OTHER'))

if genre == 'STEM':
    st.write('You selected STEM.')
else:
    st.write("You didn\'t select STEM.")


### ADD ANOTHER IF STATEMENT HERE USING AN INPUT WIDGET###



# Part Four: dataframes:
##########################
st.write("#")
st.write("#")
st.write("#")
st.write("#")

# Imports
import pandas as pd
import plotly.express as px

# This loads the dataframe
pokemon_df = pd.read_csv('https://raw.githubusercontent.com/ajaverett/data/main/poke.csv')
changed_df = pokemon_df.filter(['attack', 'defense'], axis=1)

# This displays a dataframe
st.write(  changed_df.head()  )

# This makes a scatterplot
fig = px.scatter(changed_df, x='attack', y='defense')

st.plotly_chart(fig, use_container_width=True)


### ADD A SECTION HERE TO DISPLAY A DATAFRAME AND A PLOT ###



# Part Five: Your own code:
##########################
st.write("#")
st.write("#")
st.write("#")
st.write("#")

st.write("### Add something from the website section ###")
# https://docs.streamlit.io/library/api-reference/
### ADD YOUR OWN CODE HERE ###
