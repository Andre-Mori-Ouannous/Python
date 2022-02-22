b = {}
with open("API/json_response.txt",'r') as f:
    for i in f:
        b = i
print(type(b["id"]))