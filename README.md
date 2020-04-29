# LinkedIn-Jobs-WebScrapper

Python web scrapper with CLI that searches in LinkedIn for jobs under specified parameters 


##How it works

- Select parameters of jobs search
- Can search for job and location
. You can add a filter
- Output list of jobs, their short information and link


## Pre-requirements
``python3``

## Installation

Use the package manager [pip3]

``pip3 install beautifulsoup4 <br />
pip3 install requests <br />
pip3 install argparse-utils``



### using CLI:

```bash
usage: jobs [spaces must be replaced by '-'] [-h] [-p position] [-l location]
                                             [-f filter]

Find a job in any/certain location in LinkedIn

optional arguments:
  -h, --help   show this help message and exit
  -p position  The position/job you are looking for
  -l location  The location of the job
  -f filter    What keyword to filter by
```
