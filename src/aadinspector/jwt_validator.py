from .jwks_handler import JWKSHandler
from .pub_key_handler import PublicKeyHandler
import jwt


class InvalidAuthorizationToken(Exception):
    def __init__(self, details):
        super().__init__('Invalid authorization token: ' + details)


class JWTValidator(object):
    def __init__(self, tenant_id, name_of_policy=""):
        self.tenant_id = tenant_id
        self.name_of_policy = name_of_policy
        print(f"tenant_id - {tenant_id} -name_of_policy {name_of_policy} ")

    def set_tenant(self, tenant_id):
        self.tenant_id = tenant_id

    def set_name_of_policy(self, name_of_policy):
        self.name_of_policy = name_of_policy

    def get_kid(self, token):
        headers = jwt.get_unverified_header(token)
        if not headers:
            raise InvalidAuthorizationToken('missing headers')
        try:
            return headers['kid']
        except KeyError:
            raise InvalidAuthorizationToken('missing kid')

    def get_jwks_keys(self):
        jwks_handler = JWKSHandler(self.tenant_id, self.name_of_policy)
        return jwks_handler.get_jwks_keys()

    def get_jwk(self, kid):
        jwks = self.get_jwks_keys()
        for jwk in jwks:
            if jwk["kid"] == kid:
                return jwk
        raise InvalidAuthorizationToken('kid not recognized')

    def get_public_key(self, token):
        pub_handler = PublicKeyHandler()
        return pub_handler.rsa_pem_from_jwk(self.get_jwk(self.get_kid(token)))

    def validate(self, token):
        try:
            jwt_unverified = jwt.decode(
                token, options={"verify_signature": False})
            iss = jwt_unverified["iss"]
            aud = jwt_unverified["aud"]
            public_key = self.get_public_key(token)
            decoded = jwt.decode(token,
                                 public_key,
                                 verify=True,
                                 algorithms=['RS256'],
                                 audience=aud,
                                 issuer=iss)
            return (True, decoded)
        except Exception as e:
            print(e)
            return(False, e)
