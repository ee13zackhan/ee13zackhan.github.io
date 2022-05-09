# -*- coding: utf-8 -*-
"""
Created on Mon May  9 20:02:23 2022

@author: ee13zk
"""

class LatLong():

    def __init__(self):
        self.long_degrees = -1
        self.long_direction = ""
        self.long = ""
        

        
        
    def set_long(self, longitude):
        """ Set the longitude
        
        Positional parameters:
        longitude -- a strings of a number between "0" and "180" combined with "E" or "W", e.g. "10E"
                
        Raises:
        NumberOutOfRangeError
        DirectionScrewyError
        
        """
        
        
        # If set erroneously, set defaults
        degrees = ""
        direction = ""
        self.long_degrees = -1
        self.long_direction = ""
        self.long = str(degrees) + ""
        
        
        
        for character in longitude:
            if character.isdigit():
                degrees = degrees + character
            else:
                break
        for character in longitude[len(degrees):]:  
            if character.isalpha():
                direction = direction + character
            else:
                break
                
        if len(degrees) == 0 or len(degrees) > 3:
            raise NumberOutOfRangeError(longitude)
        
                
        degrees = int(degrees)
        if degrees < 0 or degrees > 180:
            raise NumberOutOfRangeError(longitude)
        
        if len(direction) != 1:
            raise DirectionScrewyError(longitude)
 
 
        if direction != "E" and direction != "W":
            raise DirectionScrewyError(longitude)

            
        self.long_degrees = degrees
        self.long_direction = direction
        self.long = str(degrees) + direction
            

            
            
    def get_long(self):
        """Get the longitude.
        
        Returns:
        longitude -- a strings of a number between "0" and "180" combined with "E" or "W", e.g. "10E"
        
        Raises:
        NotSetError
        
        """
        if self.long == "":
            raise NotSetError("")
        else:
            return self.long
        
        
        
        
    def get_long_degrees(self):
        """Get the longitude degrees.
        
        Returns:
        longitude -- int between 0 and 180.
        
        Raises:
        NotSetError
        
        """
        if self.long_degrees == -1:
            raise NotSetError("")
        else:
            return self.long_degrees      
         
        
        
        
    def get_long_direction(self):
        """Get the longitude direction.
        
        Returns:
        longitude -- int between 0 and 180.
        
        Raises:
        NotSetError
        
        """
        if self.long_direction == "":
            raise NotSetError("")
        else:
            return self.long_degrees      



        
        
class NumberOutOfRangeError(ValueError):
    """Exception raised for errors with the number range for longitude.
    
    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message="Numbers should be between 0 and 180 for longitude."):
        self.expression = expression
        self.message = message
    

        
        
class DirectionScrewyError(ValueError):
    """Exception raised for errors with the direction for longitude.
    
    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message="Direction should be either 'E' or 'W' for longitude."):
        self.expression = expression
        self.message = message

       

       
class NotSetError(ValueError):
    """Exception raised when value not set.
    
    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message="Value not set."):
        self.expression = expression
        self.message = message        
        
        
        
        
if __name__ == '__main__':
    # This is just a little bit if we want to run 
    # the module as a script for testing during development
    a = LatLong()
    a.set_long("1000E")
    print(a.get_long())
