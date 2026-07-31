# Importing the pandas library
import pandas as pd
# Importing the list of parsed_logs
from parser import parsed_logs

# Creating a Dataframe from the parsed logs
df = pd.DataFrame(parsed_logs)

# Function for extracting Top 5 IPs
def top_ips():
    # Counts occurrences of each IP and returns the top 5
    return df['ip'].value_counts().head(5)

# Function for extracting status code counts
def top_statusCode():
    # Counts occurrences of each status code
    return df['status_code'].value_counts()

# Function for analyzing errors
def error_analysis():
    # Boolean mask: True for rows where status_code is 400 or above (error range)
    error_codes = df['status_code'] >= 400

    # Count of each error status code (e.g. how many 404s, 500s, etc.)
    error_summary = df.loc[error_codes, 'status_code'].value_counts()

    # Top 5 IPs responsible for the most errors
    error_ip = df.loc[error_codes, 'ip'].value_counts().head(5)

    # Top 5 endpoints that produced the most errors
    error_endpoints = df.loc[error_codes, 'endpoint'].value_counts().head(5)

    # Return all three results together
    return error_summary, error_ip, error_endpoints