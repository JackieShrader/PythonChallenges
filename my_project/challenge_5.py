import requests


def main() -> int:

    # Requests web url from user
    site_name = input("Please input the url of the website: ")

    # If the user enters a web url without a www or http will just add it
    # so that it can be used either way
    if not site_name.startswith('http'):
        if site_name.startswith('www'):
            site_name = "http://" + site_name
        else:
            site_name = "http://www." + site_name

    # gets the html info from the website
    html_content = requests.get(site_name)

    # creates the web download file then writes the html content to it
    with open('web-download.html', 'w') as file:
        file.write(html_content.text)

    return 0


if __name__ == '__main__':
    exit(main())
