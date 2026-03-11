import openai

def interpret_question(question):
    prompt = f"""
    Convert the user's question into a simple query format.
    
    Examples:
    'Which city has the highest laptop sales?' -> 'top 1 laptop sales by city'
    'Show me top five phone sales in Mumbai' -> 'top 5 sales in mumbai'

    Question: {question}
    """

    response = openai.ChatCompletion.create(
        model = "gpt-4o-mini",
        messages = [{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content