from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import Story

app = Flask(__name__)

app.config['SECRET_KEY'] = "cheese"
debug = DebugToolbarExtension(app)


@app.route('/')
def home_page():
    """Shows home page"""
    return render_template("home.html")


default_prompt = ["place", "noun", "verb", "adjective", "plural_noun"]
default_template = "Once upon a time in a long-ago {place}, there lived a large {adjective} {noun}. It loved to {verb} {plural_noun}."
default = Story(default_prompt, default_template)


@app.route('/madlibs')
def default_questions():
    """Shows Madlibs default questions page"""
    prompt = default.prompts
    return render_template("default_questions.html", prompts=prompt)


@app.route('/default-story')
def get_story():
    """Creates a story based on words"""
    text = default.generate(request.args)

    return render_template("default_story.html", text=text)


@app.route('/choose-your-own')
def choose_your_story():

    return render_template("choice_menu.html")


choice1_prompt = ["verb", "noun"]
choice1_template = "I love to {verb} a good {noun}"
choice1 = Story(choice1_prompt, choice1_template)


@app.route('/choice-1')
def choice_1_questions():
    prompts = choice1.prompts

    return render_template('choice1.html', prompts=prompts)


@app.route('/story-1')
def get_story1():
    """Creates a story based on words"""
    text = choice1.generate(request.args)

    return render_template("story-1.html", text=text)


choice2_prompt = ["adjective", "adjective"]
choice2_template = "A vacation is when you take a trip to some {adjective} place with you {adjective} family."
choice2 = Story(choice2_prompt, choice2_template)


@app.route('/choice-2')
def choice_2_questions():
    prompts = choice2.prompts

    return render_template('choice2.html', prompts=prompts)


@app.route('/story-2')
def get_story2():
    """Creates a story based on words"""
    text = choice2.generate(request.args)

    return render_template("story-2.html", text=text)


choice3_prompt = ["verb", "adverb", "adjective", "noun"]
choice3_template = "He {verb} {adverb} through the large tunnel that led to its {adjective} {noun}."
choice3 = Story(choice3_prompt, choice3_template)


@app.route('/choice-3')
def choice_3_questions():
    prompts = choice3.prompts

    return render_template('choice3.html', prompts=prompts)


@app.route('/story-3')
def get_story3():
    """Creates a story based on words"""
    text = choice3.generate(request.args)

    return render_template("story-3.html", text=text)
