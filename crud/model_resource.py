from import_export import resources

from crud.models import Person


class PersonResource(resources.ModelResource):
    class Meta:
        model = Person
        import_id_fields = ('id',)
        fields = ('id', 'first_name', 'last_name', 'phone', 'email')
