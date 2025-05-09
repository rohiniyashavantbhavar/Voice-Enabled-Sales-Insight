import pyttsx3
import pandas as pd

# Text-to-Speech setup
engine = pyttsx3.init()

def speak(text):
    print("AI:", text)
    engine.say(text)
    engine.runAndWait()

# Simple logic to understand typed question
def process_query(query):
    query = query.lower()
    if "top" in query and "product" in query:
        return "top_products"
    elif "total" in query and "sales" in query:
        return "total_sales"
    else:
        return "unknown"

# Sample analysis functions
def get_top_products():
    df = pd.read_excel("sales_data.xlsx")
    latest_month = df['Month'].max()
    recent_data = df[df['Month'] == latest_month]
    top = recent_data.groupby('Product')['Revenue'].sum().sort_values(ascending=False).head(3)
    return top

def get_total_sales():
    df = pd.read_excel("sales_data.xlsx")
    return df['Revenue'].sum()

# Main interaction
def main():
    speak("Welcome to the Sales Assistant.")
    query = input("Type your question here: ")
    action = process_query(query)

    if action == "top_products":
        results = get_top_products()
        products = ", ".join(results.index.tolist())
        speak("Top 3 products are: " + products)

    elif action == "total_sales":
        total = get_total_sales()
        speak(f"The total sales are ₹{total:.2f}")

    else:
        speak("Sorry, I didn't understand your question.")

# Run the assistant
main()


# What are the top products?

# What is the total sales?
