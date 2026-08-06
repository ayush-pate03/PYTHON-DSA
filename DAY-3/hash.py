student = {
    "name": "ayush", 
    "mobile number": 9453627718
}
print(student["name"])
# insert
student["year"] = 2021
print(student)
# update 
student["name"] = "anuj"
print(student)
#delete  
del student["mobile number"]
print(student)
#search 
print("anuj" in student)