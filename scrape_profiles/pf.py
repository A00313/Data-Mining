from apify_client import ApifyClient
import pandas as pd
import re

def extract_hashtags(text):
    """
    Uses a regular expression to find hashtags in the given text.
    """
    return re.findall(r"#\w+", text)

def main():
    # Initialize the ApifyClient with your API token
    client = ApifyClient("apify_api_uAld09vHtSawWpRbxDD6WxUgRJKTxm2zmDqX")
    
    # Read the list of TikTok profile usernames from a file (one username per line)
    with open("/Users/ammaralhussaini/Desktop/School/Spring 2025/Data Mining/Data-Mining/scrape_profiles/usernames.txt", "r") as f:
        usernames = [line.strip() for line in f if line.strip()]
    results = []

   
    for username in usernames:
        print(f"Scraping profile: {username}")
        # Prepare the Actor input with the correct key "profiles" (as a list)
        run_input = {
            "profiles": [username],
            "resultsPerPage": 100,  # adjust as needed
        }
        
        # Run the Actor and wait for it to finish
        run = client.actor("clockworks/free-tiktok-scraper").call(run_input=run_input)
        
        dataset_id = run.get("defaultDatasetId")
        if not dataset_id:
            print(f"No dataset found for profile {username}. Skipping...")
            continue

        print("💾 Check your data here: https://console.apify.com/storage/datasets/" + dataset_id)
        
        # Iterate over all items in the dataset
        for item in client.dataset(dataset_id).iterate_items():
            # Depending on the structure, the video description might be in "text" or "desc"
            description = item.get("text", "") or item.get("desc", "")
            hashtags = extract_hashtags(description)
            video_id = item.get("id", "")
            video_url = item.get("videoUrl", "")
            results.append({
                "username": username,
                "video_id": video_id,
                "video_url": video_url,
                "hashtags": hashtags
            })
    
    # Create a Pandas DataFrame from the results and save to CSV
    df = pd.DataFrame(results)
    df.to_csv("tiktok_hashtags.csv", index=False)
    print("Data saved to tiktok_hashtags.csv")

if __name__ == "__main__":
    main()