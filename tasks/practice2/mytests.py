import re
str="vodilkvfk DFGHJKsk,   сука       f garhwe ' ed"
str = str.replace('"', '') 
str = str.replace("'", '') 
str = re.sub(r'\s+', ' ', str)
str = str.capitalize()
uncultured_words=['сука']

for uncult_word in uncultured_words:
    str=str.replace(uncult_word,"#"*len(uncult_word))

print(str)