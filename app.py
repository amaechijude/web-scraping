from bs4 import BeautifulSoup
import requests, re, fontstyle
html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=').text

soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
comp = list()
name = list()
for job in jobs:
    published_date = job.find('span', class_ = 'sim-posted').span.text
    if 'few' in published_date:
        company_name = job.find('h3', class_ = 'joblist-comp-name').text#.replace(' ', '')
        skills = job.find('span', class_ = 'srp-skills').text.replace('  ', '')
        x = re.findall(r"\w.\w", company_name)
        y = "".join(x)
        a = re.search(r"\w.*", skills)
        b = a.group()
        comp.append(y)
        name.append(b)

print("Companies jobs that requires {} skill posted recently (less than 4 days) on https://www.timesjobs.com is listed below)".format(fontstyle.apply('Python','bold')).title())
print()
print("{:<40} Skills".format('Company Name'))
for index in range(0, len(comp)):
    print(f"{comp[index]:<40} {name[index]}")