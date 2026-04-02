import requests
from bs4 import BeautifulSoup

base = "https://www.zaubacorp.com"

url = "https://www.zaubacorp.com/companysearchresults/CHENNAI"
res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")

rows = soup.find_all("tr")

for row in rows:
    a = row.find("a")

    if a:  # only rows with company link
        name = a.text.strip()
        full_link = base + a["href"]

        print("Opening:", name)  # ✅ DEBUG (you'll see progress)

        r = requests.get(full_link)
        s = BeautifulSoup(r.text, "html.parser")

        reg_no = None

        for tr in s.find_all("tr"):
            tds = tr.find_all("td")
            if len(tds) == 2 and "Registration Number" in tds[0].text:
                reg_no = tds[1].text.strip()

        print("RESULT →", name, ":", reg_no)