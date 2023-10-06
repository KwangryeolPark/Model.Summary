class Converter(object):
    def __init__(self):
        pass
    
    def num2str(self, num, unit:str=None):
        if unit == None:
            return num
        elif unit == 'str':
            return str(num)
        elif unit == 'normal':
            return self.num2normal(num)
        elif unit == 'bit':
            return self.num2bit(num)
        elif unit == 'param2bit':
            return self.num2bit(num * 4)
        return num
    
    def num2normal(self, num):
        if num < 1000:
            return str(num)
        elif num < 1000**2:
            return f'{num/1000:.3f} K'
        elif num < 1000**3:
            return f'{num/1000**2:.3f} M'
        elif num < 1000**4:
            return f'{num/1000**3:.3f} G'
        return f'{num/1000**4:.3f} T'
    
    def num2bit(self, num):
        if num < 1024:
            return str(num)
        elif num < 1024**2:
            return f'{num/1024:.3f} KiB'
        elif num < 1024**3:
            return f'{num/1024**2:.3f} MiB'
        elif num < 1024**4:
            return f'{num/1024**3:.3f} GiB'
        return f'{num/1024**4:.3f} TiB'