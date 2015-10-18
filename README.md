# org-import-wunderlist
Converts wunderlist-export.json to an Org-mode file.

This is *not* a synchronization tool. It’s just meant to convert your Wunderlist data to Org-mode. Use it if you want to dump Wunderlist.

## How to use

1. Export your data to a `.json` file: Wunderlist.com → Account Settings → Create Backup → Download.
1. Run `$ ./convert.py wunderlist-20151018-15-23-32.json > Wunderlist.org`.

## License

Apache2.
