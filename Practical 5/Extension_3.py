def bill_estimator():
    MENU = """11 - TARIFF_11 = 0.244618
31 - TARIFF_31 = 0.136928
41 - TARIFF_41 = 0.156885
51 - TARIFF_51 = 0.244567
61 - TARIFF_61 = 0.304050
        """
    print(MENU)
    tariff_cost = {11: 0.244618, 31: 0.136928, 41: 0.156885, 51: 0.244567, 61: 0.304050}
    choice = int(input("Which tariff? 11 or 31 or 41 or 51 or 61: "))
    if choice == 11:
        daily_use = float(input("Enter daily use in kWh: "))
        billing_days = int(input("Enter number of billing days: "))
        bill = (tariff_cost[11] * daily_use * billing_days)
        print("Estimated bill:$ {:.2f}".format(bill))

    elif choice==31:
        daily_use = float(input("Enter daily use in kWh: "))
        billing_days = int(input("Enter number of billing days: "))
        bill = (tariff_cost[31] * daily_use * billing_days)
        print("Estimated bill:$ {:.2f}".format(bill))

    elif choice==41:
        daily_use = float(input("Enter daily use in kWh: "))
        billing_days = int(input("Enter number of billing days: "))
        bill = (tariff_cost[41] * daily_use * billing_days)
        print("Estimated bill:$ {:.2f}".format(bill))

    elif choice==51:
        daily_use = float(input("Enter daily use in kWh: "))
        billing_days = int(input("Enter number of billing days: "))
        bill = (tariff_cost[51] * daily_use * billing_days)
        print("Estimated bill:$ {:.2f}".format(bill))

    elif choice==61:
        daily_use = float(input("Enter daily use in kWh: "))
        billing_days = int(input("Enter number of billing days: "))
        bill = (tariff_cost[61] * daily_use * billing_days)
        print("Estimated bill:$ {:.2f}".format(bill))

    else:
        while 1:
            print("Invalid input")
            bill_estimator()
            break
bill_estimator()
