import streamlit as st
import pandas as pd
import plotly.express as px
import ast
from textblob import TextBlob
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import spacy
from spacy import displacy


st.write("---")
st.title("Section 1: Text Elements")
st.code("""
# streamlit text elements code
    st.header(":red[Text Elements]")
    st.subheader("Text Elements :sunglasses:")
    st.write("Here are some text elements. You can use these to write text to your app.")
    st.text("Text can also be in different formats.")
    st.latex("e=mc^2")
    st.code("Code can be displayed as well.")""")
st.write("---")

st.header(":red[Text Elements]")
st.subheader("Text Elements :sunglasses:")
st.write("Here are some text elements. You can use these to write text to your app.")
st.text("Text can also be in different formats.")
st.latex("e=mc^2")
st.code("Code can be displayed as well.")

### PART ONE PLAYGROUND












###

st.write("---")
st.title("Section 2a: Input Widgets")

st.write("Checkboxes and other input widgets can be used for user input. They can be assigned to variables/represent boolean values which can be used to trigger events in your app. Below they are useless since they are not assigned to variables nor used as boolean values.")

st.code("""
# streamlit widgets code
    st.checkbox("I am a checkbox")
""")
st.write("---")
st.checkbox("I am a checkbox")
st.write("---")

st.title("Section 2b: Input Widgets as conditional triggers")
st.write("Checkboxes and other input widgets can be used for user input. They can be assigned to variables/represent boolean values which can be used to trigger events in your app.")

st.code("""
# streamlit conditional widgit code
    if st.checkbox("Checkbox as a conditional trigger"):
        st.write("Checkbox was clicked")
""")
st.write("---")
if st.checkbox("Checkbox as a conditional trigger"):
    st.write("Checkbox was clicked")
st.write("---")

st.title("Section 2c: Input Widgets as variables")
st.write("Checkboxes and other input widgets can be used to store variables.")

st.code("""
# streamlit variable/functional widgit code
    your_input = st.text_input("This data will be stored in a variable")
    st.write("The data you entered is: ", your_input)
""")
st.write("---")
your_input = st.text_input("This data will be stored in a variable")
st.write("The data you entered is: ", your_input)
st.write("---")


st.title("Section 2c: Input Widgets as variables")
st.write("Checkboxes and other input widgets can be used to store variables (or run functions).")

st.code("""
# streamlit widgets code

    if st.button("Click for a surprise"):
        st.balloons()

    st.write(":red[**Text input**]")
    text = st.text_input('Enter some text')
    st.write('You entered: ', text)

    options = ['A', 'B', 'C', 'D', 'E', 'F']

    st.write(":red[**Single radio select input**]")
    radio = st.radio('Choose an option', options)
    st.write('You selected: ', radio)

    st.write(":red[**Multi select input**]")
    multiselect = st.multiselect('Select multiple options', options)
    st.write('You selected: ', multiselect)
""")
st.write("---")

st.write(":red[**Text input**]")
text = st.text_input('Enter some text')
st.write('You entered: ', text)

options = ['A', 'B', 'C', 'D', 'E', 'F']

st.write(":red[**Single radio select input**]")
radio = st.radio('Choose an option', options)
st.write('You selected: ', radio)

st.write(":red[**Multi select input**]")
multiselect = st.multiselect('Select multiple options', options)
st.write('You selected: ', multiselect)
st.write("---")


### PART TWO PLAYGROUND





###

st.title("Section 3: Visualizing Data and Dataframes")
st.code("""
    # streamlit data and data viz code
    # Load in and clean data
    pokemon_df = pd.read_csv('https://raw.githubusercontent.com/ajaverett/data/main/poke.csv')
    pokemon_df['types'] = pokemon_df['types'].apply(ast.literal_eval)
    all_types = list(set([x for t in pokemon_df['types'] for x in t]))
    st.title('Pokémon Data Explorer')

    # User chooses Pokémon type
    selected_type = st.multiselect('Select a Pokémon Type', all_types)
    filtered_df = pokemon_df[pokemon_df['types'].apply(lambda x: all(t in x for t in selected_type))]

    # Display Pokémon stats
    st.dataframe(filtered_df[['name','types','attack','defense','height_m','weight_kg']])

    # Attack vs. Defense Scatter Plot
    st.header('Attack vs. Defense Scatter Plot')
    fig1 = (px.scatter(filtered_df, 
                    x="attack", 
                    y='defense', 
                    opacity=0.8, 
                    color='speed',
                    hover_data=['name'], 
                    trendline='ols')
            .update_traces(marker_size=12, 
                        marker_line_width=2, 
                        marker_line_color='black'))

    st.plotly_chart(fig1, use_container_width=True)

    # Height vs. Weight Scatter Plot
    st.header('Height vs. Weight Scatter Plot')

    fig2 = (px.scatter(filtered_df, 
                    x="height_m", 
                    y='weight_kg',
                    opacity=0.8, 
                    color='hp',
                    hover_data=['name'], 
                    log_x=True, 
                    log_y=True, 
                    trendline="ols", 
                    trendline_options=dict(log_x=True, log_y=True))
            .update_traces(marker_size=12, 
                        marker_line_width=2, 
                        marker_line_color='black')
    )

    st.plotly_chart(fig2, use_container_width=True)
""")
st.write("---")

