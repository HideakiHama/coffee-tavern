steps = [
    [
        ## Create the table
        """
        CREATE TABLE tags (
            id SERIAL PRIMARY KEY NOT NULL,
            name VARCHAR(255) NOT NULL UNIQUE,
        );
        """,
        ## Drop the table
        """
        DROP TABLE tags;
        """,
    ]
]
