# 2250: Sample Authorization

Dataset Authorization tests that authorization is correctly set for all the dataset endpoints for all the different type of users.

Tests are built around assuming the following owner, access and public information:

Groups | Sample 1 | Sample 2 | Sample 3 | Sample 4 | Sample 5 | Sample 6 | Sample 7 |Sample 8 | Sample 9 | Sample 10 |
--- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
adminingestor | Owner | Admin | Admin | Admin | Owner | Admin | Admin | Admin | Admin | Admin |
sampleingestor | | Owner | | | | Owner | | | | Public |
group1 | | | Owner | | | Access | Owner | | Owner | Public |
group2 | | | | Owner | Access | | Access | Owner | | Public |
group3 | | Access | Access | | | | Access | | | Public |
group4 | | | | Access | | Access | | | | Public |
group5(_1) | Access | | | | Access | | | | Access | Public |
nogroup | | | | | | | | | | Owner | 

Users are contained in file functionalAccount.json.test and are the following:

User | Group | Permission Group |
--- | --- | --- |
adminIngestor | adminingestor | Admin Groups |
sampleIngestor | sampleIngestor | Samples Privileged Groups |
user1 | group1 | Samples Group |
user2 | group2 | _none_ |
user3 | group3 | _none_ |
user4 | group4 | _none_ |
user5(_1) | group5 | _none_ |

Dataset 10 is _public_, meaning its field _isPublished_ is set to _True_.

