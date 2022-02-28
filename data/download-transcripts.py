from bs4 import BeautifulSoup
import requests

for year in range(2000, 2009):

    html = requests.get(f"https://www.supremecourt.gov/oral_arguments/argument_transcript/{year}").text

    soup = BeautifulSoup(html, 'html.parser')

    case_links = []

    case_codes = []

    base_url = "https://www.supremecourt.gov/oral_arguments/"

    for a in soup.find_all('a', href=True):
        if "argument_transcripts" in a["href"]:
            case_links.append(base_url + a["href"][3:])
            case_codes.append(a.string)


    for index, link in enumerate(case_links):
        r = requests.get(link)
        with open(f'transcripts/{year}/{case_codes[index]}.pdf', 'wb') as f:
            f.write(r.content)