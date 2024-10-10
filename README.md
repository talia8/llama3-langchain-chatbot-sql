# llama3-langchain-chatbot-sql

<img src="Screenshot 2024-10-10 135816.png">

## Overview

**Data Chatbot** is an interactive chatbot application that enables users to engage in conversations with their data. By leveraging advanced language models, the chatbot can answer queries based on the relevant information retrieved from your databases. This project is built using Python and integrates with various data sources, allowing for a dynamic and informative user experience.

## Features

- **Natural Language Processing**: Understand and respond to user queries in natural language.
- **Database Integration**: Connect to SQL databases and retrieve relevant data to answer questions.
- **Conversation History**: Maintain the context of the conversation for better responses.
- **User-Friendly Interface**: A simple and intuitive interface built with Tkinter for seamless interaction.

## Technologies Used

- **Python**: The primary programming language for building the application.
- **LangChain**: A framework for building applications with LLMs (Language Model Models).
- **SQLAlchemy**: For database interactions.
- **Tkinter**: For the graphical user interface.
- **OllamaLLM**: A specific language model integration.

## Installation

To get started with the Data Chatbot, follow these steps:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/llama3-langchain-chatbot-sql.git
   ```

2. **Navigate to the project directory**:

   ```bash
   cd llama3-langchain-chatbot-sql
   ```

3. **Install the required dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

   Make sure you have [llama3](https://github.com/ollama/ollama) installed on your machine. 

## Usage

1. **Set Up the Database**:
   - Ensure you have a SQL database set up and accessible. Modify the database connection string in `chatbot.py` to point to your database.
   - Adjust the query as necessary to fit your data requirements.

2. **Run the Chatbot Application**:

   ```bash
   python main.py
   ```

3. **Interact with the Chatbot**:
   - Enter your questions in the input box and click "Send".
   - The chatbot will respond based on the conversation context and the relevant data retrieved from your database.

## Contributing

Contributions are welcome! Feel free to submit a pull request or report issues to improve the functionality or performance of the project.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
