# PlanIT Impact
=========

Check it out at <a href="http://planit-impact.herokuapp.com/">http://planit-impact.herokuapp.com/</a>

## <a name="about"></a>About

PlanIT Impact is a web service to help you examine the environmental impacts of new construction in your neighborhood.

PlanIT Impact is a <a href="https://mozillaignite.org/">Mozilla Ignite</a> sponsored expirement in gigabit speed web services.

## <a name="gigabit"></a>Gigabit?
Mozilla threw a hackathon in Kansas City a while back. Everyone who attended made some cool expirements that required gigabit speeds, made available by Google Fiber. PlanIT Impact depends on fiber to quickly pull down 3d models, and all the remote data it can find about the surrounding area. Most tools that use large amounts of geolocation data keep a local database of that data. PlanIT Impact keeps the data remote and pulls it down as it needs it. The speeds made available by fiber internet erase the distinction of local versus remote. At least thats our hypothesis.

## <a name="screenshot"></a>Screenshot
![PlanIT Impact Screenshot](/static/img/screenshot.png "PlanIT Impact Screenshot")

## <a name="development-setup"></a>Development Setup

PlanIT Impact is written in Python, and runs as a standalone [Flask application](http://flask.pocoo.org/).

1. Clone the repo `git clone git@github.com:ondrae/planit_impact.git`
2. Move into the repository folder. `cd planit_impact`
3. Run the setup script. `source setup.sh`
4. Get the AWS keys from [Ondrae](https://github.com/ondrae).
5. Uncomment line 20 in app.py and change it to your username
6. Create a database on your local postgres called 'planit'
7. Start the app. `python app.py`

## <a name="contributing"></a>Contributing
In the spirit of [free software][free-sw], **everyone** is encouraged to help
improve this project.

[free-sw]: http://www.fsf.org/licensing/essays/free-sw.html

Here are some ways *you* can contribute:

* by using alpha, beta, and prerelease versions
* by reporting bugs
* by suggesting new features
* by translating to a new language
* by writing or editing documentation
* by writing specifications
* by writing code (**no patch is too small**: fix typos, add comments, clean up
  inconsistent whitespace)
* by refactoring code
* by closing [issues][]
* by reviewing patches
* by submitting pull requests of the above

[issues]: https://github.com/ondrae/planit_impact/issues

## <a name="issues"></a>Submitting an Issue
We use the [GitHub issue tracker][issues] to track bugs and features. Before
submitting a bug report or feature request, check to make sure it hasn't
already been submitted. You can indicate support for an existing issue by
voting it up. When submitting a bug report, please include a [Gist][] that
includes a stack trace and any details that may be necessary to reproduce the
bug.

[gist]: https://gist.github.com/

