#WhoAmI
def WhoAmI():
    return("zz2655")

#getBondPrice
def getBondPrice(y,face,couponRate,m,ppy=1):
    pv=[]
    coupon=face*couponRate
    for i in range(1,m*ppy+1):
        pv.append((1/(1+y)**i)*coupon)
    totalc=sum(pv)
    total=1/(1+y)**(m*ppy)*face+totalc
    return(total)

print(getBondPrice(0.03,2000000,0.04,10))
