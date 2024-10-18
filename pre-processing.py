import re
import nltk
import spacy
import pandas as pd
from nltk.tokenize import word_tokenize

# Download necessary NLTK data
nltk.download('punkt')

# Load spaCy model for Named Entity Recognition (NER)
nlp = spacy.load('en_core_web_sm')

# 1. Data Cleaning Function
def clean_text(text):
    text = re.sub(r'\s+', ' ', text)  # Remove extra spaces
    text = re.sub(r'<.*?>', '', text)  # Remove HTML tags
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    return text.lower()

# 2. Preprocess Text (Tokenization)
def preprocess_text(text):
    cleaned_text = clean_text(text)
    tokens = word_tokenize(cleaned_text)
    return tokens

# 3. Named Entity Recognition (NER)
def extract_entities(text):
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities

# 4. Categorization Logic with Expanded Keyword Lists
def categorize_extracted_data(text, competitor_name):
    # Expanded Keywords for categorization
    channels_keywords = ['store', 'online', 'b2b', 'omnichannel', 'ecommerce', 'retail', 'physical store', 'brick-and-mortar', 'showroom']
    product_keywords = ['category', 'product', 'private labels', 'assortment', 'stock', 'inventory', 'skus', 'brand', 'product mix']
    marketing_keywords = ['media', 'advertising', 'marketing', 'campaign', 'promotion', 'branding', 'content marketing', 'social media', 'tv ads', 'digital ads', 'seo', 'sem']
    affordability_keywords = ['financing', 'exchange', 'affordability', 'pricing', 'credit', 'installments', 'discounts', 'loan', 'offers', 'buyback']
    after_sales_keywords = ['after sales', 'services', 'recycling', 'customer service', 'support', 'repair', 'warranty', 'technical support', 'maintenance', 'return policy']
    supply_chain_keywords = ['supply chain', 'supplier', 'network', 'delivery', 'logistics', 'warehouse', 'inventory management', 'distribution', 'partnership']
    technology_keywords = ['technology', 'ai', 'automation', 'digital', 'blockchain', 'machine learning', 'iot', 'cloud', 'analytics', 'big data', 'platform', 'crm']

    categories = {
        'Competitor': competitor_name,
        'Channels': '',
        'Product Portfolio': '',
        'Marketing Strategy': '',
        'Affordability Offerings': '',
        'After Sales': '',
        'Supply Chain': '',
        'Technology Use': '',
        'Geographical Presence': '',
        'Store Formats': '',
        'Financial Performance': '',
        'Customer Feedback': '',
        'Strategic Initiatives': ''
    }

    tokens = preprocess_text(text)

    # Categorize based on presence of specific keywords
    if any(keyword in tokens for keyword in channels_keywords):
        categories['Channels'] = " ".join([word for word in tokens if word in channels_keywords])
    
    if any(keyword in tokens for keyword in product_keywords):
        categories['Product Portfolio'] = " ".join([word for word in tokens if word in product_keywords])
    
    if any(keyword in tokens for keyword in marketing_keywords):
        categories['Marketing Strategy'] = " ".join([word for word in tokens if word in marketing_keywords])
    
    if any(keyword in tokens for keyword in affordability_keywords):
        categories['Affordability Offerings'] = " ".join([word for word in tokens if word in affordability_keywords])
    
    if any(keyword in tokens for keyword in after_sales_keywords):
        categories['After Sales'] = " ".join([word for word in tokens if word in after_sales_keywords])
    
    if any(keyword in tokens for keyword in supply_chain_keywords):
        categories['Supply Chain'] = " ".join([word for word in tokens if word in supply_chain_keywords])
    
    if any(keyword in tokens for keyword in technology_keywords):
        categories['Technology Use'] = " ".join([word for word in tokens if word in technology_keywords])

    # NER extraction for geographical presence, financials, and other specific entities
    entities = extract_entities(text)
    for entity, label in entities:
        if label == 'GPE':  # Geographical entity
            categories['Geographical Presence'] += entity + " "
        if label == 'ORG' and 'store' in entity.lower():  # Organization that may represent store formats
            categories['Store Formats'] += entity + " "
        if label in ['MONEY', 'PERCENT']:  # Financial figures
            categories['Financial Performance'] += entity + " "
        if label == 'PERSON':  # Customer feedback may be tied to reviews
            categories['Customer Feedback'] += entity + " "

    return categories

# 5. Apply Preprocessing, NER, and Categorization to Competitors' Data

# Sample extracted data for each competitor (replace with your actual extracted data)
extracted_data = {
    'Reliance Digital': """
        Reliance Digital offers both online and in-store channels with a diverse product portfolio, including private labels. 
        Their marketing strategy includes omnichannel campaigns across digital media platforms. They provide after-sales services 
        like recycling and financing options, with a strong focus on AI and technology to enhance customer experience. 
        They have stores across major Indian cities, and their supply chain includes strong supplier relationships.
    """,
    'Vijay Sales': """
        Vijay Sales focuses on in-store and B2B sales, offering affordable financing options and a well-curated product portfolio. 
        Their marketing strategy includes advertising through local media and digital campaigns. Their customer feedback is generally positive, 
        and they offer after-sales services. Their supply chain is optimized for quick deliveries, and their store formats vary by region.
    """
}

# List to hold structured data for all competitors
structured_data = []

# Iterate through each competitor's extracted data and categorize it
for competitor, data in extracted_data.items():
    categorized_data = categorize_extracted_data(data, competitor)
    structured_data.append(categorized_data)

# 6. Store the Structured Data in a CSV

# Convert the structured data into a DataFrame
df = pd.DataFrame(structured_data)

# Save the structured data into a CSV file
df.to_csv('enhanced_competitor_data.csv', index=False)

print("Enhanced structured data saved to enhanced_competitor_data.csv")

# Display the first few rows of the structured DataFrame
print(df.head())