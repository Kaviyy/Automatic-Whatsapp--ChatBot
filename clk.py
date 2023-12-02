from apscheduler.schedulers.blocking import BlockingScheduler
from msg import send_msg
sched=BlockingScheduler()
sched.add_job(send_msg,'interval',seconds=2)
