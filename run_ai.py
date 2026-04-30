import os
from gradio_client import Client

try:
    print("AI Model se connect ho raha hai...")
    # Hum ek naya stable model use kar rahe hain
    client = Client("prodia/fast-stable-diffusion") 
    
    print("Video generation ki request bhej di hai...")
    # Ye model sirf image banata hai pehle check karne ke liye ke API kaam kar rahi hai ya nahi
    # Agar ye chal gaya to hum agle step pe video wala model lagayenge
    result = client.predict(
        "A cinematic mountain view, high resolution", # Prompt
        "SDXL", # Model version
        api_name="/predict"
    )

    if result:
        import shutil
        shutil.copy(result, 'output_video.mp4')
        print("Mubarak ho! File ban gayi hai.")
    else:
        print("Khaali result aaya hai.")

except Exception as e:
    print(f"Masla ye aaya hai: {e}")
    exit(1)
