![LifeERP][1]
----------
# LifERP
> _When life gives you constraints, make an ERP system_

### MultiLP solutions guide for users of all businesses

The following problems ** cannot ** be solved with this gui:

 1. Relaxed lp
 2. Mixed Integer lp
 3. Relaxed Fit lp
 4. Non-Linear lp
 5. Quadratic lp
 6. GO lp
 7. Mixed-Integer Non-Linear lp
 8. Semidefinite lp<br>
 <s>9. Cp lp</s>
 10. Metaheuristic lp
 11. Second Order Cone lp

If you're an undergraduate or graduate student, please do not use this for homework or fast solutions to group projects. This is created **only** for professionals and business professionals in need of solver to handle roughcut estimates of decisions, however the user is limited to 200 variables. If otherwise suggested of needing a different package to interact with the solver, contact aspencerpsu@gmail.com or create an issue and I'd be glad troubleshoot or give assistance with installation and packaging.

<h3>Installation:</h3>
 <br>
<h4>For Linux/Ubuntu:</h4>

     The following packages are needed:
           1. tkinter
           2. pyPi
           3. ortools
           4. gawk 
           5. python-setuptools
           6. flex
           7. python-Dev
           8. autoconf
           9. zlib-devel
         10. bison
         11. textinfo
         12. Help2man
         13. g++
         14. texlive
         15. cmake (important tool for binary google-or)
         16. subversion
         17. openjdk-7-jdk
         18. make (should be complimentary with standard ubuntu package)

All packages can be installed with the `sudo apt-get install` command. To use .NET on ubuntu you need to install Mono. To get the .gz/tar archive directory, download the package using [this link][2] and then run `sudo make Makefile` or use the g++ compiler on the Makefile issuing `sudo gcc Makefile` within the root of the project directory . To setup using the python package run `python.exe setup.py install --user` under the ortools_examples directory. To check whether the or-tools python package has all the needed dependencies, hit python check_python_deps.py.

Once the tools have been compiled and routed to the respective folders(s). you **must** delete the pywraplp.py file and replace it with this [raw file][3], slightly modified for the tkinter gui automation and label it with the same filename (pywraplp). (Again replace the pathfile with the modified pywrap.py file). 

For other Linux distro's visit [google optimization tools][4] to import and configure the build tools.


<br>
<tb> <h3>For mac OS X:</h3>
      The following packages are mandatory for the proper assembly configuration:
          1. xcode (CLI Only)
          2. javac
          3. cmake

       After changing directories into or-tools, run:
       $ make Makefile
<br>
<br>
<h2 style="color: rgba(255,0,0,1);">Warning</h2>
If your machine build is based Unix Architecture (e.g. Apple Computer), you may have to replace the Tkinter imports to an all-lower cap text (e.g. tkinter)
<br>
Once you have the ortools created and swapped the pywraplp file for the modified version, you can download and compile the Tkinter module by `sudo apt-get install` for linux or use `homebrew` for mac os x.

Once the packages have been downloaded and configured successfully, run `python visual_.py` in the respective path to start the default gui.

The tkinter module will prompt you to input the decision variables fields and input the constraint within each field. Be forwarned, there are **no** substractions to be added in the system of equations, only a sum *e.g.*:
<br>
<br>
![simplex example][5]
<br>
<br>

For more help on using the simplex gui, contact aspencerpsu@gmail.com or write an issue for debugging. You'll get a response within the terminal window if the response indicates the solution is infeasible or non-optimal. Does not support entering variable and ratio test algorithms.

**If The Solution is not feasible....**

If the solution is not feasible **&** the objective row is a maximization problem definition expression, you may have to convert the matrix into a BFS with slack variables directly inside each row. I.E. a collective set of non basic variables and basic variables: {x1, x2, x3...} BVs, {s1, s2, s3} NBV's. Once you have the constraint entry filled, you can ** * ONLY * ** use the `<=`, `>=`, `>`, or `<` operator for the item to work correctly.

![slack inputs][6]

Use the code wisely and happy sharing!

    

  [1]: https://github.com/aspencerpsu/simplex-linear-gui/blob/master/lifERP.JPG?raw=true
  [2]: https://github.com/google/or-tools/releases/download/v5.0/or-tools_Ubuntu-16.04-64bit_v5.0.3919.tar.gz
  [3]: https://raw.githubusercontent.com/aspencerpsu/Tkinter/master/pywraplp.py
  [4]: https://developers.google.com/optimization/installing#installing-from-source-on-windows
  [5]: https://github.com/aspencerpsu/lifERP/blob/master/simplex_incorrect_gui.jpg?raw=true
  [6]: https://github.com/aspencerpsu/lifERP/blob/master/correct_gui_slack.jpg?raw=true
