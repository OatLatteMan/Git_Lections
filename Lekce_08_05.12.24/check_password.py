import re

text = """Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation.[32]

Python is dynamically typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly procedural), object-oriented and functional programming. It is often described as a "batteries included" language due to its comprehensive standard library.[33][34]

Guido van Rossum began working on Python in the late 1980s as a successor to the ABC programming language and first released it in 1991 as Python 0.9.0.[35] Python 2.0 was released in 2000. Python 3.0, released in 2008, was a major revision not completely backward-compatible with earlier versions. Python 2.7.18, released in 2020, was the last release of Python 2.[36]

Python consistently ranks as one of the most popular programming languages, and has gained widespread use in the machine learning community."""

rx_email = re.compile(r'\[([0-9]+)\]')
# print(rx_email.findall(text))

# print(re.findall('\d+', text))
# print(re.search('Python', text))
# print(re.findall(r'\bas\b', text))

heslo = "kfgjfdk24dgs"
rx_number = re.compile(r'\d')
rx_uppercase = re.compile(r'[A-Z]')
rx_lowercase = re.compile(r'[a-z]')
rx_spec = re.compile(r'[-._]')

def check_password(password: str) -> bool:
    match_number = rx_number.search(password)
    match_lower = rx_lowercase.search(password)
    match_upper = rx_uppercase.search(password)
    match_spec = rx_spec.search(password)

    return all((
        match_number,
        match_lower,
        match_upper,
        match_spec
    ))

a = check_password(heslo)
b = check_password('hello')
c = check_password('hello1')
d = check_password('hello2-')
