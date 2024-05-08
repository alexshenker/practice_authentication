import json
import os

user_db_path = os.path.join(os.getcwd(), 'users.json')

def save_user_data(user_data):
    try:
            if os.path.exists(user_db_path) and os.path.getsize(user_db_path) > 0:
                 with open(user_db_path, 'r+') as file:
                      all_users_data = json.load(file)

                      all_users_data.append(user_data)

                      file.seek(0)

                      json.dump(all_users_data, file, indent=4)
            else:
                with open(user_db_path, 'w') as file:
                     json.dump([user_data], file, indent=4)
    except Exception as e:
        print(f"Error saving data: {e}")

def get_user_data(email):
    try:
            with open(user_db_path, 'r') as file:
                 users = json.load(file)

                 for user in users:
                      if user['email'] == email:
                           return user
                 return None
            
    except FileNotFoundError:
        print("The file was not found.")
        return None
    except json.JSONDecodeError:
        print("Error decoding JSON.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None