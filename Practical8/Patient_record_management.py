class patients:#create the class
    def __init__(self,name,age,latest_admission,medical_history):
        self.name=name
        self.age=age
        self.latest=latest_admission
        self.history=medical_history
    def print(self):#define the print style
        print(f"Patient Name: {self.patient_name}, Age: {self.age}, Date of Latest Admission: {self.latest},Medical History: {self.history}")
#example
patient1=patients("Mike",35,"2024-01-15","High blood pressure")
patient1.print()


        