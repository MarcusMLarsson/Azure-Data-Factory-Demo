<p align="center"><img src="https://www.element61.be/sites/default/files/competence/Azure%20Factory/image%201.png" width="500"> </p>

<h1> <b>Introduction to Azure Data Factory </b></h1>

<h3> What is Azure Data Factory? </h3>

<p> What is at the core of every Business Intelligence, Data Science, and Machine Learning project? <b>Data!</b> You need to collect, move, store, transform, integrate, and prepare your data. That can be a pretty big and time-consuming task, right? Wouldn’t it be cool if we could do all of those things automatically, like, in a data factory or something? Azure Data Factory (ADF) is a hybrid data integration service that enables you to quickly and efficiently create automated data pipelines – without having to write any or little amount of code!  </p>

<h3> What can you do with Azure Data Factory </h3>

<p> At is core, Azure Data Factory can be used to ingest and transform data. You can ingest data to and from more than 80 Software-as-a-Service (SaaS) applications (such as Dynamics 365 and Salesforce), on-premises data stores (such as SQL Server and Oracle), and cloud data stores (such as Azure SQL Database and Amazon S3). During ingestion, you can even convert file formats, zip and unzip files, and map columns implicitly and explicitly – all in one task. In addition to ingesting data, you can also transform data. Previously, the only way to do this was to use external services like Azure HDInsight or SQL Server Stored Procedures. But in 2019, Azure Data Factory completed the data integration story by adding new data transformation capabilities called Data Flows. Now you can both ingest and transform data in the same user interface, making Azure Data Factory a complete ETL and data integration tool. </p>

<h3> Why should you use Azure Data Factory? </h3>

<p> In almost any Cloud project you will need to perform data movement activities across various networks (i.e. on-premise to the Cloud) and across various services (i.e. from Azure Blob Storage to Azure SQL Server). Azure Data Factory is one option to use as your cloud ETL/ELT tool.
  
 You can execute SSIS packages in Azure Data Factory. If you are comming from the SSIS side, and you are looking into how to modernize and improve your solution.

 
 
  There are some features that distinguish Azure Data Factory from other tools.


SSIS mainly used for ETL on-premises
Released in 2005 before Azure was announced. 
Some of the limitations (no big data)
You can easly lift and shift SSIS packaged to Azure


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


  
  | Azure Data Factory     | SSIS     |
| ------------- |:-------------:|
| Pipeline  | Package|
| Activity   | Task     |
| Linked Services | Connection Managers       |
| Datasets  |SSIS Sources and Destinations        |
| Source/Sink   |Source/Destination       |
| uses Json files  |uses DTSX (XML)| 


Iterative development and debugging by using visual tools


<h3> Cost </h3>


<p> Databricks , preperation, collaboration, AI / ML </p>


<p> There are six main components that you need to understand inorder to create your projects. 
  
  <ul> 
  <li> Pipeline </li>
  <p> A pipeline is a logical set of activities. The advantages of the pipeline is that it allows you to manage these activities as a set, instead of each one individually. </p>
  <li> Activitites </li>
  <p> Activities are handeling the data. There are three types of activities in Azure Data Factory. 
    <ul>
      <li> Data movement activitites </li>
      <p> Copies and moves data from different sources </p>
      <li> Data transformation activitites</li>
      <p> You can use Data Factory interface or external services like HDinsight (Hive, Hadoop, Spark, Pig, MapReduce), Databricks, Azure ML etc. 
      <li> Data Control</li>
      <p> Define the logic that your pipeline is going to follow. With options like ForEach. </p>
  </ul>       
  <li> Triggers </li>
  <p> Defineds when a pipeline needs to run.</p>
  <li> Integration runtime </li>
  <ul>
    <li> Data Flow execution </li>
    <li> Data Movement execution </li>
    <li> Dispatch of ACtivities </li>
    <li> SSIS package execution </li>
  </ul>
  <li> Datasets </li>
  <p> Datasets are about data structure </p>
  <li> Linked services </li>
  <p> Linked services are similar to connection strings </p>
  </ul>






<h3> Modern Data Warehouse</h3>

<img src="https://raw.githubusercontent.com/MarcusMLarsson/Azure-Data-Factory-Demo/master/source/img.PNG">
<img src="https://raw.githubusercontent.com/MarcusMLarsson/Azure-Data-Factory-Demo/master/source/img1.PNG">




<h3> Demo </h3>

<p> Introduction to ETL in Azure Data Factory. Importing csv data from Blob to Azure SQL </p>

<p>Drag wait activity</p>
