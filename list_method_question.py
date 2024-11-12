cars=["bmw","mahindra","suzuki","rolls royce","bently","aston martin","tata","audi","mustang"]

#1.Append
#=>append "ferrari" to the list
cars.append("ferrari")
print(cars)
#['bmw', 'mahindra', 'suzuki', 'rolls royce', 'bently', 'aston martin', 'tata', 'audi', 'mustang', 'ferrari']

#2.Insert
#=>insert "porsche" at index 3
cars.insert(3,"porsche")
print(cars)
#['bmw', 'mahindra', 'suzuki', 'porsche', 'rolls royce', 'bently', 'aston martin', 'tata', 'audi', 'mustang', 'ferrari']
'''
#3.clear
#=>clear all elements from list
cars.clear()
print(cars)
#[]
'''
#4.sort
#=>sort the original list of cars in alphabetical order
cars.sort()
print(cars)
#['aston martin', 'audi', 'bently', 'bmw', 'ferrari', 'mahindra', 'mustang', 'porsche', 'rolls royce', 'suzuki', 'tata']

#5.remove
#=>remove "audi" from list
cars.remove("audi")
print(cars)
#['aston martin', 'bently', 'bmw', 'ferrari', 'mahindra', 'mustang', 'porsche', 'rolls royce', 'suzuki', 'tata'] 

#6.index
#=> find index of mustang
print(cars.index("mustang"))
#5

#7.extend
#=>extend the list with another list of cars:["tesla","nissan"]
cars.extend(["tesla","nissan"])
print(cars)
#['aston martin', 'bently', 'bmw', 'ferrari', 'mahindra', 'mustang', 'porsche', 'rolls royce', 'suzuki', 'tata', 'tesla', 'nissan']

#8.pop
#=>pop the last element from the list and print it
print(cars.pop())
print(cars)
#nissan
#['aston martin', 'bently', 'bmw', 'ferrari', 'mahindra', 'mustang', 'porsche', 'rolls royce', 'suzuki', 'tata', 'tesla']

#9.count
#=>count how many times "bmw" appears in list
print(cars.count("bmw"))
#1

#10.append multiple
#=>append multiple cars:["jaguar","fiat"] to the list
cars1=["jaguar","fiat"]
cars.append(cars1)
print(cars)
#['aston martin', 'bently', 'bmw', 'ferrari', 'mahindra', 'mustang', 'porsche', 'rolls royce', 'suzuki', 'tata', 'tesla', ['jaguar', 'fiat']]


#11.insert multiple
#=>insert multiple cars["volvo","honda"] at index 2
cars2=["volvo","honda"]
cars.insert(2,cars2)
print(cars)
#['aston martin', 'bently', ['volvo', 'honda'], 'bmw', 'ferrari', 'mahindra', 'mustang', 'porsche', 'rolls royce', 'suzuki', 'tata', 'tesla', ['jaguar', 'fiat']]

#12.sort descending
#=>sort original list of cars in descending order
cars3=['aston martin', 'audi', 'bently', 'bmw', 'ferrari', 'mahindra', 'mustang', 'porsche', 'rolls royce', 'suzuki', 'tata']
cars3.sort(reverse=True)
print(cars3)
#['tata', 'suzuki', 'rolls royce', 'porsche', 'mustang', 'mahindra', 'ferrari', 'bmw', 'bently', 'audi', 'aston martin']


