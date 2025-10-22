dict={}
while True:
    item_id=int(input("enter the item id :"))
    item_name=input("enter the item name :")
    item_price=float(input("enter the item price :"))
    item_quantity=int(input("enter the item quantity :"))
    if item_id not in dict:
        dict[item_id]={"item name": item_name, "item price": item_price, "item quantity": item_quantity}
    else:
        print("item with the id ",item_id,"already exists.")
    print("do you want to remove items? (y/n)")
    remove=input()
    if remove.lower() == 'y':
        rem_id=int(input("enter the id of the item to remove"))
        if rem_id in dict:
            del dict[rem_id]
            print("item with id ",rem_id,"removed successfully.")
        else:
            print("item with id ",rem_id,"not found.")
    print("do you want to add more items? (y/n)")
    ch=input()
    if ch.lower() == 'y':
        continue
    else:
        break
print("inventory details:")
for i in dict:
    if i in dict:
        print(f"item id :{i}\nitem name :{dict[i]['item name']}\nitem price :{dict[i]['item price']}\nitem quantity :{dict[i]['item quantity']}\n")
    else:
        print("item id not found")
        print("item details are not available")
