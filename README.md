# toxicity_model
1st attempt to create a simple web API where use can give an input in the text format and using my own machine learning model, predict the toxicity of the text.
Toxicity in text is defined by rude, disrespectful, or unresaonable comments that is likely to make people leave a discussion.

# Gettign Started
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
    ~ tokenizer_200d_1M_10.pickle
    ~ best_model_200d_1M_10.h5
    ~ best_model_200d_1M_10_in_json.json
  * templates
    ~ simple.html
    ~ home.html
  * static
    * css
      ~ theme.css
  ~ api.py
    
