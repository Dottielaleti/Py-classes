class User:
    def __init__(self,last_name,first_name,occupation):
        self.first_name = first_name
        self.last_name = last_name
        self.occupation = occupation

    def create_user_profile(self):
        profile = f"\n {self.last_name}{self.first_name}\n {self.occupation}"
        return profile
    
f_name = "Dottie"
l_name = "Laleti"
occ = "Software Developer"
user_instance = User(f_name,l_name,occ)
new_user = user_instance.create_user_profile()
print(new_user)

