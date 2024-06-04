import requests
import sys
import os

def remove_background(api_key, input_path, output_path):
    url = 'https://api.remove.bg/v1.0/removebg'
    headers = {
        'X-Api-Key': "4pRdM8TsUoiL5vDfatLgMRcy"
    }
    
    with open(input_path, 'rb') as file:
        files = {
            'image_file': file
        }
        data = {
            'size': 'auto'
        }
        response = requests.post(url, headers=headers, files=files, data=data)

    if response.status_code == requests.codes.ok:
        with open(output_path, 'wb') as out_file:
            out_file.write(response.content)
        print(f"Background removed successfully! Output saved at {output_path}")
    else:
        print("Error:", response.status_code, response.text)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python remove_bg.py <api_key> <input_path> <output_path>")
        sys.exit(1)
    
    api_key = sys.argv[1]
    input_path = sys.argv[2]
    output_path = sys.argv[3]
    
    if not os.path.isfile(input_path):
        print(f"Error: The input file {input_path} does not exist.")
        sys.exit(1)
    
    remove_background(api_key, input_path, output_path)
