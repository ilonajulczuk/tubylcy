[![Stories in Ready](https://badge.waffle.io/atteroTheGreatest/tubylcy.png?label=ready&title=Ready)](https://waffle.io/atteroTheGreatest/tubylcy)
#Installation

```
virtualenv -p /usr/bin/python3.4 .
. bin/activate
pip install -r requirements.txt

vary on distributions but you need spatialite, GEOS and GDAL.

spatialite db.sqlite3 "SELECT InitSpatialMetaData();"
./manage.py migrate
```
