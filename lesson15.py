# class Dom():
#     def__init__(self, hight,
#             width, length, 
#             house_addres,
#             floors, color,
#             internet_status,):

#     self.hight=hight
#     self.width=width
#     self.length=length
#     self.house_addres=house_addres
#     self.floors=floors
#     self.color=color
#     self.internet_status=internet_status
#     self.city='Bishkek'

#     def get_area(self):
#         house_area=self.width*self.length
#         print(house_area)


#     def get_value(self):
#         house_value=self.hight*self.width*self.length
#         print(house_value)


#     def internet_status(self):
#         if self.internet_status==True:
#             print('этому дому не нужен интернет')
#         else:
#             print('этому дому нужен интернет. адрес дома'+self.house_addres)

        
# house1=House(10,7,9'фурманова 10' 2, 'white', False)
# house2=House(15, 10, 10, 'советская 102',)
# house1.get_area(10,15 'some text')
# house2.che

# class Car():
#     def init(self, color, model, made, value):
#         self.color=color
#         self.model=model
#         self.made=made
#         self.value=value
#         self.odometr=0
    
#     def drive(self):
#         if self.odometr>2.5:
#             self.odometr+=15
#         else:
#             self.odometr+=10
#         print(self.odometr)

#     def get_description(self):
#         print('Марка машины:', self.made)
#         print('Модель машины:' , self.model)
#         print('Цвет машины:', self.color)
#         print('Объем машины:', self.value)


# class ElectroCar(Car):
#     def init(self, battery, color, model, made, value):    
#         super().init(color, model, made, value )
#         self.battery=battery

#     def get_battery_value(self):
#         print('')

#     def get_battery_value(self):
#         print('Емкость:', self.battery)

# tesla_modelx=ElectroCar(90, 'white', 'Tesla', 'modelX', 3.0,)
# tesla_modelx.get_battery_value() 
# tesla_modelx.get_description()
# tesla_modelx.drive()
              

# class  Human():
#     def __init__(self, weigth, heigth,race, age, sex, name):
#         self.weigth = weigth
#         self.heigth = heigth
#         self.race = race
#         self.age = age
#         self.sex = sex
#         self.name = name

#     def sleep(self):
#         print('Cпит')

#     def move(self):
#         print('lets move ... ')

#     def eat(self):
#         print('кушает')

# class Student(Human):
#     def __init__(self, uni_address, money, weigth, heigth,race, age, sex, name):
#         super().__init__(weigth, heigth,race, age, sex, name)
#         self.uni_address=uni_address
#         self.money=money

#     def want_sleep(self):
#         print('Хочет спать')

#     def study(self):
#         print('учится')

# Abraham=Student('Furmanova 15', 2000,5, 180, 'Mongoloid', '22', 'm', 'Abraham' )
# Abraham.move()
# Abraham.study()

print('были изменение')




















