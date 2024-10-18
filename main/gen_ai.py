from transformers import T5Tokenizer, T5ForConditionalGeneration

# Load T5 model and tokenizer
model_name = "t5-small"
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)

# Function to ask questions and generate answers
def ask_question(context, question):
    input_text = f"question: {question} context: {context}"
    
    inputs = tokenizer(input_text, return_tensors='pt', max_length=512, truncation=True)
    answer_ids = model.generate(inputs['input_ids'], max_length=150, num_beams=4, early_stopping=True)
    answer = tokenizer.decode(answer_ids[0], skip_special_tokens=True)
    
    return answer

# Function to generate insights based on a prompt
def generate_insights(context, prompt):
    input_text = f"{prompt}: {context}"
    inputs = tokenizer(input_text, return_tensors='pt', max_length=512, truncation=True)
    
    generated_ids = model.generate(inputs['input_ids'], max_length=150, num_beams=4, early_stopping=True)
    generated_text = tokenizer.decode(generated_ids[0], skip_special_tokens=True)
    
    return generated_text

if __name__ == "__main__":
    example_text = """
    Reliance Digital offers both online and in-store channels with a diverse product portfolio. Their marketing strategy includes
    omnichannel campaigns. They provide after-sales services like recycling and financing options. The company uses AI and technology 
    to enhance customer experience. 
    """
    
    question = "What channels does Reliance Digital use?"
    answer = ask_question(example_text, question)
    print(f"Question: {question}\nAnswer: {answer}\n")

    prompt = "Summarize the marketing strategy"
    insight = generate_insights(example_text, prompt)
    print(f"Prompt: {prompt}\nInsight: {insight}\n")