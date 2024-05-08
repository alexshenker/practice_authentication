import json
import os

def save_user_data(file_path, user_data):
    try:
            if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
                 with open(file_path, 'r+') as file:
                      all_users_data = json.load(file)

                      all_users_data.append(user_data)

                      file.seek(0)

                      json.dump(all_users_data, file, indent=4)
            else:
                with open(file_path, 'w') as file:
                     json.dump([user_data], file, indent=4)
    except Exception as e:
        print(f"Error saving data: {e}")