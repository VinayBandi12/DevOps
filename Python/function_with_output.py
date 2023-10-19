def my_function():
  return 3 * 2

output = my_function()
print(output)



def format_name():
  f_name = input("Enter your first name: ")
  l_name = input("Enter your last name: ")
  return f"{l_name}, {f_name}"

print(format_name())



def format_name(f_name,l_name):
  """Returns a formatted name"""""
  if f_name == "" or l_name == "":
    return "You didn't enter a name"
  formated_f_name = f_name.title()
  formated_l_name = l_name.title()
  return f"{formated_f_name} {formated_l_name}"

print(format_name("ViNay","BandI"))