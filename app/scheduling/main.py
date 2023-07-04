import schedule
import time

from controllers.asistencias import asistencia

schedule.every(30).minutes.do(asistencia.check_expired_asistencias)

def run():
    while True:
        schedule.run_pending()
        time.sleep(1)