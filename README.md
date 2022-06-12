# SDM_Project
This project is part of the BDMA joint project at UPC. This exploit and benefit from graph-based formalisms as taught
in SDM classes.
<br />
To reproduce the project: <br />
1)Create a Local DBMS on your Neo4j.  <br />
2)Add plugins 'APOC' and 'Data Science Library'. <br />
3)Go to ... -> Open Folder -> Import and paste all the files contained in the "graph_data" folder of this repository. <br />
4)Start the database. <br />
5)Run the Python notebook "LoadGraph_SDMpj.ipynb" (remember to change the password to the password you chose when creating the db'. <br />
6)You should now be able to see the database schema by calling 'call apoc.meta.graph'. <br />
<br />
<br />
In additon: <br />
-The scripts folder contains the two scripts that wrap the Cypher queries used to create the algorithms described in the project document. <br />
-The pdf SDM_Project_RendinaWu contains a detailed description of the project. <br />
