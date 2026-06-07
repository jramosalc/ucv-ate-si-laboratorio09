from travel_assistant.tools.culture_tools import get_local_culture_info


def test_get_local_culture_info_cusco():
    result = get_local_culture_info("Cusco")

    assert result["status"] == "success"
    assert result["destination"] == "Cusco"
    assert len(result["gastronomy"]) >= 1
    assert len(result["customs"]) >= 1
    assert len(result["useful_phrases"]) >= 1


def test_get_local_culture_info_buenos_aires():
    result = get_local_culture_info("Buenos Aires")

    assert result["status"] == "success"
    assert any("asado" in food.lower() for food in result["gastronomy"])


def test_get_local_culture_info_paris():
    result = get_local_culture_info("Paris")

    assert result["status"] == "success"
    assert len(result["gastronomy"]) >= 1
    assert any("bonjour" in phrase.lower() for phrase in result["useful_phrases"])


def test_get_local_culture_info_default():
    result = get_local_culture_info("Tokio")

    assert result["status"] == "success"
    assert len(result["gastronomy"]) >= 1
    assert len(result["customs"]) >= 1
    assert len(result["useful_phrases"]) >= 1
