# Run this in Google Colab to preview churn_dashboard.py with a temporary public link.
# Make sure churn_dashboard.py is uploaded to your Colab session in the same folder.
#
# Setup (one-time):
# 1. Get a free ngrok account + auth token at https://ngrok.com
# 2. In Colab, click the key icon (Secrets) on the left sidebar
# 3. Add a new secret named NGROK_TOKEN with your token as the value
# 4. Toggle "Notebook access" on for that secret

import subprocess
import sys

subprocess.check_call([sys.executable, "-m", "pip", "install",
    "streamlit", "pyngrok", "pandas", "plotly", "scikit-learn", "-q"])

import time
import threading
from pyngrok import ngrok
from google.colab import userdata

NGROK_TOKEN = userdata.get("NGROK_TOKEN")

ngrok.kill()
ngrok.set_auth_token(NGROK_TOKEN)

def run_streamlit():
    subprocess.Popen(
        ["streamlit", "run", "churn_dashboard.py",
         "--server.port=8501",
         "--server.headless=true",
         "--server.enableCORS=false",
         "--server.enableXsrfProtection=false"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

thread = threading.Thread(target=run_streamlit)
thread.start()
time.sleep(5)

public_url = ngrok.connect(8501)
print("=" * 60)
print("YOUR DASHBOARD IS LIVE — OPEN THIS LINK:")
print(f"{public_url}")
print("=" * 60)
