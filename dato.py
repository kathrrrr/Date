class Date:
    def __init__(self,day,month,year) :
        self.day = day
        self.month = month
        self.year = year
    def setToNextDay(self) :
        self.day += 1
        self.checkForDayOverflow()
    
    def toString(self):

        return str(self.day)+"/"+str(self.month)+"-"+str(self.year)
    
    def checkForDayOverflow(self):
        if self.day > 30:
            self.day = 1
            self.month +=1
     
    


minDato = Date(31,12,2023)
minDato.setToNextDay()
print(minDato.toString())
minDato2 = Date(31,7,2023)
print(minDato2.toString())
minDato2.setToNextDay()
print(minDato2.toString())
    