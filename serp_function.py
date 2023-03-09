
import json
import urllib.request
from serpapi import GoogleSearch
import socket

def serpapi_get_google_images(queries=[], path="", verbose=True, max_images=300):
    '''
    Takes in list of queries and downloads google search images of those queries using SerpAPI. 
    Downloads to user-designated folder. 
    For my personal case, path should be "C:/Users/Polar/Downloads/AI_Camp/images/"
    max_images is the maximum number of images scraped for each query.
    '''
    image_results = []
    
    for query_no, query in enumerate(queries, start=1):
        params = {
            "q": query,
            "tbm": "isch",
            "hl": "en",
            "gl": "us",
            "api_key": "1c1295b0213adb928a4cc601381e9e0b365c4df865373c8a37a47cf7b14becc2",
            "num":"100",
            "ijn": 0                        
        }

        search = GoogleSearch(params)         # where data extraction happens

        images_is_present = True
        while images_is_present:
            if len(image_results) >= query_no * max_images:  
                images_is_present = False   
                break                         # Break after collecting max_images images
            
            results = search.get_dict()       # JSON -> Python dictionary

            # checks for "Google hasn't returned any results for this query."
            if "error" not in results:
                for index, image in enumerate(results["images_results"]):
                    if image["original"] not in image_results:
                        image_results.append(image["original"])
                        if len(image_results) == query_no * max_images:
                            continue

                # update to the next page
                params["ijn"] += 1
            else:  
                if verbose: 
                    print(results["error"])
                images_is_present = False
    
    # -----------------------
    # Downloading images

    for index, image in enumerate(image_results, start=1):
        if verbose:
            print(f"Downloading image number {index}...")
        
        socket.setdefaulttimeout(15) #timeout after 15 seconds

        try:
            opener=urllib.request.build_opener()
            opener.addheaders=[("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.63")]
            urllib.request.install_opener(opener)
            urllib.request.urlretrieve(image, f"{path}/img_{index}.jpg")
        except:
            if verbose:
                print(f"Failed to download. Skipping image {index}.")
                
    if verbose:
        print(json.dumps(image_results, indent=2))
        print(len(image_results))