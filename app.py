import streamlit as st
from model import SimpleSmartContractGenerator
import os

# Set the page configuration
st.set_page_config(
    page_title="Smart Contract Generator",
    page_icon="⚖️",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Add a custom CSS to style the app
st.markdown(
    """
    <style>
    .main {
        background-color: #f5f5f5;
        color: #333333;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 10px 24px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        transition-duration: 0.4s;
        cursor: pointer;
    }
    .stButton>button:hover {
        background-color: white;
        color: black;
        border: 2px solid #4CAF50;
    }
    .stTextInput>div>div>input {
        padding: 10px;
    }
    .stTextArea>div>div>textarea {
        padding: 10px;
    }
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        padding-left: 2rem;
        padding-right: 2rem;
    }
    h1, h3 {
        color: #333333;
        font-size: 2.5rem;
        font-weight: bold;
        text-align: center;
        margin-bottom: 2rem;
    }
    h3 {
        font-size: 1.5rem;
    }
    .examples {
        color: #555555;
        font-size: 1rem;
        margin-top: -1rem;
        margin-bottom: 2rem;
        text-align: center;
    }
    .examples-title {
        color: #333333;
        font-size: 1.5rem;
        font-weight: bold;
        text-align: center;
        margin-bottom: 1rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title and description
st.title('⚖️ Simple Smart Contract Generator')
st.write("Welcome to the Smart Contract Generator! Describe your smart contract in plain English, and we'll generate the Solidity code for you.")

# Add examples
st.markdown(
    """
    <div class="examples-title">EXAMPLES TO TYPE</div>
    <div class="examples">
        <ul>
            <li>"Create a token contract with a name 'TestToken' and symbol 'TT'."</li>
            <li>"Generate a crowdsale contract with a rate of 500 tokens per ether."</li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True,
)

# Use columns for layout
col1, col2 = st.columns([2, 1])

with col1:
    description = st.text_area('Describe your smart contract in plain English', height=200)

# Check if image exists and display it
image_path = "/mnt/data/image.png"
if os.path.exists(image_path):
    with col2:
        st.image(image_path, use_column_width=True)  # Display uploaded image

# Generate button
if st.button('Generate Smart Contract'):
    if description:
        generator = SimpleSmartContractGenerator()
        contract_code = generator.generate_contract(description)
        st.write('### Generated Smart Contract Code:')
        st.code(contract_code, language='solidity')
    else:
        st.error('Please enter a description of the smart contract.')
