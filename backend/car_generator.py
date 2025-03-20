import random

# Define the columns of the 'cars' table
columns = ["id", "make", "model", "year", "location", "color", "price"]

# Sample data for each column
def random_car_data():
    makes = ["Toyota", "Honda", "Ford", "Chevrolet", "BMW"]
    models = ["Corolla", "Civic", "Focus", "Malibu", "X5"]
    locations = ["New York", "Los Angeles", "Chicago", "Houston", "Miami"]
    colors = ["Red", "Blue", "Black", "White", "Silver"]
    
    return (
        random.randint(1000, 9999),  # id
        random.choice(makes),        # make
        random.choice(models),       # model
        random.randint(2000, 2025),  # year
        random.choice(locations),    # location
        random.choice(colors),       # color
        round(random.uniform(5000, 50000), 2)  # price
    )

# Get the number of cars to generate from user input
num_cars = int(input("Enter the number of cars to generate: "))

# Generate multiple random car data entries
car_entries = [random_car_data() for _ in range(num_cars)]

# Construct the SQL INSERT statement
values_list = ",\n".join([f"({', '.join(map(str, entry))})" for entry in car_entries])

sql = f"""
INSERT INTO cars ({', '.join(columns)})
VALUES {values_list};
"""

print(sql)
