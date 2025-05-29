import requests
import os
from dotenv import load_dotenv

load_dotenv()

PINATA_API_KEY = os.getenv("PINATA_API_KEY")
PINATA_SECRET_KEY = os.getenv("PINATA_SECRET_KEY")
PINATA_ENDPOINT = "https://api.pinata.cloud/pinning/pinFileToIPFS"

def upload_to_ipfs(file_path: str) -> str:
    """Upload a file to IPFS using Pinata"""
    if not PINATA_API_KEY or not PINATA_SECRET_KEY:
        raise ValueError("Pinata API credentials not found in environment variables")
        
    headers = {
        "pinata_api_key": PINATA_API_KEY,
        "pinata_secret_api_key": PINATA_SECRET_KEY
    }
    
    with open(file_path, "rb") as f:
        files = {"file": f}
        response = requests.post(PINATA_ENDPOINT, files=files, headers=headers)
        
    if response.status_code == 200:
        ipfs_hash = response.json()["IpfsHash"]
        return f"ipfs://{ipfs_hash}"
    else:
        raise Exception(f"Failed to upload to IPFS: {response.text}")
        
def upload_metadata_folder(folder_path: str = "metadata") -> dict:
    """Upload all JSON files in the metadata folder"""
    results = {}
    for filename in os.listdir(folder_path):
        if filename.endswith(".json"):
            file_path = os.path.join(folder_path, filename)
            try:
                ipfs_uri = upload_to_ipfs(file_path)
                results[filename] = ipfs_uri
                print(f"Uploaded {filename} to {ipfs_uri}")
            except Exception as e:
                print(f"Failed to upload {filename}: {str(e)}")
    return results
    
if __name__ == "__main__":
    # Upload metadata files
    print("Uploading metadata files to IPFS...")
    upload_metadata_folder()
    
    # Upload images
    print("\nUploading images to IPFS...")
    upload_metadata_folder("images") 