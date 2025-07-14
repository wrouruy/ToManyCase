import re

class ToManyCase:

    @staticmethod
    def kebab_case(string):
        words = re.findall(r'[A-Za-z0-9]+', string)
        return '-'.join(word.lower() for word in words)

    @staticmethod
    def camel_case(string):
        words = string.split()
        if not words:
            return ''
        return words[0].lower() + ''.join(word.capitalize() for word in words[1:])
    
    @staticmethod
    def pascal_case(string):
        return ''.join(word.capitalize() for word in string.split())
    
    @staticmethod
    def snake_case(string):
        words = re.findall(r'[A-Za-z0-9]+', string)
        return '_'.join(word.lower() for word in words)
    
__all__ = ['ToManyCase']