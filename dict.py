# def packer(**kwargs):
# 	print(kwargs)

# def unpacker(first_name=None, last_name=None):
# 	if first_name and last_name:
# 		print("Hi {} {}!".format(first_name, last_name))
# 	else:
# 		print("Hi no name.")


# packer(name="Ted", num=42, dragon_age_inquisition=None)

# unpacker(**{"last_name": "Runyon", "first_name": "Ted"})

template = "Hi, I'm {name} and I love to eat {food}!"

def string_factory(**kwargs):
    stuff = [{"name": "ted", "food": "wopper"}, {"name": "james", "food": "strawberries"}]
    
    
    
    return template

print(string_factory())