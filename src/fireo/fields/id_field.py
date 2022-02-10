from fireo.fields.base_field import Field
from google.cloud.firestore_v1.field_path import FieldPath


class IDField(Field):
    """Specify custom id for models

    User can specify model id and will save with the same id in firestore otherwise it will
    return None and generate later from firestore and attached to model

    Example
    --------
    .. code-block:: python
        class User(Mode):
            user_id = IDField()

        u = User()
        u.user_id = "custom_doc_id"
        u.save()

        # After save id will be saved in `user_id`
        print(self.user_id)  # custom_doc_id
    """
    def contribute_to_model(self, model_cls, name):
        self.name = name
        setattr(model_cls, name, None)
        model_cls._meta.add_model_id(self)

    @property
    def db_column_name(self):
        """Get field according to column name

        Return the name of the field according to `column_name` attribute if no `column_name` is
        specify then same field name will return
        """
        return '__name__'