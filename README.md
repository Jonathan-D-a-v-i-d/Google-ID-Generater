# Google-ID-Generater
![image](https://github.com/Jonathan-D-a-v-i-d/Google-ID-Generater/assets/44530894/de2a207e-39cc-4e2d-97d0-921d773829f1)

This is an ID generator modeled for use in creating ID's suitable for Google account creation. It is built in Python and uses flavorings of both functional programming and object oriented programming to input parameters to form a base ID structure, then initialize a dictionary object of a full Google user account using class initializations.



# Prerequisites
To use Google ID Generator, you will need the following:

Python 3.6 or higher installed on your system. You can check your current version by typing python --version in your command line interface (CLI).

The following Python libraries installed on your system:

* Faker: This library is used to generate fake data for the IDs.
* argparse: This library is used for command-line option and argument parsing.
* art: This library is used for ASCII art generation.
* tqdm: This library is used for progress bar generation.
* colorama: This library is used for colorful command line outputs.
* json: This library is used for generating the final output as a JSON file.
  
If these libraries are not installed, you can install them via pip by running:
pip install faker argparse art tqdm colorama json in your CLI.


# Usage
Clone the repository to your local machine: git clone <repo-link>.

Navigate to the project directory in your terminal: cd <path-to-project>.

Run the script with the desired arguments. Here are some examples:

To generate 10 random IDs, run: python Google-ID-Generator.py --random 10

To generate 5 male IDs and 7 female IDs, run: python Google-ID-Generator.py --male 5 --female 7

To generate 5 male IDs and export them to a JSON file, run: python Google-ID-Generator.py --male 5 --output filename.json

Here is the full list of command-line arguments that you can use:

-r or --random: To generate a specific number of random IDs.
-m or --male: To generate a specific number of male IDs.
-f or --female: To generate a specific number of female IDs.
-o or --output: To specify an output file. If no file is specified, the output will be written to stdout.


# Security-Testing
Any form of security testing done through web scraping automatically yeilds to data manipulation of kinds.
In the OWSAP world of web applcation attacks, if you just look statistically at how many platforms are supported 
in their account creation by Google accounts, you'd be shocked and yet not surprised since you already knew Google 
to be the biggest big data collector :)

Test the security posture of an organization's http session load balancing protection with HTTP Session DDOS. 
Large organizations will usually place load balancers as the first public facing IP of an FQDN, so that sessions and 
requests can be properly streamed to ensure low latency. The reverse of this inclination for proper functioning 
is a DDOS attack, so sessions are open forcing the servers to accept them and if the speed of the requests along side
the amount of the connections (associated of course with some IP proxying so that you won't get blocked by a predictable
WAF rule) trumps the load balancing capacity/architecture for request management, then the application will get delayed
intensively, or crash. 

The benefit of implementing this as a security research measure towards an organization with written consent as per 
cyber security consulting, is that organization anti-DDOS measures/implementations can be tested in real time, just like 
any other offensive security research initiative, where vulnerabilities and weaknesses are elucidated for cyber posture
improvement.

 
# APP Testing 
To test certain areas of your application for proper functionality
in the SDLC, you need fake accounts to then drive the API's with 
to see that everything works, before you actuallt launch the API 
so that real users can benefit off of your functionality. 

It's like building the blueprint for a building before you build it, 
for the safety af the people who are going to be interacting with it.

This can be done through batch operations, mass account management, and 
account automation - it doesn't really matter. What matters is that your 
blueprint is tested with real data objects before you let real people represent
those data objects.





# - Reminder
Remember, this is just the cannon fodder, not the fighting.

Meaning, all further use cases of actual API / WebDriver implementation
will need to be coded in seperate modules, but can all import the JSON 
export of the users created for Google accounts through this code-up.
