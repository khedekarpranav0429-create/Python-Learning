Customer_data={2938:{"Name":"Pranav","Location":"Mumbai"},
               3938:{"Name":"Virat","Location":"Benglore"},
               8339:{"Name":"Dhoni","Location":"Chennai"}}
print(Customer_data[3938])
print(Customer_data[2938]["Name"])
for Customer , Information in Customer_data.items():
    for key,Value in Information.items():
        print(key,Value)
    
