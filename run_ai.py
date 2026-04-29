import os
from gradio_client import Client

# Hugging Face Space se connect kar rahe hain
client = Client("ali-vilab/modelscope-damo-text-to-video-synthesis")

print("Video generation shuru ho rahi hai...")

# Video generate karne ka order
result = client.predict(
    "A beautiful waterfall in a green forest, cinematic high quality", # Aapka prompt
    api_name="/predict"
)

# Video file ko rename karna
import shutil
shutil.copy(result, 'output_video.mp4')
print("Video ban gayi hai: output_video.mp4")
