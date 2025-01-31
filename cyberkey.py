import os
import random
import time
from itertools import product

# Banner
BANNER = """
\033[1;32m
 ██████╗██╗   ██╗██████╗ ███████╗██╗  ██╗██╗   ██╗
██╔════╝██║   ██║██╔══██╗██╔════╝██║  ██║╚██╗ ██╔╝
██║     ██║   ██║██████╔╝███████╗███████║ ╚████╔╝ 
██║     ██║   ██║██╔═══╝ ╚════██║██╔══██║  ╚██╔╝  
╚██████╗╚██████╔╝██║     ███████║██║  ██║   ██║   
 ╚═════╝ ╚═════╝ ╚═╝     ╚══════╝╚═╝  ╚═╝   ╚═╝   
 🔒 CyberKey - Advanced Wordlist Generator 🔒
         Author: CyberKallan (@imarjunarz)
\033[0m
"""

# Loading effect
def loading_animation(text):
    print(f"\n\033[1;34m{text}\033[0m", end="")
    for _ in range(5):
        time.sleep(0.4)
        print(".", end="", flush=True)
    print("\n")

# Read words from a file
def read_file(filename):
    path = os.path.join("names_data", filename)
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as file:
            return [line.strip() for line in file if line.strip()]
    return []

# Generate wordlist
def generate_wordlist(options, output_file):
    loading_animation("Generating your advanced wordlist")
    
    selected_data = []
    
    if "1" in options:
        selected_data.append(read_file("First.txt"))
    if "2" in options:
        selected_data.append(read_file("Middle.txt"))
    if "3" in options:
        selected_data.append(read_file("Last.txt"))
    if "4" in options:
        selected_data.append(read_file("Petnames.txt"))
    if "5" in options:
        selected_data.append(read_file("Badwords.txt"))
    if "6" in options:
        selected_data.append(read_file("Symbols.txt"))
    if "7" in options:
        selected_data.append([str(num) for num in range(1000, 9999)])
    if "8" in options:
        selected_data.append(read_file("Indiannumber.txt"))
    if "9" in options:
        selected_data.append(read_file("CommonPasswords.txt"))
    if "10" in options:
        selected_data.append(read_file("LoverNames.txt"))
    if "11" in options:
        selected_data.append(read_file("KeralaNames.txt"))
    if "12" in options:
        selected_data.append(read_file("IndianGirlsNames.txt"))

    # Generate combinations
    wordlist = ["".join(combo) for combo in product(*selected_data)]
    
    # Save to file
    with open(output_file, "w", encoding="utf-8") as file:
        file.write("\n".join(wordlist))
    
    print(f"\n\033[1;32m✅ Wordlist generated successfully: {output_file}\033[0m")
    print("\n📢 Follow @imarjunarz on Instagram for more hacking tools!")

# Main menu
def main():
    os.system("clear")
    print(BANNER)

    print("\n\033[1;36m[+] Select Wordlist Options:\033[0m")
    print(" 1️⃣  Indian Names")
    print(" 2️⃣  Middle Names")
    print(" 3️⃣  Last Names")
    print(" 4️⃣  Pet Names")
    print(" 5️⃣  Bad Words")
    print(" 6️⃣  Symbols")
    print(" 7️⃣  Random Numbers (1000-9999)")
    print(" 8️⃣  Indian Phone Numbers")
    print(" 9️⃣  Common Passwords")
    print(" 🔟  Lover Names")
    print(" 1️⃣1️⃣  Kerala Names")
    print(" 1️⃣2️⃣  Indian Girls Names")
    
    choices = input("\n🔹 Enter multiple options (comma-separated): ").split(",")

    # Custom output filename
    output_name = input("\n📝 Enter output file name (default: wordlist.txt): ")
    output_file = output_name if output_name else "wordlist.txt"

    generate_wordlist(choices, output_file)

if __name__ == "__main__":
    main()

