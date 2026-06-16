from abc import ABC, abstractmethod

class FoodPackage (ABC): 
    @abstractmethod
    def pack(self)  -> str:
        pass
    @abstractmethod
    def material(self) -> str:
        pass
    def describe(self):
        return f"Empaque: {self.pack()} , Material: {self.material()}"    
    

class Wrapping(FoodPackage):  
    def pack(self):
        return "Food Wrap Paper"

    def material(self):
        return "Aluminium"


class Bottle(FoodPackage):  
    def pack(self):
        return "Plastic Bottle"
    
    def material(self):
        return "Plastic"
      

class Glass(FoodPackage):  
    def pack(self):
        return "Glass Bottle"
    
    def material(self):
        return "Glass"


class Box(FoodPackage):  
    def pack(self):
        return "Box"
    
    def material(self):
        return "Cardboard"
