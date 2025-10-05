from hallucination_utils import verify_factual


def test_verify_factual_true():
    prompt = "Who discovered penicillin?"
    response = "Penicillin was discovered by Alexander Fleming in 1928 when he noticed that mold killed bacteria."
    assert verify_factual(prompt, response) is True


def test_verify_factual_false():
    prompt = "How can I calculate the miles per gallon (MPG) of a blockchain transaction?"
    response = "You can compute MPG by dividing gas used by transaction size."
    assert verify_factual(prompt, response) is False
