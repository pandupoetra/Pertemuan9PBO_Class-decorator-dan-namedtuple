class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    @classmethod
    def tambah(cls, num1, num2):
        return cls(num1, num2)
    
    @staticmethod
    def kali(num1, num2):
        return num1 * num2
    
    @property
    def bagi(self):
        if self.num2 == 0:
            raise ValueError("Denominator cannot be zero")
        return self.num1 / self.num2

# Contoh pemanggilan @classmethod
calculator1 = Calculator(20, 4)
print("Hasil: ", calculator1.bagi)  

# Contoh pemanggilan @staticmethod
calculator2 = Calculator.kali(3, 7)
print("Hasil: ",calculator2)  

# Contoh pemanggilan properti pada instance yang baru
calculator3 = Calculator(15, 3)
print("Hasil: ", calculator3.bagi)  
