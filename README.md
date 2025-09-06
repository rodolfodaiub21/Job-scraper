🔎 JobScraper – LinkedIn Job Search Automation

This project is a personal tool I built to practice my skills Python and web scraping.
Its main goal is to help me (and others) find remote jobs more efficiently – particularly in fields like Cybersecurity Analyst and Web Scraping roles.

I use it as part of my journey to land my first remote job. 🚀

📌 Features

Scrapes job postings from LinkedIn.

Randomized headers to reduce bot detection.

Supports searching for remote or US-based roles.

Collects data such as:

Job title

Company name

Location

Job URL

Date of scraping

Saves results into a clean CSV file for further analysis.

⚙️ Installation

Clone the repo:

git clone https://github.com/rodolfodaiub21/Job-scraper.git
cd JobScraper


Install dependencies:

pip install -r requirements.txt


requirements.txt should contain:

requests
beautifulsoup4
pandas

🚀 Usage

Run the script with:

python job_scraper.py --role "Cybersecurity Analyst" --remote --out
<img width="1612" height="190" alt="image" src="https://github.com/user-attachments/assets/476f02b2-e0e2-4dbb-b824-ac20a6fd8018" />


Arguments:

--role (required) → Job title or keywords to search.

--remote (optional) → Search for remote jobs worldwide (default is US-based).

--out (optional) → Save the results into a CSV file.

Example:

python scraper.py --role "Cybersecurity analyst" --remote

📊 Output

Jobs are saved in a CSV file named like if the name is not specified:

jobs_2025-09-06.csv


Sample columns:

Title	Business	Loc	url	Page	date
Cybersecurity Analyst	ACME Inc.	Remote	link	LinkedIN	2025-09-06
💡 Why I Built This


This project was:

A way to practice Python, web scraping, and data analysis.

A tool to accelerate my own remote job search.

🛠️ Next Steps:
add more webpages to search jobs such as indeed
add more parameters, to search for jobs based on experience level

📬 Contact

If you’re a recruiter or hiring manager looking for someone who’s resourceful and eager to learn — feel free to connect!

Rodolfo Daiub-rodolfodaiub2003@gmail.com

🌍 Interested in: Cybersecurity Analyst, Web Scraping, Remote Tech Roles

📧 Email: rodolfodaiub2003@gmail.com

💼 LinkedIn: https://www.linkedin.com/in/rodolfo-daiub-3a2b3928b/

