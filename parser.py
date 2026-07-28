#Opening the access.log file in read mode to read the logs
with open("sample_logs/access.log","r") as file:
  logs = file.readlines()
  
def data_parser():
 #Running a loop for scanning each log in the file
 parsed_logs = []
 for  log in logs:
        if log.strip() == "":
         continue
        parts = log.split()
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
        data['status_code'] = int (parts[8])
        #For parsing Bytes
        data['bytes'] = int(parts[9])
        parsed_logs.append(data)
 return parsed_logs                                                                                                                 
       
#Calling the function
parsed_logs = data_parser()

          
        
        
       
      

        
    

