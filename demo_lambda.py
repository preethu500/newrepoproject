import re
password=input("Enter password:")
pass1=password.split(",")
list(pass1)
res=[]
pass_pattern="^.*(?=.{6,12})(?=.*\d)(?=.*[a-z])(?=.[A-Z])(?=.*[@#$]).*$"
for i in pass1:
    result=re.findall(pass_pattern,i)
    if(result):
        res.append(result)
    if not res:
        print("No valid password found")
    else:
        print(res)
