
def delete_all(connection):
    cursor = connection.cursor()
    cursor.execute(
        "DELETE FROM new_user"

    connection.commit()