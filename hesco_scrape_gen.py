import hashlib
import requests
from bs4 import BeautifulSoup
import csv

# Function to generate hash key using SHA256 algorithm
def generate_hash_key(data):
    sha256_hash = hashlib.sha256(data.encode()).hexdigest()
    return sha256_hash

# Function to fetch data from the open-source API
def fetch_data_from_api(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch data from the API.")
        return None

# Function to scrape URLs related to open source intelligence
def scrape_osint_urls(html_content):
    urls = []
    soup = BeautifulSoup(html_content, 'html.parser')
    # Your code to scrape URLs goes here
    # Example: Find all <a> tags with href containing "open source intelligence"
    for link in soup.find_all('a'):
        href = link.get('href')
        if href and "open source intelligence" in href:
            urls.append(href)
    return urls

# Function to store the data
def store_data(data):
    # Your code to store the data goes here
    print("Data stored successfully.")

# Function to save data to a CSV file
def save_to_csv(hash_key, osint_urls, data_urls):
    filename = "data.csv"
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Hash Key", "OSINT URLs", "Data URLs"])
        for i in range(len(hash_key)):
            writer.writerow([hash_key[i], osint_urls[i], data_urls[i]])
    print("Data saved to", filename)

# Main function
def main():
    # URL of the open-source API
    api_url = "https://api.osint_data.com/data"

    # Fetch data from the API
    data = fetch_data_from_api(api_url)
    if data:
        # Generate hash key for the data
        hash_key = generate_hash_key(str(data))

        # Store the data
        store_data(data)

        # Parse additional lines to find URLs related to open source intelligence
        html_content = "<html>...</html>"
        osint_urls = scrape_osint_urls(html_content)

        # Example list of data URLs
        data_urls = ["https://osint_data.com/data1", "https://osint_data.com/data2", "https://osint_data.com/data3"]

        # Print the hash key, URLs, and save to CSV file
        print("Hash Key:", hash_key)
        print("OSINT URLs:")
        for url in osint_urls:
            print(url)
        print("Data URLs:")
        for url in data_urls:
            print(url)

        # Save the data to a CSV file
        save_to_csv(hash_key, osint_urls, data_urls)

if __name__ == "__main__":
    main()
