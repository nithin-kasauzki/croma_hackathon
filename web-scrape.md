Here’s a full example of how to implement **data collection and web scraping** for a competitive intelligence solution using Python. This example will cover basic web scraping using `requests` and `BeautifulSoup`, downloading and parsing PDFs using `PyPDF2`, and gathering structured data from APIs.

### Prerequisites

Make sure you have the following libraries installed:

```bash
pip install requests beautifulsoup4 pandas PyPDF2
```

### 1. **Web Scraping Using `requests` and `BeautifulSoup`**

This example scrapes data from a website such as a news or investor relations page to collect information about a competitor.

```python
import requests
from bs4 import BeautifulSoup

# Function to scrape a webpage
def scrape_webpage(url):
    # Send a request to the website
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the webpage content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract relevant information (for example, all text inside <p> tags)
        paragraphs = soup.find_all('p')
        text = ' '.join([para.get_text() for para in paragraphs])
        
        return text
    else:
        print(f"Failed to retrieve data from {url}")
        return None

# Example usage
url = "https://economictimes.indiatimes.com/markets/expert-view/expecting-one-of-the-best-years-due-to-strong-consumer-spending-nilesh-gupta-vijay-sales/articleshow/110869447.cms"
webpage_text = scrape_webpage(url)

# Output the scraped text
if webpage_text:
    print("Scraped text from the webpage:\n")
    print(webpage_text[:500])  # Display first 500 characters
```

### 2. **Downloading and Parsing PDFs Using `PyPDF2`**

Here’s how to download and extract text from a PDF file (such as annual reports):

```python
import requests
import PyPDF2
import os

# Function to download a PDF and save it
def download_pdf(pdf_url, save_path):
    response = requests.get(pdf_url)
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f"PDF saved to {save_path}")
    else:
        print(f"Failed to download PDF from {pdf_url}")

# Function to extract text from a PDF
def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        # Loop through all pages and extract text
        for page in range(len(reader.pages)):
            text += reader.pages[page].extract_text()
    return text

# Example usage
pdf_url = "https://www.ril.com/ar2022-23/pdf/RIL-Integrated-Annual-Report-2022-23.pdf"
save_path = "annual_report.pdf"

# Download the PDF
download_pdf(pdf_url, save_path)

# Extract text from the PDF
pdf_text = extract_text_from_pdf(save_path)

# Output the extracted text
print("Extracted text from PDF:\n")
print(pdf_text[:500])  # Display first 500 characters

# Clean up - remove the downloaded file if needed
os.remove(save_path)
```

### 3. **Scraping Data from an API**

Here’s how to collect data from an API (like a stock market API for investor presentations):

```python
import requests

# Function to fetch data from an API
def fetch_data_from_api(api_url):
    response = requests.get(api_url)
    
    if response.status_code == 200:
        data = response.json()  # Assuming the API returns JSON data
        return data
    else:
        print(f"Failed to fetch data from API {api_url}")
        return None

# Example usage
api_url = "https://api.example.com/competitor/data"  # Replace with actual API URL
api_data = fetch_data_from_api(api_url)

if api_data:
    print("Data fetched from API:\n")
    print(api_data)
```

### 4. **Storing Data in a CSV File**

Once you have the collected data, you can store it in a CSV format using the `pandas` library for easier analysis:

```python
import pandas as pd

# Example: Storing scraped data in a CSV file
data = {
    'Competitor': ['Reliance Digital', 'Vijay Sales'],
    'Source': ['Economics Times', 'Investor Relations'],
    'Extracted Text': [webpage_text, pdf_text]
}

# Convert dictionary to DataFrame
df = pd.DataFrame(data)

# Save DataFrame to CSV
df.to_csv('competitor_data.csv', index=False)

print("Data saved to competitor_data.csv")
```

### Summary of Code Components:

1. **Web Scraping**:
   - The `scrape_webpage` function scrapes text from a webpage.
   - It uses `requests` to send an HTTP request and `BeautifulSoup` to parse and extract text.

2. **PDF Download and Parsing**:
   - The `download_pdf` function downloads a PDF from a given URL.
   - The `extract_text_from_pdf` function extracts text from the PDF using `PyPDF2`.

3. **API Data Collection**:
   - The `fetch_data_from_api` function retrieves data from an API and parses it as JSON.

4. **Storing Data**:
   - The collected data is stored in a CSV file using the `pandas` library, which makes it easy to handle structured data.

### Things to Keep in Mind:
- **Ethical scraping**: Ensure that the websites you scrape do not have terms of service that prohibit scraping.
- **Error handling**: The code includes basic error handling to check if requests succeed before proceeding.
- **Data cleaning**: You may want to further clean the extracted text depending on your use case.

By combining these steps, you can build a robust data collection pipeline for the competitive intelligence solution.