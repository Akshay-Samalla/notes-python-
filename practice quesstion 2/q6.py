'''


6) Extract Emails of Verified Users
  You have a list of user records with email and a verification status. Extract the emails of verified users.
	users = [
    {"email": "alice@example.com", "verified": True},
    {"email": "bob@example.com", "verified": False},
    {"email": "charlie@example.com", "verified": True},
    {"email": "daisy@example.com", "verified": False}
	 ]



'''


users = [
    {"email": "alice@example.com", "verified": True},
    {"email": "bob@example.com", "verified": False},
    {"email": "charlie@example.com", "verified": True},
    {"email": "daisy@example.com", "verified": False}
	 ]
users=filter(lambda x:x['verified']==True , users)
print(list(users))