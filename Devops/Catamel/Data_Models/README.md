## Users

Two types of users exist: LDAP/AD and functional users.

LDAP/AD users are imported from LDAP settings, configured in providers.json.

Functional users, like ingestor, and proposalIngestor exist for a purpose e.g. to ingest specific dataset.


## Datasets
Stores the meta data information for a given collection of files. It defines a list of mandatory and optional metadata fields to be defined. Datasets have a PID field for unique identification. This is the base 'class' for derived documents like raw datasets or derived datasets. The type field is used to distinguish between the different types of datasets. For each dataset in addition an embedded DatasetLifecycle is created. However the definition of which files belong to a given dataset is defined in an extra OrigDatablock collection.



## Datablocks

When archiving a dataset all files contained in the dataset are listed here together with their checksum information. Several datablocks can be created if the file listing is too long for a single datablock. This partitioning decision is done by the archiving system to allow for chunks of datablocks with managable sizes. E.g a dataset consisting of 10 TB of data could be split into 10 datablocks of about 1 TB each. The upper limit set by the data catalog system itself is given by the fact that documents must be smaller than 16 MB, which typically allows for datasets of about 100000 files.

A Dataset can contain many datablocks, which then contains the actual datafiles. When a Dataset is sent to the backup system, the datafiles are split up into Datablocks \(for size limitations\). These are mirrored in the database, but not visible to end users. In order to retrieve the files associated with a Dataset, queries must go through the Datablock API.

## Proposal 

Defines the purpose of an experiment and links an experiment to principal investigator and main proposer


