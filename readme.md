<p align="center"><img src="https://www.element61.be/sites/default/files/competence/Azure%20Factory/image%201.png" width="500"> </p>

<h1> <b>Introduction to Azure Data Factory </b></h1>

<h3> What is Azure Data Factory? </h3>

<p> What is at the core of every Business Intelligence, Data Science, and Machine Learning project? <b>Data!</b> You need to collect, move, store, transform, integrate, and prepare your data. That can be a pretty big and time-consuming task, right? Wouldn’t it be cool if we could do all of those things automatically, like, in a data factory or something? Azure Data Factory (ADF) is a hybrid data integration service that enables you to quickly and efficiently create automated data pipelines – without having to write any or little amount of code!  </p>

<h3> What can you do with Azure Data Factory? </h3>

<p> At is core, Azure Data Factory can be used to ingest and transform data. You can ingest data to and from 
<ul> <li> more than 80 Software-as-a-Service (SaaS) applications (such as Dynamics 365 and Salesforce) </li>
  <li> on-premises data stores (such as SQL Server and Oracle) </li>
  <li> and cloud data stores (such as Azure SQL Database and Amazon S3) </li>
  </ul>

During ingestion, you can even convert file formats, zip and unzip files, and map columns implicitly and explicitly – all in one task. In addition to ingesting data, you can also transform data. Previously, the only way to do this was to use external services like Azure HDInsight or SQL Server Stored Procedures. But in 2019, Azure Data Factory completed the data integration story by adding new data transformation capabilities called Data Flows. Now you can both ingest and transform data in the same user interface, making Azure Data Factory a complete ETL and data integration tool. </p>

<h3> On-premise ETL vs Cloud ETL</h3>

<b> On-premise ETL </b>
<p> For on-premise ETL solutions, SQL Server Integration Services (SSIS) is still the industry-standard. SSIS has been around since 2005. It’s very mature and has a lot of learning resources, blogs and articles as how to setup and develop with it. SSIS provides connectors to many different sources and contains many different transformation tasks that can handle pretty much any kind of traditional ETL workflow. For those people moving to Azure and who has sunk a lot of development time into SSIS, have no fear. It's very easy to lift and shift your solution to the cloud.
<ul>
  <li> If you are looking for a PaaS-based approach, you can simply lift your SQL Server virtual machine running SSIS into the cloud </li>
  <li> For those who want to leverage a PaaS-based approaches, Azure now offers the facility to publish your SSIS packages directly into Data Factory. </li>
</ul>
 
 <b> Cloud ETL </b> 
  
<p> In almost any Cloud project you will need to perform data movement activities across various networks (i.e. on-premise to the Cloud) and across various services (i.e. from Azure Blob Storage to Azure SQL Server). Azure Data Factory is one option to use as your cloud ETL/ELT tool.
  
 
It was becoming increasingly more difficult to do traditional ETL using tools like SSIS as the scale, size and shape of the data to be processed meant that you’d be hard pressed to fit it all in memory and process. What Data Factory allows you to do is copy the data at massive scale into your data lake, and then use processing tools more appropriate to the job to transform the data ready for usage downstream. This pattern is not dissimilar in fact to a common pattern seen in SSIS wherein developers simply used SSIS as the orchestrator and called a series of SQL Statements (often Stored Procedures) to handle the processing. The difference now is that it’s not just relational tables we’re dealing with and SQL code. It’s parquet, orc and avro combined with SQL and Python, mixed with a healthy does of JSON, NoSQL, Key Value pairs and Graph databases plus a sprinkle of Spark. 

  | Azure Data Factory     | SSIS     |
| ------------- |:-------------:|
| High volumn of data | Medium volumn of data|
| Batch & Streaming | Batch    |
| Structured, Unstructured & Schema-drift | Structured       |
| Browser  |SSDT        |
| Drag and Drop & Code (CLI & SDK)  | Drag and Drop       |
| VB, C# & Biml  |C#, Python, PowerShell CLI| 
| On-Premises, Own Hardware, Scale out  |Hybrid, Managed, Scale up | 
| Licenses  |Pay as you go | 

  <h3> How to learn Azure Data Factory </h3> 
  
  <img src="https://www.cathrinewilhelmsen.net/scribbles/wp-content/uploads/2019/11/CathrineWilhelmsenBeginnersGuidetoAzureDataFactory03_Components-1.png">
  <p> There are six main components of Azure Data Factory. If you understand these components, you understand Azure Data Factory. </p>
  
  <ul> 
  <li> <b>Pipeline </b></li>
  <p> A pipeline is a logical set of activities. The advantages of the pipeline is that it allows you to manage these activities as a set, instead of each one individually. </p>
  <li> <b>Activitites </b></li>
  <p> Activities are handeling the data. There are three types of activities in Azure Data Factory. 
    <ul>
      <li> Data movement activitites</li>
      <p> Copies and moves data from different sources </p>
      <li> Data transformation activitites</li>
      <p> You can use Data Factory interface or external services like HDinsight (Hive, Hadoop, Spark, Pig, MapReduce), Databricks, Azure ML etc. 
      <li> Data Control</li>
      <p> Define the logic that your pipeline is going to follow. With options like ForEach. </p>
  </ul>   
    <li> <b>Datasets </b></li>
  <p> Datasets are about data structure </p>
  <li> <b>Linked services </b></li>
  <p> Linked services are similar to connection strings </p>
   <li> <b>Integration runtime </b></li>
  <ul>
    <li> Data Flow execution </li>
    <li> Data Movement execution </li>
    <li> Dispatch of ACtivities </li>
    <li> SSIS package execution </li>
  </ul>
  <li> <b>Triggers </b></li>
  <p> Defineds when a pipeline needs to run.</p>
  </ul>

  
  
  
  | Azure Data Factory     | SSIS     |
| ------------- |:-------------:|
| Pipeline  | Package|
| Activity   | Task     |
| Linked Services | Connection Managers       |
| Datasets  |SSIS Sources and Destinations        |
| Source/Sink   |Source/Destination       |
| uses Json files  |uses DTSX (XML)| 
  
  
  
  <h3> Demo </h3>
  
  
  
  <hr>
  
  


<h3> Cost </h3>


<p> Databricks , preperation, collaboration, AI / ML </p>



Iterative development and debugging by using visual tools













<h3> Modern Data Warehouse</h3>

<img src="https://raw.githubusercontent.com/MarcusMLarsson/Azure-Data-Factory-Demo/master/source/img.PNG">
<img src="https://raw.githubusercontent.com/MarcusMLarsson/Azure-Data-Factory-Demo/master/source/img1.PNG">




<h3> Demo </h3>

<p> Introduction to ETL in Azure Data Factory. Importing csv data from Blob to Azure SQL </p>

<p>Drag wait activity</p>


<p> https://sqlofthenorth.blog/category/data-factory/ </p>
