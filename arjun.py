import pandas as pd

with open("sample_logs/access.log","r") as file:
  logs = file.readlines()


for index, log in enumerate(logs):
        parts = logs[index].split()
       
        data = {}
        data["ip"] = parts[0]
        print(data)
        
        
       
      

        
    

