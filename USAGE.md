## Usage

Steps to follow:

1. Create directories for specific topics. For example if you solve a problem on 
	*HackerRank* create a directory named `Competitive Programming` or if you 
	learned something new in JavaScript, create a directory for the same.

	Some example categories:

	- Data Structures & Algorithms
	- Meetups
	- C++/JavaScript/Python
	- HTML/CSS
	- Git/Version Control
	- Machine Learning

2. Inside those directories create a [`Markdown`](https://www.markdownguide.org/basic-syntax/) file with your title for example `Variables-in-JavaScript.md`,`Create_React_App.md` etc. Make sure that the markdown file has a title (beginning with a single "#").
Spaces in titles are _not_ recommended since different services render 
markdown differently.

3. Run `python build.py` to auto-generate the new README file for you 
	
	OR
	
	If you are using git, you can install this script as a pre-commit git hook so the REAMDME is autogenerated on each commit.

	`cd .git/hooks/ && ln -s ../../build.py pre-commit && cd -`
 
4. Push your changes.