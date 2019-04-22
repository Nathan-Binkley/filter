import io, sys

query = "clemson.edu\n"
List = [];
with open("data/raw.txt", "r") as f:
    for email in f:
        if(email[-len(query):]) == query:
            List.append(email)
        
f.close()

print("Sorting")
List.sort()

with open("data/filtered.txt","a+") as f:
    for i in List:
        f.write(i)
        
