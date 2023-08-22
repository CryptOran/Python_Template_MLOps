import pytest
from src.App import add

def test_add():
    """Test the add function."""
    
    # Arrange: Set up any necessary data or preconditions
    x = 5
    y = 10
    
    # Act: Call the function/method you're testing
    result = add(x, y)
    
    # Assert: Check the result against expected outcomes
    assert result == 15, f"Expected {x + y}, but got {result}"