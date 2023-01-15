n=input('Enter the city name:')

obj = {
 "India" : {
 "Karnataka" : ["Bangalore", "Mysore"],
 "Maharashtra" : ["Mumbai", "Pune"]
 },
 "USA" : {
 "Texas" : ["Dallas", "Houston"],
 "IL" : ["Chicago", "Aurora", "Pune"]
 }
}
res=[]
for country,state in obj.items():

    for city in state :
        for i in state[city]:
            if i==n:
                res.append(city)
print(res)



