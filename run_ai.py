import os
import shutil
from gradio_client import Client

def generate():
    # GitHub se token lena
    my_token = os.getenv("HF_TOKEN")
    
    try:
        print("Model se connect ho raha hai...")
        # Galti fix: 'hf_token' ki jagah sirf 'token' likha hai
        client = Client("ByteDance/AnimateDiff-Lightning", token=my_token)

        print("Video generation shuru ho gayi hai... (1-3 minute lag sakte hain)")
        
        # Video generate karne ki request
        result = client.predict(
            prompt="A majestic lion running in the snow, cinematic, 4k",
            infer_steps="6-Step",
            api_name="/generate"
        )

        if result:
            # Result ko save karna
            shutil.copy(result, 'output_video.mp4')
            print("SUCCESS: Video ban gayi hai!")
        else:
            print("ERROR: Result khaali aaya.")
            exit(1)

    except Exception as e:
        print(f"ASLI ERROR YE HAI: {str(e)}")
        exit(1)

if __name__ == "__main__":
    generate()
