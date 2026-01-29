from uuid import uuid4

class SessionPersistence:
    def __init__(self, session):
        self.session = session
        if 'lists' not in self.session:
            self.session['lists'] = []

    def all_lists(self):
        return self.session['lists']

    # search for a list by its ID within the session
    def find_list(self, list_id):
        found = (lst for lst in self.session['lists'] if lst['id'] == list_id)
        return next(found, None)

    # add a new list
    def create_new_list(self, title):
        lists = self.all_lists()
        lists.append({
            'id': str(uuid4()),
            'title': title,
            'todos': [],
        })
        session.modified = True

    def update_list_by_id(self, list_id, new_title):
        lst = self.find_list(list_id)
        if lst:
            lst['title'] = new_title
            session.modified = True

    def delete_list(self, list_id):
        self.session['lists'] = [lst for lst in session['lists']
                                if lst['id'] != list_id]
        session.modified = True

    def create_new_todo(self, list_id, todo_title):
        lst = self.find_list(list_id)
        if lst:
            lst['todos'].append({
            'id': str(uuid4()),
            'title': todo_title,
            'completed': False,
            })
            session.modified = True

    def delete_todo_from_list(list_id, todo_id):
        lst = self.find_list(list_id)
        lst['todos'] = [todo for todo in lst['todos'] if todo['id'] != todo_id]
        session.modified = True

    def update_todo_status(list_id, title_id, new_status):
        lst = self.find_list(list_id)
        todo = next(todo for todo in lst['todos'] if todo['id'] == todo_id)
        todo['completed'] = new_status
        session.modified = True

    def mark_all_todos_completed(list_id):
        lst = self.find_list(list_id)
        for todo in lst['todos']:
            todo['completed'] = True
        
        session.modified = True






