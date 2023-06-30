import streamlit as st
import random
from streamlit_extras.let_it_rain import rain
import os

current_file_path = os.path.realpath(__file__)

current_directory = os.path.dirname(current_file_path)

os.chdir(current_directory)

# Define the options
options = ['rock', 'paper', 'scissors']

st.title('Rock Paper Scissors Game')


# Check if game has been started by looking for 'Start' button press
if st.button('Start Game'):
    st.session_state.game_started = True

    st.session_state.user_choice = None
    
    st.session_state.comp_choice = None
    
    st.session_state.result = None

if 'game_started' in st.session_state and st.session_state.game_started:

    # Use radio buttons for the options with corresponding images
    user_choice = st.radio(
        "Choose your move",
        options
    )

    # Display the user's choice as an image with width 100px
    st.image(user_choice + '.png', width=100)

    if st.button('Shoot!'):
        print('Shoot!')
    

        # Once the user has made a choice, play the game
        if user_choice in options:

            # Computer choice
            comp_choice = random.choice(options)
            
            st.session_state.comp_choice = comp_choice

            # Show computer's choice
            st.write('Computer choice:')
            
            # Display the computer's choice as an image with width 100px
            st.image(comp_choice + '.png', width=100)

            # Determine the winner
            if user_choice == comp_choice:
            
                st.session_state.result = 'It is a tie.'
            
            elif (user_choice == 'rock' and comp_choice == 'scissors') or (user_choice == 'scissors' and 
                                                                           comp_choice == 'paper') or (user_choice == 'paper' and comp_choice == 'rock'):
                st.session_state.result = 'You win!'
                rain(
                    emoji="🏆",
                    font_size=54,
                    falling_speed=5,
                    animation_length="5s",
                )

            else:
                st.session_state.result = 'You lose!'
                rain(
                    emoji="😔",
                    font_size=54,
                    falling_speed=5,
                    animation_length="5s",
                )


            st.write(st.session_state.result)

        if st.button('Reset Game'):
       
            st.session_state.game_started = False
