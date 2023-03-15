# sitesounds
sitesounds is a simple python script that make a web traffic noise

# what it does

this script make a web noise traffic to distract and confuse your ISP, in other words it just add a litter to his logs. useful if you are paranoiac or if you really care for your privacy and confidentiality in internet. 

# instaling

everything is simple:

`git clone https://github.com/aiivy782/sitesounds && cd sitesounds` and start by `python sitesounds.py`

if you want to use this script with Docker, then execute following commands in terminal.

`docker build -t sitesounds .` and start by `docker run -it sitesounds`

# how to use
usage: sitesounds.py [-h] [--websites] [--useragents]
options:

-h, --help            show this help message and exit
  
--websites, -w        the name of the JSON file containing website URLs (websites.json as default)
                        
--useragents, -u      the name of the JSON file containing useragents (useragents.json as default)
