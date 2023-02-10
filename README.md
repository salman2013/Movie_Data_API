## Project Setup instructions


## Install Scrapy
As this project use scrapy so we need to install scrapy package with following command

`
    pip install scrapy
`
if you are using pipenv 
```
    pipenv install scrapy
```

## Create scrapy project
The reason to re-create scrapy project is to actually get the scrapy setting file which is system dependent.
- Save torrentcue_spider.py file
- Save vofomovies_spider file
- Please delete the existing scraper folder in the project and scrapy.cfg file. 
- Run the following command to create scrapy project. 

```
    scrapy startproject scraper
```

## Adding files

 - Copy the torrentcue_spider.py file into spider folder.
 - Copy the vofomovies_spider file into spider folder.

## Directory Structure

Your project directory should look something like this:

```
movies_project/
    manage.py
    movies_project/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
    scraper/
        __init__.py
        spiders/
            torrentcue_spider.py
            vofomovies_spider.py
        helpers.py
        items.py
    scrapy.cfg
    movies/
        __init__.py
        management/
            commands/
                crawl_t.py
                crawl_v.py
```

## Use these commands in the terminal to start the Spiders
Open the terminal into the main project folder

Run the following commands on terminal:

To run the TorrentCue spider use the following command:

```
    python manage.py crawl_t
```

To run the VofoMovies spider use the following command:
```
    python manage.py crawl_v
```

`The extracted data will be saved inside a JSON file.`


## Export data from json files into database.
Run following command store the scrappeed data from json file into database 
```
    python manage.py import_data <filePath>
```

## Export data Django model data into wordpress template
In the file 'post_data_wordpress.py' we have to set the wordpress url, admin user and password and create data. 
Run following command to export data into wordpress template
```
    python manage.py post_data_wordpress
```

