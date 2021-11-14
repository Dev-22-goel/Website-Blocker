from datetime import datetime
host_path='C:/Windows/System32/drivers/etc/hosts'
redirect = "127.0.0.1"

website_list=["cheese.com"]

year= int(input("Enter which year: "))
month= int(input("Enter which month: "))
starting_date= int(input("Enter start date: "))
ending_date=int(input("Enter end date: "))

start_date = datetime(year,month,starting_date)
end_date = datetime(year,month,ending_date)
today_date = datetime(datetime.now().year,datetime.now().month,datetime.now().day)

while True:
    if start_date <= today_date < end_date:
        with open(host_path,"r+") as file:
            content = file.read()
            for site in website_list:
                if site in content:
                    pass
                else:
                    file.write(redirect+" "+site+"\n")
        print("all sites are blocked")
        break
    else: # end_date < today_date
        with open(host_path,"r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(site in line for site in website_list):
                    file.write(line)
            file.truncate()
        print("all sites unblocked")
        break