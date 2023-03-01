# AutopilotCRM

Goal of this project is to make open source CRM and make on that road knowledge and fun. 
That would be great portfolio for me and training, for you - the best product that you could find =) 


## Basic funcionality for Autopolit CRM: 

1. Automated customer service: Automatically respond to customer inquiries, provide personalized customer service, and manage customer relationships.

2. Lead generation: Automate the process of identifying and qualifying leads, and then routing them to the appropriate sales team or individual.

3. Sales automation: Automatically track sales activities and progress, as well as manage sales pipelines and forecasts.

4. Reporting & analytics: Generate reports on customer interactions, sales performance, and other key metrics to help inform business decisions.

5. Integration with other systems: Integrate with existing CRM systems to ensure data accuracy and consistency across platforms.

## architecture for CRM




```mermaid
flowchart TD;
    client(client channels)
    Kafka
    Front
    BI
    SalesTeam
    AutoContextLoader
    client<-->APIsCloud
    APIsCloud<-->SalesTeam
    APIsCloud<-->AI
    BI-- Real time analytics -->Spark
    APIsCloud-- clients messages -->Kafka
    AutoContextLoader-->contextFileRules
    BI-- History analytics -->Spark
    Spark<-- History analytics -->DB
    Spark-- Real time analytics -->Kafka
    Spark-- routing sales -->Kafka
    subgraph APIsCloud
        APIs-->contextFileRules
    end
    OtherCRMs-->Kafka
    Spark--real time data-->DB
    APIsCloud--read for sales team messages -->Kafka
    AdminFront-- basic data -->AutoContextLoader
    AutoContextLoader-- scraping -->YourSite
``` 

### Issues 
AutoContextLoader - there is no point in parsing info. The first goal was to automate parsing product data, upload it to chatGPT (or else) and on base on provided info we will get the AI that knows about the product. 
But there is limit that you could provide to AI:
1. A lot of info need to update, when you will do it? On initialization of client could lead to sla problem 
2. limit of chatGPT 
3. Inconsistency of context of chatGPT , how to check that it will be in context of product ? 


### ideas 
1. Build something in between - general AI to make predefined workflow more alive , as is its just conversation, but with help of AI analyse what root should be for speaking with clients. All roots and scripts will be part of decision engine  - scripts for speaking with client, preferable personalized 
2. Application from chat with verification based on AI analyses. (application forms predefined for a root - lives in Decision Engine)