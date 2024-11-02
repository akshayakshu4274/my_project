from password_validator import validate_passwords

def test_validate_passwords():
    assert validate_passwords("asqwr1234@1,aF145#,2w3E*,2We3345") == "asqwr1234@1"

