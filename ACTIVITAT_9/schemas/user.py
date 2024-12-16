def user_schema(user) -> dict:
    return {
        "user_id": int(user[0]), 
        "user_name": str(user[1]),        
        "user_surname": str(user[2]),        
        "user_age": str(user[3]),         
        "user_email": str(user[4]),
        "user_telefon": int(user[5])           
    }

def users_schema(users) -> dict:
    return [user_schema(user) for user in users]