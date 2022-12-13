# gve_devnet_umbrella_dc_connection_rating
This sample code tests the connection quality to each IPsec-enabled Umbrella data center from a specific location via ping. The output is formatted as a sorted table based on the mean latency, which includes further information about each data center.  

## Contacts
* Ramona Renner

## Solution Components
* Umbrella Secure Internet Gateway (SIG)

## Related Sandbox Environment

This sample code can be tested using a Cisco dCloud demo instance that contains a Cisco [Umbrella Secure Internet Gateway (SIG)](https://developer.cisco.com/docs/sandbox/#!security/overview).

## Workflow

![/IMAGES/migration_workflow.png](/IMAGES/workflow.png)

## High-Level Architecture

![/IMAGES/migration_workflow.png](/IMAGES/architecture.png)

## Prerequisites
The [Umbrella API](https://developer.cisco.com/docs/cloud-security/#!getting-started/getting-started) follows RESTful principles and uses standard JSON format for requests and responses. To generate a key for the API follow these steps:
1. Log into [Umbrella](https://dashboard.umbrella.com)
2. In Umbrella, navigate to **Admin > API Keys** or in a Multi-org, Managed Service Provider (MSP), or Managed Secure Service Provider (MSSP) console navigate to Console **Settings > API Keys**.
3. Click **Add** in the header of the page.
4. Enter a **name** for the key. 
5. Select the **Deployments** scope.
6. Click **Create Key**.
7. Copy and save your **API Key** and **Key Secret** in a safe place for a later step.
8. Click **Accept And Close**.
> Note: You have only one opportunity to copy your API secret. Umbrella does not save your API secret and you cannot retrieve the secret after its initial creation.

More detailed instructions are available under https://developer.cisco.com/docs/cloud-security/#!authentication/create-umbrella-api-key.


## Installation/Configuration

9. Make sure you have [Python 3.10](https://www.python.org/downloads/) and [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) installed

10. (Optional) Create and activate a virtual environment for the project ([Instructions](https://docs.python.org/3/tutorial/venv.html)).

11. Access the created virtual environment folder
    ```
    cd [add name of virtual environment here] 
    ```

12. Clone this Github repository:  
  ```git clone [add github link here]```
  * For Github link: 
      In Github, click on the **Clone or download** button in the upper part of the page > click the **copy icon**  
      ![/IMAGES/giturl.png](/IMAGES/giturl.png)
  * Or simply download the repository as zip file using 'Download ZIP' button and extract it

13. Access the downloaded folder:  
    ```cd gve_devnet_umbrella_dc_connection_rating```

14. Install all dependencies:  
  ```pip3 install -r requirements.txt```

15. Fill in the variables in the **.env** file:    
```
API_KEY="[Add key from step 7 here]"
API_SECRET="[Add secret from step 7 here]"

COUNT="[Set number of pings executed for each data center latency test]"
TIMEOUT="[Set timout for ping]"
TTL="[Set TTL for ping]"
```

## Usage
To run the code, use the command:
```
$ python3 connection_rating.py
```

# Screenshots

![/IMAGES/0image.png](/IMAGES/screenshot.png)

> Note: The mean latency value 100000000 identifies data centers for which the ping tests returned "Timeout" or "Unknown Host".

### LICENSE

Provided under Cisco Sample Code License, for details see [LICENSE](LICENSE.md)

### CODE_OF_CONDUCT

Our code of conduct is available [here](CODE_OF_CONDUCT.md)

### CONTRIBUTING

See our contributing guidelines [here](CONTRIBUTING.md)

#### DISCLAIMER:
<b>Please note:</b> This script is meant for demo purposes only. All tools/ scripts in this repo are released for use "AS IS" without any warranties of any kind, including, but not limited to their installation, use, or performance. Any use of these scripts and tools is at your own risk. There is no guarantee that they have been through thorough testing in a comparable environment and we are not responsible for any damage or data loss incurred with their use.
You are responsible for reviewing and testing any scripts you run thoroughly before use in any non-testing environment.