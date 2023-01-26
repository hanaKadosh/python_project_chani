import os
from dotenv import load_dotenv
from log import Log as l
from datetime import datetime
from messages import m
load_dotenv()
class Car():
    log=l()
    mass=m()
    def __init__(self):
        self.liter=int(os.getenv('LITER'))
        self.liter_per_km=int(os.getenv('LITER_PER_KM'))
        self.geur=int(os.getenv('GRUE'))
        self.km=int(os.getenv('KM'))
        self.money=int(os.getenv('MONEY'))
        self.status=bool(os.getenv('STATUS'))
        self.dif=int(os.getenv('DIF'))      
        self.speed = 0
       
    def drive(self,km):
        '''
        name:chani
        date:22/01
        The function drives the car
        :return:
        '''
        try:
            if self.liter==0:
                raise Exception(self.mass.error_messages['error_code_1'])
            elif self.status==True:
                raise Exception(self.mass.error_messages['error_code_1'])
            elif km//self.liter_per_km>self.liter:
                raise Exception(self.mass.error_messages['error_code_2'])
            elif self.geur != 0:
                raise Exception(self.mass.error_messages['error_code_3'])
            else:  
                self.geur= km//self.dif
                self.speed=km
                self.liter-=km//self.liter_per_km
                self.status=True
                self.log.writeLog(self.mass.error_messages['error_code_4'])
        except:
               self.log.writeLog(self.mass.error_messages['error_code_5'])

    def fuel_up(self,how_much_refuel):
        '''
        name:chani
        date:22/01
        The refueling function
        :return:
        '''
        try:
            if how_much_refuel*10>self.money:  
                raise ValueError(self.mass.error_messages['error_code_6'])
            elif self.liter+how_much_refuel>=80:
                 raise ValueError(self.mass.error_messages['error_code_6'])
            elif how_much_refuel<0: 
                 raise ValueError(self.mass.error_messages['error_code_6'])
            else:
                self.liter+=how_much_refuel
                self.money-=how_much_refuel*10
                self.log.writeLog(f"Refueled {self.money} liters, current fuel level is {how_much_refuel} liters.{datetime.now()}\n")
                return True
               
        except ValueError as e:
            self.log.writeLog(f' - {e}')
            raise

    def shiftUp(self,speed):
        '''
        name:chani
        date:22/01
        The function raises a gear
        :return:
        '''
        try:    
            if speed%self.dif==0 and self.geur+(speed//self.dif)!=6:
                self.geur+=speed//self.dif
                
            elif self.geur==6:
                raise Exception(self.mass.error_messages['error_code_8'])
            else:
                self.geur+=speed//self.dif+1
                str=f"Accelerated by {self.geur*30} to {speed} km/h\n"
                self.speed+=speed
                self.log.writeLog(str)
        except ValueError as e:
            self.log.writeLog(f'- {e}')
            raise

    def shiftDown(self,speed):
        '''
        name:chani
        date:22/01
        The function downshifts
        :return:
        '''
        try:
            if speed % self.dif == 0 and self.geur-(speed//self.dif)!=0:
                self.geur-=speed//self.dif
            elif self.status==False:
                raise Exception(self.mass.error_messages['error_code_7'])
            else:
                self.geur-=(speed//self.dif)+1
                return True
        except ValueError as e:
            self.log.writeLog(f'- {e}')
            raise
        
    #  stop
    def stop(self):
        '''
        name:chani
        date:22/01
        The function stops the car
        :return:
        '''
        try:
            if not self.status:
                raise Exception("Car is already stopped.")
            else:
                self.geur=0
                self.km=0
                self.status=False
                self.log.writeLog("Car stopped.\n")
                return True
        except ValueError as e:
            self.log.writeLog(f'- {e}')
            raise

    # def getCurrentliter(self):
    #     return self.liter,self.money
    # def getG(self):
    #     pass