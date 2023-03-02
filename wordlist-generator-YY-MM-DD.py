# Scenerio: Suppose you have got a file where year-month-day along with file name and extention 
# Example: 2022-01-01-upload.pdf
# And now you want to fuzz these files then you can use this script by 
# changing start date and end date inside script
# Useful keywords to fuzz for filename: backup, password, service,config,settings,adm,admin, identity etc

from datetime import timedelta, date
print("Welcome to Year-Month-Day Fuzzing wordlist generator:")
print("")
print("[*] Edit: Change start date and end date and the file name along with extension in the script![*]")
print("")
print("[*] Usage: python3 wordlist-generator-YY-MM-DD.py")


def daterange(date1, date2):
    for n in range(int ((date2 - date1).days)+1):
        yield date1 + timedelta(n)

start_dt = date(2022, 1, 1)
end_dt = date(2023, 12, 31)
for dt in daterange(start_dt, end_dt):
    print(dt.strftime("%Y-%m-%d-upload.pdf"))
print("")   
print("Success!")
