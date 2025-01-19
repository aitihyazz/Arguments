def to_cal(bill,tip_percent):
    total=bill+(1+0.01*tip_percent)
    total =round(total,2)
    print(f"please pay ${total}")
to_cal(170,20)
