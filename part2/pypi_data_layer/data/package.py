import datetime

import mongoengine


class Package(mongoengine.Document):
    id = mongoengine.StringField(primary_key=True)

    created_date = mongoengine.DateTimeField(
        default=datetime.datetime.now)
    summary = mongoengine.StringField(required=True)
    description = mongoengine.StringField()

    home_page = mongoengine.StringField()
    docs_url = mongoengine.StringField()
    package_url = mongoengine.StringField()

    author = mongoengine.StringField()
    author_email = mongoengine.StringField()

    license = mongoengine.StringField()

    languages = mongoengine.ListField(mongoengine.StringField())

    maintainers = mongoengine.ListField(mongoengine.ObjectIdField())
    # health = mongoengine.EmbeddedDocumentField(HealthDoc)

    meta = {
        'db_alias': 'core',
        'collection': 'packages',
        'indexes': [
            'author_email',
            'created_date',
            'license',
            # 'languages.name'
        ]
    }
