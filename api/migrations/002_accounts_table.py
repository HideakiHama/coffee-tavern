steps = [
    [
        ## Create the table
        """
        CREATE TABLE accounts (
            id SERIAL PRIMARY KEY NOT NULL,
            email VARCHAR(255) NOT NULL UNIQUE,
            hashed_password VARCHAR (255) NOT NULL,
            user_name VARCHAR(255) NOT NULL,
            role VARCHAR(10) NOT NULL

        );
        """,
        ## Drop the table
        """
        DROP TABLE accounts;
        """,
    ]
]
