#Create a JSON of all object types and import the JSON into a SQL Database
import json
#dictionary
print(json.dumps({"Name":"Hema","doe":19}))
#list
print(json.dumps(["Shine","Deepa"]))
#string
print(json.dumps(("Sneha","Abi")))
#tuple
print(json.dumps("Jammy"))
#integer
print(json.dumps(10))
#float
print(json.dumps(12.2))
#True
print(json.dumps(True))
#False
print(json.dumps(False))
#None
print(json.dumps(None))

