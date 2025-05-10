import requests
from PIL import Image
from io import BytesIO

def download_envelope_image():
    # URL of an envelope with seal image from iStock
    url = "https://media.istockphoto.com/id/1293280172/photo/envelope-with-seal-isolated-on-white-background.jpg?s=612x612&w=0&k=20&c=cU4hCm2hhX00GHV9pWF_3T2chDmkYQ43p-cvjsUITBM="
    
    try:
        # Download the image
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for bad status codes
        
        # Open the image using PIL
        image = Image.open(BytesIO(response.content))
        
        # Save the image
        image.save("envelope_decorated.png")
        print("Image downloaded successfully as 'envelope_decorated.png'")
        
    except Exception as e:
        print(f"Error downloading image: {e}")

if __name__ == "__main__":
    download_envelope_image() 