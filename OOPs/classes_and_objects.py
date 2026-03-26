class Car:
    vehicle_type = 'four wheeler'
    tyre = 4


    def set_details(self,brand,color):
        self.brand = brand
        self.color = color
    
    def start_engine(self):
        print(f"The {self.color} {self.brand} car is starting.... Vrrrrommmmm")


Toyota_glanza = Car()
Maruthi_Ciaz = Car()

Toyota_glanza.set_details('toyota','green')
Maruthi_Ciaz.set_details('maruthi','yellow')


Toyota_glanza.start_engine()
Maruthi_Ciaz.start_engine()


