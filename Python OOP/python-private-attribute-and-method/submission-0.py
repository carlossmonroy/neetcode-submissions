class PasswordManager:
    def __init__(self,password : str):
        self.__password = password 
    
    def __get_password(self) -> str:
        return self.__password
    
    def verify_password(self,user_password) -> bool:
        return True if user_password == self.__get_password() else False




# Don't modify the code below this line
my_password = PasswordManager("secret123")
print(my_password.verify_password("secret123"))  # Should print: True
print(my_password.verify_password("wrong"))      # Should print: False
