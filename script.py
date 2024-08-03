#  Create a function called username_generator take two inputs, first_name and last_name and returns a user_name. The username should be a slice of the first three letters of their first name and the first four letters of their last name. If their first name is less than three letters or their last name is less than four letters it should use their entire names.

def username_generator(first_name, last_name):
  user_name = ""
  if len(first_name) < 3 or len(last_name) < 4:
    user_name = first_name + last_name
  else:
    user_name = first_name[0:3] + last_name[0:4]
  return user_name

print(username_generator("Abe", "Simpson"))

# Shifting one letter to the right e.g. AbeSimp ->>> pAbeSim
def password_generator(user_name):
  password = ""
  first_letter = user_name[-1]
  password = first_letter + user_name[:-1]
  return password

print(password_generator("AbeSimp"))

# Inside password_generator, create a for loop that iterates through the indices of user_name by going from 0 to len(user_name).

def password_generator2(user_name):
  password2 = ""
  for i in range(0, len(user_name)):
    password2 += user_name[i - 1]
  return password2

print(password_generator2("AbeSimp"))
