# Scryer

## Description
Scryer is a RESTful frontend to Apple's iCloud Find My iPhone using [pyicloud](https://github.com/picklepete/pyicloud).

## Setup
Copy example_config.py to config.py and modify to suit your needs. Note that iCloud passwords are stored in plaintext
so take appropriate precautions. iCloud passwords are *not* passed over the wire other than from the server
to Apple (much like any time you would use Find My iPhone).

## Status
This is a very first stab at this. Barely functional and not pretty. Currently outputting in HTML only.
