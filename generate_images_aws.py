
import boto3
import json
import base64
import os

# Configuration
MODEL_ID = 'amazon.titan-image-generator-v2:0'
REGION_NAME = 'us-east-1' # Adjust if necessary

def generate_image(prompt, output_file):
    """
    Generates an image using AWS Bedrock (Titan Image Generator v2) and saves it to a file.
    """
    try:
        bedrock_runtime = boto3.client(
            service_name='bedrock-runtime', 
            region_name=REGION_NAME
        )
        
        # Payload for Amazon Titan Image Generator v2
        body = json.dumps({
            "taskType": "TEXT_IMAGE",
            "textToImageParams": {
                "text": prompt
            },
            "imageGenerationConfig": {
                "numberOfImages": 1,
                "height": 1024,
                "width": 1024,
                "cfgScale": 8.0,
                "seed": 0
            }
        })

        print(f"Generating image for: '{prompt}'...")
        response = bedrock_runtime.invoke_model(
            body=body, 
            modelId=MODEL_ID, 
            accept='application/json', 
            contentType='application/json'
        )

        response_body = json.loads(response.get('body').read())
        # The structure of response for Titan
        base64_image = response_body.get('images')[0]
        
        with open(output_file, 'wb') as f:
            f.write(base64.b64decode(base64_image))
            
        print(f"Successfully saved image to {output_file}")
        return True

    except Exception as e:
        print(f"Error generating {output_file}: {e}")
        return False

def main():
    # Prompt for Exercise 1: PC Components
    prompt_ex1 = (
        "Internal components of a desktop computer tower, realistic educational illustration. "
        "Visible components: Motherboard, CPU cooler fan, RAM sticks, Graphics card (GPU), "
        "Power Supply Unit (PSU) at bottom, Hard Drive (HDD) in bay. "
        "Clean cable management, side panel removed to show internals. High resolution, clear lighting."
    )
    
    # Prompt for Exercise 2: Peripherals
    prompt_ex2 = (
        "A modern student desk setup showing computer peripherals. "
        "Includes: a monitor displaying a document, a keyboard, a mouse, "
        "a pair of headphones resting on the desk or monitor, a USB flash drive plugged into a port (visible), "
        "and a printer sitting on the side of the desk. Realistic style, well-lit, educational context."
    )

    # Generate images
    generate_image(prompt_ex1, "image_ex1_pc_components.jpg")
    generate_image(prompt_ex2, "image_ex2_peripherals.jpg")

if __name__ == "__main__":
    main()
