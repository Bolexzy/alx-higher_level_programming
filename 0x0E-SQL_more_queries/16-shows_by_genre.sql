-- Lists all shows and genres linked to the show from the
-- database hbtn_0d_tvshows.
-- Records are ordered by ascending show title and genre name.
SELECT s.title, g.name
    FROM tv_shows AS s
    LEFT JOIN tv_show_genres AS sg
        ON sg.show_id = s.id
    LEFT JOIN tv_genres AS g
        ON sg.genre_id = g.id
    ORDER BY s.title, g.name;

