<h3 align="center">aadinspector</h3>

<p align="center"> This package will help to validate azure b2c jwt token.
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Authors](#authors)

## 🧐 About <a name = "about"></a>

This package will help to validate azure b2c jwt token.

## 🏁 Getting Started <a name = "getting_started"></a>
- Dependancy & prerequisite 
    - Python >=3.6 should be installed.
    - "cryptography==37.0.4"
    - "PyJWT==2.4.0"
    - "requests==2.28.1"

- To Start experimenting this package you need to install it.

- [Step - 1]
```

    pip install aadinspector

```
 jwt_validator = JWTValidator("{tenant_id}")
    #jwt_validator.set_name_of_policy("name_of_policy")
    is_verified, token = jwt_validator.validate("{encoded_token}")
    # if token is verified then is_verified=True if not it will be False
    # if token verified you will get decoded token in token else error.
    print(is_valid)
    print(token)
```

## ✍️ Authors <a name = "authors"></a>

- [Dinesh Kushwaha](https://pypi.org/user/dinesh-pypi/) - Idea & Initial work

See also the list of [contributors](https://github.com/dinesh-kushwaha) who participated in this project.