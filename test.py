import requests
import random
import sys


student_data ={
    "index_number": f"{random.randint(1000, 9999)}",
    "password": "1234",
    "full_name": "Random",
    "name_with_initials": "Random",
    "date_of_birth": "Random",
    "gender": "M",
    "enrolled_date": "12-12-2020",
    "address": "Random",
    "special_notes": "",
}

if __name__ == "__main__":
    choise = input("add, update, delete, superuser") 
    if choise == "add":
        response = requests.post("http://127.0.0.1:8000/api/students/add", json=student_data)
        print(response.json())
    
    elif choise == "update":
        response = requests.put("http://127.0.0.1:8000/api/students/1", json=student_data)
        print(response.json())
        
    elif choise == "delete":
        response = requests.delete("http://127.0.0.1:8000/api/students/1")
        print(response.json())
                
    