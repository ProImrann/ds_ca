# Background for the development of the chosen distributed system
The development of this system was as a result of a problem of booking hotel and tracking the restaurant activities. Thus a need to come up with a solution that can allow multiple users at the same time without crushing the system and minimizing the errors encountered. Also, as multiple users can work together, it will be profitable to the restaurant by increasing sales, good marketing and reaching many people by using this web based distributed system. Also, there has been an increase demand fo a high availability and fault tolerant system, since in a centralized system, one system failure can cause the system to go down.

Distributed systems allow resources to be connected and used together. Increased demand for scalability: Distributed systems can scale horizontally by adding more computers to the system. This allows the system to handle increased workloads and larger data sets.

# Scope including requirements for the distributed system to be developed
Fault tolerance: The system should be designed to handle faults or failures in one or more nodes or components without affecting the overall system performance.
Consistency: The system should provide consistent data access and update operations across the distributed nodes, even in the presence of failures or concurrent access.
Concurrency: The system should be able to handle multiple concurrent users or processes accessing and updating shared data in a distributed environment.
Security: The use of authentication passwords and also hashing the passwords to prevent malicious attacks and unauthorized access
Performance: The system should provide fast response times and efficient resource utilization, while minimizing communication overhead and network latency.
Documentation and training: The system should provide comprehensive documentation and training materials for developers, administrators, and users, including design specifications, user manuals, API references, and tutorials

# Design of the chosen distributed system
This is a Flask app that manages restaurant offers and bookings. Users can register and log in to the app, view different types of offers (rooms, dishes, sports, and conference rooms), and book available offers. The app also allows users with admin privileges to add new offers.
The app is divided into different routes. The home() function is the default route that requires users to log in before they can access the app. The login() function logs in a user, while the logout() function logs them out. The register() function creates a new account for a user. The new_offer() function allows admin users to add a new offer. The about() function displays information about the app. The rooms(), dishes(), sports(), and halls() functions display different types of offers. The offer() function displays a single offer, and the buy_offer() function books an offer.

# Analysis of the implemented distributed system, in terms of properties such as scalability, fault-tolerance, concurrency etc.
Scalability: The implemented distributed system is designed to be highly scalable. The use of a distributed architecture allows the system to scale horizontally by adding more nodes to the system.
Fault-tolerance: The implemented distributed system is fault-tolerant, meaning that it can continue to operate even in the presence of failures.
Concurrency: The implemented distributed system is designed to handle high levels of concurrency. Consistency: The implemented distributed system ensures consistency of data across all nodes in the system through the use of data replication and synchronization mechanisms. 

# Evaluation of the benefits of the implemented design over one or more possible alternative designs, noting any disadvantages or trade-offs.
The implemented design of a distributed system has several benefits over alternative designs:
Scalability: The distributed system allows for horizontal scaling, which means that the system can be expanded by adding more servers to handle increased workload. This is a major advantage over traditional monolithic architectures, which have limitations in scaling due to their centralized design.
Fault tolerance: The distributed system is designed to handle failures of individual nodes by distributing the workload across multiple servers. This means that if one node fails, the system can continue to function with minimal disruption.
Concurrency: The distributed system allows for parallel processing of requests, which improves system performance and reduces latency. 
Decentralized control: In a distributed system, each node operates independently, which means that there is no single point of failure or control. 
One of the disadvantage is the network latency problem since the system depends on the communication between nodes.

