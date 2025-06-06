# Simple Crypto Advisor Chatbot
print("Welcome to Crypto Advisor!")
print("I can tell you about: Bitcoin, Ethereum, Cardano")

while True:
    # Ask user which crypto they want info about
    crypto = input("\nWhich cryptocurrency? (or type 'quit' to exit): ")
    
    if crypto.lower() == 'quit':
        print("Goodbye!")
        break
    
    # Give simple advice based on the crypto
    if crypto.lower() == "bitcoin":
        print("Bitcoin: Popular but uses lots of energy. Price is rising.")
    elif crypto.lower() == "ethereum":
        print("Ethereum: Stable price. Medium energy use.")
    elif crypto.lower() == "cardano":
        print("Cardano: Rising price. Energy efficient.")
    else:
        print("Sorry, I don't know that one. Try Bitcoin, Ethereum or Cardano.")