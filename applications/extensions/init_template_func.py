from datetime import datetime
import datetime as datetimeO
def init(app):
    @app.template_global()
    def getDatetimeSplit(d):
        if d:
            dt=datetime.strptime(d,"%Y-%m-%dT%H:%M:%S")
            return [dt.year,dt.month,dt.day,dt.hour,dt.minute,dt.second]
        else:
            return None
    @app.template_global()
    def getDateSplit(d):
        if d:
            dt=datetime.strptime(d,"%Y-%m-%d")
            return [dt.year,dt.month,dt.day]
        else:
            return None
    @app.template_global()
    def _len(d):
        return len(d)
    @app.template_global()
    def _toString(d):
        return str(d)
    @app.template_global()
    def _enumerate(d):
        return enumerate(d)
    @app.template_global()
    def _strftime(d,formatStr='%Y-%m-%d'):
        if "T" in d :
            dt = datetime.strptime(d, "%Y-%m-%dT%H:%M:%S")
        else:
            dt=datetime.strptime(d,"%Y-%m-%d")
        return dt.strftime(formatStr)

    @app.template_global()
    def _timedelta(d,days=0,hours=0,minutes=0,seconds=0,formatStr='%Y-%m-%d'):
        dt= datetime.strptime(d,formatStr)
        dt=dt+ datetimeO.timedelta(days=days,hours=hours,minutes=minutes,seconds=seconds)
        return datetime.strftime(dt,formatStr)

    @app.template_global()
    def _round(n,d):
        return  round(n,d)


def init_template_func(app):
    init(app)
