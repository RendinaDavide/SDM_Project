# SDM_Project
This project is part of the BDMA joint project at UPC. THis exploit and benefit from graph-based formalisms as taught
in SDM classes.
<br />
To reproduce the project: <br />
1)Create a Local DBMS on your Neo4j.  <br />
2)Add plugins 'APOC' and 'Data Science Library'.
3)Go to ... -> Open Folder -> Import and paste all the files contained in the "graph_data" folder of this repository.
4)Start the database.
5)Run the Python notebook "LoadGraph_SDMpj.ipynb" (remember to change the password to the password you chose when creating the db'.
6)You should now be able to see the database schema by calling 'call apoc.meta.graph'.


In additon:
-The scripts folder contains the two scripts that wrap the Cypher queries used to create the algorithms described in the project document.
-The pdf SDM_Project_RendinaWu contains a detailed description of the project.
