

class Information:

    def __init__(self,first_name,last_name) -> None:

        self.first_name = first_name
        self.last_name = last_name
        
    @property
    def full_name(self):
        print("{} {}".format(self.first_name,self.last_name))

    
    @full_name.setter
    def full_name(self,name):
        first,last = name.split(" ")
        self.first_name = first
        self.last_name = last        




i = Information("raja",'sen')

i.full_name = "monu sen" 
i.full_name