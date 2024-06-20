### ytGenCaption

This project enables the generation of captions for YouTube videos leveraging the power of OpenAI's Whisper model and yt_dlp.

### Requirements

```
python 3.9
yt_dlp
faster_whisper
pysrt
```

### Quick Start
1. **Clone the repository**
   ```bash
   git clone https://github.com/hsiehbocheng/yt-gen-caption.git
   ```
2. **Create a virtual environment(optional)**
    1. python venv
         ```bash
         python3 -m venv venv
         source venv/bin/activate
         ```
   2. install ffmpeg (Ubuntu)
      ```bash
      sudo apt update
      sudo apt upgrade
      sudo apt install ffmpeg
      ```

3. **Install the requirements**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the script**
   
   Run the script with the following command, replacing your_yt_url with the URL of the YouTube video you want to caption:
    ```bash
    python ytGenCaption/main.py -url your_yt_url
    ```

### **Command-Line Arguments**:
- `-url`: Specify the YouTube video URL for which you want to generate captions.
- `-model_size_or_path`: Set the model size or provide a path to a specific model. Default is "small".
- `-temperatures`: Adjust the temperature to control the randomness during model inference. Default is 0.001.
- `-initial_prompt`: Provide an optional initial prompt for the model to influence the beginning of the captions.

**example**:
```bash
python ytGenCaption/main.py -url "https://www.youtube.com/watch?v=LUHGvz8skoo" -model_size_or_path "small" -temperatures 0.001 -initial_prompt "蔡冠雙頭喜劇演員"
```