# Imports
import requests
import csv

# Part 0 - Menu
while True:
    print("===== Lab 8 - Accessing data via APIs =====")
    print("1: Non-authenticated API: universities.hipolabs.com")
    print("2: Authenticated API: api.themoviedb.org")
    print("*: Exit")
    user_input = input("\n")

    if user_input == '1':
        # Part 1 - non-authenticated api
        print("===== Non-Authenticated API =====")

        """
            Documentation about the data source: HipoLabs is a software company that helps startups and many different companies with their tech
        and data needs. They are the hosts for this university list API we are accessing.

            API being used: This API is public with no access key, and it contains the domains, names and countries of
        most of the universities of the world. There is no pagination for this API, the pagination part of the project is completed on the second API.

            Login credentials: There are no login credentials needed for this public API.
        """

        # save the URL for later use
        url = "http://universities.hipolabs.com/search"

        # Try statement to ensure connection to API is successful
        try:
            # Send out the GET request to the API using the URL and requests library
            response = requests.get(url)
            # Convert the data into a python dictionary
            data = response.json()
            # Store the headers of the data into headers
            headers = data[0].keys()

            # Create the output file and write the data to it
            with open("data/output.csv", "w", newline="", encoding="utf-8") as csvFile:
                csvWriter = csv.DictWriter(csvFile, fieldnames=headers)
                csvWriter.writeheader()
                csvWriter.writerows(data)
            print("Data saved to data/output.csv successfully!")
        # Handle any unsuccessful connections to the API
        except requests.exceptions.RequestException as e:
            print('An error occurred:', e)

        input("\n...")

    elif user_input == '2':
        # Part 2 - authenticated api
        print("===== Authenticated API =====")

        """
            Documentation about the data source: The Movie Database (TMDB) is a community built movie and TV database.
        It is home to all types of data surrounding movies, tv shows, and media. It also has many APIs available with key access.

            API being used: We are using an API provided by TMDB that gives both basic and in depth information on specific Movies
        It requires and access key and has multiple pages which we will be accessing.

            Login credentials: api_key = bf0dcf314517c1b9a6b89ef9c9934636
        """

        # Store the base URL and API Key for later use
        base_url = "https://api.themoviedb.org/3/discover/movie"
        api_key = "bf0dcf314517c1b9a6b89ef9c9934636"

        # Define the parameters that will be added to the URL to grant access and allow pagination
        params = {"api_key": api_key, 'page': 1}

        # Counter variables and max variable to track while loop and set the limit to 10 pages max
        counter = 1
        Max = 10
        headers = {}
        all_movies = []

        # Try statement to ensure connection to API is successful
        try:  # Condition: continue looping until 10 pages have been pulled in
            while counter <= Max:
                # Send out the GET request to the API using the baseURL and params
                response = requests.get(base_url, params=params)
                # Convert the data into a python dictionary
                data = response.json()
                # Check that the data exists, if the JSON object was empty, break the loop
                if not data:
                    break
                # Get the headers from the data and store them into headers, and store the values into all movies
                results = data['results']
                # Since we do not cant overwrite each page, we need to store each page into the all movies list until we exit the loop, then we can output
                for movie in results:
                    all_movies.append(movie)
                headers = results[0].keys()
                # Iterate the page value in params to access the next page in the upcoming GET request
                params['page'] += 1
                # Iterate the counter variable before the next iteration
                counter += 1
            # Create the output file and write the data to it
            with open("data/output2.csv", "w", newline="", encoding="utf-8") as csvFile:
                csvWriter = csv.DictWriter(csvFile, fieldnames=headers)
                csvWriter.writeheader()
                csvWriter.writerows(all_movies)
            print("Data output to data/output2.csv successfully!")
        # Handle any unsuccessful connections to the API
        except requests.exceptions.RequestException as e:
            print('An error occurred:', e)

        input("\n...")
    else:
        print('Exiting...')
        break
