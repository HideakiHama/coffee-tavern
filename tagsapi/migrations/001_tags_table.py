steps = [    
    [
        ## Create the table
        ## Add profile_picture
        """
        CREATE TABLE tags (
            id SERIAL PRIMARY KEY NOT NULL,
            tag VARCHAR(255)
        );
        """,
        ## Drop the table
        """
        DROP TABLE tags;
        """,
    ],
]