### sevice to store binary data  

#### azure blob storage used as storage:)  

You have to add .flaskenv file with:
  - FLASK_APP=testprojmain.py
  - AZURE_STORAGE_CONNECTIONSTRING=`<yourconnectionstringtoazurestorageblob>`


here we have two endpoints:
  - *host*/blob/ - to store binary data. Method PUT
  - *host*/blob/<file_id> - to get stored data. Method GET  

*host - default localhost is 127.0.0.1:5000*


get some images or create files to test service (I was using images)  

with curl:
1. put two images to azure storage - `curl -s -T "{one.png,two.png}" 127.0.0.1:5000/blob`
    - here we upload two images. 
    - in response we get id's to retrieve them later (split by "/n")
2. get one of uploaded images - `curl -s -o somefilename.png 127.0.0.1:5000/blob/<file_id_youve_got_previously>` 
    - here we download data by file_id.
    - in case there are (in blob storage) no such file_id - you ve got 404 status