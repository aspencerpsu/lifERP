# USE CASE REQUIREMENTS & METHODOLOGY
--------
The current project deliverables requires the user to have the ability to:

 -Input data, variables and nodes for the neural net 
 -The option to specify the networking logic that should be inherited within the system
 -The ability to perform back-propagation and genetic algorithm test cases
 -Revert to linear assignments or transportation assignments through the menu
 -Create the model through fields on simplex problems
 -Click event to sync the data stream through their respective database to create a 'behind-the-scenes' analysis
<br>
<br>
Upon completion of the network model and structure, it's intrinsic for the user to have an easier experience to 
generate the model and the data characteristics. 
<br>
<br>
### Database Requirements
------
- Machines can be 64 bit or 32 bit
- ORM capablities for OLAP & OLTP (Online Transactional & Analytical Processing) through Redis or PostgreSQL
- PreExisting table with at least 30 customers, dedicated finate transportation problems, and inventory capacity analysis

### Languages
------
The stack should adhere to C, C++, & Python.

### Build
------
The setup architecture should have a finalized setup.py structure to build and the filepath must conform to the Root User's bin
(e.g. /usr/bin/lifERP.exe). The client should have access to the source application through the mercurial pypi build path, utilizing the pip2.exe command on win or unix applications

