from bs4 import BeautifulSoup
import requests
import time

for year in range(2000, 2010): # 2000 - 2009 are the years for which we want the documents

    html = requests.get(f"https://www.supremecourt.gov/oral_arguments/argument_transcript/{year}").text # Gets the HTML for the given year's transcript page

    soup = BeautifulSoup(html, 'html.parser')

    case_links = []

    case_codes = []

    base_url = "https://www.supremecourt.gov/oral_arguments/" # This is the base URL for where each transcript is stored

    # The next part parses the HTML to find all 'a' elements where the href link includes argument_transcripts
    # This is how we get a list of all of the HTML elements with URLs that link to a transcript
    for a in soup.find_all('a', href=True):
        if "argument_transcripts" in a["href"]:
            # This appends the full URL with the PDF to case_links and the case code to case_codes
            case_links.append(base_url + a["href"][3:])
            case_codes.append(a.string)

            print(base_url + a["href"][3:])

    for index, link in enumerate(case_links):
        # Makes a request to get the PDF from each link and saves it to its corresponding folder while setting its name to {id}.pdf
        time.sleep(1)
        r = requests.get(link)
        with open(f'transcripts/{year}/{case_codes[index]}.pdf', 'wb') as f:
            f.write(r.content)
        
        print(f"{case_codes[index]} - {r.status_code}")