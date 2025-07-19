##########################################################
############# Web Scraping Task 2 (Wuzzuf) ###############
##########################################################

import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest

web_page = requests.get("https://wuzzuf.net/search/jobs/?q=python&a=hpb")
page_content = BeautifulSoup(web_page.content, "lxml")
# print(page_content)

# get job titles, company names, locations and job skills
job_titles = page_content.find_all("h2", {"class": "css-m604qf"})
company_names = page_content.find_all("a", {"class": "css-17s97q8"})
locations = page_content.find_all("span", {"class": "css-5wys0k"})
job_skills = page_content.find_all("div", {"class": "css-y4udm8"})

job_titles_list = []
company_names_list = [] 
locations_list = [] 
job_skills_list = []
links = []
salary = []

# Extract info from the html 
for i in range(len(job_titles)):
    job_titles_list.append(job_titles[i].text)
    company_names_list.append(company_names[i].text)
    locations_list.append(locations[i].text)
    job_skills_list.append(job_skills[i].text)
    links.append(job_titles[i].find('a').attrs['href'])

# Extract each job info "salary & job requirments"
for link in links:
      result = requests.get(link)
    #   print(result.text)
      link_content = BeautifulSoup(result.content, "lxml")
      salaries = link_content.find('span', {'class': 'css-4xky9y'})
    #   print(salaries)
    #   salary.append(salaries.text)

# print(salary)

# save in csv file
file_list = [job_titles_list, company_names_list, locations_list, job_skills_list, links]
exported = zip_longest(*file_list)
with open("D:/ITI Backend using Python/ITI_Labs/Web-Scraping/wuzzuf-details.csv", 'w', encoding='utf-8') as output_file:
        doc = csv.writer (output_file)
        doc.writerow(["Job Title", "Company Name", "Location", "Skills Required", "Link"])
        doc.writerows(exported)
        print("file created")
