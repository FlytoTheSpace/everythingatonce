Databases


# Relational Databases:

## SQL

### DataTypes:

- `varchar(size)`: a String with Size Limit of size
- `int`: An Integer
- `NULL`: Representation of Literal 'NOTHING' / Absence of Value
- `boolean`: True or False, that's it!
    
### Operators:

- `=` : is Equal? 
- `<` : a is less than b?
- `>` : a is greater than b?
    

### Commands:

Every line of Commands must end in `;`

- `USE database>` switch to Database

- `SHOW`:

    - `SHOW DATABASES`: Lists Tables in The Current Database
    - `SHOW TABLES`: Lists Databases

- `CREATE`:
        
    - `CREATE DATABASE <name>`
    - `CREATE TABLE name ( columnName DataType , ... )`

    ```sql
    CREATE table accounts (
        username varchar(255),
        email varchar(255),
        password varchar(255),
        age int,
        verified: boolean,
        userID int
    );
    ```

- `DROP`
    -  `DROP TABLE table` Deletes the table
    -  `DROP DATABASE database` Deletes the Database

- `TRUNCATE`
    - `TRUNCATE TABLE table` Deletes all the data inside the table

- `DESCRIBE table`: Shows Info about the Table

- `INSERT`:

    - `INSERT INTO table`:

        `INSERT INTO table VALUES (<Values...>)`:

        ```sql
        INSERT INTO accounts VALUES ("master", "user@example.com", "secretpassword", 1878429132);
        ```

- `SELECT` Outputs The Data from The Table
    
    - `SELECT DISTINCT column1, column2 FROM table <WHERE?>;`: Outputs The Data from The Table
    - `SELECT <column | *> FROM table <WHERE?>;`: Outputs The Data from The Table

    ```sql
    SELECT * FROM accounts;
    SELECT username FROM accounts;
    SELECT * FROM account WHERE username = "admin";
    SELECT * FROM account WHERE username = "admin" OR username = "root";
    SELECT * FROM account WHERE age > 13 AND age < 18;
    SELECT * FROM account WHERE NOT verified = True;
    ```
    
    - `LIMIT count`: Limits The Output to <count>

        ```sql
        SELECT username FROM account ORDER BY username LIMIT 3;
        ```

    - `LIMIT count OFFSET offset`: Limits The Output and Skips the offset count of rows

        ```sql
        SELECT username FROM account ORDER BY username LIMIT 3 OFFSET 2;
        ```
    
- `FROM table`: specified Table to look in

- `WHERE <NOT?> column < =, <, >, <=, >= > value <OR | AND> `: filters the search
    
- `ORDER BY column <ASC | DESC>`: sorts the output of tables in either Ascending or Descending

- `DELETE <column?> FROM table <WHERE?>`

    ```sql
    DELETE FROM accounts WHERE username = "default";
    DELETE * FROM account WHERE verified = False;
    ```

- `UPDATE table SET column = value <WHERE?>`:

    ```sql
    update accounts set password = "myNewPassword" where username = "master";
    ```

- `alter table <name>`:

    - `ALTER TABLE name ADD COLUMN datatype`: add a new Column to a Table
    - `ALTER TABLE name DROP COLUMN column`: drop a column
    - `ALTER TABLE name RENAME COLUMN old_name TO new_name`: rename a column
    - `ALTER TABLE name MODIFY COLUMN column datatype`: change datatype of a row

- text after `--` or `#` can used to specify comments

    (xvi) Nodejs:

        (a) `npm install mysql`
        (b) `index.js`

            import mysql from 'mysql';
            const db = mysql.createConnection({
                host: "localhost",
                user: "user",
                password: "password",
                database: "my_db"
                //... More Options Available see Documentation
            });
            // const db = mysql.createConnection('mysql://user:password@host/database?debug=true&charset=BIG5_CHINESE_CI&timezone=-0700');

            db.connect();

            db.query('SELECT * FROM accounts', (error, results, fields)=>{
                if (error) {
                    // Handle Error
                    return null;
                }
            })

            db.destroy(); 

            // Pool

            const dbPool  = mysql.createPool({
                connectionLimit: 10,
                host: 'localhost',
                user: 'user',
                password: 'password',
                database: 'my_db'
            });

