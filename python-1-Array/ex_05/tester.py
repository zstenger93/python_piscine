from load_image import ft_load
from pimp_image import ft_invert, ft_red
from pimp_image import ft_green, ft_blue, ft_grey


array = ft_load("landscape.jpeg")
ft_invert(array)
ft_red(array)
ft_green(array)
ft_blue(array)
ft_grey(array)
print(ft_invert.__doc__)
print(ft_red.__doc__)
print(ft_green.__doc__)
print(ft_blue.__doc__)
print(ft_grey.__doc__)
