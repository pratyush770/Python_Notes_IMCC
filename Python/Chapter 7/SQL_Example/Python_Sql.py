from mysql.connector import connect, Error

# Establish connection
connection = connect(
    host="localhost",
    user="root",
    port=3307,
    password="matsumoto"
)

if connection.is_connected():
    print("Connection established to database")


# Function to create a database
def create_database(connection, db_name: str):
    try:
        cursor = connection.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
        print(f"Database '{db_name}' created or already exists.")
    except Error as e:
        print(f"An error occurred while creating the database: {e}")


# Function to create the student table
def create_student_table(connection):
    try:
        cursor = connection.cursor()
        connection.database = "college"  # Use the "college" database
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS student (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name NVARCHAR(100) NOT NULL,
                roll_number INT NOT NULL
            )
        """)
        print("Table 'student' created or already exists.")
    except Error as e:
        print(f"An error occurred while creating the table: {e}")


# Function to insert data into the student table
def insert_into_student(connection, name: str, roll_number: int):
    try:
        cursor = connection.cursor()
        query = """
            INSERT INTO student (name, roll_number)
            VALUES (%s, %s)
        """
        cursor.execute(query, (name, roll_number))
        connection.commit()
        print(f"Data inserted successfully: {name}, Roll Number: {roll_number}")
    except Error as e:
        print(f"An error occurred while inserting data: {e}")


# Function to insert multiple data into the student table
def insert_many_into_student(connection, student_data: dict):
    try:
        cursor = connection.cursor()
        query = """
            INSERT INTO student (name, roll_number)
            VALUES (%s, %s)
        """
        # Prepare data for batch insertion
        data = [(name, roll_number) for name, roll_number in student_data.items()]
        cursor.executemany(query, data)
        connection.commit()
        print(f"Batch insertion successful. Inserted {cursor.rowcount} records.")
    except Error as e:
        print(f"An error occurred while inserting data: {e}")


# Function to delete a user based on user_id
def delete_user(connection, user_id: int):
    try:
        cursor = connection.cursor()
        query = "DELETE FROM student WHERE id = %s"
        cursor.execute(query, (user_id,))
        connection.commit()
        if cursor.rowcount > 0:
            print(f"User with ID {user_id} deleted successfully.")
        else:
            print(f"No user found with ID {user_id}.")
    except Error as e:
        print(f"An error occurred while deleting the user: {e}")


# Function to update a user's details
def update_user(connection, user_id: int, name: str = None, roll_number: int = None):
    try:
        cursor = connection.cursor()
        updates = []
        values = []

        if name:
            updates.append("name = %s")
            values.append(name)
        if roll_number:
            updates.append("roll_number = %s")
            values.append(roll_number)

        if not updates:
            print("No updates provided.")
            return

        values.append(user_id)
        query = f"UPDATE student SET {', '.join(updates)} WHERE id = %s"
        cursor.execute(query, values)
        connection.commit()

        if cursor.rowcount > 0:
            print(f"User with ID {user_id} updated successfully.")
        else:
            print(f"No user found with ID {user_id}.")
    except Error as e:
        print(f"An error occurred while updating the user: {e}")


# Function to delete multiple users based on their user_ids
def delete_many_users(connection, user_ids: list):
    try:
        if not user_ids:
            print("No user IDs provided for deletion.")
            return

        cursor = connection.cursor()
        query = "DELETE FROM student WHERE id IN (%s)" % ",".join(["%s"] * len(user_ids))
        cursor.execute(query, tuple(user_ids))
        connection.commit()

        if cursor.rowcount > 0:
            print(f"{cursor.rowcount} users deleted successfully.")
        else:
            print("No users found with the provided IDs.")
    except Error as e:
        print(f"An error occurred while deleting multiple users: {e}")


def get_users(connection, user_id=None, name=None, roll_number=None):
    try:
        cursor = connection.cursor()
        query = "SELECT * FROM student WHERE 1=1"
        values = []

        if user_id is not None:
            query += " AND id = %s"
            values.append(user_id)
        if name is not None:
            query += " AND name = %s"
            values.append(name)
        if roll_number is not None:
            query += " AND roll_number = %s"
            values.append(roll_number)

        cursor.execute(query, tuple(values))
        result = cursor.fetchall()

        if result:
            print("Users retrieved successfully:")
            for row in result:
                print(row)
        else:
            print("No matching users found.")

        return result
    except Error as e:
        print(f"An error occurred while retrieving users: {e}")
        return []


def update_many_users(connection, updates: list):
    try:
        if not updates:
            print("No updates provided.")
            return

        cursor = connection.cursor()

        for update in updates:
            user_id = update.get("user_id")
            if not user_id:
                print("User ID missing in update request. Skipping entry.")
                continue

            fields = []
            values = []

            if "name" in update:
                fields.append("name = %s")
                values.append(update["name"])
            if "roll_number" in update:
                fields.append("roll_number = %s")
                values.append(update["roll_number"])

            if not fields:
                print(f"No fields to update for user_id {user_id}. Skipping.")
                continue

            values.append(user_id)
            query = f"UPDATE student SET {', '.join(fields)} WHERE id = %s"
            cursor.execute(query, tuple(values))

        connection.commit()
        print(f"{cursor.rowcount} user(s) updated successfully.")
    except Error as e:
        print(f"An error occurred while updating users: {e}")


# Create the "college" database
create_database(connection, "college")

# Create the student table
create_student_table(connection)

# Insert student data and display result
# insert_into_student(connection, "Pratyush", 2401121)
# insert_into_student(connection, "Om", 2401114)

# Insert multiple students using a dictionary
# students_to_insert = {
#     "Saad": 2401179,
#     "Nihal": 2401181,
#     "Sahil": 2401155
# }
# insert_many_into_student(connection, students_to_insert)

# Delete a student by ID
# delete_user(connection, 3)

# Update a user's details
# update_user(connection, 2, name="Om Lakade")  # Update name only
# update_user(connection, 4, roll_number=2401180)  # Update roll number only
# update_user(connection, 5, name="Aditya", roll_number=2401154)  # Update both

# Delete multiple users by their IDs
# delete_many_users(connection, [2, 3, 5])  # Provide a list of user IDs

get_users(connection)
# get_users(connection, user_id=1)
# get_users(connection, name="John Doe")
# get_users(connection, roll_number=2401121)
# get_users(connection, name="Alice Johnson", roll_number=103)

# Example updates
# user_updates = [
#     {"user_id": 1, "name": "John Updated", "roll_number": 2401121},  # Update both fields
#     {"user_id": 2, "name": "Jane Doe"},  # Update only name
#     {"user_id": 3, "roll_number": 303}  # Update only roll_number
# ]

# Call the function
# update_many_users(connection, user_updates)
