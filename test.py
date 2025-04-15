class Task:
    def _init_(self,title,status = "To-do"):
        self.title = title
        self.status = status
        
    def mark_done(self):
        self_status = "done"