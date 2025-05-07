class UserRole:
    def __init__(self, role):
        self.role = role
        self.access_count = 0
        if role == 'premium':
            self.max_access = 10
        elif role == 'normal':
            self.max_access = 2
        else:
            raise ValueError("Invalid role. Choose 'premium' or 'normal'.")
        
        def access_data(self):
            if self.access_count < self.max_access:
                self.access_count += 1
                print(f"Data accessed {self.access_count} times.")
            else:
                print("Access limit reached.")
# Example of use:

premium_user = UserRole('premium')
normal_user = UserRole('normal')
# Premium user tries to access data 12 times:
for i in range(12):
    premium_user.access_data()
# Normal user tries to access data 3 times:
for i in range(3):
    normal_user.access_data()
    
