# encounter-generator

Random encounter generator for Microlite20 that runs in a browser using CherryPy.

Required python modules:  
cherrypy  
names  
math  
random  

To run locally:  
python cherrym20.py

By default, serves on port 8080, so go to:  
127.0.0.1:8080/?lvl=foo  
where 'foo' is the level of encounter you want. If no level is given, it defaults to level 1.

Example output:

![Example output](screenshot.png?raw=true)

Code is covered under the MIT license (See: LICENSE-CODE).  
Game content is based on Microlite20 and is under the Open Game License (See: LICENSE-CONTENT)
