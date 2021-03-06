from enum import Enum


class VarType(Enum):
    STRING = 1


class VarSystem:
    """
    Class responsible for handling variables in pytux program
    """

    __variables = {}

    def init_or_assign(self, name: str, value, type: VarType):
        """
        Initializes variable or assigns value to existing variable.

        :param name: variable identifier
        :param value: variable value
        :param type: variable type
        :return: None.
        """
        if name in self.__variables:
            var_type = self.__variables[name][1]
            if var_type != type:
                raise ValueError(f"trying to assign value of type {type} to the variable {name} of type {var_type}")
        self.__variables[name] = (value, type)

    def get_value(self, name: str):
        """
        Gets variable value if variable with such identifier exists.

        :param name: variable identifier
        :return: variable value.
        """
        if name in self.__variables:
            return self.__variables[name][0]
        else:
            return None

    def get_type(self, name: str):
        """
        Gets variable type if variable with such identifier exists.

        :param name: variable identifier
        :return: variable type.
        """
        if name in self.__variables:
            return self.__variables[name][1]
        else:
            return None


Varya = VarSystem()
