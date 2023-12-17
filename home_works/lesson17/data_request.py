def insert_user(cursor):
    name = input("Enter name: ")
    cursor.execute(
        f"INSERT INTO users (name) VALUES ('{name}') RETURNING user_id;"
    )
    return cursor.fetchone()[0]


def insert_product(cursor):
    name = input("Enter product name: ")
    protein = float(input("Enter proteins (grams): "))
    fats = float(input("Enter fats (grams): "))
    carbohydrates = float(input("Enter carbohydrates (grams): "))
    cursor.execute(
        f"INSERT INTO product (name, protein, fats, carbohydrates) VALUES ('{name}', {protein}, {fats}, {carbohydrates}) RETURNING product_id;"
    )
    return cursor.fetchone()[0]


def insert_food_intake(cursor, user_id, product_id):
    cursor.execute(
        f"INSERT INTO food_intake (user_id, product_id) VALUES ({user_id},{product_id});"
    )
