### Prerequisites

To run the programs in this repo, do the following:

- create a virtual environment using the command:
  - `python -m venv venv`
- activate the virtual environment
  - `cd ./venv/Scripts/activate` (windows users)
  - `source ./venv/bin/activate` (mac and linux users)
- install the requirements
  - `pip install --upgrade pip` (to upgrade pip)
  - `pip install -r requirements.txt`

Once the requirements have been installed, The programs will run successfully.
Except for the `person_and_phone.py` script which requires a model to be downloaded.

More on that later.

For vision:

```
Tensorflow>2
OpenCV
sklearn=0.19.1 # for face spoofing.
The model used was trained with this version and does not support recent ones.
```

For audio:

```
pyaudio
speech_recognition
nltk
```

## Vision

It has six vision based functionalities right now:

1. Track eyeballs and report if candidate is looking left, right or up.
2. Find if the candidate opens his mouth by recording the distance between lips at starting.
3. Instance segmentation to count number of people and report if no one or more than one person detected.
4. Find and report any instances of mobile phones.
5. Head pose estimation to find where the person is looking.
6. Face spoofing detection

### FPS obtained

| Functionality              | On Intel i5 |
| -------------------------- | ----------- |
| Eye Tracking               | 7.1         |
| Mouth Detection            | 7.2         |
| Person and Phone Detection | 1.3         |
| Head Pose Estimation       | 8.5         |
| Face Spoofing              | 6.9         |

If you testing on a different processor a GPU consider making a pull request to add the FPS obtained on that processor.

## Audio

It is divided into two parts:

1. Audio from the microphone is recording and converted to text using Google's speech recognition API. A different thread is used to call the API such that the recording portion is not disturbed a lot, which processes the last one, appends its data to a text file and deletes it.
2. NLTK we remove the stopwods from that file. The question paper (in txt format) is taken whose stopwords are also removed and their contents are compared. Finally, the common words along with its number are presented to the proctor.

The code for this part is available in `audio_part.py`

Steps to build and run this Project.

### 1. **Set Up Your Environment**

- Ensure you have Python installed. You’re currently using Python 3.10.15, which should be fine.
- It's good practice to work in a virtual environment to manage dependencies.

```bash
python3 -m venv venv  # Create a virtual environment
source venv/bin/activate  # Activate the virtual environment
```

### 2. **Install Dependencies**

- If your project has a `requirements.txt` file (as shown in your screenshot), install dependencies listed there:

```bash
pip install -r requirements.txt
```

### 3. **Run the Code in `main.py`**

- Execute the `main.py` script to test it:

```bash
python main.py
```

### 4. **Building the Code for Distribution (Optional)**

- If you want to package your code into an executable, you can use `PyInstaller` to bundle the code and dependencies:

```bash
pip install pyinstaller
pyinstaller --onefile main.py  # Creates a single executable file
```

- This will generate a `dist` folder with an executable file. To clean up unnecessary build files, you can remove the `build` and `dist` folders if needed.
