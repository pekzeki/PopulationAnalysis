# Population Analysis

Turkish	Statistical	Institute provides access to census data of Turkey. The project analyzes the census data between 1965-2000 and plots basic graphs in order to reveal hidden important factors that leads to population growths and recession between those years. It helps to see;

  - Population distribution w.r.t. gender, city.
  - Population in the urban and rural area. 
  - The growth of metropolises.

### Version
1.0

### Tech

The project uses a number of open source projects to work properly:

* [Python] - General purpose programming language. 2.7+
* [Pygal] - SVG charting library for pyhton. 
* Pandas - Data analysis tool for python.
* BeautifulSoup - XML parser for pyhton.

### Installation

Installation of required pyhton libraries.

```sh
$ pip install pandas
$ pip install BeautifulSoup
$ pip install pygal
```

### Run

Some of the scripts needs parameters to execute. The output of the programs will be generated under the "/output" directory. Such as...

```sh
$ pyhon evolution.py İstanbul
$ python evolution_urban_rural.py Ankara
```

### Todos

 - Write Tests
 - Add Code Comments
 - Create GIF from SVGs programmatically. 

### License
MIT

----

**Free Software, Hell Yeah!**

[//]: # 
   [Python]: <https://www.python.org/>
   [Pygal]: <http://www.pygal.org/en/stable/>

