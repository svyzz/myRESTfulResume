myRESTfulResume
===============
This repository makes an attempt at geeking out and transforming my resume (parts of it, technically) into different RESTful APIs that can be consumed programatically. The APIs themselves are intended to be simple, perform little/no processing and only support GET requests.

(The good parts of) HATEOAS have been included where possible! POST, PUT and DELETE requests return a 405 and additional documentation (inside the source code) explains why things work the way they do.

Usage
=====
NONE of the APIs need authentication and the following endpoints are supported; 
* **/about**
* **/education**
* **/contact**
* **/github**
* **/work**
* **/work/\<organization\>**

Whilst most of the RESTful endpoints are straight-forward and self explanatory, '/github' makes a call to the public GitHub API and forwards the response received. '/work' returns an array comprising of IDs/symbols/stock-codes that correspond to the organizations I've worked for so far.

The individual details can then be read by making a GET request to '/get/\<insert-symbol/ID-here\>'. NOTE that this is an experiment, and if you really want more information, please write to me.

Obligatory ASCII art!
=====================

        ________
      =[________]========-------[]<--
        |  ___ |
        |==|  ||
        |==| _| |
        |==||   |
        |  ||   |
        |  ||    |
        |  ~~    |
        |________|
      __L________\_
     <_|_L___/   | |,
        |__\_____|_|___
       /L___________   `---.___________________________
      | | .----. _  |---v--.______ _ _ _ _ _ _ _ _ _ _ `--------------------------.--.__
     [| | |    |(_) |]__[_____]____My resume (well, parts of it!), as an API!_____]__ __]
      | |___________|---^--'___________________________.--------------------------`--'
       \L______________.---'
      __|__/_    | |
     <_|_L___\___|_|'
        L________/
        |        |
        |   _    |
        |  ||    |
        |  ||   |   
        |==||_  |
        |==|  | |
        |==|__||        
        |______|
      =[________]========-------[]<--
