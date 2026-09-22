# -*- coding: utf-8 -*-
from config import LOGS
from app import App

if __name__ == "__main__":
    try:
        App().mainloop()
    except Exception:
        import traceback
        err = traceback.format_exc()
        try:
            (LOGS / "startup_error.txt").write_text(err, encoding="utf-8")
        except Exception:
            pass
        raise
