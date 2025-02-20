# app.py
import streamlit as st
from query_cache import store_query, retrieve_query
from text_to_sql import generate_sql
from optimize_sql import optimize_sql

# Streamlit UI Title
st.title("AI-Powered Text-to-SQL Generator 🚀")

# Section 1: Generate SQL Query
st.header("Generate SQL Query")

# User Input for Natural Language Query
nl_query = st.text_input("Enter your natural language query:")

# Generate SQL Query
if st.button("Generate SQL"):
    if nl_query:
        # Check cache first
        cached_query = retrieve_query(nl_query)
        if cached_query:
            generated_query = cached_query
        else:
            # Generate SQL query using the LLM without schema information
            generated_query = generate_sql(nl_query, schema_info={})
            if generated_query:
                store_query(nl_query, generated_query)
        
        if generated_query:
            st.subheader("Generated SQL Query:")
            st.code(generated_query, language="sql")
        else:
            st.error("Failed to generate SQL query.")
    else:
        st.warning("Please enter a natural language query.")

# Section 2: Optimize SQL Query
st.header("Optimize SQL Query")

# User Input for SQL Query
sql_query = st.text_area("Enter your SQL query:")

# Optimize SQL Query
if st.button("Optimize SQL"):
    if sql_query:
        # Optimize the provided SQL query
        optimized_query = optimize_sql(sql_query)
        st.subheader("Optimized SQL Query:")
        st.code(optimized_query, language="sql")
    else:
        st.warning("Please enter an SQL query.")