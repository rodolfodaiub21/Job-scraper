import requests 
from bs4 import BeautifulSoup
import pandas as pd
import time
import random
import argparse
from datetime import datetime
class JobScraper():
    def __init__(self):
            #Headers to  avoid Bot detection
            self.headers_list = [
            {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0...'},  # Chrome en Windows
            {'User-Agent': 'Mozilla/5.0 (Macintosh...'},  # Safari en Mac
            {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64...'}  # Chrome en Linux
        ]
    def scrape_linkedin(self,role,remote=False,max_pages=3):
          print("Searching on LinkedIN...")
          jobs=[]
          base_url="https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search"

          #Search parameters
          keywords = f"keywords={role.replace(' ', '%20')}"  
          location="location=Worldwide" if remote else 'location=United%20States'
          remote_param="f_WT=2" if remote else "" #remote parameter for linkedin
          print("Searching on pages in Linkedin:...")

          for page in range(max_pages):
                
                try:
                    start=page*25
                    url=f"{base_url}?{keywords}&{location}&{remote_param}&start={start}"    
                    #RANDOM choice of headers to avoid detection.
                    headers=random.choice(self.headers_list)
                    response=requests.get(url,headers=headers)
                    soup=BeautifulSoup(response.text,'html.parser')      
                    job_cards=soup.find_all('div',class_='base-search-card__info')
                    link_job=soup.find_all('a',class_=lambda x:x and 'base-card__full-link' in x.split())
                    print(len(job_cards),len(link_job))
                    for card,link in zip(job_cards,link_job):
                          #print(f"reading card: {i} -> {card} ")
                          try:
                                print('trying...')
                                title=card.find('h3',class_='base-search-card__title').text.strip()
                                company=card.find('a',class_='hidden-nested-link').text.strip()
                                location= card.find('span',class_='job-search-card__location').text.strip()
                                url_tag = link
                                url = url_tag['href'].split('?')[0] if url_tag else None
                                job_data= {
                                      'Title': title,
                                      'Business':company,
                                      'Loc':location,
                                      'url':url,
                                      'Page':'LinkedIN',
                                      'date':datetime.now().strftime("%Y-%m-%d")
                                }
                                print("Data to append from Linkedin: ",job_data)
                                jobs.append(job_data)
                          except Exception as e:
                                print(F'Exception: ...{e}')   
                                continue
                    time.sleep(random.uniform(1,3))

                except Exception as e:
                      print("Error during scraping through Linkedin,",e)
                      #print("Response: ",response.text)
                      continue
          return jobs

    
    def scrape_all_sources(self,role,remote=False,max_pages=2):
          all_jobs=[]
          linkedin =self.scrape_linkedin(role,remote,max_pages)
          all_jobs.extend(linkedin)
          #indeed=self.Scrape_indeed(role,remote,max_pages)
          #all_jobs.extend(indeed)
          return all_jobs
    def save_to_csv(self,jobs,filename=None):
            if not filename:
                timestamp= datetime.now().strftime('%Y-%M-%d')
                filename= f'jobs_{timestamp}.csv'
            df=pd.DataFrame(jobs)
            df.to_csv(filename,index=False,encoding='UTF-8')
            print(f'Found {len(jobs)} in the webpages now saved at: {filename}')
def main():
      parser=argparse.ArgumentParser(description='Job Searcher')
      parser.add_argument('--role',type=str,required=True,help='Role or job to search')
      parser.add_argument('--remote',action='store_true',help='Search for remote role')
      parser.add_argument('--out',action='store_true',help='Save with csv name')
      args=parser.parse_args()
      scraper=JobScraper()
      jobs=scraper.scrape_all_sources(args.role,args.remote)
      if jobs:
            output_file=scraper.save_to_csv(jobs,args.out)
            df=pd.DataFrame(jobs)
            print('file created')
            print('Short analysis:')
            print('Jobs founded:',len(jobs))
if __name__=='__main__':
      main()