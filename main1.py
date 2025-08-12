from bs4 import BeautifulSoup
import requests

# print("skills you dont know ")
unfamiliar_skill= input("skill you dont know:")
print("filtering out:", unfamiliar_skill)

# Fetch the HTML content
html_text = requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=").text

# Parse with BeautifulSoup
soup = BeautifulSoup(html_text, 'lxml')

# this would find all the job postings on the webpage
jobs= soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
# print(jobs)
for job in jobs :
     
 #  /inside a for loop we are givivng a condition for published date
 #  
     published_date= job.find("span", class_="sim-posted").text

#the cxondition and if satisfied we print the job details

     if "few days ago" in published_date:
          
          job_title = job.find('h2', class_="heading-trun").text

          company_name = job.find('h3', class_="joblist-comp-name").text

          skills_needed= job.find('div', class_="more-skills-sections").text.replace(' ', '')

          location= job.find('li', class_="srp-zindex location-tru").text

          exp_required =job.find('li' , class_="srp-icons experience").text

          more_info = job.header.h2.a["href"]


#  another condition where you can input a skill which you dont know about and this would filter out the job postings which dont have that skill

          if unfamiliar_skill not in skills_needed:
          
               print(f"Job Title     : {job_title.strip()}\n"
                     f"Company Name  : {company_name.strip()}\n"
                     f"Location      : {location.strip()}\n"
                     f"exp_required  : {exp_required}\n"
                     f"more_info     : {more_info.strip()}\n"
                     f"Skills Needed : {skills_needed.strip()}\n")
              
# so this is a small project made with purpose of showing that how you can use python to scrape a website and use different filters to get the desired output.
# you can use this project as a starting point and make it more complex by adding more filters and features.
