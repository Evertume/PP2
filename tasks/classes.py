class person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
p1 = person("Mykhailo", "Mudryk")
class student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.a = {
            1:"KBTU",
            2:"NU",
            3:"MIT",
            4:"Harvard",
            5:"Yale"
        }
        self.b = {
            1:"football",
            2:"singing",
            3:"basketball",
            4:"reading",
            5:"gaming"
        }
   
    def uni(self, u):
        return self.a[u]
    def hobby(self, h):
        return self.b[h]
            
        
s1 = student("Dias", "Kuspanov")
class employee:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.c = {
            1:"Google",
            2:"Air Astana",
            3:"Starbucks",
            4:"Clearlake Capital",
            5:"Nike"
        }
        self.d = {
            1:"$25000",
            2:"$50000",
            3:"$100000",
            4:"$250000",
            5:"$1000000",
        }
    def company(self, f):
        return self.c[f]
    def salary(self, s):
        return self.d[s]
e1 = employee("Sherlock", "Holmes")
print(p1.name)
print(p1.surname)
print(s1.name)
print(s1.surname)
print(s1.uni(1))
print(s1.hobby(1))
print(e1.name)
print(e1.surname)
print(e1.company(4))
print(e1.salary(4))