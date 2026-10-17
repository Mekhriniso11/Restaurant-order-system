name=input('Enter your name: ')
has_student_id=input("Do you have student id (yes/no): ")
order_time=float(input("Enter order time: "))

first_dish=input('Enter first dish name: ')
first_price=float(input('Enter price: '))
first_quantity=int(input('Enter quantity: '))

second_dish=input('Enter second dish name: ')
second_price=float(input('Enter price: '))
second_quantity=int(input('Enter quantity: '))

third_dish=input('Enter third dish name: ')
third_price=float(input('Enter price: '))
third_quantity=int(input("Enter quantity: "))

subtotal=first_price*first_quantity+second_price*second_quantity+third_price*third_quantity

is_student_eligible=has_student_id=='yes'
student_discount=subtotal*0.15 if is_student_eligible else 0

is_happy_hour_eligible=14<=order_time<=17
happy_hour_discount=subtotal*0.20 if is_happy_hour_eligible else 0

if student_discount>=happy_hour_discount and is_student_eligible:
    applied_main="Student Discount"
elif happy_hour_discount>student_discount and is_happy_hour_eligible:
    applied_main="Happy Hour Discount"
else:
    applied_main="None"

main_discount=student_discount*(student_discount >= happy_hour_discount) + happy_hour_discount * (happy_hour_discount > student_discount)

is_large_order_eligible=subtotal>=150000
large_order_discount=subtotal*0.05 if is_large_order_eligible else 0

total_discount=main_discount+large_order_discount
subtotal_after_discounts=subtotal-total_discount

service_charge=subtotal_after_discounts*0.10
delivery_fee=(subtotal>=100000)*15000
is_delivery_fee=delivery_fee==0

final_total=subtotal_after_discounts+service_charge+delivery_fee
total_amount_saved=subtotal-final_total

print(f"\n\n{'='*50}")
print(f"Customer name: {name}")
print(f"Student status: {has_student_id}")
print(f"Order time: {order_time:.2f}")
print(f"{'='*50}")
print(f"Dish 1: {first_dish} | Price: {first_price:.2f} | Quantity: {first_quantity}")
print(f"Dish 2: {second_dish} | Price: {second_price:.2f} | Quantity: {second_quantity}")
print(f"Dish 3: {third_dish} | Price: {third_price:.2f} | Quantity: {third_quantity}")
print(f"{'='*50}")
print(f"Subtotal before discounts: {subtotal:.2f} sum")
print(f"{'='*50}")
print(f"Student discount eligibility: {is_student_eligible} | Amount: {student_discount:.2f} sum")
print(f"Happy hour eligibility: {is_happy_hour_eligible} | Amount: {happy_hour_discount:.2f} sum")
print(f"Which discount was applied: {applied_main}")
print(f"Large order discount eligibility: {is_large_order_eligible} | Amount: {large_order_discount:.2f} sum")
print(f"Total Discounts: {total_discount:.2f} sum")
print(f"{'='*50}")
print(f"Subtotal after discounts: {subtotal_after_discounts:.2f} sum")
print(f"{'='*50}")
print(f"Service charge amount: {service_charge:.2f} sum")
print(f"Delivery fee: {delivery_fee:.2f} sum")
print(f"{'='*50}")
print(f"Final total: {final_total:.2f} sum")
print(f"Total amount saved: {total_amount_saved:.2f} sum")
print(f"{'='*50}\n")