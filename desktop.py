import eel, os

def _stop():
    os._exit(0)

eel.init('web')
# eel.start("templates/index.html", 
#           port=8080,
#           jinja_templates="/",
#           close_callback=_stop,
#           block=True
#           )
eel.start('templates/index.html',
          jinja_templates="",
          port=8080,
        #   mode=None,
          close_callback=_stop,
          block=True
        )

