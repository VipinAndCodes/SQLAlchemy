
from main import User,Session,engine


local_session=Session(bind=engine)

# #returns all objects
# users=local_session.query(User).all()[:3]


# #returns onjects limited to 3
# users=local_session.query(User).all()[:3]
# for user in users:
#     print(user.username)

#query for one object

john = local_session.query(User).filter(User.username=="john").first()

print(john)

