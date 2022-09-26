class User:

    def __init__(self, user_id = '1234567890', user_name='Jack', user_password='123456', user_role='admin'):
        """Constructor for User class

        Args:
            user_id (str, optional): _description_. Defaults to '1234567890'.
            user_name (str, optional): _description_. Defaults to 'Jack'.
            user_password (str, optional): _description_. Defaults to '123456'.
            user_role (str, optional): _description_. Defaults to 'admin'.
        """
        self.user_id = user_id
        self.user_name = user_name
        self.user_password = user_password
        self.user_role = user_role

    def __str__(self):
        """String representation of User class"""
        return f"{self.user_id};;;{self.user_name};;;{self.user_password};;;{self.user_role}"