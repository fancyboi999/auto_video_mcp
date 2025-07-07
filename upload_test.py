import requests
import os

# --- Configuration ---
# Replace with your actual authorization token
YOUR_AUTH_TOKEN = "a541cc8ccbce480c"
# Path to the file you want to upload
FILE_TO_UPLOAD = "/Users/mini/Downloads/05f1b018-0cc4-4907-a6e9-87bc24cc9b37_speed.mp3"

# Base URL for the API
BASE_API_URL = "https://hfw-api.hifly.cc"

def get_upload_url(file_extension: str) -> dict:
    """
    Gets a pre-signed upload URL from the API.
    """
    url = f"{BASE_API_URL}/api/v2/hifly/tool/create_upload_url"
    headers = {
        "Authorization": f"Bearer {YOUR_AUTH_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "file_extension": file_extension
    }

    print(f"Requesting upload URL for extension: {file_extension}")
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error getting upload URL: {e}")
        if hasattr(e, 'response') and e.response is not None:
            print(f"Response content: {e.response.text}")
        return {}

def upload_file(upload_url: str, content_type: str, file_path: str):
    """
    Uploads a file to the given pre-signed URL.
    """
    if not os.path.exists(file_path):
        print(f"Error: File not found at {file_path}")
        return

    print(f"Uploading file: {file_path} to {upload_url}")
    try:
        with open(file_path, 'rb') as file:
            headers = {
                "Content-Type": content_type
            }
            response = requests.put(upload_url, headers=headers, data=file)
            response.raise_for_status()  # Raise an exception for HTTP errors
            print(f"File upload successful! Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error uploading file: {e}")
        if hasattr(e, 'response') and e.response is not None:
            print(f"Response content: {e.response.text}")

def main():
    # Extract file extension from the file path
    file_extension = os.path.splitext(FILE_TO_UPLOAD)[1].lstrip('.')
    if not file_extension:
        print("Could not determine file extension. Please check FILE_TO_UPLOAD path.")
        return

    # Step 1: Get upload URL
    upload_info = get_upload_url(file_extension)

    if upload_info and upload_info.get("upload_url") and upload_info.get("content_type"):
        upload_url = upload_info["upload_url"]
        content_type = upload_info["content_type"]
        file_id = upload_info.get("file_id", "N/A")
        request_id = upload_info.get("request_id", "N/A")

        print(f"\nSuccessfully obtained upload URL:")
        print(f"  Upload URL: {upload_url}")
        print(f"  Content Type: {content_type}")
        print(f"  File ID: {file_id}")
        print(f"  Request ID: {request_id}")

        # Step 2: Upload the file
        upload_file(upload_url, content_type, FILE_TO_UPLOAD)
    else:
        print("\nFailed to get valid upload URL information. Aborting file upload.")

if __name__ == "__main__":
    main()
