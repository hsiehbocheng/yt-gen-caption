### ytGenCaption

This is a Porject for generating captions for YouTube videos using machine learning.</p>

### Requirements

```
python 3.9
yt_dlp
faster_whisper
```

### Quick Start
1. Clone the repository
   `git clone https://github.com/hsiehbocheng/yt-gen-caption.git`
2. Create a virtual environment(optional)
    ```bash
    python3.9 -m venv venv
    source venv/bin/activate
    ```
3. Install the requirements
   `pip install -r requirements.txt`
4. Run the script
    `python ytGenCaption/main.py -vurl your_yt_url`