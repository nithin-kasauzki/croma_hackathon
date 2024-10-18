from text_scraper import scrape_source
from preprocessor import clean_text, tokenize_text
from gen_ai import ask_question, generate_insights

def run_pipeline(urls, questions, prompts):
    for url in urls:
        # Step 1: Scrape the source (HTML, PDF, or Excel)
        scraped_text = scrape_source(url)
        
        if scraped_text:
            if isinstance(scraped_text, str):  # Only preprocess text, not Excel
                # Step 2: Preprocess the text
                cleaned_text = clean_text(scraped_text)
                tokens = tokenize_text(cleaned_text)
                
                print(f"Cleaned Text from {url[:50]}: {cleaned_text[:300]}...")  # Show first 300 chars
                
                # Step 3: Answer questions and generate insights
                for question in questions:
                    answer = ask_question(cleaned_text, question)
                    print(f"Question: {question}\nAnswer: {answer}\n")

                for prompt in prompts:
                    insight = generate_insights(cleaned_text, prompt)
                    print(f"Prompt: {prompt}\nInsight: {insight}\n")
            else:
                print(f"Excel data extracted from {url[:50]}:\n{scraped_text}\n")
        else:
            print(f"Failed to scrape text from {url}")

# Define the URLs, questions, and prompts
urls = [
    "https://www.careratings.com/upload/CompanyFiles/PR/202401120134_Vijay_Sales_(India)_Private_Limited.pdf",  # PDF
    "https://example.com/somepage.html",  # HTML (replace with a real URL)
    "https://www.screener.in/screens/499306/reliance-company/?order=desc&page=46",  # Excel (replace with a real URL)
]

questions = [
    "What channels does the company use?",
    "What is the company's marketing strategy?",
]

prompts = [
    "Summarize the channels used",
    "Summarize the marketing strategy",
]

if __name__ == "__main__":
    run_pipeline(urls, questions, prompts)