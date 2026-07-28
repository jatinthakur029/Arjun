# Importing the pandas library
import pandas as pd
# Importing the list of parsed_logs
from parser import parsed_logs
# Creating a Dataframe 
df = pd.DataFrame(parsed_logs)
print(df)
# Function for extracting Top 5 IPs
def top_ips():
    highest_IPs = df['ip'].value_counts().nlargest(5)
    print(highest_IPs)
# Calling the ip function
top_ips()
# Function for extracting Top 5 status codes
def top_statusCode ():
    highest_sCode = df['status_code'].value_counts().nlargest(5)
    print(highest_sCode) 
# Calling the status code function
top_statusCode()   