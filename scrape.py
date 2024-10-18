import requests
from bs4 import BeautifulSoup
import PyPDF2
import os
import pandas as pd

### 1. Web Scraping Using BeautifulSoup ###

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

# Example usage for web scraping
url = "https://economictimes.indiatimes.com/markets/expert-view/expecting-one-of-the-best-years-due-to-strong-consumer-spending-nilesh-gupta-vijay-sales/articleshow/110869447.cms"
webpage_text = scrape_webpage(url)

### 2. Downloading and Parsing PDFs ###

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

# Example usage for PDF download and extraction
pdf_url = "https://www.ril.com/ar2022-23/pdf/RIL-Integrated-Annual-Report-2022-23.pdf"
save_path = "annual_report.pdf"

# Download the PDF
download_pdf(pdf_url, save_path)

# Extract text from the PDF
pdf_text = extract_text_from_pdf(save_path)

# Clean up - remove the downloaded file if needed
os.remove(save_path)

### 3. Fetching Data from an API ###

# Function to fetch data from an API
def fetch_data_from_api(api_url):
    response = requests.get(api_url)
    
    if response.status_code == 200:
        data = response.json()  # Assuming the API returns JSON data
        return data
    else:
        print(f"Failed to fetch data from API {api_url}")
        return None

# Example usage for API data fetching
# Replace this with an actual API URL for competitive intelligence
api_url = "https://api.example.com/competitor/data"
api_data = fetch_data_from_api(api_url)

### 4. Storing Data in a CSV File ###

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

### Example Output ###

if webpage_text:
    print("Sample Webpage Text:\n", webpage_text[:500])  # Display first 500 characters

if pdf_text:
    print("Sample PDF Text:\n", pdf_text[:500])  # Display first 500 characters


    '''
    Explanation:
    Explanation of the Full Code:

	1.	Web Scraping:
	•	The scrape_webpage function uses requests to fetch a webpage and BeautifulSoup to extract text inside the <p> tags.
	•	This is used to collect competitor insights from articles, interviews, or press releases.
	•	Example: Scraping a news article about Vijay Sales.
	2.	PDF Downloading and Parsing:
	•	The download_pdf function downloads a PDF file (e.g., an annual report) and saves it locally.
	•	The extract_text_from_pdf function extracts text from the PDF using PyPDF2, allowing you to analyze financial reports or other documents.
	•	Example: Downloading and parsing Reliance’s annual report.
	3.	API Data Collection:
	•	The fetch_data_from_api function fetches data from an API that returns JSON. You would replace the placeholder api_url with an actual API endpoint.
	•	This can be used for gathering structured competitor data from sources like financial aggregators, stock market platforms, or other business intelligence sources.
	4.	Storing Data in a CSV:
	•	The scraped text from webpages and PDFs is stored in a structured format (CSV) using the pandas library.
	•	This allows you to maintain a dataset that can later be analyzed for competitive intelligence insights.

Output:

	•	The script will:
	•	Scrape text from the provided webpage.
	•	Download the PDF, extract the text, and delete the file after extraction.
	•	Fetch API data (if a valid API URL is used).
	•	Store the collected data into a CSV file (competitor_data.csv).
	•	Additionally, it will print a sample of the scraped text from both the webpage and the PDF for verification.

Considerations:

	•	Error handling: The code contains basic error handling to deal with cases where the request might fail.
	•	Ethical scraping: Ensure you have permission to scrape content from the sites, and always respect robots.txt files.
	•	Further analysis: The data can later be used for summarization or analysis by your Generative AI solution for competitive intelligence.

Let me know if you’d like to expand or modify any parts of this!
    '''