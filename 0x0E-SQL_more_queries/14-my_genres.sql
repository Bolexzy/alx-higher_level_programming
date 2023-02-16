-- Lists all genres of the show Dexter in the database hbtn_0d_tvshows.
-- Records are ordered by ascending genre name.
SELECT g.name
    FROM tv_genres AS g
    INNER JOIN tv_show_genres AS sg
        ON sg.genre_id = g.id
    INNER JOIN tv_shows AS s
        ON s.id = sg.show_id
    WHERE s.title = 'Dexter'
    ORDER BY g.name;
