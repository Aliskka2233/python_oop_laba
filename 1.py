
class Car:
    color = None
    fuel = None
    model = None
    color_wheel = None



    def drive(self):
        pass
	
    def turn(self):
        pass

    def stop(self):
        pass

   
MyCar = Car()
MyCar.color = 'red' 
MyCar.fuel = 50 
MyCar.model = 'Subaru'
MyCar.color_wheel = 'green'

# MyCar.go() 
# MyCar.turn() 
# MyCar.stop()

print(MyCar.color)
print(MyCar.fuel)
print(MyCar.model)
print(MyCar.color_wheel)