# Load in and clean data
pokemon_df = pd.read_csv('https://raw.githubusercontent.com/ajaverett/data/main/poke.csv')
pokemon_df['types'] = pokemon_df['types'].apply(ast.literal_eval)
all_types = list(set([x for t in pokemon_df['types'] for x in t]))
st.title('Pokémon Data Explorer')

# User chooses Pokémon type
selected_type = st.multiselect('Select a Pokémon Type', all_types)
filtered_df = pokemon_df[pokemon_df['types'].apply(lambda x: all(t in x for t in selected_type))]

# Display Pokémon stats
st.dataframe(filtered_df[['name','types','attack','defense','height_m','weight_kg']])

# Attack vs. Defense Scatter Plot
st.header('Attack vs. Defense Scatter Plot')
fig1 = (px.scatter(filtered_df, 
                   x="attack", 
                   y='defense', 
                   opacity=0.8, 
                   color='speed',
                   hover_data=['name'], 
                   trendline='ols')
        .update_traces(marker_size=12, 
                       marker_line_width=2, 
                       marker_line_color='black'))

st.plotly_chart(fig1, use_container_width=True)

# Height vs. Weight Scatter Plot
st.header('Height vs. Weight Scatter Plot')

fig2 = (px.scatter(filtered_df, 
                   x="height_m", 
                   y='weight_kg',
                   opacity=0.8, 
                   color='hp',
                   hover_data=['name'], 
                   log_x=True, 
                   log_y=True, 
                   trendline="ols", 
                   trendline_options=dict(log_x=True, log_y=True))
        .update_traces(marker_size=12, 
                       marker_line_width=2, 
                       marker_line_color='black')
)

st.plotly_chart(fig2, use_container_width=True)


### PART THREE PLAYGROUND




###

st.write("---")
st.title("Section 4: Others")
st.code("""
# streamlit fun elements code
    # Sentiment Analysis
    st.subheader(':red[Example of some quick NLP]')
    user_text = st.text_area("Enter Semtiment Text Here")

    blob = TextBlob(user_text)
    result = blob.sentiment

    st.write("Sentiment polarity: ", round(result.polarity, 3))
    st.write("Sentiment subjectivity: ", round(result.subjectivity, 3))

    # Phase similiarity
    st.subheader(':red[Example of two columns and using other libraries]')

    a1, a2 = st.columns(2)

    with a1:
        user_text1 = st.text_area("Cosine Similarity between two texts")

    with a2:
        user_text2 = st.text_area("")


    if user_text1 != "" and user_text2 != "":
        try:
            vectorizer = TfidfVectorizer().fit_transform([user_text1, user_text2])
            st.write("Cosine similarity: ", round(cosine_similarity(vectorizer)[0,1], 2))
        except Exception as e:
            st.write("Error: ", str(e))
    else:
        st.write("Enter two texts to compare")
    """)

st.write("---")

# Sentiment Analysis
st.subheader(':red[Example of some quick NLP]')
user_text = st.text_area("Enter Semtiment Text Here")

blob = TextBlob(user_text)
result = blob.sentiment

st.write("Sentiment polarity: ", round(result.polarity, 3))
st.write("Sentiment subjectivity: ", round(result.subjectivity, 3))


# Phase similiarity
st.subheader(':red[Example of two columns and using other libraries]')

a1, a2 = st.columns(2)

with a1:
    user_text1 = st.text_area("Cosine Similarity between two texts")

with a2:
    user_text2 = st.text_area("")


if user_text1 != "" and user_text2 != "":
    try:
        vectorizer = TfidfVectorizer().fit_transform([user_text1, user_text2])
        st.write("Cosine similarity: ", round(cosine_similarity(vectorizer)[0,1], 2))
    except Exception as e:
        st.write("Error: ", str(e))
else:
    st.write("Enter two texts to compare")
    


### PART FOUR PLAYGROUND


###

st.write("\n\n\n")
st.write("\n\n\n")
st.write("\n\n\n")
st.write("\n\n\n")
st.write("\n\n\n")
st.write("\n\n\n")
st.write("\n\n\n")
st.write("\n\n\n")
st.write("\n\n\n")
st.write("\n\n\n")
st.write("\n\n\n")
st.write("\n\n\n")
st.write("\n\n\n")
st.write("\n\n\n")
st.write(":red[**Yay!**]")
if st.button("Click for a surprise"):
    st.balloons()
    st.write("You did it!")
    