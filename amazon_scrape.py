import re
import urllib.request
from lxml import etree
import json


def fetch_html_tree(url):
    try:
        # Send a GET request to the URL and retrieve the HTML content
        response = urllib.request.urlopen(url)
        html_content = response.read()

        # Parse the HTML content
        tree = etree.HTML(html_content)
        return tree
    except Exception as e:
        print("An error occurred while fetching the HTML tree:", e)
        return None
    
def extract_element(tree, index, xpath):
    try:
        return tree.xpath(xpath)[index].strip()
    except IndexError:
        return None
    

def scrape_amazon_product_details(url):
    final_dict = {}
    additional_info = {}
    try:
        # Fetch and parse the HTML content
        tree = fetch_html_tree(url)
        if tree is None:
            return None
        
        # Extracting product details using XPath
        final_dict["Name"] = extract_element(tree, 0, "//span[contains(@id,'productTitle')]/text()")
        Model_Numer = re.search(r'\((.*?)\)',final_dict["Name"])
        if Model_Numer is not None: final_dict["Model_Numer"] = Model_Numer.group(1)
#         final_dict["Model_Numer"] = re.search(r'\((.*?)\)',final_dict["Name"]).group(1)
        rating_node = extract_element(tree, 0, "//span[contains(@data-hook,'rating-out-of-text')]/text()")
        if rating_node: final_dict["Rating"] = float(rating_node.split("out of")[0])
        review_node = extract_element(tree,0,"//span[contains(@id,'acrCustomerReviewText')]/text()")
        if review_node: final_dict["No_of_rating"] = float(re.sub('\D', '', review_node.split(" ")[0]))
        price_node = extract_element(tree,0,"//span[contains(@class,'a-price')]//span/text()")
        if price_node : final_dict["price"] = float(price_node.split("$")[1])
        final_dict["image"] = extract_element(tree,0,"//img[contains(@id,'landingImage')]/@src")
        
        additional_info["screen_size"] = extract_element(tree,1,"//tr[contains(@class,'po-display.size')]//span/text()")
        additional_info["brand_name"] = extract_element(tree,1,"//tr[contains(@class,'po-brand')]//span/text()")
        additional_info["supported_internet_services"] = extract_element(tree,1,"//tr[contains(@class,'po-supported_internet_services')]//span/text()")
        additional_info["display_technology"] = extract_element(tree,1,"//tr[contains(@class,'po-display.technology')]//span/text()")
        additional_info["product_dimension"] = extract_element(tree,1,"//tr[contains(@class,'po-item_depth_width_height')]//span/text()")
        additional_info["resolution"] = extract_element(tree,1,"//tr[contains(@class,'po-resolution')]//span/text()")
        additional_info["refresh_rate"] = extract_element(tree,1,"//tr[contains(@class,'po-refresh_rate')]//span/text()")
        additional_info["special_feature"] = extract_element(tree,1,"//tr[contains(@class,'po-special_feature')]//span/text()")
        additional_info["model_name"] = extract_element(tree,1,"//tr[contains(@class,'po-model_name')]//span/text()")
        additional_info["included_components"] = extract_element(tree,1,"//tr[contains(@class,'po-included_components')]//span/text()")
        final_dict["additional-information"] = additional_info
        
        return final_dict
    except Exception as e:
        print("An error occurred:", e)
        return None
    
def main():
    # Array of URLs of the Amazon product pages
    urls = ["https://www.amazon.com/dp/B09ZLTMWWH","https://www.amazon.com/dp/B092Q1TRJC","https://www.amazon.com/dp/B0BCMND272","https://www.amazon.com/dp/B0BTTVRWPR","https://www.amazon.com/dp/B09N6F9NV3","https://www.amazon.com/dp/B0BC9Z81P6","https://www.amazon.com/dp/B09N719G17","https://www.amazon.com/dp/B0B3GTSQ9Q","https://www.amazon.com/dp/B08T6F8YBH","https://www.amazon.com/dp/B0C1J1TWQM","https://www.amazon.com/dp/B0C1JDMVDM","https://www.amazon.com/dp/B0CMDH95GG","https://www.amazon.com/dp/B094RJ41WY","https://www.amazon.com/dp/B08PDTM9ZD","https://www.amazon.com/dp/B094RKDNMZ","https://www.amazon.com/dp/B09WQC4XJQ","https://www.amazon.com/dp/B09ZLTWXST","https://www.amazon.com/dp/B0C1HZX7M1","https://www.amazon.com/dp/B0BVMY9NCN","https://www.amazon.com/dp/B09N6ZRH6C","https://www.amazon.com/dp/B0CLFD3NF5","https://www.amazon.com/dp/B0CMDJ8TK3","https://www.amazon.com/dp/B092Q1W365","https://www.amazon.com/dp/B0CLFLHR7K","https://www.amazon.com/dp/B0CCBYJQ7D","https://www.amazon.com/dp/B0C1J2SVKD","https://www.amazon.com/dp/B0BVMWSQVY","https://www.amazon.com/dp/B0BCMRRKRX","https://www.amazon.com/dp/B07CL4GLQW","https://www.amazon.com/dp/B0C1J1FS2C","https://www.amazon.com/dp/B09WQRYD5N","https://www.amazon.com/dp/B0B3H6JPYZ","https://www.amazon.com/dp/B0C1J5RZD8","https://www.amazon.com/dp/B0C1HZ9HCM","https://www.amazon.com/dp/B07YXH57B8","https://www.amazon.com/dp/B0BVMYL399","https://www.amazon.com/dp/B0BVXDPZP3","https://www.amazon.com/dp/B0C1HYMT79","https://www.amazon.com/dp/B0BMK5B4TF","https://www.amazon.com/dp/B0CMDHXZF8","https://www.amazon.com/dp/B0C1HZ8QF4","https://www.amazon.com/dp/B09RS56X9S","https://www.amazon.com/dp/B09RRYWQ59","https://www.amazon.com/dp/B09JHSVTSD","https://www.amazon.com/dp/B09WQDRL83","https://www.amazon.com/dp/B0BVMYQXGZ","https://www.amazon.com/dp/B0BVMXZ32B","https://www.amazon.com/dp/B09VCVGH7B","https://www.amazon.com/dp/B0B3HG269B","https://www.amazon.com/dp/B0CLFSWK9V"]
    
    # List to store scraped product details
    all_product_details = []

    # Scrape product details for each URL
    for url in urls:
        print("Scraping product details for:", url)
        product_details = scrape_amazon_product_details(url)
        if product_details:
            # Append product details to the list
            all_product_details.append(product_details)

            # Print product details
            for key, value in product_details.items():
                print(key + ":", value)
            print("\n***************************************************************************\n")

    # Write all product details to a JSON file
    with open("all_product_details.json", 'w') as f:
        json.dump(all_product_details, f, indent=4)
        print("All product details written to: all_product_details.json")

if __name__ == "__main__":
    main()


