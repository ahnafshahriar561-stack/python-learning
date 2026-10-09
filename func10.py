def order_summary(customer,*items,discount=0,**extra):

    num = len(items)
    extra_text=""
    for key,values in extra.items():
        extra_text += (f"{key} : {values}")
    return f" the name :{customer}\n the amount of orders {num} \n discount  is  {discount}% \n the extra knowledge is {extra_text}"
print( order_summary('Ahnaf',"pizza","burger","juice",discount=10 ,allergy = "beef"))