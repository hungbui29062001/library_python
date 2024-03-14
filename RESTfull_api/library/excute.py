# # import required packages 
# import json
# from datetime import date
# from extension import db
# from common.json_serializable import JsonSerializable
  
# # custom class 
# # class Student: 
# #     def __init__(self, roll_no, name, batch): 
# #         self.roll_no = roll_no 
# #         self.name = name 
# #         self.batch = batch

# class Student2(db.Model, JsonSerializable):
#     __tablename__ = 'students'

#     id = db.Column(db.Integer, primary_key = True)
#     name = db.Column(db.String(100), nullable = False)

#     def __init__(self, name):
#         self.name = name

#     # def toJson(self):
#     #     return {
#     #         'name': self.name
#     #     }
    
#     def toJson(self):
#         return json.dumps(self.__dict__)
    
#     def __repr__(self) -> str:
#         return super().__repr__()
  
# class Car(JsonSerializable):
#     def __init__(self, name):
#         self.name = name
  
# # main function 
# if __name__ == "__main__": 
    
#     # create two new student objects 
#     # s1 = Student2("85", "Swapnil", "IMT") 
#     # s2 = Student2("124", "Akash", "IMT") 
  
#     # create two new car objects 
#     c1 = Car("Honda")
#     a = Student2(name='Student 1')
  
#     # convert to JSON format 
#     # jsonstr1 = json.dumps(s1.__dict__) 
#     # jsonstr2 = json.dumps(s2.__dict__) 
#     # jsonstr3 = json.dumps(c1.__dict__) 
#     # jsonstr5 = json.dumps((a))
  
#     # print created JSON objects 
#     # print(jsonstr1) 
#     # print(jsonstr2) 
#     print(c1) 
#     print(a.toJson())