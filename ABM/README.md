# ABM
Agent based modelling for programming course

This is my Agent Based Model (ABM) for GEOG5990. My student ID is 200779106

How to use

In the current folder there are three folders, Model Docbuild and Documentation. 
The DocBuild folder contains all the files used to create the model's
documentation. The Documentation folder contains the html files for the documentation.
The Model folder includes just the files needed for the model

To run the agent based model open up the "model.py" file in a python IDE
(I recommend Spyder). When you run the model, two windows will pop up,
and on one of them it will have a drop down menu called "Model". Click
on that then click "Run Model" and you will see the model animation begin
to run. You can close both windows and stop the model if it hasn't already.
Feel free to change some of the initial parameters if you would like to
experiment

The ABM code is written in Python and when run displays some agents who
move, eat, reproduce (asexually, similar to bacteria) and die

The starting coordinates for each agent are taken from a website, as requested in the practical notes, 
or are random when the list finishes. The movement of the agents is in a random
direction, or they stay still. When they eat, a set amount is subtracted from the environment
and added to the agents store. Reproduction and death occur with varying degrees of
probability depending on age and store value of the agent

The environment is a raster and in a file called "in.txt". It is read into the model
through the module called "enviro.py". There is also a class used to store all the agents'
data and methods in a module called "agentframework.py"

If you would like some more information on how the model works, the
documentation is available on my webiste (Connection to Leeds University Network Required)
https://ee13zackhan.github.io/ or alternatively you can open the webpages locally through the
documentation folder

Please read the LICENSE file.