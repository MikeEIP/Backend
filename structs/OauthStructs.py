# from mongoengine import *
#
#
# class OauthUserData(Document):
#     id = IntField(required=True, primary_key=True)
#     username = StringField(required=True, unique=True, null=False)
#
#     meta = {'collection': 'oauth_users'}
#
#
# class OauthClientData(Document):
#     name = StringField(required=True)
#     client_id = StringField(required=True, primary_key=True)
#     client_secret = StringField(required=True, unique=True, null=False)
#     client_type = StringField(default="public")
#     _redirect_uris = StringField()
#     default_scope = StringField(default="email address")
#
#     meta = {'collection': 'oauth_client'}
#
#     @property
#     def user(self):
#         return OauthUserData.objects.get()
#
#     @property
#     def redirect_uris(self):
#         if self._redirect_uris:
#             return self._redirect_uris.split()
#         return []
#
#     @property
#     def default_redirect_uri(self):
#         return self.redirect_uris[0]
#
#     @property
#     def default_scopes(self):
#         if self.default_scope:
#             return self.default_scope.split()
#         return []
#
#     @property
#     def allowed_grant_types(self):
#         return ['authorization_code', 'password', 'client_credentials',
#                 'refresh_token']
#
#
# class OauthGrantData(Document):
#     meta = {'collection': 'oauth_grant'}
#
#     id = IntField(primary_key=True)
#     user_id = IntField(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE')
#     )
#     user = relationship('User')
#
#     client_id = db.Column(
#         db.String(40), db.ForeignKey('client.client_id', ondelete='CASCADE'),
#         nullable=False,
#     )
#     client = relationship('Client')
#     code = db.Column(db.String(255), index=True, nullable=False)
#
#     redirect_uri = db.Column(db.String(255))
#     scope = db.Column(db.Text)
#     expires = db.Column(db.DateTime)
#
#     def delete(self):
#         db.session.delete(self)
#         db.session.commit()
#         return self
#
#     @property
#     def scopes(self):
#         if self.scope:
#             return self.scope.split()
#         return None
