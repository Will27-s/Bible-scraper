# Bible-scraper
A python script that can pull any Bible version from bible.com and create a csv file that can be uploaded to OpenLP

This script uses the JSON files on bible.com and also the data written on the actual site.
From these files it can be seen that each bible version corresponds to a certain id and each chapter has it's own unique page that is the same for all versions.

It then iterates through every verse, chapter and book for the chosen Bible version and stores that data in 2 csv files.
This data can then be uploaded to OpenLP an open-source Church Worship presentation software to display the selected Bible version during worship.

Run the site_scraper.py file to run the script
