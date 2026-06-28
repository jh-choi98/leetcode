# LLD / OOP Interview

## Create simple, maintainable, and easy to understand code.

## Logical and maintainable overview

This interview is exploring how you structure your methods and classes to ensure the logical separation of concerns is clear. It's exploring how you name variables, methods, and classes in a way that future developers with no previous knowledge of the code can understand how it works, evolve the logic, investigate it, and debug it when needed.

Test names should describe business and technical requirements, and the
test code should be consistent with the test names.

### What does the logical and maintainable competency assess?

This competency measures your ability to write maintainable, readable,
reusable, and understandable code.

### How should I best prepare for this competency

- Get technical. We are a technology company. So be as technical as possible in your answers.
- Be ready to write code in real-time on an online editor during your interview.
- Be prepared to gather qualifying requirements and translate into clean written code, checking edge cases.
- Be prepared to write syntactically correct code, no pseudo code.

## How to best showcase logical and maintainable

### Criteria and pro tips for addressing them

#### Simple Code

Criteria: Create simple code (e.g., leverage reuse, properly format, no improper coding constructs).

Tips:

- Feel free to write out examples of how your code will be used. If it seems overly complex, go back and think if that's how you'd want your coworkers to use their code, and if there are ways to simplify it.
- Time is precious; rather than spending time trying to think of an optimal solution start with a working solution, no matter how simple, and enhance it as you go.
- Think about extendibility, make sure you are able to extend the code
  when/if requirements change, avoid a single function that does
  everything.

#### Maintainable Code

Criteria: Create maintainable code (e.g., quickly able to trace impact of changes, clear variable naming conventions).

Tips:

- Make sure that your method, parameter, and variable names are clear & descriptive (e.g. don't just use "a" or "foo") and try to separate out functionality into discrete methods/functions with clear responsibilities. Remember that we'll likely run/operate software longer than it took to write it, so the clearer things are future maintainers will thank you.
- Your code should be reasonably easy to maintain as the traffic or load
  increases.

#### Organize Code

Criteria: Organize code in a way that is easy to read and understand.

Tip:

- Use functions and classes, and inheritance to break up your solution
  into logical components. This improves readability and makes it easier
  to extend the solution for new requirements.

#### Syntactically Correct Code

Criteria: Create syntactically correct code, or it would be with minor improvements.

Tips:

- Pick the coding language you are most comfortable with - we're not looking for any language-specific knowledge (unless you've been told otherwise). Ensure that you're comfortable with the idioms and conventions of your chosen language (e.g. error/exception handling, managing resources like file I/O or network connections etc.) and use descriptive variable and method names.
- If you need a method call but forget its exact name or arguments, call
  that out and ask the interviewer if you can make up a name and
  arguments.

#### Working Code

Criteria: Create code that works as intended.

Tips:

- Start small, solving one thing at a time, and iterate over your
  solution as you ask questions or the interviewer does more follow-ups.
  If you see clear design patterns or abstractions that can be applied
  from the very beginning, apply those! It is better to realize code can
  be refactored to support more requirements in a maintainable way,
  rather than building a complex solution or investing time applying a
  design pattern that doesn't solve the requirements.
- Think through test cases (both working and breaking), edge cases,
  boundary conditions, null/nil/none etc. Try and enumerate these cases
  before you begin coding so that when you have a solution you feel
  works, you can use these as validation. Be sure to also confirm test
  cases with your interviewer.

## Example

Now that you have an understanding of the coding competency, logical and
maintainable, let's take a look at what this looks like in action.

```C++
1 class BookFilter

2      {

3          virtual bool apply(Book) = 0;

4      };

5      class TitleFilter : public BookFilter

6      {

7      private:

8          std::string m_title;

9      public:

10          TitleFilter(std::string title)

11         {

12              m_title = title;

13         }

14          override bool apply(const Book& book)

15         {

16             if (Book.title.find(m_title) != std::string::npos)17

17                  return true;

18

19              return false

20          }

21      };

22      typedef enum

23      {

24          Big,

25          Medium,

26          Small

27      } BookSize;

28      class BookSizeFilter : BookFilter

29      {

30      private:

31          BookSizeFilter(BookSize desiredSize)

32          {

33             m_desiredSize = desiredSize;

34          }

35          override bool apply(const Book& book)

36          {

37              unsigned int minPages = 0;

38              unsignedint maxPages = 0;

39

40              switch m_desiredSize

41              {

42              case Big:

43                  minPages = 0;

44                  maxPages = 100;

45              case Medium:

46                  minPages = 101;

47                  maxPages = 500;

48              case Small:

49                  minPages = 501;

50                  maxPages = std::UINT_MAX;

51              }

52              return (Book.pageCount >= minPages) && (Book.pageCount < maxPages);

53          }

54      }

55      bool BookPassesFilters(const Book& book, std::List<BookFilter>& filters)

56      {

57          for (BookFilter filter : filters)

58          {

59              if (!filter.apply(book))

60                  return false;

61          }

62          return true;

63      }

64      std::set<Book> FilterBooks(std::List<Book> bookList, std::List<BookFilter>& filters)

65      {

66          std::set<Book> rval;

67          for (Book book : bookList)

68          {

69              if (bookPassesFilters(book, filters))

70                  rval.push_back(book);

71          }

72          return rval;

73      }
```

