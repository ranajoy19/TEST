# class Cache():

#     def __init__(self) -> None:
#         self.cache = {}
#         self.access_element = []
#         self.capacity = 2

#     def put(self,k,v):
#         if k in self.access_element:
#             self.access_element.remove(k)
#         if len(self.cache) >= self.capacity:
#             key = self.access_element[0]
#             self.access_element.pop(0)
#             del self.cache[key]
#         self.cache[k]=v
#         self.access_element.append(k)

#     def get(self,k):
#         if k in self.cache:
#             self.access_element.remove(k)
#             self.access_element.append(k)
#             return self.cache[k]
#         else:
#             return None


# c1 =Cache()
# c1.put(1,100)
# c1.put(2,200)
# print(c1.get(1))
# c1.put(3,300)
# print(c1.get(2))






