# Amazon-Product-Details-Scraper

This Python script is designed to scrape product details from Amazon product pages and store them in a JSON file. Here's a detailed description of its functionality:

Fetching HTML Content: The script starts by defining a function fetch_html_tree(url) to fetch the HTML content of a given URL. It uses urllib.request to send a GET request to the URL and retrieves the HTML content. Then, it parses the HTML content into an HTML tree structure using lxml.etree.

Extracting Product Details: Another function scrape_amazon_product_details(url) is defined to scrape specific product details from the HTML tree using XPath expressions. It extracts various details such as product name, model number, rating, number of ratings, price, image URL, and additional information like screen size, brand name, supported internet services, etc.

Main Function: The main function main() contains an array of URLs of Amazon product pages. It iterates over each URL, calls the scrape_amazon_product_details() function to scrape product details, and prints them. It also appends the product details to a list named all_product_details.

Writing to JSON File: After scraping details for all URLs, the script writes all the collected product details into a JSON file named "all_product_details.json" using the json.dump() function.

Error Handling: Error handling is implemented throughout the script to catch exceptions that might occur during HTML fetching, parsing, or scraping. If an error occurs, it prints an error message to the console.

Overall, this script provides a systematic approach to extract and store product details from multiple Amazon product pages, facilitating tasks such as data analysis or comparison.
