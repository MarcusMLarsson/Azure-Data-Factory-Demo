<p align="center"><img src="https://www.element61.be/sites/default/files/competence/Azure%20Factory/image%201.png" width="500"> </p>

<h1> <b>Introduction to Azure Data Factory </b></h1>

<h3> What is Azure Data Factory? </h3>

<p> What is at the core of every Business Intelligence, Data Science, and Machine Learning project? <b>Data!</b> You need to collect, move, store, transform, integrate, and prepare your data. That can be a pretty time-consuming task, right? Wouldn’t it be cool if we could do all of those things automatically, like, in a data factory or something? Azure Data Factory (ADF) is a <b>cloud  ETL and data integration tool</b> that enables you to quickly and efficiently create automated data pipelines – without having to write any or little amount of code!  </p>

<h3> What can you do with Azure Data Factory? </h3>

<p> At its core, Azure Data Factory can be used to ingest and transform data. You can ingest data to and from 
<ul> <li> more than 80 Software-as-a-Service (SaaS) applications (such as Dynamics 365 and Salesforce) </li>
  <li> on-premises data stores (such as SQL Server and Oracle) </li>
  <li> and cloud data stores (such as Azure SQL Database and Amazon S3) </li>
  </ul>

During ingestion, you can even convert file formats, zip and unzip files, and map columns implicitly and explicitly – all in one task. In addition to ingesting data, you can also transform data. Previously, the only way to do this was to use external services like Azure HDInsight or SQL Server Stored Procedures. But in 2019, Azure Data Factory completed the data integration story by adding new data transformation capabilities called Data Flows. Now you can both ingest and transform data in the same user interface, making Azure Data Factory a complete ETL and data integration tool. </p>

<h3> On-premise ETL vs Cloud ETL</h3>

<b> On-premise ETL </b>
<p> For on-premise ETL solutions, SQL Server Integration Services (SSIS) is still the industry-standard. SSIS has been around since 2005. It’s very mature and has a lot of learning resources, blogs and articles as how to setup and develop with it. SSIS provides connectors to many different sources and contains many different transformation tasks that can handle pretty much any kind of traditional ETL workflow. For those people moving to Azure and who has sunk a lot of development time into SSIS, have no fear. It's very easy to lift and shift your solutions to the cloud.
<ul>
  <li> If you are looking for a PaaS-based approach, you can simply lift your SQL Server virtual machine running SSIS into the cloud. </li>
  <li> For those who want to leverage a PaaS-based approaches, Azure now offers the facility to publish your SSIS packages directly into Data Factory. </li>
</ul>
 
 <b> Cloud ETL </b> 
  
<p> It has becoming increasingly more difficult to do traditional ETL using tools like SSIS as the scale and the size of the data to be processed has grown. Azure Data Factory allows you to copy data at massive scale, and then use processing tools (e.g. Databricks) more appropriate to the job to transform the data ready for usage downstream. This pattern is not dissimilar to a common pattern seen in SSIS wherein developers used SSIS as the orchestrator and calls a series of SQL Statements (often Stored Procedures) to handle the processing. The difference now is that it’s not just relational tables we’re dealing with and SQL code. It’s parquet, orc and avro combined with SQL and Python, mixed with JSON, NoSQL, Key Value pairs and Graph databases plus a sprinkle of Spark etc. The table below, highlights some of the differences between Azure Data Factory and SSIS.

  | Azure Data Factory     | SSIS     |
