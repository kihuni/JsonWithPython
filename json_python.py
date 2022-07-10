import json

people_string='''
{
"people": [
{
"emp_name":"stephen kihuni",
"emp_no.":"12334",
"emp_email":["stephenkihuni55@gmail.com"],
"has_license":"false"
},
{
"people": "stephen muiruri",
"emp_no.":"12234",
"emp_email":["stephenmichaeli55@gmail.com"],
"has_license":"true"
}
]
}
'''
   
   ##loaders converts json string into respective python data  
data = json.loads(people_string)
print(data)