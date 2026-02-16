import re
def extract_email(text):
    """
    Uses RegEx to find the first email address in a string.
    """
    # Pattern: [chars]@[chars].[chars]
    email_pattern = r"[\w\.-]+@[\w\.-]+"

    match  = re.search(email_pattern, text)
    if match:
        return match.group()
    return None

def standardize_names(name_list):
    """
    Uses a lambda to fix capitalization and remove spaces.
    """
    # 1. Strip whitespace ( " bob" -> "bob")
    # 2. Title case ("bob" -> "Bob")
    clean_func = lambda x: x.strip().title()

    # Apply the lambda to every item in the list
    return list(map(clean_func, name_list))