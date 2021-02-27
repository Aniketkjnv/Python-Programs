def ReverseGST(total, rate):
    gst = total - (total * 100/(100 + rate))
    return gst


amount = int(input("Enter Total Amount: "))
rate = int(input("Enter Tax Percentage: "))
print(round(ReverseGST(amount, rate)))
