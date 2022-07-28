# 🚀 Friendly Web Interface for ML Projects with Gradio & Streamlit 🚀

There are many ways to make web interfaces to allow interaction with Machine Learning models and we will cover two of them.

[![python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
[![MIT licensed](https://img.shields.io/badge/license-mit-blue?style=for-the-badge&logo=appveyor)](./LICENSE)
![Issues](https://img.shields.io/github/issues/PapiHack/wimlds-demo?style=for-the-badge&logo=appveyor)
![PR](https://img.shields.io/github/issues-pr/PapiHack/wimlds-demo?style=for-the-badge&logo=appveyor)
[![Open Source Love png1](https://badges.frapsoft.com/os/v1/open-source.png?v=103)](https://github.com/ellerbrock/open-source-badges/)


<!-- You can find the slides of my talk at <https://meissa-wimlds-presentation.netlify.app>. -->

## Description

<!-- 
[gradio](https://gradio.app/)
[streamlit](https://streamlit.io/)
-->

You will have a minimal interface demo with [Gradio](https://gradio.app/) & [Streamlit](https://streamlit.io/), this will just serve you to make sure that everything works correctly. Then, you will have to make your own interfaces, those allowing you to interact with a Machine Learning model, that is to say:
- Pass values through the interface;
- Recover these values in backend;
- Apply the necessary processing;
- Submit the previously processed values to the ML model to make the predictions;
- Process the predictions obtained and display them on the interface.

## Installation

You have two ways in order to setup and run this project.

### Manual Setup

For manual installation, you need to have [`Python3`](https://www.python.org/) on your system. Then you can clone this repo and being at the repo's `root` follow the steps below:

- Create a virtual environment with the command :
        
        python3 -m venv venv

- Activate the virtual environment with the command :
  
  Windows:

      venv/bin/activate 
  
  Linux: 

      source venv/bin/activate

- Install the necessary dependencies with the command :
        
      python -m pip install --upgrade pip | pip install -r requirements.txt

- Run the demo app :
        
  Gradio:

      python gradio_project/demo_app.py

  - Go to your browser at the following address :
        
      http://127.0.0.1:7860/


  Streamlit: 

      streamlit run streamlit_project/demo_app.py

  - Go to your browser at the following address :
        
      http://localhost:8501

## Structure
### File: app.py

### Folder: ml

<!-- ## How to use this repository
### Import the repo
Clone or download the repo on your local machine.
### Setup the environment
1. Install Python 3 on your system. 
2. Being in the repository, activate the virtual environment : 

this command line will work in linux
```console
source venv/bin/activate
```        

this command line will work in windows
```console
venv\Scripts\activate
```           

### Run the Flask app

```console
```

If there is an error, replace `python3` by `python`. -->


## Resources
Here are some ressources you would read to have a good understanding of Gradio and Streamlit :
- [Get started with Streamlit](https://docs.streamlit.io/library/get-started/create-an-app)

- [Get started with Gradio](https://gradio.app/getting_started/)




## Contributing

Feel free to make a PR or report an issue 😃.

Oh, one more thing, please do not forget to put a description when you make your PR 🙂.

## Author

- [Emmanuel KOUPOH](https://www.linkedin.com/in/esa%C3%AFe-alain-emmanuel-dina-koupoh-7b974a17a/)
[![My Twitter Link](https://img.shields.io/twitter/follow/emmanuelkoupoh?style=social)](https://twitter.com/emmanuelkoupoh)