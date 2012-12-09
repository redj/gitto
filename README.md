Gitto
=====

Gitto as in 'ditto' with Git.

An instantaneous, automatic, potentially collaborative, content backup system powered by Git.

What is it?
-----------

Gitto is experimental software.

At present, the only implemented is a simple bash script. The goal is to have a fully cross-platform implementation in eC providing a solid monitor rendering the use of GittonOnSave plugins merely accessory.

Gitto is a backup tool that will backup all revisions of your files as soon as you create / delete or save them. The backup is a (you guessed it) Git repository. You can have as many backups (remotes) of this repository as you want and they will be updated each time you save a file.

You can choose between the sync and update modes. The sync mode will automativally add and remove files while the update mode will only backup changes to currently tracked files. Since Gitto is powered by Git you can use Git's facilities to choose which files will or will not be included. By default the sync mode will even track files that are inside of regular Git repositories.

Warning
-------

Use Gitto at your own risks.

Gitto in Bash
=============

Commands
--------

 - create
 - check
 - update
 - sync
 - push
 - flash
 - ls-new / lsn
 - disk-use / du
 - destroy
 - loop-dirs
 - monitor

Monitor
-------

NOTE: The monitor command is not functional and might never be. Use GittoOnSave plugins until the eC implementation of Gitto Monitor is ready.

Gitto Monitor (currently a command in the gitto script) uses inotifywait to listen to file system events for a given list of directories. For each event received gitto is invoked to 'sync' or 'update' all gitto repositories that potentially track the file(s) affected by the event.

Dependencies
------------

The script uses the following programs:

 - git (commands: init, branch, symbolic-ref, clone, remote add, remote show, push, ls-files, diff, add, rm, commit)
 - lockfile
 - grep
 - find (for loop-dirs command only)
 - inotifywait (for monitor command only)

GittoOnSave
===========

GittoOnSave is a series of plugins that you can use instead or in combination with Gitto Monitor.

GittoOnSave for Ecere IDE
-------------------------

plugins/ecereIDE/GittoOnSave.ec
plugins/ecereIDE/GittoOnSave.epj

GittoOnSave for Sublime Text 2
------------------------------

plugins/sublimeText2/GittoOnSave.py
