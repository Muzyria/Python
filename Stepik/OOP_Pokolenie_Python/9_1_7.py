class Pagination:
    def __init__(self, data, page_size):
        self.data = data
        self.page_size = page_size
        self.total_pages = self._calculate_total_pages()
        self.current_page = 1

    def get_visible_items(self):
        start_index = (self.current_page - 1) * self.page_size
        end_index = start_index + self.page_size
        return self.data[start_index:end_index]

    def prev_page(self):
        if self.current_page > 1:
            self.current_page -= 1
        return self

    def next_page(self):
        if self.current_page < self.total_pages:
            self.current_page += 1
        return self

    def first_page(self):
        self.current_page = 1
        return self

    def last_page(self):
        self.current_page = self.total_pages
        return self

    def go_to_page(self, page_number):
        if 1 <= page_number <= self.total_pages:
            self.current_page = page_number
        elif page_number <= 0:
            self.current_page = 1
        else:
            self.current_page = self.total_pages
        return self

    def _calculate_total_pages(self):
        return (len(self.data) + self.page_size - 1) // self.page_size
