# toxicity_model
1st attempt to create a simple web API where user can give an input in the text format and using our own machine learning model, predict the toxicity of the text.
Toxicity in text is defined by rude, disrespectful, or unresaonable comments that is likely to make people leave a discussion.

# Getting Started
A very unpleasant, aggressive, filled with hatred comments or otherwise very likely to make a user leave a discussion or give up sharing their point of view. I tired to make model receptive to use of curse words in positive way. However, it must be mention in the documentation that this is very simple and initial level model for the beginner. The dataset used to train model is also having curse words in the abstract format, such as use of special characters like * # @ ! etc. So, it has sensitivity to the toxicity in the form of abbreviations.

Follow this document to download, use and understand the toxicity_model.

## Prerequisites
```
Python 3.0 or above
Disk Space 1 GB or more
```

Following python libraries:
```
Flask - 1.1.1
json - 2.0.9
requests - 2.22.0
pandas - 0.25.2
numpy - 1.17.3
keras - 2.2.4
tensorflow - 1.14.0
pickle
os
```

## Installing

Open command prompt and type following to install required packages:

Flask
```
pip install Flask
```
Requests
```
pip install requests
```
Pandas
```
pip install pandas
```
NumPy
```
pip install numpy
```
Keras
```
pip install keras
```
TensorFlow
```
pip install tensorflow==1.14
```
## Project Structure
Download the repository on the local drive
The structure of the project folder should look like this:
* Project Folder
  * Models
    - tokenizer_200d_1M_10.pickle
    - best_model_200d_1M_10.h5
    - best_model_200d_1M_10_in_json.json
  * templates
    - simple.html
    - home.html
  * static
    * css
      - theme.css
  - api.py

### Important
Makes changes in the api.py as follows:

1. Find
```
with open(os.path.expanduser('~/Python_Work/Deployment_001/Projects/api_007/Models/tokenizer_200d_1M_10.pickle'), 'rb') as handle:
```
and change it to
```
with open(os.path.expanduser('$$YOUR_PATH_TO_PROJECT$$/Models/tokenizer_200d_1M_10.pickle'), 'rb') as handle:
```

2. Find
```
with open(os.path.expanduser('$$YOUR_PATH_TO_PROJECT$$/Models/best_model_200d_1M_10_in_json.json'),'r') as f:
```
and change it to
```
with open(os.path.expanduser('$$YOUR_PATH_TO_PROJECT$$/Models/best_model_200d_1M_10_in_json.json'),'r') as f:
```

3. Find
```
loaded_model.load_weights(os.path.expanduser('$$YOUR_PATH_TO_PROJECT$$/Models/best_model_200d_1M_10.h5'))
```
and change it to
```
loaded_model.load_weights(os.path.expanduser('$$YOUR_PATH_TO_PROJECT$$/Models/best_model_200d_1M_10.h5'))
```

# Running the api
Once, the above steps are completed, we are good to go!

Run api.py Visual Studio or any other complier.

or 
from command line of the project folder:
```
$python api.py
```
Once, you get the following message:
```
> Debugger is active!
> Debugger PIN: ***-***-***
```
Open any web browser.
type:
```
https://127.0.0.1:5000/
```
If you have local host is different, use the one shown on your screen.

# Test the model
On screen you can see a dialouge box asking for text:
Write down any text.
Click on Analyze button.

If everything is setup properly, you can see the toxicity score of the post.
This toxicity score is ranging from 0 (Being the least toxic) to 1 (Being the most toxic).

Feel free to try out different texts.
**Enjoy..!!!**

# Authors
* Nirav Chhayani - *Initial Work*
  - Jr. Data Scientist . 
    Avrij Insights Inc.  
    Canada.

# Issues
Write down in comment section of the git repository.

# Acknowledgments
I sincerely appreciate the efforts of "Conversion AI" that aims to help increase empathy, participation, and quality in online conversion at scale.
https://github.com/conversationai
