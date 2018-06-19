#gamer:bit Code set up for easy use
#Based on https://github.com/MrYsLab/gamerbit - I just added an easy way for kids to add functions.
#06/19/18 Kris Swanson, Young Makers Lab


from microbit import *
class GamerBit:
 def __init__(self,callback,scans=1):
  self.pins=[pin0,pin1,pin2,pin8,pin12,pin16,button_a,button_b]
  self.callback=callback
  self.number_of_scans=scans
  for pin in self.pins[:-2]:
   pin.set_pull(pin.PULL_UP)
  self.previous_readings=[0]*8
  self.current_readings=[0]*8
  self._scanner()
 def scan(self):
  readings=[int(not pin.read_digital())for pin in self.pins[:-2]]
  readings.append(int(button_a.is_pressed()))
  readings.append(int(button_b.is_pressed()))
  self.current_readings=[int(self.current_readings[pin]or readings[pin])for pin in range(0,len(readings))]
 def _scanner(self):
  pin_ids=['pin0','pin1','pin2','pin8','pin12','pin16','button_a','button_b']
  while True:
   for scans in range(0,self.number_of_scans):
    self.scan()
   report={}
   for x in range(0,8):
    if self.current_readings[x]!=self.previous_readings[x]:
     report[pin_ids[x]]=self.current_readings[x]
   self.previous_readings=self.current_readings
   self.current_readings=[0]*8
   if report:
    if self.callback:
     self.callback(report)

def my_callback(report):
    print('number of elements', len(report))
    for key in report:
        print(key, report[key])

        if  key == "pin0" and report[key] == 1:
            #Add code for pin0 press here
        if  key == "pin0" and report[key] == 0:
            #add code for pin0 release here

        if  key == "pin8" and report[key] == 1:
            #Add code for pin8 press here
        if  key == "pin8" and report[key] == 0:
            #add code for pin8 release here

        if  key == "pin1" and report[key] == 1:
            #Add code for pin1 press here
        if  key == "pin1" and report[key] == 0:
            #add code for pin1 release here

        if  key == "pin2" and report[key] == 1:
            #Add code for pin2 press here
        if  key == "pin2" and report[key] == 0:
            #add code for pin2 release here

        if  key == "pin12" and report[key] == 1:
            #Add code for pin12 press here
        if  key == "pin12" and report[key] == 0:
            #add code for pin12 release here

        if  key == "pin16" and report[key] == 1:
            #Add code for pin16 press here
        if  key == "pin16" and report[key] == 0:
            #add code for pin16 release here





gb = GamerBit(my_callback, 5)