import re
import nltk
import spacy
import pandas as pd
from nltk.tokenize import word_tokenize

# Download necessary NLTK data
nltk.download('punkt')

# Load spaCy model for Named Entity Recognition (NER)
nlp = spacy.load('en_core_web_sm')

### 1. Data Cleaning ###

# Function to clean the extracted text
def clean_text(text):
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text)
    
    # Remove HTML tags if any
    text = re.sub(r'<.*?>', '', text)
    
    # Remove special characters and punctuation (optional, depends on the context)
    text = re.sub(r'[^\w\s]', '', text)
    
    # Convert to lowercase
    return text.lower()

# Example usage: Apply cleaning to the extracted text from web scraping or PDF parsing
def preprocess_text(text):
    cleaned_text = clean_text(text)
    
    # Tokenization: Split text into words (tokens)
    tokens = word_tokenize(cleaned_text)
    
    return tokens

### 2. Named Entity Recognition (NER) ###

# Function to extract entities using spaCy
def extract_entities(text):
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities

### 3. Data Structuring and Categorization ###

# Function to categorize extracted data based on predefined categories
def categorize_extracted_data(text, competitor_name):
    categories = {
        'Competitor': competitor_name,
        'Channels': '',  # (store, online, B2B)
        'Product Portfolio': '',  # Categories, assortment, private labels
        'Marketing Strategy': '',  # Media presence, strategy
        'Affordability Offerings': '',  # Financing, exchange
        'After Sales': '',  # Services, customer service, recycling
        'Supply Chain': '',  # Supplier relationships, delivery promises
        'Technology Use': '',  # Use of technology
        'Geographical Presence': '',  # Stores by location, additions
        'Store Formats': '',  # Formats, space for advertising
        'Financial Performance': '',  # Capex, working capital, sales per sq ft
        'Customer Feedback': '',  # NPS, reviews
        'Strategic Initiatives': '',  # Investments, acquisitions, etc.
    }

    # Tokenized words
    tokens = preprocess_text(text)

    # Example logic to categorize the tokens based on keywords
    # (In a real-world scenario, you'd implement more complex logic for categorization)
    if 'store' in tokens or 'b2b' in tokens:
        categories['Channels'] = text
    if 'marketing' in tokens or 'media' in tokens:
        categories['Marketing Strategy'] = text
    if 'affordability' in tokens or 'financing' in tokens:
        categories['Affordability Offerings'] = text
    if 'technology' in tokens:
        categories['Technology Use'] = text

    # Return categorized information
    return categories

### 4. Applying Preprocessing, NER, and Categorization ###

# Sample extracted data for each competitor (This is where you'd use your real extracted data)
extracted_data = {
    'Reliance Digital': "Reliance Digital offers a wide range of products both in stores and online. Their marketing strategy includes large media presence. They have strong after-sales services including recycling. Technology like AI is widely used.",
    'Vijay Sales': "Vijay Sales is known for its B2B and store presence. They focus on affordability with financing options. Their geographical presence has expanded with new stores. Technology use is moderate."
}

# List to hold structured data for all competitors
structured_data = []

# Iterate through each competitor's extracted data and preprocess it
for competitor, data in extracted_data.items():
    # Clean, tokenize, and extract entities from the data
    cleaned_text = clean_text(data)
    entities = extract_entities(cleaned_text)

    # Categorize the extracted information
    categorized_data = categorize_extracted_data(data, competitor)
    
    # Add the categorized data to the structured data list
    structured_data.append(categorized_data)

### 5. Store the Structured Data in a CSV ###

# Convert the structured data to a DataFrame
df = pd.DataFrame(structured_data)

# Save the DataFrame to a CSV file
df.to_csv('structured_competitor_data.csv', index=False)

print("Structured data saved to structured_competitor_data.csv")

### 6. Display Sample Data ###

# Display the first few rows of the structured DataFrame
print(df.head())

'''
Breakdown of the Code:

	1.	Text Cleaning:
	•	The clean_text function removes unnecessary spaces, HTML tags, punctuation, and converts the text to lowercase for uniformity.
	2.	Tokenization:
	•	The preprocess_text function tokenizes the cleaned text into words (tokens) using the nltk.word_tokenize method.
	3.	Named Entity Recognition (NER):
	•	The extract_entities function uses the spaCy NER model to identify and extract entities such as store locations, financial figures, and competitor names.
	4.	Data Structuring and Categorization:
	•	The categorize_extracted_data function takes the cleaned and tokenized text, then categorizes it into key business areas based on keywords. The categories include channels, product portfolio, marketing strategy, supply chain, etc. You can enhance this logic with more complex keyword matching or even machine learning models for more accurate categorization.
	5.	Storing Data in CSV:
	•	After categorizing the extracted data, it is stored in a pandas.DataFrame and saved to a CSV file for later analysis. Each competitor’s data is organized into specific categories such as marketing strategy, geographical presence, etc.
	6.	Output:
	•	The final structured data is saved in a CSV file (structured_competitor_data.csv), which can be used for further analysis, visualization, or input into your AI-powered solution.
'''