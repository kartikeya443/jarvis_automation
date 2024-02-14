import re

#filter python code for gpt response
def filter(txt):
    
    pattern = r"'''python(.*?)'''"
    matches = re.findall(pattern, txt, re.DOTALL)
    
    if matches:
        python_code = matches[0].strip()
        return python_code
    else:
        return None