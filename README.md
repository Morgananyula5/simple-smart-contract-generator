# NL-Smart-Contract-Generator: Empowering Smart Contract Creation Through Natural Language

### Deployed on Streamlit: [NL-Smart-Contract-Generator](https://simple-smart-contract-generator-morgancloudd.streamlit.app/)

## Overview

The **NL-Smart-Contract-Generator** is a groundbreaking tool designed to simplify the creation of smart contracts using natural language inputs. This tool allows users, regardless of their programming expertise, to generate complex smart contract codes by simply describing their requirements in plain English. By leveraging advanced AI technology and the power of Google Cloud Platform (GCP), the NL-Smart-Contract-Generator democratizes access to blockchain technology and smart contract development.

## Problem Statement

Creating smart contracts typically requires a deep understanding of programming languages such as Solidity, which can be a significant barrier for non-technical users. This complexity hinders widespread adoption and innovation within the blockchain space. The NL-Smart-Contract-Generator addresses this issue by providing an intuitive interface where users can input their contract requirements in natural language, making smart contract development accessible to a broader audience.

## How It Works

### AI Integration

The tool uses a sophisticated natural language processing (NLP) model to interpret user inputs and convert them into smart contract code. The model is based on open-source AI technologies and has been fine-tuned to understand and generate smart contract code effectively. The language libraries have been inspired by Google Cloud Platform (GCP) services.

### Technical Details

1. **User Input**: The user provides a description of the desired smart contract in natural language through the Streamlit-based web interface.
2. **NLP Model**: The input is processed by an NLP model, which translates the natural language description into smart contract code. The model leverages the `transformers` library from Hugging Face and GCP's natural language API for enhanced understanding and accuracy.
3. **Code Generation**: The generated code is displayed to the user, who can then copy and paste the code for deployment or further modification.

### GCP Integration

The NL-Smart-Contract-Generator integrates several features from GCP, including:

- **GCP Natural Language API**: For parsing and understanding the natural language inputs.
- **GCP Compute Engine**: To handle the computational requirements of the NLP model.
- **GCP Cloud Storage**: For storing and managing model data and user inputs securely.

## Setup and Usage Instructions

### Prerequisites

- Python 3.8 or higher
- Streamlit
- Hugging Face Transformers library
- Google Cloud SDK

### Installation Steps

1. **Clone the Repository**

   ```sh
   git clone https://github.com/your-username/nl-smart-contract-generator.git
   cd nl-smart-contract-generator
   ```

2. **Set Up Virtual Environment**

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**

   ```sh
   pip install -r requirements.txt
   ```

4. **Set Up GCP**

   Ensure you have the Google Cloud SDK installed and authenticated. Set up the necessary GCP services (Natural Language API, Compute Engine, Cloud Storage) as per your project requirements.

5. **Run the Application**

   ```sh
   streamlit run app.py
   ```

### Using the Tool

1. **Access the Web Interface**

   Open your web browser and navigate to `http://localhost:8501` to access the Streamlit interface.

2. **Input Contract Description**

   Enter the description of your smart contract in natural language. You can copy and paste examples provided on the user interface to see how different inputs generate different contract codes.

3. **Generate and Copy Code**

   Click the "Generate" button. The smart contract code will be displayed below the input box. Copy the generated code for deployment or further customization.

## Conclusion

The NL-Smart-Contract-Generator is a powerful tool that leverages AI and GCP to make smart contract development accessible to everyone. By simplifying the process and reducing the technical barriers, this tool empowers users to innovate and create in the blockchain space without needing to master complex programming languages.

**Open-Source Libraries, Frameworks, and Programming Languages Used:**

- Python
- Streamlit
- Hugging Face Transformers
- Google Cloud Platform SDK

This prototype tool incorporates AI technology to interpret natural language inputs and integrates multiple features of GCP, showcasing the potential of combining AI with cloud services to solve real-world problems.

---