### What Makes This A Good Response

This response shows strength in:

- Code shows breaking functionality into separate functions and classes rather than a monolithic implementation.
- The use of an enum helps consistency and provides an idiomatic way for users of the code to specify parameters.
- A class structure makes the addition of new filters, even by those who don't have access to the source code easy.
- Code is easy to read. Classes and member variables are descriptive enough to know what they represent without being verbose.

## Logical and maintainable Podcast Audio Transcript

Derek:

All right, thanks for joining us today, everyone. My name is Derek, and I am a lead recruiter with the operations business in Amazon. And I'm joined today by two of our senior engineers, Carlos and Aaron. Today, our focus will be on the logical and maintainable coding session of your interviews during your interview loop. I know there's other podcasts, YouTube videos you'll be able to do, but for this section, we will be focusing on the coding portion.

Derek:

So just to jump into it, Aaron and Carlos, when candidates are prepping, they often see questions online that might give them some additional insight to what they'll experience. And they notice that there might be a similarity between both these systems design interviews and the logical and maintainable interviews. Can you guys highlight what the difference is between those?

Carlos:

Sure, yeah. Hey, everyone. My name is Carlos here. So yeah, we can start by saying that they are in touch with completely two different areas, right? On system design, we are talking more about different components and how those interact between each other on a high level on a product that we are building, or a service, right?

Carlos:

On the other hand, when we are talking about logical and maintainable, it focuses more on the code quality, and not only on the code quality, but also on the code extensibility, in the sense of making sure that the code that you build is great, is extensible, can be maintained by other people, and that we can add new and new requirements going forward in the future. So even though both of them are looking into this idea of your extensibility and growth, both of them do it in a different level, code-wise, compared to the design-wise, in that sense. Aaron, do you want to add something there?

Aaron:

No, plus one on that. I think it's just, yeah, mainly we're in system design. Like you said, we're concentrating on high level architecture, the interplay between different components and talking about things generally at maybe even the service level, right? Like you said, we're coding here. And logical and maintainable is great to see throughout the coding and all the codings. We love when people break things up into functions and use good variable names, and those sorts of things. But the logical and maintainable question specifically is really going to provide an opportunity to showcase that and to show that you can break a problem up into different logical coding components and then improve them or show the interactions between them.

Derek:

Awesome, yeah. And then to follow up on that, so that's really essentially what interviewers are going to be looking for. And when a candidate is sent confirmation, they will see and have access to a "live code link." So can you give us an idea of what this live code looks like and how it works, and how interviewers might use that to assess and evaluate the code that's provided?

Aaron:

Sure, yeah. Live code's essentially just a collaborative text editor. You may have seen other sort of text editors for code online, or whatnot, but live code itself is just you're going to be able to type into it, the interviewer can type into it, and you'll be able to see what each other is typing. You can pick a programming language in it, but there's no actual compiler behind live code. So all it's going to really be doing is some syntax highlighting to help things out.

Carlos:

Yeah. And I would say, though, as Aaron put it, there's a really nice text editor, that we can see what each person is writing. And I highly recommend, even if we are not dealing specifically with code, it's also a good place to share the ideas. And you see that [inaudible 00:03:56] like a notepad where you can write your ideas, your actions, your thoughts. And you can share that idea with the interviewer at that time in real life, right?

Aaron:

Yeah. And the other thing live code lets you do is it lets you pick sort of a syntax editor for whatever code programming language you are most comfortable with. So in the interview, we definitely recommend candidates pick the language they're most comfortable with or even the language they think is going to be best suited to the problem, if you're an expert in multiple programming languages. We're not hiring specifically for a specific programming language that you might know. We're definitely looking more for the underlying computer science fundamentals that a candidate has, rather than knowledge of a specific tech area or programming language.

Derek:

Got it. And having said that, how might a candidate overcome ... or is it ever an issue if someone might have expertise with C++? Their interviewer might have never necessarily used that as a primary stack. Are there any areas where that might be a concern or issue, Aaron?

