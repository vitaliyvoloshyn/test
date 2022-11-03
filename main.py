import os

import models.create_database as db_creator
from models.create_database import add_user
from models.database import DATABASE_NAME
from models.hash import check_password

if __name__ == "__main__":
    if not os.path.exists(DATABASE_NAME):
        db_creator.create_database()

u = check_password('obobileva', '%9To')
print(u)
print(check_password('obobileva', '%8To'))
add_user('obobileva', '%8To')
# print(type(u))
# print(list(u))
# print(u.password)
# for i in u:
#     print(i.password)