No-SQL Databases:

2. MongoDB

    (i) Structure: https://phoenixnap.com/kb/wp-content/uploads/2021/04/mongodb-vs-mysql-database-structure.png

    (ii) Installation (Debian Based):

        $ sudo apt-get install gnupg curl
        $ curl -fsSL https://www.mongodb.org/static/pgp/server-7.0.asc | sudo gpg -o /usr/share/keyrings/mongodb-server-7.0.gpg --dearmor
        $ echo "deb [ signed-by=/usr/share/keyrings/mongodb-server-7.0.gpg ] http://repo.mongodb.org/apt/debian bookworm/mongodb-org/7.0 main" | sudo tee /etc/apt/sources.list.d/mongodb-org-7.0.list
        $ sudo apt-get install -y mongodb-org

    (iii) Commands for Databases

        (a) `show dbs` Lists Databases
        (b) `db` shows current Database
        (c) `use <DatabaseName>` Creates or switches to The Database
            (Note: When Creating a Database it Requires The Database to atleast have 1 Collection inside it or it'll be not Saved)
        (d) `db.dropDatabase()` Deletes Current Database

    (iv) Commands Collections

        (a) `show collections` shows Collections
        (b) `db.createCollection('<Collection Name>')` Creates a New Collection with the Specified Name
        (c) `db.<CollectionName>.drop()` Deletes Specified Collection

    (v) Commands for Documents (BSON)

        (a) `db.<CollectionName>.insert(<Object>)` Insert a JavaScript Object as a BSON Document in the Collection as BSON

            db.accounts.insert({
                'username': 'FlytoTheSpace',
                'email': 'dummy@gmail.com',
                'password': '123abc'
            })

        (b) `db.<CollectionName>.insertMany(<Array of Objects>)` Insert Many JavaScript Objects into individual BSON Documents in the Collection

            db.accounts.insertMany([
                {
                    'username': 'FlytoTheSpace',
                    'email': 'dummy@gmail.com',
                    'password': '123abc'
                },
                {
                    'username': 'Sarah',
                    'email': 'Sarah1234@outlook.com',
                    'password': '123abc'
                },
                {
                    'username': 'Michael',
                    'email': 'Michaelzbit32@gmail.com',
                    'password': '123abc'
                }
            ])

        (c) `db.<CollectionName>.find(<JSON>)` searches for Documents with the matching Key-Value Pairs,

            db.accounts.find({'username': 'Michael'})
            db.accounts.find() // Returns all of the Documents in the Collection

        (d) `db.<CollectionName>.findOne(<JSON>)` same as `.find()` function but Stops The Search after just finding One Document

        (e) `db.<CollectionName>.update(<searchJSON>, <UpdateToJSON>, <optionsJSON>)` first Argument is used to Search The Document in the Database and then the Key-Value pairs in the Second Argument will replace those one's in the Document

            db.accounts.find({'username': 'Michael'}, {'password': "mysecretpassword"})

            (I) <optionsJSON>:

                (A) `upsert: boolean`: Whether to Insert a Document or Not If No Document is been found in the Search

        (f) `db.<CollectionName>.remove(<JSON>)` removes the Documents

    (vi) Examples:-

        (a) Create A Database

            use MyDB
            db.createCollection('comments')

        (b)

    (vii) Chained Functions

        (a) `.pretty()` formats the Displaying Content of `.find()`

            db.accounts.find().pretty()

        (b) `.limit(<count>)` Limits the Document Output of `.find()` function

            db.accounts.find().pretty().limit(2) // Only shows 2 Documents

        (c) `.count()` counts the Number of Documents found by `.find()` function (`.limit()` function will not effect this)

            db.accounts.find().count()

        (c) `.sort({<key>: <1 or -1>})` sorts the output of `.find()` function in Ascending/Descending order (1 for Ascend, 0 for Descend)

            db.accounts.find().sort({since: 1}) // Ascending Order
            db.accounts.find().sort({since: -1}) // Decending Order
        
        (d) `.skip(<count>)` Skips The <count> of Documents

            db.accounts.find().pretty().limit(2).skip() // Shows 3rd and 4th Document and skips 1st and 2nd

Other:

3. Redis

    (i) Installation:

        $ sudo apt install redis
        $ redis-server # start the server 
        $ redis-cli # interact with the Server Server

    (ii) `redis-cli` Connects to The Redis Database

        (a) `-h <host>`
        (b) `-p <port>`
        (c) `-a <Password>`
        (d) `-u <URI>` Requires the URI in the following Format:

            redis://username:password@subdomain.hosted.com:16379/0
                        ↓       ↓            ↓             ↓     ↓
                    username password    Domain/IP        Port  Subnet


    Commands:

    (ii) `quit` quits out of the database
    (iii) `clear` clears the terminal
    (iv) `Info` Info about the Redis Server

    (iv) CRUD:

        (a) `set <key> <value>`: set a key-value pair
        (b) `get <key>`: get a key-value pair
        (c) `del <key>`: delete a key-value pair
        (d) `exists <key>`: check if a key-value pair exists (1 for true, 0 for false)
        (e) `keys <pattern>`: Shows Keys matching a certain Pattern

            Patterns:

            (I) `*` Shows all The Keys-value paris

        (f) `flushall`: Empties the Database

    (v) Expiry:

        (a) `expire <key> <seconds>`: makes a Key-Value Pair Expire after <seconds>
        (b) `ttl <key>:` shows the expiry (in-seconds) of the Key-Value Pair

            (I) `-1` stands for "Permanent"
            (II) `-2` stands for "Gone"

        (c) `setex <key> <seconds> <value>`: make Expireable Key-value Pairs

    (vi) List (Array):

        (a) `lpush <key> <value> [<values...>]`: push values to the left side of a the List
        (b) `rpush <key> <value> [<values...>]`: push values to the right side of a the List

        (c) `lrange <listKey> <startIndex> <stopIndex>`: outputs all the values in a list

                > lpush fruits apple
                > lrange fruits 0 -1
                (1) apple

            (a) set <stopIndex> to `-1` to get all the Items in the List

        (d) `lpop <listKey>`: removes the left most item in the list and returns it
        (e) `rpop <listKey>`: removes the right most item in the list and returns it

    (vii) SET:

        (a) `sadd <key> <value> [<values...>]` create a SET
        (b) `smembers <setKey>` outputs all the Key-Value Pairs inside the SET
        (c) `srem <setKey> <value>` remove the value from the SET

    (viii) Hashmap (Map, Dict, Object):

        (a) `hset <key> <field> <value>` create a Hashmap

            > hset person name Dave
            > hset person age 29

        (b) `hget <key> <field>`
            
            > hget person name
            "Dave"

        (c) `hgetall <key>` outputs all the fields and values

            > hgetall person
            (1) "name"
            (2) "dave"
            (3) "age"
            (4) "29"

        (d) `hdel <key> <field> [<fields...>]` deletes the specifed field-value pairs

        (e) `hexists <key> <field>` check if the specified Field-Value Pair Exists

    Redis for Programming Languages:

    (ix) JavaScript

        (i) Install redis:
            
            $ npm install redis

        (ii) import Redis

            import Redis from 'redis';

        (iii) create a Client

            const redisDB = Redis.createClient({ url: '127.0.0.1:6379' });

        (iv) Interact with The database

            redisDB.set("test", "name")

        (Note: All The Commands are the same but are Instead Represeted as Functions)
   
