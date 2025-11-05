def write_email(email):
    at = email.find("@")
    find = (email[0])
    return find + "***" + (email[at:])

def center(name,width):
    cal_name = len(name)
    cal_width = len(width)
    version = cal_width - cal_name
    version_real = version//2
    return f"{name:>{version_real}}"

print(write_email("jkraft@bayviewglen.ca"))
print(center("Gobi","GobiCats"))