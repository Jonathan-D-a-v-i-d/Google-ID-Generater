import art
import argparse
from ID import ID
import json
from colorama import Fore, Style
import sys
from tqdm import tqdm


def main():

    # - Printing Logo
    print(art.text2art("Google - ID - Generator"))
    print("by Jonathan David \n")

    # - Generating description and epilogue
    parser = argparse.ArgumentParser(
        description="Generate Google ID's with ease using Google-ID-Generator.",
        epilog="Thank you for using Google ID Generator. Happy ID generating!",
        formatter_class=argparse.RawDescriptionHelpFormatter
                                     
                                     
    )

    # Error handling to terminate program for negatie values
    def positive_int(value):
        ivalue = int(value)
        if ivalue <= 0:
            raise argparse.ArgumentTypeError(f"{value} is an invalid positive int value")
        return ivalue

    # - Adding options for male, female, and random ID generation types.
    parser.add_argument("-r", "--random", type=positive_int, default=0,
                        help="Generate RANDOM number of random IDs. Provide a positive integer.")
    parser.add_argument("-m", "--male", type=positive_int, default=0,
                        help="Generate MALE number of male IDs. Provide a positive integer.")
    parser.add_argument("-f", "--female", type=positive_int, default=0,
                        help="Generate FEMALE number of female IDs. Provide a positive integer.")
    parser.add_argument("-o", "--output", default="default",
                        help="Export the generated ID's to JSON format. Provide a filename to write to that file ('file'.json/'file'), or leave blank for standard output to terminal.")
    

    args = parser.parse_args()

    
    # - Error handling to show help if no values were entered
    if args.random == 0 and args.male == 0 and args.female == 0:
        parser.print_help()
        sys.exit(1)

    # - Setting aside list to append to for stdout or JSON
    ids = list()

    # Initializing ID class in ID.py, to take input params from users into functions ID.male(), ID.female() and ID.random()
    # The ID's are then all appended to var:ids, then will be processed for output options.
    if args.male >= 1:
        message = Fore.BLUE + Style.BRIGHT + "[+] Generating: " + Style.RESET_ALL + Fore.GREEN + Style.BRIGHT + f"{args.male}" + " Male accounts  " + Style.RESET_ALL
        for _ in tqdm(range(args.male), desc=message):
            ids.append(ID().male())

    if args.female >= 1:
        message = Fore.BLUE + Style.BRIGHT + "[+] Generating: " + Style.RESET_ALL + Fore.GREEN + Style.BRIGHT + f"{args.female}" + " Female accounts" + Style.RESET_ALL
        for _ in tqdm(range(args.female), desc=message):
            ids.append(ID().female())

    if args.random >= 1:
        message = Fore.BLUE + Style.BRIGHT + "[+] Generating: " + Style.RESET_ALL + Fore.GREEN + Style.BRIGHT + f"{args.random}" + " Random accounts" + Style.RESET_ALL
        for _ in tqdm(range(args.random), desc=message):
            ids.append(ID().random())



    ##########
    # OUTPUT #
    ##########
    total = (args.female + args.male + args.random)

    if args.output == 'default':
        total_message = Fore.BLUE + Style.BRIGHT + "[+] Totaling:   " + Style.RESET_ALL + Fore.GREEN + Style.BRIGHT + f"{total}" + " Google ID's" + Style.RESET_ALL + Fore.BLUE + Style.BRIGHT + " exported to "  +  Fore.LIGHTMAGENTA_EX + '"'  + Style.BRIGHT + "stdout" + '"' + Style.RESET_ALL
        print("\n" + "\n" + total_message + "\n" )
        print(json.dumps(ids, indent=4))  # Pretty print to stdout

    else:  # If a file path is provided
        with open(args.output, 'w') as f:
            json.dump(ids, f, indent=4)  # Write to the specified file as JSON
            total_message = Fore.BLUE + Style.BRIGHT + "[+] Totaling:   " + Style.RESET_ALL + Fore.GREEN + Style.BRIGHT + f"{total}" + " Google ID's" + Style.RESET_ALL + Fore.BLUE + Style.BRIGHT + " exported to path: " +  Fore.LIGHTMAGENTA_EX + '"'  + Style.BRIGHT + args.output + '"' + Style.RESET_ALL
            print("\n" + "\n" + total_message)


if __name__ == "__main__":
    main()







#import sys; print(sys.path)