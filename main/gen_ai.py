from transformers import T5Tokenizer, TFT5ForConditionalGeneration

# Load pre-trained T5 model and tokenizer for TensorFlow
model_name = "t5-small"
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = TFT5ForConditionalGeneration.from_pretrained(model_name)

# Define a context and question to test it
context = "Reliance Digital offers both online and in-store channels with omnichannel campaigns."
question = "What channels does Reliance Digital use?"

# Function to ask a question using the TensorFlow-based T5 model
def ask_question(context, question):
    input_text = f"question: {question} context: {context}"
    inputs = tokenizer(input_text, return_tensors='tf', max_length=512, truncation=True)
    outputs = model.generate(inputs['input_ids'], max_length=64, num_beams=4, early_stopping=True)
    answer = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return answer

# Example usage
answer = ask_question(context, question)
print(f"Question: {question}")
print(f"Answer: {answer}")

# if __name__ == "__main__":
#     example_text = """
#     Reliance Digital offers both online and in-store channels with a diverse product portfolio. Their marketing strategy includes
#     omnichannel campaigns. They provide after-sales services like recycling and financing options. The company uses AI and technology 
#     to enhance customer experience. 
#     """
    
#     question = "What channels does Reliance Digital use?"
#     answer = ask_question(example_text, question)
#     print(f"Question: {question}\nAnswer: {answer}\n")

#     prompt = "Summarize the marketing strategy"
#     insight = generate_insights(example_text, prompt)
#     print(f"Prompt: {prompt}\nInsight: {insight}\n")