Aaron:

There shouldn't be. We expect our interviewers to also be strong in their CS fundamentals. And so like you mentioned, C++, that's the primary language that I code in. But obviously, I interview a lot of people who code in Java or Python. While I have familiarity with those languages, I'm not an expert in them. But I can still read the code. Right? I can still read the code. And if I have a question, I ask a candidate to explain it to me. And so it can be a little bit of a learning process, but generally a good programmer is going to be able to follow along.

Aaron:

And as long as the candidate is being open and communicative about their process, it's going to be great. And we're not generally, as interviewers, grading people, I guess, on their syntax, right? So like I said, live code doesn't have a compiler behind it. So the syntax, while it's still important, we want to see good syntax as much as possible, if you forget a semicolon here or there, the interviewer generally isn't going to care, and it's not going to affect the outcome of the interview.

Derek:

Got it. And Carlos, anything to add there?

Carlos:

Oh, yeah. One thing I wanted to add there in that sense is that, as interviewers, we may face sometimes people that are coding in a language that we are not proficient with. But even if we are proficient with a language, what you will see a lot as a candidate is that we would like to know how you are thinking. And how you are thinking means asking questions of what you are creating. And that way, we understand the idea, the approach that you are taking. And with that, we can understand the way that you are coding it in whatever language it's being done, even if we are not that proficient with that specific language, right? So the nit-pick there to say is expect questions from the interviewers, expect to describe the idea, the approach, and clarify any kind of doubt of what you are using specifically on that language.

Derek:

Got it.

Aaron:

Yeah. And something that candidates will often do as well is they'll both verbally say what their solution is, and they'll write out a bit of pseudo code, that they'll use comments to sort of lay out their algorithm before they go into implementation. If you've got time for that, that's great too, because again, that's letting us as interviewers see what your thought process is and how you're able to lay things out logically.

Derek:

Okay, awesome. Awesome. And then just in final about the live code link itself and where a candidate would be typing his or her answer, oftentimes a recruiter in preparation might be asked, "Hey, can I use a whiteboard or maybe a pen and paper before I start to put together a solution or answer the question?" What are your thoughts on that, Carlos?

Carlos:

So I mean, it's completely fine. Using any tool that you can for cleaning out your ideas, I think is super fine. I personally think that it's even better ... So just to set some context there, the interviewer there is to help you, not to measure you. So I personally always encourage candidates to use live code as your own whiteboard to write your ideas and to write your thought process, because it helps us to know where to help you, where you are stuck, what is your way of achieving it. But if you feel more comfortable with a pen and paper and you want to try the first approach there, fine, no big deal, go for it, but be ready to stand up and explain the approach and explain your thought process, which is the most interesting thing for the interview, right?

Derek:

Oh yeah, thank you. Aaron, anything else to add there?

Aaron:

Yeah, I think that's great. I would say just some problems lend themselves to drawing them out, like drawing out a tree or a graph or some boxes for an array. And go ahead and do that. Just let your interviewer know that's what you're doing: "Hey, I'm going to draw some things out on paper here to get my thought process going." Let the interviewer know. And then when you're done, hold it up to the camera, right? Let the interviewer see what you've drawn out, just to get that feedback so we can see what you're going for.

Derek:

Awesome. So yeah, it sounds like a couple of the areas that a candidate would set themselves up for some success is asking questions, discussing their approach before putting any code into the live code link, or things of that nature. What if we take the other side of that, and what might be some areas that candidates might fall short or you see struggles when candidates do start to potentially propose a solution, Aaron?

Aaron:

Yeah. I think sometimes candidates get hung up trying to think about the most optimal solution. They're trying to find the trick to the question, or something like that. While there are generally are sometimes with certain problems, optimal solutions, logical and maintainable usually has less of those, right? Like I said, we're really looking for you to lay out your code with functions, classes, to break things up into logical components. And that's much more important, I think, for logical and maintainable than trying to find the most optimal or best solution.

Aaron:

So I do see sometimes candidates spending time at the beginning really trying to find, "Okay, how can I best solve this? What's the best data structure? What's the best algorithm that's going to get me the least amount of time complexity?" And I would say for logical and maintainable, listen to your interviewer. It's great to think about those things up front, but your interviewer will probably be guiding you to building those extensible solutions as opposed to the one that's going to be most optimal, especially if it's taking some time to get there.

Derek:

Absolutely. Carlos, what about you? I know you've run mini interviews. Anything you might have seen in previous interviews?

Carlos:

