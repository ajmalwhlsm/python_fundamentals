#2
first_name ="john"
last_name="doe"
full_name=first_name+" "+last_name
country="oceania"
city="meji"
age=209
year=2026
is_married=False
is_true=True
is_light_on=True
-----------
name,city_name,current_age="Aj","TVM",22
-----------------------
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
------------------------
print(first_name)
print(last_name)
print(full_name)
print(country)
print(city)
print(age)
print(year)
print(len(first_name))
print(len(full_name))

print(first_name.upper())
print(last_name.capitalize())
print(full_name.title())
print(first_name[0])
print(last_name[-1])
print(full_name.split())
print(full_name.replace("john","Jane"))
print(age+1)
print(age-10)
print(age*2)
print(age/2)
print(age>100)
print(year==2026)
print(is_married)
print(not is_married)
print(is_true and is_light_on)
print(type(name))
print(type(city_name))
print(type(current_age))

print(name)
print(city_name)
print(current_age)
print(name.upper())
print(city_name.lower())

print(f"My name is {full_name}")
print(f"I live in {city},{country}")
print(f"I am {age} years old")
