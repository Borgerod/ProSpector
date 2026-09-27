## Scraper Inventory

Here's a one-row-per-scraper breakdown:

| File | Target URL | Method | Captcha Handling |
|------|-----------|--------|------------------|
| **brreg.py** | `https://data.brreg.no/enhetsregisteret/api/enheter/lastned` | API (JSON download) | None |
| **_1881.py** | `https://www.1881.no/{industry}`, `https://www.regnskapstall.no/informasjon-om-{profile}` | HTML parse (BeautifulSoup) | None (checks for captcha in header but not actively handled) |
| **google.py** | `https://www.google.com/search?q={search_term}` | Selenium (webdriver) | **YES** – checks for "Systemene våre har oppdaget uvanlig trafikk" alarm, sets result to "CaptchaTriggered" |
| **gulesider.py** | `https://www.gulesider.no/{category}/bedrifter/{page_num}` | API (JSON from `__NEXT_DATA__` script tag) | None |
| **proff.py** | `https://proff.no/bransjesøk?q={industry}` | HTML parse (BeautifulSoup) | None |
| **industries_1881.py** | `https://www.1881.no/sitemap/industries-{letter}` | HTML parse (BeautifulSoup) | None |
| **industries_gulesider.py** | `https://www.gulesider.no/bedriftsregister/kategorier-{letter}` | HTML parse (BeautifulSoup) | None |
| **industries_proff.py** | `https://proff.no/industry/select?beginLetter={letter}` | HTML parse (BeautifulSoup) | None |

**Utilities:**
- **recaptcha_solver.py** – Selenium-based reCAPTCHA v2 image solver (instantiates but not actively used in current extractors; calls `check_exists_by_xpath()`, switches iframes, clicks tiles, submits)

Only **google.py** actively implements captcha detection (stops extraction and flags results); **recaptcha_solver.py** has image-solving logic available but unused.
