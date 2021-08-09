from app import catfact

def test_catfact():
    fact = catfact().json
    print(fact)

    assert fact['length'] > 0

test_catfact()