import requests
from bs4 import BeautifulSoup

url = "https://realpython.github.io/fake-jobs/"

page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")
python_jobs = results.find_all("h2", string= lambda text: "python" in text.lower())
print(python_jobs)
results = []
for python_job in python_jobs:
    results.append(python_job.parent.parent.parent)


# job_elements = results.find_all("div", class_="card-content")
for job_element in results:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    apply_link = job_element.find_all("a")
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    print(apply_link[1]["href"])
    print()