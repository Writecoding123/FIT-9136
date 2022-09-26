import random
from tkinter.tix import Tree

from user import User

class UserOperation:
    """
    Returns:
        _type_: _description_
    """
    user_info_path = None
    user_info_list = []
    
    def load_user_info(self):
        """
        A boolean result should be returned to indicate the success of the method i.e. True if completed, False if an error has occurred.
        """
        try:
            with open(self.user_info_path, 'r') as f:
                for line in f:
                    self.user_info_list.append(line.strip())
            return True
        except:
            return False

    def user_registration(self, user_name, user_password, user_role):
        """
        If you have any questions, please contact me, wechat: juing529
            param user_name: user name
            param user_password: user password
            param user_role: user role
            return: Boolean
        """
        for user_info in self.user_info_list:
            if user_name == user_info.split(';;;')[1]:
                return False
        
        user_id = ''
        while user_id == '':
            for _ in range(10):
                user_id += str(random.randint(0, 9))
            
            for user_info in self.user_info_list:
                if user_id == user_info.split(';;;')[0]:
                    user_id = ''
                    break
        
        self.user_info_list.append(f"{user_id};;;{user_name};;;{user_password};;;{user_role}")
        return True
    
    def user_login(self, user_name, user_password):
        """ user login

        Args:
            user_name: user name
            user_password: user password

        Returns:
            _type_: Boolean
        """

        for user_info in self.user_info_list:
            if user_name == user_info.split(';;;')[1] and user_password == user_info.split(';;;')[2]:
                return True
        return False
    
    def write_user_info(self):
        """ 
            write user info to file
            return: Boolean
            If you have any questions, please contact me, wechat: juing529
        """
        try:
            with open(self.user_info_path, 'w') as f:
                for user_info in self.user_info_list:
                    # The format for each user object written in the file should follow the format of the __str__ method.
                    f.write(User(user_info.split(';;;')[0], user_info.split(';;;')[1], user_info.split(';;;')[2], user_info.split(';;;')[3]).__str__())
                    f.write('\n')
            return True
        except:
            return False
        