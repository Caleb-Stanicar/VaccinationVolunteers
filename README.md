# VaccinationVolunteers
We noticed that old folks we knew were having trouble figuring out if they were eligible for the coronavirus vaccine, and even then had to navigate a complicated registration process online. Furthermore, most resources for determining eligibility and signing up are only in English, a further challenge to people who can't speak or read English. 

## Solution & details
Our solution has two main components. The first is a robust reminder apparatus which pulls data on each state's vaccine eligibility criteria and generates a robocall to be sent out to everyone on our calling list in that state. The code performing this functionality is found in the VaccineNotification.py script, whiel the VaccineMessages directory holds a custom-generated message for each state. VaccinationVolunteerScript.sql sorts the phone numbers by state in order to add them to a robocall list with the correct message.

The second aspect of our solution is a website and training program where volunteers can sign up to help old folks navigate the vaccination process. After signing up, the volunteers are assigned several states they must learn the registration process of before receiving calls. This state assignment is executed by the AssignState.py script. Volunteers register on the website (stored in the various html documents in this repository), where they can find a link to a Google form asking when they can volunteer and what languages they speak fluently. [Website found here](https://vaccinationvolunteers.bss.design/index.html)

## Status
This project won first prize at the 2021 DevFest Hackathon at Columbia University!
