import os
import shutil
from gradio_client import Client

def generate():
    hf_token = os.getenv("HF_TOKEN")
    try:
        # Hum ek fast aur aksar chalne wala model use kar rahe hain
        print("Model se connect ho raha hai...")
        client = Client("ByteDance/AnimateDiff-Lightning", hf_token=hf_token)

        print("Video generation start ho gayi hai (is mein 1-3 minute lag sakte hain)...")
        # Is model ke liye parameters
        result = client.predict(
            "A majestic waterfall in a fantasy world, 4k, cinematic", # Prompt
            "6-Step", # Infer steps
            api_name="/generate"
        )

        if result:
            # Result path check karna
            video_path = result if isinstance(result, str) else result[0]
            shutil.copy(video_path, 'output_video.mp4')
            print("SUCCESS: Video ban gayi hai!")
        else:
            print("ERROR: Model ne koi file generate nahi ki.")
            exit(1)

    except Exception as e:
        print(f"FAILED: Error ye hai -> {str(e)}")
        exit(1)

if __name__ == "__main__":
    generate()
