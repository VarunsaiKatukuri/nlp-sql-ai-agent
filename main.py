from database import initialize_database, run_query
from nlp_to_sql import generate_sql

def main():

    print("\nAI DATA ANALYST AGENT STARTED")
    print("Type 'exit' to quit\n")

    # Initialize database
    conn = initialize_database()

    while True:

        question = input("Ask your question: ")

        if question.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        # convert natural language -> SQL
        simplified_query = interpret_question(user_question)
        sql_query = generate_sql(simplified_query)

        if sql_query is None:
            print("Sorry, I couldn't understand your question.\n")
            continue

        print("\nGenerate SQL:")
        print(sql_query)

        try:
            results = run_query(conn, sql_query)
            print("\nResult:")
            for row in results:
                print(row)
        except Exception as e:
            print("Error executing query:", e)
        
        print()

if __name__ == "__main__":
    main()