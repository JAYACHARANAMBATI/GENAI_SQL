import os
from dotenv import load_dotenv
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.utilities import SQLDatabase
from langchain.chains import create_sql_query_chain
from pymysql.err import ProgrammingError

# Load environment variables
load_dotenv()

# Initialize the LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",
    google_api_key=os.environ["GOOGLE_API_KEY"]
)

# Connect to SQL database
db_user = "root"
db_password = "Charan5507"
db_host = "localhost"
db_name = "retail_sales_db"

db = SQLDatabase.from_uri(f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}", sample_rows_in_table_info=3)

# Create the SQL query chain
chain = create_sql_query_chain(llm, db)

# Define function to handle user query
def execute_query(question):
    try:
        # Generate SQL from the question
        response = chain.invoke({"question": question})
        cleaned_query = response.strip('```sql\n').strip('\n```')
        result = db.run(cleaned_query)
        return cleaned_query, result
    except ProgrammingError as e:
        return None, f"An error occurred: {e}"

# Streamlit UI
st.title("🧠 Natural Language to SQL Query App")
st.write("Ask your question about the database using natural language:")

user_question = st.text_input("Enter your question:")

if st.button("Submit"):
    if user_question:
        with st.spinner("Thinking..."):
            sql_query, result = execute_query(user_question)
            if sql_query:
                st.subheader("📝 Generated SQL Query:")
                st.code(sql_query, language="sql")
                st.subheader("📊 Query Result:")
                st.write(result)
            else:
                st.error(result)
    else:
        st.warning("Please enter a question.")
