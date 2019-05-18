# Backups

- [Backups](#backups)
  - [Backup](#backup)
  - [Restore](#restore)

Since our production environment is using docker, most of our data is stored
on a local volume. So in theory, we can easily backup that folder to restore our database state.

Although, we also offer few scripts to backup/restore our database through SQL.


## Backup

To backup a docker container database, simply execute that script:

```bash
./bin/backup.sh [prod] [filename]
```

You can specify `prod` as a first argument to backup from production.

```bash
./bin/backup.sh prod [filename]
```

You can also specify a `filename` as a last argument. The backup will be created with
this name. Otherwise, it will follow this template: `website-YYYY-MM-DD_HH_mm_SS.sql`

```bash
./bin/backup.sh dev_backup_01.sql
```


## Restore

To restore a database in a docker container, simply execute that script:

```bash
./bin/restore.sh [prod] filename
```

You can specify `prod` as a first argument to restore production database.

```bash
./bin/restore.sh prod my_backup.sql
```

The last argument is mandatory. You must specify the path of the backup file to restore.

```bash
./bin/restore.sh prod dev_backup_01.sql
```