Yeah. I think that most of the candidates, they struggle to take the interviewer as your colleague and explain their ideas, right? I think that it's really important to think about the interviewer as a person there to help you, to guide the process, to understand what you are doing, and so on, right? So I think that one of these pitfalls that sometimes candidates fall into is talking. Keep an open talk, discuss your approach. Even if it's not the best one, don't feel bad for that. Say, "Hey I'm thinking about this thing. It's not the best or most approached one, or the best one for this problem, but I'm not coming up with a better solution." And then, let's discuss with the interviewer. Let's see what path can we take there from there, and move on, right?

Carlos:

And aligned with what Aaron was saying, I think that the second point there is try to deliver something, try to get something rolling on the website and get even a first proof of concept. Even if it's not the most proficient and performant one, it's better to have something and then iterate over it than not having anything, and then struggling for getting the best approach there. So yeah, those two things, I think, are the most common ones I have seen in my experience.

Derek:

Awesome.

Aaron:

Yeah. I think it's really important to remember to listen to the interview. A lot of times, we see candidates sort of maybe get stuck in their heads and dive towards their solution, and the interviewer is trying to guide them to get the data that they need. You got to remember, you only got generally half an hour or so to do these problems together. So the interviewer is going to maybe be interrupting you and asking you to move off to a different section of the code or work on something else, or say, "Hey, what you're doing right now isn't that important for what I want to see, so let's move on to something else," right? And you want to, as a, I think, candidate, listen to that and be aware of it and follow the guidance of the interviewer so you can get to the points that the interviewer most wants to see.

Derek:

No, absolutely. And then on that point, you mentioned about 30 minutes in theory to potentially provide a solution, what if a candidate does run out of time or maybe they aren't able to get to the best solution? What comes up in those instances, Aaron?

Aaron:

Well, remember, we're assessing not necessarily getting to the best solution, we're assessing thought process, right? We're assessing, are you able to extend the solution? We're imagining, especially with logical material, "Hey, if I use this code, would I be able to use this code? Would I understand it? If I came in a year after you wrote it in a real environment, would I be able to tell what's going on with it? Would I be able to make changes to it?"

Aaron:

So it's not necessarily the final solutions. Oftentimes, the problems are bigger than what you would get or what you can solve in 30 minutes, but we'll be able to see where you're going with it, right? So I would say, don't worry too much about if you don't get to the "best solution," just sort of get to a solution and then be able to discuss it with the interviewer. I think that is the most important data point that we're looking for.

Derek:

Awesome. Carlos, what about you? What are your thoughts there?

Carlos:

Yeah, yeah. I completely agree with what Arran has said. At the end of the day, we are measuring, as we said, your ways of achieving the problems with your thought process. So if you are clean off, if you are open discussing the idea, the approaches from the day one, from the first minute, right, even if the code that is produced is not the best one or more proficient and performant one, the goal there is to see and to be able to see, how would you operate on a day-to-day basis on that kind of task, right?

Carlos:

And most importantly, when we are talking about logical and maintainable, one thing to quote there from Aaron is the idea of saying you have to be able to understand this code in one year time, or make one of your team members to understand this code in one year time. So when crafting that code, think about, how can I make sure that someone else in sometime will be able to handle it and will be able to understand what's happening there, right? Yeah, so it's not like a yes or no, pass or fail. It's more about, "Okay, how much can we understand your code? How much can we extend your code forward?"

Derek:

Got it. Understood. And then to piggyback off of that, and actually the last question I have here, you mentioned this from a logical and maintainable perspective, you see, "Hey, how can someone handle it? How can someone potentially in the future be able to extend it?" So we have three coding interviews. And with logical and maintainable in particular, how might an engineer see the logical and maintainable code be present in their day-to-day life as an engineer in Amazon? Aaron, what are your thoughts there?

Aaron:

I think logical and maintainable is really probably, maybe even the most important of the three coding competencies there. It's closest to what we'd actually be doing in "real life" in the real job, right? You can always optimize something. You can always ask or talk to people through code reviews about better ways to have solved the problem, working as a team. Obviously, we want people to be able to do that on their own as well, but constructing a solution or constructing a system that can be changed and modified and worked on by other people that will be understood by someone coming in just looking at the code is really important, right? We can always over time go back and improve code. But if the code is a spaghetti mess of one-liners and tricks and other things, then it's going to be really hard to optimize that. It's going to be really hard to extend it. It's going to be really hard to understand it. And so, I think logical and maintainable really shows a candidate's ability to work in a collaborative environment on real code.

Derek:

Okay. Thank you for that, Aaron. Now, Carlos, curious, when it comes to logical and maintainable, how would an engineer see logical and maintainable play into their day-to-day life over here?

