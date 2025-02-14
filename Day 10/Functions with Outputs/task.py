def format_name(f_name, l_name):
    """
    Take a first and last name and format it to return the
    title case version of tne name
    :param f_name: first name
    :param l_name: last name
    :return: first name + last name in title case
    """
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name}{formated_l_name}"

print(format_name("Angela",'Yu'))

