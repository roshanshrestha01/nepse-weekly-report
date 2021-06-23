# GOAL

Always wanted to view weekly report from [nepalstock.com](http://www.nepalstock.com/reports-by-category/1) page. Automated download and sending that report as email to list to receving emails.

## TODO 

- [x] Download report and save in proper location
- [x] Send report as attachment to list of receiving emails.
- [ ] Add cron job to send on weekly basis
- [ ] Parse xlsx content and generate a graph report

## Install

```bash
mkdir report
cd report
git clone git@github.com:roshanshrestha01/nepse-weekly-report.git app
virtualenv env
source env/bin/activate
cd app
pip install -r requirements.txt
cp .env.samples .env #Add necessary config and keys 
python main.py
```
