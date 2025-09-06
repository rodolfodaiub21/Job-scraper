def Scrape_indeed(self,role,remote=False,max_pages=3):
          print("Searching on indeed")
          jobs=[]
          base_url="https://www.indeed.com/jobs"
          params={
                'q':role,
                'l':'remote' if remote else '',
                'start':0
          }
          for page in range(max_pages):
                
                try:
                      params['start']=page*10
                      headers= random.choice(self.headers_list)
                      response= requests.get(base_url,headers=headers)
                      soup = BeautifulSoup(response.text,'html.parser')
                      job_cards= soup.find_all('div',class_='job_seen_beacon')
                      for card in job_cards:
                            try:
                                  title=card.find('h2',class_='JobTitle').text.strip()
                                  company=card.find('span',class_='companyName').text.strip()
                                  location=card.find('div',class_='companyLocation').text.strip()
                                  url = "https://www.indeed.com" + card.find('a')['href']
                                  job_data= {
                                      'Title': title,
                                      'Business':company,
                                      'Loc':location,
                                      'url':url,
                                      'Page':'indeed',
                                      'date':datetime.now().strftime("%Y-%m-%d")
                                }
                            except Exception as e:
                                  print('Error on page: ',e )
                                  continue
                            time.sleep(random.uniform(1,3))
                            jobs.append(job_data)              

                except Exception as e:
                      print("Error on page: ",e)
                      continue
          return jobs