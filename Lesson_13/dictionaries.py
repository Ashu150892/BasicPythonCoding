dictionaries_data={}     # empty

student_details = { "Name :" : " Ashutosh",
                     "age :" : " 34",
                     "Emp_Id :" : "0485"}
print(student_details["Emp_Id :"])
for i in student_details:
    print(i)
for i in student_details.values():
    print(i)
for i in student_details.items():
    print(i)

std_id = { 
    "student_1":{"name :" : "Ashutosh",
                "age :" : 56,
                "branch :" : "Chemistry"},
    "student_2" : {
                 "name :" : "bittu",
                "age :" : 87,
                "branch :" : "Physic"} 
                 
}
for student,details in std_id.items():
    print(student)
    print(details)

voter_list={
    "voter_delhi_west" : {
        "name": "Amit",
        "age": 60,
        "Gender" : "Female",
        "Constituency Agency":"Nangloi"  
          },
    "voter_delhi_north" : {
                "name": "Sumit",
                "age": 40,
                "Gender" : "Male",
                "Constituency Agency":"Paschim Puri"  
                  },
    "voter_delhi_northeast" : {
            "name": "Rakesh",
            "age": 39,
            "Gender" : "Male",
            "Constituency Agency":"R K Puram"  
              },
     "voter_delhi_northeast_01" : {
                "name": "Saksh",
                "age": 59,
                "Constituency Agency":"R K Puram"  
                  }
}
voter_list["voter_delhi_east"] = {}
voter_list["voter_delhi_east"].update({
    "name": "Sonam",
    "age": 32,
    "Gender" : "Female",
    "Constituency Agency":"Ashok Nagar" 
})
voter_list["voter_delhi_south"] = {}
voter_list["voter_delhi_south"].update({
    "name": "Priya",
    "age": 28,
    "Gender" : "Female",
    "Constituency Agency":"Ashok Saket" 
})
eligible_voter=0
for name,details in voter_list.items():
    if details["age"]>=40:
        eligible_voter +=1
        print(name)
        print(details["Constituency Agency"])
        print(details["name"])
        print(details.get("Gender", "Not Available"))
print("Voter Total :", eligible_voter)

data ={}
data.setdefault("A",67)
data.setdefault("B",69)
data.setdefault("A",95)
print(data)
data.setdefault("C", []).append(90)
data.setdefault("C", []).append(95)
print("Data after Append :",data)