def main():
    months_list = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
    date = input("Date: ").strip()

    for i in date:
        
        if i == "/":
            month, day, year = date.split("/")
            try:
                month = int(month)
                day = int(day)
                year = int(year)

                print(outdated(year, day, month))
                break

            except ValueError:
                break
        
        elif i == " ":
            month, day, year = date.split(" ")
            day = day.strip(",")

            if month == "January":
                month = "01"
            elif month == "February":
                month = "02"
            elif month == "March":
                month = "03"
            elif month == "April":
                month = "04"
            elif month == "May":
                month = "05"
            elif month == "June":
                month = "06"
            elif month == "July":
                month = "07"
            elif month == "August":
                month = "08"
            elif month == "September":
                month = "09"
            elif month == "October":
                month = "10"
            elif month == "November":
                month = "11"
            elif month == "December":
                month = "12"
               
            try:
                month = int(month)
                day = int(day)
                year = int(year)
                   
                print(outdated(year, day, month))
                break

            except ValueError:
                break

        else:
            continue


        
            

def outdated(year, day, month):
    
    
    return f"{year}-{month:02d}-{day:02d}"

if __name__ == "__main__":
    main()