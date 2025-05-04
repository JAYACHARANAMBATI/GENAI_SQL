# Natural Language to SQL Query App

This project enables users to interact with a MySQL database using natural language questions. It leverages [LangChain](https://github.com/langchain-ai/langchain), Google's Gemini LLM, and Streamlit to generate and execute SQL queries from user input.



https://github.com/user-attachments/assets/9f2281cb-dea1-4d53-9d45-530921b9ee6c



## Features

- **Ask questions in plain English** and get SQL queries generated automatically.
- **Execute queries** and view results directly in the web interface.
- **Database selection**: Choose which MySQL database to connect to (see `data.py`).
- **Jupyter notebook** for experimentation and testing (`db.ipynb`).

## Tech Stack

- [Python 3.10+](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [LangChain](https://python.langchain.com/)
- [Google Generative AI (Gemini)](https://ai.google.dev/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [PyMySQL](https://pymysql.readthedocs.io/)
- [dotenv](https://pypi.org/project/python-dotenv/)

## Setup

1. **Clone the repository**

    ```sh
    git clone <your-repo-url>
    cd <your-repo-directory>
    ```

2. **Install dependencies**

    ```sh
    pip install -r requirements.txt
    ```

3. **Set up environment variables**

    Create a `.env` file in the project root with your Google API key:

    ```
    GOOGLE_API_KEY=your_google_api_key_here
    ```

4. **Configure your MySQL database**

    - Ensure MySQL is running and accessible.
    - Update database credentials in `app.py` and `data.py` if needed.

5. **Run the Streamlit app**

    ```sh
    streamlit run app.py
    ```

    Or, for the database selection interface:

    ```sh
    streamlit run data.py
    ```

6. **(Optional) Use the Jupyter notebook**

    Open `db.ipynb` in Jupyter for interactive testing.

## Usage

- Open the Streamlit app in your browser.
- Enter your natural language question (e.g., "How many customers are there?").
- View the generated SQL query and the results.

## Example Questions

- "How many unique customers are there for each product category?"
- "Calculate total sales amount per product category."
- "Identify the top spending customers based on their total amount spent."


