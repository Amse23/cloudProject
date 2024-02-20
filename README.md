# cloudProject

# azure-infra-assignment-zlatan

## Azure Infrastructure and Data Security with Terraform and Python 

This project is the example of creating Azure Infrastruacure with Terraform, including Azure SQL Server, Database, Storage account, and Table. Python has been used for
Populating table and add a layer of security fpr PII.

![image](https://github.com/Amse23/cloudProject/assets/128851103/7fbaf6dc-7ce0-4eb9-91ce-fe36f14f1292)

The following steps best describe the progression:
1. Azure Infrastructure with Terraform
2. Python Script for Data Population
3. PII Detection and Masking Solution

# Azure Infra with Terraform
Resources created with Terraform in order are: Azure Resource Group, Azure Storage Account, Azure Table, Azure SQL server, and Azure Database.

Terraform init was run for initializing the Terraform working directory. Following that Terraform Plan was run to provide safety by previewing changes and catching potential problems before they happen, help to visualize the impact of the changes you intend to make, and generate a plan and prompt for your approval before modifying the infrastructure.
And the last step was Terraform apply to execute the actions provided by Terraform plan.

In the next step, files were pushed to Github by Git commands - Git add ., Git status, Git commit, and Git push.

# Python scrpit

This script reads customer data from a JSON file and inserts it into an Azure Table Storage.
It uses the Azure SDK for Python (azure-data-tables) to interact with the Azure Table Storage service.

Requirements:
- Install the Azure SDK for Python: pip install azure-data-tables

The script defines two TypedDict classes (Address and Customer) to represent the structure of customer data.
It also includes functions to parse the JSON file and insert entities into the Azure Table Storage.

Usage:
1. Set the 'file' variable to the path of your customer data JSON file.
2. Set the 'table_name' variable to the name of your Azure Storage Table.
3. Set the 'connection_string' variable to the connection string of Azure Storage account details.

Run the script to insert the customer data into the specified Azure Table.

# Azure Data Factory

At first SQL db and server had to connect with ADF. Two Linked services are needed to this project to write the masked
data to the SQL db amsedbtest in the MaskedData table.

With ADF, non-relational data from Azure Table Storage was converted to relational in a Copy Activity pipeline: pl_copy_tbl_to_sql. Two Linked Services AzureTableStorage1, and AzureSqlDatabase2 was used for this activity.

For Masking data df_mask Data Flow was used and pl_copy_tbl_to_sql Pipeline for running the Data flow. 
In the df_Mask, Source ws set to the MaskedData in SQL db, follwoing Derived Columns to mask the columns, Alter Row for settig the policy for update table in the SQL db, and at last Sink for the same table of MaskedData. 
By running the pl_copy_tbl_to_sql, we will have a relational table with masked columns in MaskedData table.


