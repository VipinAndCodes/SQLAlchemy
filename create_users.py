from main import User,Session,engine


users=[
    {
        "username":"jerry",
        "email":"jerry@company.com"
    },
    {
        "username":"sara",
        "email":"sara@company.com"
    },
    {
        "username":"raj",
        "email":"raj@company.com"
    },
    {
        "username":"sheldon",
        "email":"sheldon@company.com"
    },
    {
        "username":"jim",
        "email":"jim@company.com"
    },

    {
        "username":"pam",
        "email":"pam@company.com"
    }

]




local_session=Session(bind=engine)
# new_user=User(username="john",email="john@companay.com")

# local_session.add(new_user)

# local_session.commit()

for u in users:
    new_user=User(username=u["username"],email=u["email"])
    
    local_session.add(new_user)

    local_session.commit()

    print(f"added { u['username'] }")


