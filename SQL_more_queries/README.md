# SQL More Queries

This project focuses on more advanced MySQL concepts such as:

- Managing user privileges
- Understanding and using different types of `JOIN` operations
- Filtering data using conditions
- Using subqueries and logical operators

## File: `0-privileges.sql`

This script lists all privileges granted to the MySQL users `user_0d_1` and `user_0d_2` on `localhost`.

### Usage

```bash
cat 0-privileges.sql | mysql -hlocalhost -uroot -p
