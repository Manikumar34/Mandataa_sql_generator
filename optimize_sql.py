
import re

def optimize_sql(sql_query):
    # Use DATE_TRUNC('YEAR', DATE) instead of STRFTIME('%Y', DATE)
    optimized_query = re.sub(r'STRFTIME\("%Y",\s*(\w+)\.(\w+)\)', r'DATE_TRUNC(\'YEAR\', \1.\2)', sql_query)
    
    # Ensure consistent use of column names and aliases
    optimized_query = re.sub(r'AS\s+\w+', lambda m: m.group().upper(), optimized_query)
    
    # Remove redundant ORDER BY clauses
    if 'ORDER BY' in optimized_query:
        optimized_query = re.sub(r'ORDER BY\s+\w+\s*(ASC|DESC)?', '', optimized_query)
    
    # Remove redundant LIMIT and OFFSET clauses
    if 'LIMIT' in optimized_query and 'OFFSET' in optimized_query:
        optimized_query = re.sub(r'LIMIT\s+\d+\s+OFFSET\s+\d+', '', optimized_query)
    
    # Add ORDER BY clause to sort the results by year if it is not already present
    if 'GROUP BY' in optimized_query and 'ORDER BY' not in optimized_query:
        match = re.search(r'(\w+)\.(\w+)', optimized_query)
        if match:
            table_alias, column_name = match.groups()
            optimized_query += f"\nORDER BY {table_alias}.{column_name}"
    
    return optimized_query
