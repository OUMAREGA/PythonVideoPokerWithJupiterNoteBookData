import pyflix.catalogue as c


def test_show_created_with_right_title():
    my_show = c.TvShow('supergirl')
    assert my_show.title == "Supergirl"


def test_add_of_one_episode():
    my_show = c.TvShow('supergirl')
    my_show.add_episode("Episode 1", 1, 2, 45, 2015)
    assert len(my_show.episodes) == 1


def test_attributes_are_not_mutable():
    my_show = c.TvShow('supergirl')
    my_show.add_episode("Episode 1", 1, 2, 45, 2015)
    playlist = my_show.episodes
    playlist.append("my other episodes to watch")
    assert len(my_show.episodes) == 1
