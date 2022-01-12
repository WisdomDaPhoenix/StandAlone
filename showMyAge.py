# ----- DEFAULT PROGRAM ---------------
def showMyAge():
    import datetime
    yob = eval(input("Enter your year of birth: "))
    mob = eval(input("Enter your birth month (1-12): "))
    day = eval(input("Enter day of birth: "))
    birthdate = datetime.date(yob,mob,day)
    today = datetime.date(2022,1,12)
    diff = (today - birthdate).days
    print("Current age is: ",abs(diff//365),"yrs")

showMyAge()