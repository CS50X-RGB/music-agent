import json

from app.agents.schema import MusicPlan
from app.tools.music_tools import search_music
from app.tools.last_fm_tools import get_similar_artists


def execute_plan(plan: MusicPlan):

    results = []

    for i, task in enumerate(plan.tasks):

        # Normal task
        if task.depends_on is None:

            if task.agent == "MusicBrainz":

                result = search_music.invoke({
                    "query": task.query,
                    "search_type": task.search_type
                })

            elif task.agent == "Last.fm":

                result = get_similar_artists.invoke({
                    "query": task.query
                })

            else:

                result = f"Unknown agent: {task.agent}"

            # IMPORTANT
            results.append(result)

        # Dependent task
        else:

            previous_result = results[task.depends_on]

            if task.agent == "MusicBrainz":

                # Last.fm returns JSON string
                similar_artists = json.loads(previous_result)

                # For testing, use only top 5
                similar_artists = similar_artists[:5]

                music_results = []

                for artist_data in similar_artists:

                    artist = artist_data["artist"]

                    songs = search_music.invoke({
                        "query": artist,
                        "search_type": "artist"
                    })

                    music_results.append({
                        "artist": artist,
                        "songs": songs
                    })

                results.append(music_results)

            else:

                results.append(
                    f"Dependent task not supported for {task.agent}"
                )

    return results