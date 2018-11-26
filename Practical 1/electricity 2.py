def bill_estimator():
    MENU="""11 - TARIFF_11 = 0.244618
31 - TARIFF_31 = 0.136928
    """
    print(MENU)
    tariff_11=0.244618
    tariff_31=0.136928
    choice=int(input("Which tariff? 11 or 31: "))


    if choice==11:
        daily_use=float(input("Enter daily use in kWh: "))
        billing_days=int(input("Enter number of billing days: "))
        bill= (tariff_11*daily_use*billing_days)
        print("Estimated bill:$ {:.2f}".format(bill))
    elif choice==31:
        daily_use = float(input("Enter daily use in kWh: "))
        billing_days = int(input("Enter number of billing days: "))
        bill = (tariff_31 * daily_use * billing_days)
        print("Estimated bill:$ {:.2f}".format(bill))
    else:
        while 1:
            print("Invalid input")
            bill_estimator()
            break

bill_estimator()


