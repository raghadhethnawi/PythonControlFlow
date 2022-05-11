weight = 41.5

# Ground Shipping

if(weight <= 2):
  ground_cost = weight * 1.50 + 20
elif(2 < weight <= 6):
  ground_cost = weight * 3 + 20
elif(6 < weight <= 10):
  ground_cost = weight * 4 + 20
else:
  ground_cost = weight * 4.75 + 20

print("Ground Cost: ", ground_cost)

# Premium Ground Shipping

premium_ground_cost = 125.00
print("Premium Ground Cost: ", premium_ground_cost)


# Drone Shipping
if(weight <= 2):
  drone_cost = weight * 4.50
elif(weight <= 6):
  drone_cost = weight * 9
elif(weight <= 10):
  drone_cost = weight * 12
else:
  drone_cost = weight * 14.25

print("Drone Cost: ", drone_cost)




