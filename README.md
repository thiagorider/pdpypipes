# PagerDuty Python tools for Azure Pipelines

This repository contains Python tools for use with Azure Pipelines to help with PagerDuty Alerting and Incident handling.

## USAGE

This tool can be used as a command-line tool for testing pourposes or embedded in an Azure Pipeline task.


```
pgincident.py summary source component buildstate buildnumber link severity
```
### Parameters

#### positional arguments:
| *argument*    | *description*                |
|---------------|------------------------------|
| *summary*     | summary of the event         |
| *source*      | source of the event          |
| *component*   | component of the event       |
| *buildstate*  | build state of the pipeline  |      
| *buildnumber* | build number of the pipeline |       
| *link*        | link for the pipeline        |    
| *severity*    | severity of the event        |   
  
Here is an example:
```
./pgincident.py 'app-XYZ 20220905.3 Deploy failed!' 'Pipeline ABC' 'failed' '20220905.3' 'https://example.visualstudio.com/myproject/_build/results?buildId=702006&view=results' 'error'
```