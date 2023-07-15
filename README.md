# Google-ID-Generater
This is an ID generator modeled for use in creating ID's suitable for Google account creation. It is built in Python and uses flavorings of both functional programming and object oriented programming to input parameters to form a base ID structure, then initialize a dictionary object of a full Google user account using class initializations.




  __  __          _____               ____              __  _                ___ __      
 / / / /__ ___   / ___/__ ____ ___   / __/_ _____  ____/ /_(_)__  ___  ___ _/ (_) /___ __
/ /_/ (_-</ -_) / /__/ _ `(_-</ -_) / _// // / _ \/ __/ __/ / _ \/ _ \/ _ `/ / / __/ // /
\____/___/\__/  \___/\_,_/___/\__/ /_/  \_,_/_//_/\__/\__/_/\___/_//_/\_,_/_/_/\__/\_, / 
                                                                                  /___/  
# ###################################
# APP Testing through API Integration
# ###################################
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


# ################
# Security-Testing
# ################
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
cyber security consulting, is that organization anit-DDOS measures/implementations can be tested in real time, just like 
any other offensive security research initiative, where vulnerabilities and weaknesses are elucidated for cyber posture
improvement.


# - Reminder
Remember, this is just the cannon fodder, not the fighting.

Meaning, all further use cases of actual API / WebDriver implementation
will need to be coded in seperate modules, but can all import the JSON 
export of the users created for Google accounts through this code-up.
