from bs4 import BeautifulSoup
import requests
import csv

# Parse our Html file

# with open('simple.html') as html_file:
#   soup = BeautifulSoup(html_file, 'lxml')

# print(soup.prettify()) # "prettify()" is to arrange the data more structured


# match = soup.title.text # To actually get the first 'title' of the page

# match = soup.find('div', class_='footer') # The "find" method is to find a particular element

# for article in soup.find_all('div', class_='article'): # This provides the first class with name "article" 
  
#   headline = article.h2.a.text # After instantiating the var in charge of the info, we can decide to use another var to now access data from it

#   print(headline)

#   summary = article.p.text
#   print(summary)

#   print() # TO have a blank line between the articles


# source = requests.get('https://lucky-gumption-ac20fd.netlify.app/').text # This is to get the info from the website

# soup = BeautifulSoup(source, 'lxml')


# # Don't loop over a list if you are just trying to work on one container, instead extract it

# vidpreview = soup.find('div', class_='video-info')
# video_author = vidpreview.find('p', class_='video-title')
# print(video_author.text)



source = requests.get("https://lucky-gumption-ac20fd.netlify.app/").text
soup = BeautifulSoup(source, 'lxml')

csv_file = open('youtube-clone.csv', 'w') # We open up a file to save the data
csv_writer = csv.writer(csv_file) # Then we set a variable to call the "writer" func from 'csv' to write into the file
csv_writer.writerow(['Video Title', 'Youtube Link']) # Then we set the Headers for the data, their rows, the rows must match the amount of fields of data we want to write into the csv file 

for video_preview in soup.find_all('div', class_='video-preview'): # Sometimes only the container name is needed, not necessary to look for the class
 
  try:
    video_title = video_preview.find('p', class_='video-title')
    print(video_title.text)
    
    vid_src = video_preview.find('a')['href'] # To specify on that element specific atttribute
    print(vid_src)


    # Trying to get the Video Id, not necessarily the link
    vid_id = vid_src.split('/')[3] # This is to split the element based on what we specify on, e.g ("/")

    # Doing another split on the "?" to get the ID alone
    vid_id_complete = vid_id.split("?")[0]

    # print(vid_id_complete)

    # This is used to create a youtube-link based on the ID of the video
    yt_link = f"https://youtube.com/watch?v={vid_id_complete}"

  except Exception as e: # To put the error as a variable
    yt_link = None # Just to let them know we didn't get the link 
  
  print(yt_link)

  print()

  csv_writer.writerow([video_title.text, yt_link]) # This fields must correllate with the csv "writerow" we set at the top

csv_file.close() # And after all conditions are met, we close the csv file outside the "for-loop"



  # video_info = video_preview.find('p', class_='video-title')
  # print(video_info.text)

  # headline = container.h2.text
  # print(headline)




