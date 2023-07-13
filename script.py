import re

input_file = "web_flask/100-dump.sql"
output_file = "web_flask/101-dump.sql"

with open(input_file, "r") as file:
    sql_content = file.read()

modified_content = re.sub(r"\'", "", sql_content)

with open(output_file, "w") as file:
    file.write(modified_content)

print("File modified and saved as", output_file)

