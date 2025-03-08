class MultiDBRouter:
    def db_for_read(self, model, **hints):
        """Send read queries to the appropriate database."""
        if model._meta.app_label == 'student_app':
            return 'default'  # Use student_db
        elif model._meta.app_label == 'library_app':
            return 'library'  # Use library_db
        return None

    def db_for_write(self, model, **hints):
        """Send write queries to the appropriate database."""
        if model._meta.app_label == 'student_app':
            return 'default'  
        elif model._meta.app_label == 'library_app':
            return 'library'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """Allow relationships within the same database only."""
        if obj1._state.db == obj2._state.db:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """Control which database migrations are applied to."""
        if app_label == 'student_app':
            return db == 'default'
        elif app_label == 'library_app':
            return db == 'library'
        return None
