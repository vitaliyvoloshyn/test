from models.database import create_db, save_to_db, get_users, user_contacts, gt

if __name__ == "__main__":
    # create_db()
    # save_to_db('cendy', '123')
    user_contacts()
    # u = get_users()
    # print(u)
    # print(type(u))
    u = gt()
    for i in u:
        print(i)
