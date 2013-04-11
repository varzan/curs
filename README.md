This project uses the exchange rate API of http://openapi.ro and the [flot](http://www.flotcharts.org/) Javascript library to show a graph of the history of the Romanian leu vs. euro exchange rate. The user interface and logging messages are in Romanian.

To run this on your own machine, a quick and dirty solution would be to drop the project in your Dropbox folder and have a cron job run curs.py every weekday to update the exchange rate in the JSON file.

You can find a running copy (which hasn't been updated in a while) [here](http://dl.dropboxusercontent.com/u/28507684/dev/curs/index.html).