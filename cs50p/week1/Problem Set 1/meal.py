
def main():
    
    whole_time = input("What time is it? ")
    # check if there is am or pm in the input
    if whole_time.endswith("am"):
        is_am = True 
        time , suffix = whole_time.split(" ") 
    elif whole_time.endswith("pm"):
        is_am = False
        time , suffix = whole_time.split(" ")
    

    # converting to 24hr 
    if whole_time.endswith("am")| whole_time.endswith("pm"):
        # seperating hours and mintues 
        hours , mintues = time.split(":")
        hours = int(hours)
        hours = is_12(hours,whole_time)
    else:
        # seperating hours(this input doest have am or pm) and mintues 
        # already 24 so just split and calcualte
        hours , mintues = whole_time.split(":")
        

    # converting to float
    inHr = convert(hours,mintues)

    if (7<= inHr <= 8 ) or 7<= inHr <= 8 and is_am == True:
        print("breakfast time.")
    elif 12<= inHr <= 13:
        print("lunch time.")
    elif (18<= inHr <= 19) or 18<= inHr <= 19 and is_am != True:
        print("dinner time.")
    else:
        exit()

def convert(hours,mintues):
    inHr = int(hours) + (float(mintues) / 60)
    return float(inHr)


def is_12(hours,time):
    # if its in 12hr, it converts it to 24hr
    if hours == 12 and time.endswith("am"):
        hours = 0 
    elif time.endswith("pm") and hours < 12:
        hours += 12
    return hours
        
if __name__ == "__main__":
    main()