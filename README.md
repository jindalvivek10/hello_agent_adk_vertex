jindal_vivek10@cloudshell:~$ **mkdir -p ~/projects/hello-agent && cd ~/projects/hello-agent**

jindal_vivek10@cloudshell:~/projects/hello-agent$ **pwd**
/home/jindal_vivek10/projects/hello-agent


jindal_vivek10@cloudshell:~/projects/hello-agent$ **uv init**
Initialized project `hello-agent`

jindal_vivek10@cloudshell:~/projects/hello-agent$ **uv add google-genai google-adk fastapi uvicorn**

jindal_vivek10@cloudshell:~/projects/hello_agent$ **uv venv**

After that I went to console.cloud.google.com and created a new project and enabled “Vertex AI API” in that project .and then replaced the actual project ID in the agent.py file with my project ID named “vjindal-project-ai-basic” 

AFter that I clicked on link https://console.developers.google.com/billing/enable?project=vjindal-project-ai-basic and enabled billing

jindal_vivek10@cloudshell:~/projects/hello_agent (vjindal-project-ai-basic)$ **gcloud auth application-default login**

jindal_vivek10@cloudshell:~/projects/hello_agent$ **gcloud projects list**

## jindal_vivek10@cloudshell:~/projects/hello_agent$ gcloud auth application-default set-quota-project vjindal-project-ai-basic
Credentials saved to file: [/tmp/tmp.zkQJWhgoW2/application_default_credentials.json]

These credentials will be used by any library that requests Application Default Credentials (ADC).

Quota project "vjindal-project-ai-basic" was added to ADC which can be used by Google client libraries for billing and quota. Note that some services may still bill the project owning the resource.
( **Ran above command explicitly otherwise when I was invoking the agent with a prompt then I used to get a warning message -- UserWarning: Your application has authenticated using end user credentials from Google Cloud SDK without a quota project. You might receive a "quota exceeded" or "API not enabled" error. See the following page for troubleshooting: https://cloud.google.com/docs/authentication/adc-troubleshooting/user-creds**)


jindal_vivek10@cloudshell:~/projects/hello_agent$ **uv run adk run .**

## Vertex AI API has not been used in project your-project-id before or it is disabled. Enable it by visiting https://console.developers.google.com/apis/api/aiplatform.googleapis.com/overview?project=your-project-id
## This API method requires billing to be enabled. Please enable billing on project #vjindal-project-ai-basic by visiting https://console.developers.google.com/billing/enable?project=vjindal-project-ai-basic


jindal_vivek10@cloudshell:~/projects/hello_agent$ **uv run adk web agent.py --port 8080** (but this is not working so far)