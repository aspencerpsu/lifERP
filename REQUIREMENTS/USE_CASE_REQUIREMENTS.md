# USE CASE REQUIREMENTS & METHODOLOGY
--------
The current project deliverables requires the user to have the ability to:
<br>
 - Input data, variables and nodes for the neural net, via drag and drop or through the ODBC click
 - The option to specify the networking logic that should be inherited within the system
 - The ability to perform back-propagation and genetic algorithm test cases depending on the model
 - Revert to linear assignments or transportation assignments through the menu
 - Create the model through fields on simplex problems as an option (Dynamic Otherwise)
 - Click event to sync the data stream through their respective database to create a 'behind-the-scenes' analysis if one 
   problem methods doesn't achieve the expected results.
<br>
<br>
Upon completion of the network model and structure, it's intrinsic for the user to have an easier experience to 
generate the model and the data characteristics of the set he or she is trying to solve.
<br>
<br>

### Database Requirements
------
- Machines can be 64 bit or 32 bit (Preferably MACOSX or Linux Distros)
- ORM capablities for OLAP & OLTP (Online Transactional & Analytical Processing) through Redis or PostgreSQL
- PreExisting table with at least 30 customers, dedicated finate transportation problems, and inventory capacity analysis
  IF the user decides to do a 'data dump' on the canvas

### Languages

The stack should adhere to C, C++, Python respectively.

### Build
------
The setup architecture should have a finalized setup.py structure to build and the filepath must conform to the 'root' user's bin
(e.g. /usr/bin/lifERP.exe). The client should have access to the source application through the mercurial pypi build path, utilizing the pip2.exe command on win or unix applications. (MUST COMPILE!)

### ROUGH SKETCH
------
This a layout I'm considering:

![Sketch #1][1]
<br>
<br>
![Sketch #2][2]
<br>
<br>
[1]: https://github.com/aspencerpsu/lifERP/blob/master/REQUIREMENTS/SKETCH_PROTO(cpy).JPG?raw=true

[2]: https://github.com/aspencerpsu/lifERP/blob/master/REQUIREMENTS/Loading.JPG

