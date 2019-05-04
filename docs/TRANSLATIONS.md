# TRANSLATIONS

## Requirements

In order to play with translations, you need to have `gettext` installed on your pc.

### Linux

**gettext** is generally easy to install on any linux OS. 

For Debian-like distos: 

```bash
apt-get update && apt-get install gettext
```


### OSX

You can follow those [instructions](http://macappstore.org/gettext/) to install gettext on OSX.

### Windows

For windows, it a bit more complicated. 

Everything is detailed in [this thread](https://groups.google.com/forum/#!topic/django-i18n/V3r9rvE5KVg).

In general, you need to:

1. Download [this file](http://ftp.gnome.org/pub/gnome/binaries/win32/dependencies/gettext-tools-0.17.zip)
 and [this file](http://ftp.gnome.org/pub/gnome/binaries/win32/dependencies/gettext-runtime-0.17-1.zip). 
 2. Extract the content of the zip somewhere in your computer (you will need to add these paths to your PATH env variable)
 3. Add the extract `/bin` paths to the `PATH` environment variable. 
 4. Restart your terminal and you should be able to call `gettext`.

## How to translate
For this project, most of the translations can be done through the interface.
Although, there are some translations that need to be done on the server side.

The website translations are stored into `website/locale/<language>`. 

To translate a new language, you must run the following command inside the `website` folder:

```bash
django-admins makemessages -l en
```

It will generate a `django.po` file inside `/website/locale/en/LC_MESSAGES` directory.

You can edit manually those files to translate them.

Once you're done translating the files, you must compile them!

To do so, run the following command inside the `website` folder:

```bash
django-admins compilemessages
```

The `django.po` files should be compiled into `django.mo` files. At this point, translations should be loaded
into your website!