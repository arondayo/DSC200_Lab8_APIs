
"""
    Documentation about the data source: HipoLabs is a software company that helps startups and many different companies with their tech
and data needs. They are the hosts for this university list API we are accessing.

    API being used: This API is public with no access key, and it contains the domains, names and countries of
most of the universities of the world. There is no pagination for this API, the pagination part of the project is completed on the second API.

    Login credentials: There are no login credentials needed for this public API.
"""

#Import the requests and csv libraries to help access and store the data from the API
import requests
import csv

#save the URL for later use
url = "http://universities.hipolabs.com/search"

#Try statement to ensure connection to API is successful
try:
    #Send out the GET request to the API using the URL and requests library
    response = requests.get(url)
    # Convert the data into a python dictionary
    data = response.json()
    #Store the headers of the data into headers
    headers = data[0].keys()

    #Create the output file and write the data to it
    with open("output.csv", "w", newline="", encoding="utf-8") as csvFile:
        csvWriter = csv.DictWriter(csvFile, fieldnames=headers)
        csvWriter.writeheader()
        csvWriter.writerows(data)
    print("Data saved to output.csv successfully!")
#Handle any unsuccessful connections to the API
except requests.exceptions.RequestException as e:
    print('An error occurred:', e)



