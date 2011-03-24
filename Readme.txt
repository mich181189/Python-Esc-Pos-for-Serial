In theory this script *should* run on windows or linux (or pretty much any other platform for that matter)
HOWEVER the windows implementation of pyserial seems to be pretty buggy (at least on 64-bit windows) so
I can't get it working properly.

To run it you need:

* pyserial

To run the Tweceipt script (which may get moved to a different repo):

* serialEscPos
* python-twitter - >= 0.7 because that supports search http://code.google.com/p/python-twitter/