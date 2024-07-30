def test_columns_present(db_cursor):

    db_cursor.execute("PRAGMA table_info(features)")
    columns_info = db_cursor.fetchall()
    column_names = [col[1] for col in columns_info]
    
    # Define the expected column names
    expected_columns = ["home_id", "bathroom1", "hallway"]  
    
    for col in expected_columns:
        assert col in column_names, f"Column {col} is missing"
    
    assert len(column_names) == len(expected_columns), "Unexpected columns found in the table"
