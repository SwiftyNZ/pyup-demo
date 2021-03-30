# Example using pyup

## About
Information about pyup can be found at their GitHub: https://github.com/pyupio/pyup. A quick summary is that it is a tool to help automatically keep Python libraries up to date with the latest version.

## Prerequisite
You will need to have a Person Access Token to allow pyup to access GitHub to read the requirements files and create Pull Requests.
- Login to GitHub
- Go to Settings -> Developer Settings -> Personal access tokens
- Create a new access token with repo and user email scopes

## Guide
1. Install pyup

```
pip install pyupio
```
2. Run the pyup bot. This will read requirements files in your repo and make sure they are up to date. It will create a Pull Request for any updates. Adding the --inital flag means it will package up all the changes into a single Pull Request which works well for if you want to do the first update to your repository.
```bash
pyup --repo=username/repo --provider_url=https://api.github.com --user-token=<YOUR TOKEN> --branch main --inital
```
3. All going well you should have Pull Requests being created for any out of date libraries.