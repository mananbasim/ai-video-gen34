import os
import shutil
from gradio_client import Client

def generate_video():
    # GitHub Secrets se token uthana
    hf_token = os.getenv("HF_TOKEN")
    
    try:
        print("Hugging Face Space se connect ho raha hai...")
        
        # Hum 'KingNish/Instant-Video' use kar rahe hain jo kafi active rehta hai
        # hf_token dene se priority milti hai
        client = Client("KingNish/Instant-Video", hf_token=hf_token)

        print("AI Video generate ho rahi hai... Is mein 2 se 5 minute lag sakte hain.")
        
        # API ko request bhejna
        result = client.predict(
            prompt="A majestic lion walking through a futuristic neon city, cinematic, 4k",
            api_name="/generate_video"
        )

        # Agar video ban gayi hai to usay copy karna
        if result:
            shutil.copy(result, 'output_video.mp4')
            print("Mubarak ho! Video successfully ban gayi hai aur 'output_video.mp4' ke naam se save ho gayi hai.")
        else:
            print("Galti: Model ne koi result nahi diya.")
            exit(1)

    except Exception as e:
        print(f"Error: {str(e)}")
        # Agar ye space band ho to ye error print karega
        if "PAUSED" in str(e):
            print("Mashwara: Ye model abhi so raha hai (PAUSED). Kuch der baad try karein ya koi aur model use karein.")
        exit(1)

if __name__ == "__main__":
    generate_video()
