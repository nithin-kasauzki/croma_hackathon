import requests
from bs4 import BeautifulSoup
import PyPDF2
import pandas as pd
import io

# Function to scrape HTML, PDF, or Excel based on the URL
def scrape_source(url):
    try:
        if url.lower().endswith('.pdf'):
            # Handle PDF files
            return scrape_pdf(url)
        elif url.lower().endswith('.xls') or url.lower().endswith('.xlsx'):
            # Handle Excel files
            return scrape_excel(url)
        else:
            # Assume it's an HTML page
            return scrape_html(url)
    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return None

# Function to scrape PDF files
def scrape_pdf(url):
    response = requests.get(url)
    response.raise_for_status()
    pdf_content = io.BytesIO(response.content)
    reader = PyPDF2.PdfReader(pdf_content)
    
    text = ""
    for page_num in range(len(reader.pages)):
        text += reader.pages[page_num].extract_text()
    return text

# Function to scrape HTML pages
def scrape_html(url):
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, 'html.parser')
    paragraphs = soup.find_all('p')
    text = ' '.join([para.get_text() for para in paragraphs])
    return text

# Function to download Excel files and extract data
def scrape_excel(url):
    response = requests.get(url)
    response.raise_for_status()
    
    # Load the Excel file into a pandas DataFrame
    excel_data = pd.read_excel(io.BytesIO(response.content), engine='openpyxl')
    return excel_data.to_string()  # Convert the DataFrame to a string

# Example usage
# if __name__ == "__main__":
#     urls = [
#         "https://example.com/somefile.pdf",
#         "https://example.com/somepage.html",
#         "https://example.com/somefile.xlsx"
#     ]
    
#     for url in urls:
#         scraped_data = scrape_source(url)
#         print(f"Scraped Data from {url[:50]}: {scraped_data[:500] if isinstance(scraped_data, str) else scraped_data}\n")