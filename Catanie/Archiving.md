# Archiving/Retrieving/Resetting Datasets

Actions performed on Datasets in the GUI are executed as a `job`, they are then handled by the queuing system you have. 

At PSI rabbitMQ is used as a queue. Jobs go to the queue and are passed onto the archiving system which is AREMA based at PSI. At this time the archive system is not availble
and so it would be necessary to implement your own. At this early stage ESS does not use any archive facility and all data is stored on disk. This means data files can be accessed directly using the file tab of dataset details in the client.


## Archive
Send a job to initiate a transfer of data from local disk to tape. Local data can be deleted upon completion but this should be done by the data owner.


## Retrieve
Copy data from tape to a staging area on disk where users can execute an rsync to copy the data to a desired location.


## Reset
Remove the data from the tape facility.




