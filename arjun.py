import pandas as pd
#Opening the access.log file in read mode to read the logs
with open("sample_logs/access.log","r") as file:
  logs = file.readlines()
  
def data_parser():
 #Running a loop for scanning each log in the file
 for index, log in enumerate(logs):
        parts = logs[index].split()
        data = {}
        # For parsing IPs
        data['ip'] = parts[0]
        # For parsing timestamp
        data['timestamp'] = parts[3][1:] + " " + parts[4][:5]
        #For parsing Methods
        data['method'] = parts[5][1:]
        #For parsing Endpoint
        data['endpoint'] = parts[6] 
        #For parsing protocol
        data['protocol'] = parts[7][:8]
        #For parsing Statuscode
        data['status_code'] = parts[8]
        #For parsing Bytes
        data['bytes'] = parts[9]
        # Printing the dictionary
        print(data)
                                                                                                                  
       
#Calling the function
data_parser()
          
        
        
       
      

        
    

