import os
from dotenv import load_dotenv
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.utilities import SQLDatabase
from langchain.chains import create_sql_query_chain
from pymysql import connect
from pymysql.err import ProgrammingError, OperationalError

# Load environment variables
load_dotenv()

# Database connection info
db_user = "root"
db_password = "Charan5507"
db_host = "localhost"

# Function to list databases
def list_databases():
    conn = connect(user=db_user, password=db_password, host=db_host)
    cursor = conn.cursor()
    cursor.execute("SHOW DATABASES")
    databases = [row[0] for row in cursor.fetchall() if row[0] not in ("information_schema", "mysql", "performance_schema", "sys")]
    conn.close()
    return databases

# UI: Database selection
st.title("🗃️ Select a Database")

databases = list_databases()
selected_db = st.selectbox("Choose a database to connect", databases)

# Proceed only if a database is selected
if selected_db:
    st.markdown("---")
    st.title("🧠 Natural Language to SQL Query App")
    st.write(f"Connected to **{selected_db}**. Ask your question:")

    # Initialize LLM
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-pro",
        google_api_key=os.environ["GOOGLE_API_KEY"]
    )

    try:
        db = SQLDatabase.from_uri(f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{selected_db}", sample_rows_in_table_info=3)
        chain = create_sql_query_chain(llm, db)

        user_question = st.text_input("Enter your question:")

        if st.button("Submit"):
            if user_question:
                with st.spinner("Thinking..."):
                    try:
                        response = chain.invoke({"question": user_question})
                        cleaned_query = response.strip('```sql\n').strip('\n```')
                        result = db.run(cleaned_query)
                        st.subheader("📝 Generated SQL Query:")
                        st.code(cleaned_query, language="sql")
                        st.subheader("📊 Query Result:")
                        st.write(result)
                    except ProgrammingError as e:
                        st.error(f"SQL Error: {e}")
            else:
                st.warning("Please enter a question.")
    except OperationalError as e:
        st.error(f"Database connection error: {e}")
