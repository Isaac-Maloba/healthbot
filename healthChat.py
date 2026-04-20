import pandas as pd

# Load your data to a dataframe
df = pd.read_csv("health_data.csv")
# print(df)

print("Clara: Hello there! How are you feeling today?😊 I am your Health Assistant, Clara. Feel free to ask me anything concerning your health❤️‍🩹.")

while True:
    # 1. Get the user input and store it in a variable
    user_text = input("\n You: ").lower()

    # Chekc if the user wants to exit
    if user_text == "quit":
        print("Clara: Good bye for now👋. Have a wonderful day😊!")
        break

    # Create a variable that will store the details structure in the csv
    found_answer = False

    # Come up with a loop that loops through the entire dataframe created before
    for index, row in df.iterrows():
        # Clean up the key words from the csv rows
        keywords_list = str(row['Keywords']).split(',')

        # Belwow we check every keyword in the given row (Keywords)
        for word in keywords_list:
            clean_word = word.strip().lower()

            # If the keyword is inside the user's sentence
            if clean_word in user_text:
                print("Clara:", row["Response"])
                found_answer = True
                break # Stop looking at other key words

        if found_answer:
            break # Stop looking at other answers since we already found a match

    # If we went through the entire csv and never find a match of the keywords, we need to display a message to the user
    if not found_answer:
        print("Clara: My apologies😓: currently, I have not been trained on an appropriate response to such a query😔. But you can try asking another question...😁")

