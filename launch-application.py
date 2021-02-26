#! python
#
# tkinterguiexample
# launch-application.py
# This file is intended to by invoked by the user to launch the application.
# Borrowing from the Flask application factory structure.
from MyExampleApp import create_app

app = create_app()

app.mainloop()
