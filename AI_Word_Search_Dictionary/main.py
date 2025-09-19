from openai import OpenAI 

# put your key 
#API_KEY = "your openai api_key here"
#client = OpenAI(api_key=API_KEY)

# create your openai client
client = OpenAI()

# select model name
MODEL_NAME = "gpt-4o-mini" 

# word search function
def word_search(word, mode="all"):
  """Fetch word info using OpenAI"""
  
  if mode == "definition":
    prompt = f'Define the word "{word}" in one simple sentence.'
  
  elif mode == "synonyms":
    prompt = f'Give 3 synonyms and 3 antonyms for the word "{word}".'
  
  elif mode == "examples":
    prompt = f'Give 2 example sentences using the word "{word}".'
  
  else: # all
    prompt = (
      f'For the word "{word}", provide:\n' 
      "1. A simple definition.\n"
      "2. Two example sentences.\n"
      "3. Two synonyms and two antonyms.\n"
      )
  
  # response generation
  response = client.responses.create(model = MODEL_NAME, input=prompt)
  return response.output_text.strip()

# displays availbale options related to word search
def show_menu():
  print("PrashBOT: ")
  print("=== AI Word Dictionary ===")
  print("1. Definition")
  print("2. Synonyms & Antonyms")
  print("3. Example Sentences")
  print("4. All-in-one")
  print("5. History")
  print("0. Exit")

# github: github.com/prashant-g0
# main function to power the code
def main():
  # history keeper
  history = []
  while True:
    show_menu()
    choice = input("PrashBOT: Choose an option: ").strip() # takes input

    if choice == "0": # exit command
      print("\nPrashBOT: GoodBye!")
      break
    
    if choice == "5": # show history command
      if history:
        print("\nPrashBOT: Search History:")
        for i,word in enumerate(history, 1):
          print(f"{i}. {word}")
      else:
        print("\nPrashBOT: No history yet.")
      continue

    # Word search commands
    if choice in {"1", "2", "3", "4"}:
      word = input("PrashBOT: Enter a word: ").strip()
      if not word:
        print("PrashBOT: Please enter a valid word!")
        continue

      history.append(word)
      mode_map = {
        "1":"definition",
        "2":"synonyms",
        "3":"antonyms",
        "4":"all"
      }
      mode = mode_map[choice]

      print("\nPrashBOT: Searching with OpenAI.....\n")
      # result display
      try:
        result = word_search(word, mode)
        print("PrashBOT: \n" + result + "\n")
      except Exception as e:
        print("PrashBOT: Error calling api key:", str(e))
    
    else:
      print("\nPrashBOT: Invalid option. Try again.")

# insta: @prash.coder
# Start point of code
if __name__ == "__main__":
  main()