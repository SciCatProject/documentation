# PSI URLs

These are the urls in use at PSI for all of the services. Currently \(8th March 2018\), the Node-RED deployments cannot be accessed using their URLs and a workaround for accessing them can be seen in the Node-RED section.

## Environments:

* development
* qa
* production

## Services

* discovery.psi.ch - Web Frontend
* dacat.psi.ch - API Server
* aries.psi.ch - Node-RED ingestor \(note that the ending slash is needed for correct loading\)
  * /jobs/ -  Jobs ingestor
  * /&lt;BEAMLINE&gt;/ - beamline name
* hal.psi.ch - RabbitMQ

## Node-RED

Nginx is unable to locate the Node-RED instances currently, so the `aries.psi.ch` is not working. You will need `kubectl` installed in your system \(and available in your path\).

1. `kubectl get pods -n <NAMESPACE>`
2. `kubectl port-forward <PODNAME> 8001:1880`
3. `Navigate to localhost:8001`
4. Login with admin credentials \(can be found in the `secrets` section of the Kubernetes Web dashboard.

The following is an example screenshot of the job-assembler Node-RED process

![Job-Assembler at PSI](img/job-assembler.png)

# Archiving/Retrieving/Resetting Datasets

Actions performed on Datasets in the GUI are executed as a `job`, they are then handled by the queuing system you have. 

At PSI RabbitMQ is used as a queue. Jobs go to the queue and are passed onto the archiving system which is AREMA based at PSI. At this time the archive system is not publicly availble
and so it would be necessary to implement your own. 

## Archive
Send a job to initiate a transfer of data from local disk to tape. Local data can be deleted upon completion but this should be done by the data owner.


## Retrieve
Copy data from tape to a staging area on disk where users can execute an rsync to copy the data to a desired location.


## Reset
Remove the data from the tape facility.

