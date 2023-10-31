# Scraping a local html file
from bs4 import BeautifulSoup
# Open and read the file.
with open('index.html', 'r') as html_file:
    content = html_file.read()

#initialise BeautifulSoup
soup = BeautifulSoup(content, 'lxml')

# Logic. Find all the courses and print it to the console with their prices

course_tag = soup.find_all('div', class_='card')
for courses in course_tag:
    course_name = courses.h5.text
    course_price = courses.a.text
    print(f"{course_name} costs {course_price.split()[-1]}")