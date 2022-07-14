# Deep-Learning-based-Internet-of-Vehicles-Framework-for-Real-Time-Traffic-Anomaly-Detection-in-Smart




##### Table of Contents  
[Abstract](#abstarct)<br>[Introduction](#inroduction)<br>[Design](#design) 


<a name="abstarct"/>

Abstract
======
This project aims to automate the traffic violations detection system and facilitate the Traffic Department’s monitoring of traffic and act against the owner of the violating vehicle quickly and accurately, due to transport accidents causing 2.1 million deaths each year and 30-50% of them due to traffic violations. People’s non-compliance with traffic rules. As some of them know there are surveillance cameras, and they avoid them. Not being able to monitor the traffic with a fixed camera around the city in addition to the fixed camera will cost a lot of money, if we want to cover the whole city for that, to overcome all these problems we came up with our proposed solution. It is the creation of a mobile surveillance camera on specific public transportation in smart cities, where we must know each transportation route, to be aware of the areas and time in which the city is being monitored. We will use traffic jams as a case study. By checking the number of cars, speed, and location of the car to detect if the street has crowded, then display the results as a city heat map as an output to display the current state of the city. This is done by the Transport and Public Transport Authority, which is licensed by the Ministry of Interior, to try to strike a balance between efficiency and cost.



<a name="inroduction"/>

Inroduction
======

Smart city initiatives to enhance quality of life have been made possible by the ubiquity of Internet of Things devices and the proliferation of artificial intelligence. One of the most important components of smart cities is sustainable mobility, which strives to establish intelligent public transportation systems based on real-time data, platforms for traffic management to reduce congestion, and applications for safety and pro-active traffic control. Rapid monitoring is needed to reduce the risk of loss of life and property due to the increased stress that the growing number of vehicles on the road places on road traffic management staff and authorities to handle problems like road accidents. Cities therefore use CCTV surveillance cameras for traffic monitoring in order to detect and prevent mistakes like accidents. Manually reviewing the CCTV footage in real time to track the flow of traffic and spot the emergence of any undesirable situations. The use of human staff is not a workable approach. Additionally, CCTV camera videos are continuously streamed, so manual surveillance is error-prone and might miss some unexpected activity. This makes the development of an automated model for spotting uncommon occurrences, such as accidents, necessary for efficient traffic management and sustainable transportation. For intelligent traffic surveillance and management, computer-vision based approaches have been widely adopted as a panacea. Segmentation of automobiles from the background and other road items from still images as well as moving video scenes is the general pipeline of computer vision-based approaches. Classification of all vehicle classifications, including buses, vans, cars, and so forth. Extraction of spatiotemporal features for various traffic-related tasks, such as vehicle counting, vehicle tracking, trajectory tracking, and anomaly event detection similar mishaps. Additionally, such computer vision-based devices ought to function in a variety of lighting and traffic situations. A deep learning strategy for the detection and localisation of traffic accidents has been proposed as a result of the same motivation. In particular, we view the occurrence of a traffic collision as a special case of anomalous behaviour. Road accident detection and localization would speed up the response time of rescue crews and promote travel safety. Now we will take a deep look to every details related to our project to explain clearly the objective of the project.

<a name="design"/>

Design
======

System Modelling
There are two main use-case: the prove of concept tracker application and On-board unit applications.
High-Level Perspective

![image](https://user-images.githubusercontent.com/33600370/179090094-75f8e326-8765-431b-9202-e72d7a725b26.png)

•	The first Application works as prove of concept (POC) that illustrates the proposed idea. The clinet AUTOS application works as collecting data unit that collects the interested data (Spatial Data, frames, and speed) then if the clinet the clinet is online then send these data to centralized server. If not, store the data locally until the client become online then start syncronization process with server. Then the server collectes the data from all the connected nodes (Clinets) and then apply the AI models that responsible to detect the anomalies of interest then generates the predictive reports, and visualizes a heat map. [Repo Link for this app]

[Repo Link for this app]: https://github.com/HossamAElsayed/Traffic-Anomaly-Detection-Mobile-App

![image](https://user-images.githubusercontent.com/33600370/179090225-d8cb0fe2-50e2-4147-9a02-5cd86e9caa9a.png)


•	The second and the more realistic application is On-board unit that have the ability to do some anomaly algorithms on the edge and send only the frames that has anomaly and the record of this anomaly. This will decrease the computation power and load over the centralized server. [OBU-C Repo Link]

[OBU-C Repo Link]: https://github.com/HossamAElsayed/OBU_Connector
	
System Modelling
Sequence Diagram 

Authentication

![image](https://user-images.githubusercontent.com/33600370/179090340-ca7a6a23-40d8-4083-83e6-910a4ee9bf7f.png)

•	The two applications have the authentication feature that will allow us to know the identiy of the the client sending the data to the main server; as a level of security. The following sequence diagram of authentication illuestrates the actual  steps of authentication process:
1.	The user enters the credentials.
2.	Send credentials to main server to lookup for validity.
3.	If it is valid then home page will be shown, else an error message will appear asks him to correct the credentials.

![image](https://user-images.githubusercontent.com/33600370/179090390-9639e699-bab1-4ba0-a256-906669b34853.png)


OBU-Connector
------
•	The On-Board Unit Connector application is responsible for controlling the on-board unit functionalities: 

•	The main functionalities of the application are to start and stop and also halt the machine 
•	The On-board unit is also responsible to run and apply anomaly detect algorithms, then if any frame detected then it will be sent to centralized server.
 
 ![image](https://user-images.githubusercontent.com/33600370/179090416-216bc509-2718-47bf-bd44-c9ec136e912a.png)

 
Activity Diagram 
The following activity diagram illustrates the main functionality of the POC application:
•	After user login successfully, the home page will be displayed and the user will be able to start detection algorithm. 
•	If the client is online the collected data will be sent to the centralized server. If not the data will be stored locally untill the the client will become online again then the app will run a synchronization function with the main server. 



___
@Developers
1 | 2 | 3 | 4 |
--- | --- | --- | --- |
[Ghada Sallam](https://github.com/g-sallam "g-sallam") | [Haidi Tarek](https://github.com/haidyta "haidyta") | [Hossam Ahmed](https://github.com/HossamAElsayed "HossamAElsayed") | [Samar Ibrahim](https://github.com/samar283 "samar283")
