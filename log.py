import os
from dotenv import load_dotenv
from datetime import datetime
load_dotenv()
class Log():
    os.chdir(r'C:\\Users\\Chani\\Desktop\\bootcamp')
    file = open('car_log.txt', 'a')

    def  __init__(self):
        self.path=os.getenv('PATH')
        self.log_file=os.getenv('LOG_FILE')
    
    def writeLog(self,message):
        self.file.write(f"{datetime.now()} - {message}\n")


     
    
