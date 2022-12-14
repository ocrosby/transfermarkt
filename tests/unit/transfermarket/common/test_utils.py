import pytest

from transfermarket.common import utils


class TestUrlJoin:
    # noinspection PyTypeChecker
    def test_undefined_base(self):
        with pytest.raises(ValueError, match="Undefined base URL!"):
            utils.urljoin(None, "path")

    # noinspection PyTypeChecker
    def test_undefined_path(self):
        with pytest.raises(ValueError, match="Undefined path!"):
            utils.urljoin("base", None)

    # def test_empty_base(self):
    #     with pytest.raises(ValueError, match="Empty base URL!"):
    #         utils.urljoin("", "path")

    # def test_empty_path(self):
    #     with pytest.raises(ValueError, match="Empty path!"):
    #         utils.urljoin("base", "")

    def test_base_ends_with_slash(self):
        assert utils.urljoin("base/", "path") == "base/path"

    def test_path_starts_with_slash(self):
        assert utils.urljoin("base", "/path") == "base/path"

    def test_base_ends_with_slash_and_path_starts_with_slash(self):
        assert utils.urljoin("base/", "/path") == "base/path"

    def test_base_does_not_end_with_slash_and_path_does_not_start_with_slash(self):
        assert utils.urljoin("base", "path") == "base/path"

    def test_base_ends_with_slash_and_path_does_not_start_with_slash(self):
        assert utils.urljoin("base/", "path") == "base/path"

    def test_base_does_not_end_with_slash_and_path_starts_with_slash(self):
        assert utils.urljoin("base", "/path") == "base/path"

    def test_base_ends_with_slash_and_path_is_empty(self):
        assert utils.urljoin("base/", "") == "base/"

    def test_base_is_empty_and_path_starts_with_slash(self):
        assert utils.urljoin("", "/path") == "/path"

    def test_base_is_empty_and_path_is_empty(self):
        assert utils.urljoin("", "") == ""

    def test_base_is_empty_and_path_does_not_start_with_slash(self):
        assert utils.urljoin("", "path") == "path"

    def test_base_is_empty_and_path_ends_with_slash(self):
        assert utils.urljoin("", "path/") == "path/"


class TestSlugify:
    def test_with_undefined_value(self):
        assert utils.slugify(None) is None

    def test_with_empty_value(self):
        assert utils.slugify("") == ""

    def test_with_simple_name(self):
        assert utils.slugify("John Jones") == "john-jones"

    def test_removes_dots(self):
        assert utils.slugify("a.b c") == "ab-c"

    def test_removes_single_quotes(self):
        assert utils.slugify("Shae O'Malley") == "shae-omalley"
