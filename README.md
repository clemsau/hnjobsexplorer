# hnjobsexplorer

To run the project locally:
- install the requirements from `requirements.txt`
- Create a `.env` file in the `hnjobsexplorer` according to the template

## Management commands

In order to simply get the jobs, two managements have been created:

```python
python manage.py fetch_new_thread # Get the two latests `who is hiring` threads and store them in the db if they don't exists

python manage.py fetch_new_jobs # Get all the kids of the two latests threads, then get only the kids that have not been stored and try to store them
```

We can run them from linux's cron jobs:
- Edit the cron jobs with `crontab -e`
- Add a new line: `<CRON_SCHEDULE> <PATH_TO_PYTHON> <PATH_TO_MANAGE.PY> <MANAGEMENT_COMMAND>`