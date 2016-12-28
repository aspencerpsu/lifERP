
 # simplex linear-gui
----------
### simplex linear gui for linear programming answers

The following problems ** cannot ** be solved with this gui:

 1. Relaxed lp
 2. Mixed Integer lp
 3. Relaxed Fit lp
 4. Non-Linear lp
 5. Quadratic lp
 6. GO lp
 7. Mixed-Integer Non-Linear lp
 8. Semidefinite lp
 9. Cp lp
 10. Metaheuristic lp
 11. Second Order Cone lp

If you're an undergraduate or graduate student, please do not use this for homework or fast solutions to group projects. This is created **only** for professionals and business professionals in need. If otherwise suggested you need the package, contact aspencerpsu@gmail.com or create an issue and I'd be glad troubleshoot or give assistance with installation and packaging.

## ** Installation: **
#### <tb><tb>  For Linux/Ubuntu:

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

All packages can be installed with the `sudo apt-get install` command. To use .NET on ubuntu you need to install Mono. To get the .gz/tar archive directory, download the package using [this link][1] and then run `sudo make Makefile` or use the g++ compiler on the Makefile issuing `sudo gcc Makefile` within the root of the project directory . To setup using the python package run `python.exe setup.py install --user` under the ortools_examples directory. To check whether the or-tools python package has all the needed dependencies, hit python check_python_deps.py.

Once the tools have been compiled and routed to the respective folders(s). you **must** delete the pywrap.lp and replace it with this [raw file][2] slightly modified for the tkinter gui automation and replace where the setup configured the module directory. (Again replace the pathfile with the modified pywrap.py file). 

For other Linux distro's visit [google optimization tools][3].


<br>
 #### <tb> For mac OS X:  
      The following packages are mandatory for proper configuration:
          1. xcode (CLI ONLY)
          2. javac
          3. cmake

       After changing directories into or-tools, run:
       $ make Makefile

<br>
<br>
Once you have the or tools created and swapped the pywraplp file for the modified version, you can download and compile the Tkinter module by `sudo apt-get install` for linux or use `homebrew` for mac os x.

Once the packages have been downloaded and configured successfully, run `python visual_example.py` to start the simplex gui.

The tkinter module will prompt you to input the decision variables fields and constraints. Be forwarned, there are **no** substractions to be added in the system of equations, only a sum *e.g.*:
<br>
<br>
![simplex example][4]
<br>
<br>

For more help on using the simplex gui, contact aspencerpsu@gmail.com or write an issue for debugging issues.

Use the code wisely.

    


  [1]: https://github.com/google/or-tools/releases/download/v5.0/or-tools_Ubuntu-16.04-64bit_v5.0.3919.tar.gz
  [2]: https://raw.githubusercontent.com/aspencerpsu/Tkinter/master/pywraplp.py
  [3]: https://developers.google.com/optimization/installing#installing-from-source-on-windows
  [4]: https://raw.githubusercontent.com/aspencerpsu/Tkinter/master/simplex_gui.JPG
