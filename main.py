import os
import requests

def ubuntu_image_fetcher():
    print("--- Ubuntu Image Fetcher ---")
    print("I am because we are. Let's fetch a resource from the community.")
    
    # 1. Prompt the user for a URL
    url = input("Please enter the image URL: ").strip()
    
    if not url:
        print("Error: No URL provided.")
        return

    # 2. Create the directory 'Fetched_Images' 
    # The assignment requires exist_ok=True
    folder_name = "Fetched_Images"
    os.makedirs(folder_name, exist_ok=True)

    try:
        print(f"Connecting to {url}...")
        
        # 3. Request the image (Fetch)
        # stream=True is good practice, but standard get is fine for this assignment
        response = requests.get(url, timeout=10)
        
        # 4. Check for HTTP errors (404, 500, etc.)
        response.raise_for_status() 
        
        # 5. Extract filename or generate one
        # We split the URL by '/' and take the last part
        filename = url.split("/")[-1]
        
        # If the filename looks empty or doesn't have an extension, give it a default name
        if not filename or "." not in filename:
            filename = "downloaded_image.jpg"
            
        # Create the full path (Fetched_Images/filename)
        save_path = os.path.join(folder_name, filename)

        # 6. Save the image in binary mode ('wb')
        with open(save_path, 'wb') as file:
            file.write(response.content)
            
        print(f"\nSuccess! The image has been saved to: {save_path}")
        print("Ubuntu Spirit: Resource successfully shared and preserved.")

    except requests.exceptions.MissingSchema:
        print("\nError: The URL format is incorrect. Did you forget 'http://' or 'https://'?")
    except requests.exceptions.HTTPError as err:
        print(f"\nHTTP Error occurred: {err}")
    except requests.exceptions.ConnectionError:
        print("\nConnection Error: Could not connect to the server. Check your internet.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")

if __name__ == "__main__":
    ubuntu_image_fetcher()