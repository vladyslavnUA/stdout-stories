A programming challenges in which the CL accepts only JSON input that gets stored into a collection of stories on a separate file.

How to run the challenge:

```
Clone the repo
git clone https://github.com/vladyslavnUA/stdout-stories.git story && cd story

To generate the stories
python3 story.py

To view stats (after you've generated a couple of stories)
python3 stats.py
```

If you would like to reset the previous stories, simply delete the `stories.json` and a new one will be generated when you run the story again. 
I suggest generating a few stories before trying out statistics.

The JSON input I used
```
{"number": "4", "unit": "feet", "place": "kitchen", "adjective": "small", "noun": "note"}
```