Carlos:

All right, yeah. Okay. Yeah, so I think that logical and maintainable is one of the things that we see on our day-to-day basis, right? As engineers, we are always creating new technologies from what we currently have, and we get new requirements from our projects and we evolve the code from what we are doing. So at the end of the day, the maintainability and the extensibility of the code that we have created, it helps us drive innovation and grow from there. Yeah, so I think that logical and maintainable is probably one thing that we use on our day-to-day mostly, like on every single scenario we are doing.

Derek:

Okay. I know I promised that the last one was the last question, but I have one more based off of what we just covered. Are there any other ways that you can see a candidate optimize their experience in their preparation? We know of HackerRank, we know of Leetcode. Are there any other mediums or tips that you might have as somebody is preparing for their interview loop, Aaron?

Aaron:

Yeah. Obviously, especially for logical maintainable, treat it like you would be writing code for a real job. HackerRank and Leetcode are great places to work on the other coding competencies and really get a good, solid understanding and practice at doing those sorts of questions that require the correct use of data structures and algorithms, or to solve weird problems. But like we've said in the past, logical maintainable is not so much looking for that. We're really looking for how you would write code that other people would use.

Aaron:

Some things I think I could suggest there to watch out for while you're doing your logical and maintainable thing, and this applies to other coding competencies too, is if you see yourself copying and pasting code, like a bunch of if statements all in a row, that's a good signal that maybe it's time to break that out and put that into a function. And remember that talking and listening to your interviewer is going to really help with logical and maintainable. We're not always looking for a trick question. These aren't trick questions or things that have specific best answers to them even necessarily, but we want to get through the first parts of the problem, and then we want to get onto the extensions of the problem.

Aaron:

So ask the interviewer questions, try to clarify those requirements up front, and then spend enough time thinking about the problem and the solution so that you can craft code that is going to be able to be easily modified and easily understood by other people. That's really what the interviewers are looking for. So just being present and aware, I think, during the logical and maintainable is the best thing that you can do. I don't know that there's a huge number of other HackerRank or Leetrank style problems that you can do, but you can certainly practice breaking things up into functions, crafting good solutions that would be easily understood by other people while you're doing those sorts of practice problems.

Derek:

Right. Yeah, no, absolutely. Carlos?

Carlos:

Oh sure, okay. They're [inaudible 00:20:13] in the internet, right? Of course, there is this Leetcode and HackerRank to train maybe the data-centered skills or the problem-solving skills. When we are touch racing on logical and maintainable, I would say that it's always good to take any of those exercises and try to make it as clean as possible and as extensible as possible, right? And think about it not that much about trying to solve the best problem in the best way, but more about like, "Okay, how can I add more and more features to these requirements? How can I add more and more ideas there," and increase your project gradually. So I think that any of those tools would work, and any of those tools ... like even taking the smallest exercise and trying to make it bigger and bigger, is a really great approach to practice it.

Aaron:

Yeah. Another thing that you can do while you're sort of practicing on the online coding questions too, is often those solutions will get run through a whole bunch of different test cases. And one thing to look out for is when it fails a test case, if you're deleting all of your code and rewriting your solution from the beginning, that may be a signal that you're not thinking about the problem as much as you should up front, or that you've not created your solution in as extensible a way as maybe it could be done.

Aaron:

So both in those sorts of environments for practice and also in your interview, as new requirements get added on or test cases get brought up that maybe show flaws in the solution, try to make sure you're working with the solution that you've already crafted and not just deleting the whole thing and starting over. That's a signal that maybe you haven't put as much thought into the solution, or maybe it wasn't created as cleanly and extensively as it could have been. So, something you could watch out for as you're practicing. I certainly practiced before my Amazon interview on those sorts of sites, and it was really helpful.

Derek:

Awesome. Well, thank you both so much. Going to ask one thing. Did I miss anything? Are there any last minute tidbits you want to add before letting the two of you go on your way?

Carlos:

I would like to say, I mean, I don't think we have visited ... we have talked a little bit about it, or even a lot about it, but I think it's really, really important to remember and to bring back the idea that the interviewer is not just for judging you, is for helping you. So keep an open discussion with them. Listen to their thoughts, listen to their ideas, and be open to describe your approaches. That would be my one-liner best recommendation or suggestion there.

Derek:

Awesome. Aaron, anything else to send us on our way?

Aaron:

No, that's exactly what I was going to say. I look forward to interviewing anybody who might be listening to this.

Derek:

Awesome. Well, thank you both so much. And thank you all for listening. Hopefully, this provided some good insights for you all to have a fun and exciting interview loop with Amazon.
