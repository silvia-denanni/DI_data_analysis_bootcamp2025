import math

# Create a Pagination class that simulates a basic pagination system.

# Step 1: Create the Pagination Class to represent paginated content.
# Step 2: Implement the __init__ Method
# Step 3: Implement the get_visible_items() Method


class Pagination():
    def __init__(self, items = None, page_size = 10):
        self.items = items
        self.page_size = page_size
        self.current_index = 0
        self.total_pages = math.ceil(len(self.items) / self.page_size)
        if items is None:
            items = []

    def get_visible_items(self):
        return self.current_index
    
# This method returns the list of items visible on the current page.
# Use slicing based on the current_idx and page_size.


# Step 4: Implement Navigation Methods

# These methods should help navigate through pages:

# go_to_page(page_num)
# → Goes to the specified page number (1-based indexing).
# → If page_num is out of range, raise a ValueError.

# first_page()
# → Navigates to the first page.

# last_page()
# → Navigates to the last page.

# next_page()
# → Moves one page forward (if not already on the last page).

# previous_page()
# → Moves one page backward (if not already on the first page).

# 📝 Note:

# Pages are indexed internally from 0, but user input is expected to start at 1.
# All navigation methods (except go_to_page) should return self to allow method chaining.
