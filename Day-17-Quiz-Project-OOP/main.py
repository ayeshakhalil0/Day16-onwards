class User:
    def __init__(self, user_id, user_name):
        self.user_id = user_id
        self.user_name = user_name
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User(5,"Ayesha")
user_2 = User(10,"Khalil")

user_1.follow(user_2)

print("-----user 1 Followers and Following -----")
print(user_1.followers)
print(user_1.following)


print("-----user 2 Followers and Following-----")
print(user_2.followers)
print(user_2.following)