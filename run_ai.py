import os
from gradio_client import Client

try:
    token = os.getenv("HF_TOKEN")
    print(f"Token check: {'Token mil gaya' if token else 'Token NAHI mila'}")
    
    # Simple Image model for testing
    print("Connecting to Test Model...")
    client = Client("stabilityai/stable-diffusion-3-medium", hf_token=token)
    
    print("Generating a test image...")
    result = client.predict(
        prompt="A simple red apple",
        negative_prompt="",
        seed=0,
        customize_seed=False,
        width=512,
        height=512,
        guidance_scale=5,
        num_inference_steps=20,
        api_name="/infer"
    )
    
    if result:
        # Image result ko rename karna
        import shutil
        shutil.copy(result[0], 'output_video.mp4') # Naam wahi rakha taake workflow na badalna paray
        print("SUCCESS: Test file ban gayi!")
    
except Exception as e:
    print(f"ASLI ERROR YE HAI: {str(e)}")
    exit(1)
