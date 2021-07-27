# 
<p align="center">
  <img width="200" src="https://user-images.githubusercontent.com/55149010/127099805-4e36c8a0-143a-4b53-bc84-6d7fc2f14d6b.png" alt="Dependabot-X">
<h1 align="center">Dependabot-X</h1>
</p>





Dependabot-X is a tool written in Python3 that allows GitHub Organization/User to automate enabling Dependabot alerts feature for all repositories. 


Since GitHub currently allows system admins and individual developers to manually configure Dependabot for each repository, which takes time and effort, Dependabot-x can be used to automate the process.

<img width="1335" alt="Dependabot-x" src="https://user-images.githubusercontent.com/55149010/127097461-5259bf95-8e53-4335-8eaa-d2ca181a953e.png">


## Requirements <br>
* Python 3
* Linux/Windows/MAC OSX
* GITHUB API KEY

## Installation 

* Installing Python dependencies 

   ```pip3 install -r requirements.txt```

* Configuring GitHub API KEY as env variable

   ```export  GITHUB_API_KEY=""```
 

## Usage

* To enable Dependabot for Org repos: 

   ```python3 dependabot-x.py -o ORG_NAME ```
   
* To enable Dependabot for user's repos: 

   ```python3 dependabot-x.py -a ```

