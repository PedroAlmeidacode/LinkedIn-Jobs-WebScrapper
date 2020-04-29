import requests
from bs4 import BeautifulSoup
import argparse

# returns clean search with the parameters passed
def scrape_jobs(position,location=None):
    if location:
        URL = f"https://www.linkedin.com/jobs/search/?keywords={position}&location={location}"
    else:
        URL = f"https://www.linkedin.com/jobs/search/?keywords={position}"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="main-content")
    return results


def filter_jobs_by_keyword(results, word):
    filtered_jobs = results.find_all(
        "h2", string=lambda text: word in text.lower()
    )
    for f_job in filtered_jobs:
        link = f_job.find("a")["href"]
        print(f_job.text.strip())
        print(f"Apply here: {link}\n")


def print_all_jobs(results):
    job_elems = results.find_all("div", class_="result-card__contents job-result-card__contents")

    for job_elem in job_elems:
        # keep in mind that each job_elem is another BeautifulSoup object!
        title_elem = job_elem.find("h3", class_="result-card__title job-result-card__title")
        company_elem = job_elem.find("h4", class_="result-card__subtitle job-result-card__subtitle")
        location_elem = job_elem.find("div", class_="result-card__meta job-result-card__meta")
        if None in (title_elem, company_elem, location_elem):
            continue
            # print(job_elem.prettify())  # to inspect the 'None' element
        print("Job: ", title_elem.text.strip())
        link_elem = company_elem.find("a")
        decripton_elem = location_elem.find("p", class_="job-result-card__snippet")
        datetime_elem = location_elem.find("time", class_="job-result-card__listdate--new")
        link = link_elem["href"]
        if link is not None:
            print("Link: ", link)
        print("Company: ", company_elem.text.strip())

        if decripton_elem is not None:
            decripton_elem = decripton_elem.text.strip()
        if datetime_elem is not None:
            datetime_elem = datetime_elem.text.strip()
        location_elem = location_elem.text.strip()

        if decripton_elem is not None:
            location_elem = location_elem.replace(decripton_elem, '\n')
        if datetime_elem is not None:
            location_elem = location_elem.replace(datetime_elem, '\n')

        print("Location: ", location_elem)

        if decripton_elem is not None:
            print("Description: ", decripton_elem)
        if datetime_elem is not None:
            print("Published: ", datetime_elem)

        print()
        print()


# script CLI
# -----------------------------
# -----------------------------


my_parser = argparse.ArgumentParser(prog="jobs [spaces must be replaced by '-']", description="Find a job in any/certain location in LinkedIn")
my_parser.add_argument("-p", metavar="position", type=str, help="The position/job you are looking for")
my_parser.add_argument("-l", metavar="location", type=str, help="The location of the job")
my_parser.add_argument("-f", metavar="filter", type=str, help="What keyword to filter by")

args = my_parser.parse_args()
position, location, keyword = args.p, args.l, args.f



print("Scrapping the pretended information from LinkedIn...\n\n")
results = scrape_jobs(position, location)
print("LinkedIn results:\n\n")
if keyword: # se escrever filtro de keyword
    filter_jobs_by_keyword(results, keyword.lower())
else: # senao imrpime todos os jobs
    print_all_jobs(results)
