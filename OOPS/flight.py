#Write a Java program to create a class called "Airplane" with a flight number, destination, 
# and departure time attributes, and methods to check flight status and delay.
from datetime import datetime,timedelta
class AirPlane:
    def __init__(self,flightNumber,destination,scheduledDeparture):
        self.flightNumber=flightNumber
        self.destination=destination
        self.scheduledDeparture=scheduledDeparture
        self.delayTime=0
    def getFlightNumber(self):
        return self.flightNumber
    def setFlightNumber(self,flightNumber):
        self.flightNumber=flightNumber
    def destination(self,destination):
        self.destination=destination
    def getDeparture(self):
        return self.scheduledDeparture
    def setDeparture(self,scheduledDeparture):
        self.scheduledDeparture=scheduledDeparture
    def getDelayTime(self):
        return self.delayTime
    def delay(self,minutes):
        self.delayTime=minutes
        self.scheduledDeparture=self.scheduledDeparture+timedelta(minutes=self.getDelayTime)
    def status(self):
        if(self.delayTime==0):
            print(f"Flight {self.flightNumber} is on time")
        else:
            print(f"Flight {self.flightNumber} is delayed by {self.delayTime} minutes")
     
    
#still dont understand this , lets paste this on gpt and ask a review
# now i'll translate the java code into python , just for fun