| ------------- |:-------------:|
| High volumn of data | Medium volumn of data|
| Batch & Streaming | Batch    |
| Structured, Unstructured & Schema-drift | Structured       |
| Drag and Drop & Code (CLI & SDK)  | Drag and Drop       |
| C#, Python, PowerShell CLI  |  VB, C# & Biml| 
| Hybrid, Managed, Scale up  |On-Premises, Own Hardware, Scale out | 
| Pay as you go  | Licenses| 

  <h3> A deeper dive into Azure Data Factory </h3> 

  <p> Azure Data Factory consists of 6 main components. If you understand these components, you understand Azure Data Factory. The components are the following: </p>
     <img src="https://www.cathrinewilhelmsen.net/scribbles/wp-content/uploads/2019/11/CathrineWilhelmsenBeginnersGuidetoAzureDataFactory03_Components-1.png">
  
  <ul> 
  <li> <b>Pipeline </b></li>
  <p> A pipeline is a logical set of activities. The advantages of the pipeline is that it allows you to manage these activities as a set, instead of each one individually. </p>
  <li> <b>Activitites </b></li>
  <p> Activities are handeling the data. There are three types of activities in Azure Data Factory. 
    <ul>
      <li> Data movement activitites</li>
      <p> Copies and moves data from different sources </p>
      <li> Data transformation activitites</li>
      <p> You can use Data Flows (Azure Data Factory interface) or external services like Databricks, HDinsight (Hive, Hadoop, Spark, Pig, MapReduce), Azure ML etc. 
      <li> Data Control</li>
      <p> Defines the logic that your pipeline is going to follow. Its the orchestration of pipeline activities that includes chaining activities in a sequence, branching etc. </p>
  </ul>   
    <li> <b>Datasets </b></li>
  <p> Datasets represent data structures within the data stores, which simply point to or reference the data you want to use in your activities as inputs or outputs. </p>
  <li> <b>Linked services </b></li>
  <p> This is very similar to the concept of a connection string, where you are specifying what the source and destination of your data is. </p>
   <li> <b>Integration runtime </b></li>
  <p> The Integration Runtime (IR) is the compute infrastructure used by Azure Data Factory </p>
  <li> <b>Triggers </b></li>
  <p> A trigger determines when a pipeline needs to be run. </p>
  </ul>  
<h3> <b>Demo - Delivering a Modern Data Warehouse with Azure Data Factory</b></h3>

<p> The traditional data warehouse has served us well for many years, but new trends are causing it to break in four different ways:<ul>
  <li>data growth </li>
  <li> fast query expectations from users </li>
  <li> non-relational/unstructured data </li>
  <li> cloud-born data </li>
 </ul>
  <p>Enter the modern data warehouse, which is designed to support these new trends. A modern data warehouse on Azure provides a way to easily interface with all these types of data through one query model, and can handle “big data” while providing very fast queries (via MPP). </p>
  
<img src="https://raw.githubusercontent.com/MarcusMLarsson/Azure-Data-Factory-Demo/master/source/image.PNG">

<p> In this demo, I will show how easy and quick it is to set up a modern data warehouse using Azure Data Factory. The architecture which we are going to create are displayed in the figure above. Follow the following steps:</p>

<ul>
 <li> Provision Azure Storage Account, Azure Blob Storage, Azure Databricks, Azure SQL Warehouse </li>
  <li> Created linked services and data tables for each service </li>
  <li> Create the pipeline </li>
</ul>

<hr>
<h3> Appendix </h3>
<p>Good to know knowledge for the demo </p>
<ul>
   <li> What is Apache Spark? </li>
     <p> Apache Spark is an open-source distributed general-purpose cluster-computing framework. Spark provides an interface from programming entire clusters with implicit data parallelism and fault tolerance. </p>
  <li> What is Azure Databricks? </li>
  <p> It's a scalable apache spark based analytics platform that is optimized for Azure. Designed in collaboration with the founders of Apache Spark, Azure Databricks provides streamline workflow in an interactive workspace that enables collaboration between your data scienties, your data engineers etc. </p>
  <li> What is Azure Storage Account? </li>
  <p>A storage account is an cloud repository for data (Blob, File, Queue, Table) </p>
  <li> What is Azure Blobstorage? </li>
  <p> Blob Storage is optimized to store massive amount of unstructured data (e.g. audio, video, csv) in the cloud, servering documents directly to the browser. Blob Storage is widely used for data back-ups and restores. </p>
 
