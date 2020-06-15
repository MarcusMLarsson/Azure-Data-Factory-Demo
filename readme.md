<h1> Introduction to Azure Data Factory </h1>

<h3> What is Azure Data Factory? </h3>

<p> What is at the core of every Business Intelligence, Data Science, and Machine Learning project? <b>Data!</b> You need to collect, move, store, transform, integrate, and prepare your data. That can be a pretty big and time-consuming task, right? Wouldn’t it be cool if we could do all of those things automatically, like, in a data factory or something? Azure Data Factory (ADF) is a hybrid data integration service that enables you to quickly and efficiently create automated data pipelines – without having to write any or little amount of code!  </p>

<h3> What can you do with Azure Data Factory </h3>

<p> At is core, Azure Data Factory can be used to ingest and transform data. </p>
<p>
You can ingest data to and from more than 80 Software-as-a-Service (SaaS) applications (such as Dynamics 365 and Salesforce), on-premises data stores (such as SQL Server and Oracle), and cloud data stores (such as Azure SQL Database and Amazon S3). During ingestion, you can even convert file formats, zip and unzip files, and map columns implicitly and explicitly – all in one task. </p>

<p>
In addition to ingesting data, you can also transform data. Previously, the only way to do this was to use external services like Azure HDInsight or SQL Server Stored Procedures. But in 2019, Azure Data Factory completed the data integration story by adding new data transformation capabilities called Data Flows. Now you can both ingest and transform data in the same user interface, making Azure Data Factory a complete ETL and data integration tool. </p>



<img src="https://github.com/Azure-Data-Factory-Demo/tree/master/source/img.PNG" width="900">




<h3> Why should you use Azure Data Factory? </h3>

  
  | Azure Data Factory     | SSIS     |
| ------------- |:-------------:|
| Pipeline  | Package|
| Activity   | Task     |
| Linked Services | Connection Managers       |
| Datasets  |SSIS Sources and Destinations        |
| Source/Sink   |Source/Destination       |
| uses Json files  |uses DTSX (XML)| 












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





<h3> Demo </h3>




<h3> Demo </h3>

<p> Introduction to ETL in Azure Data Factory. Importing csv data from Blob to Azure SQL </p>

<p>Drag wait activity</p>
