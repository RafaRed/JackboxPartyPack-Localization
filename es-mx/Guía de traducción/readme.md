1.  Create a GitHub account.

2.  The first step in translation will be to find the game you want to start, for example, “pack 6”.

![](.//media/image1.png)

3.  Upon entering the game folder you will probably find a Localization.json file that will be responsible for the words of the game menu. I consider the folder "games" that is more important, let's enter in it for that guide.

![](.//media/image2.png)

4.  Here we find all the games related to that version of the game,
    let's choose "PushTheButton" for this example.

![](.//media/image3.png)

5.  Inside we find 2 files, Localization which is again
    responsible for translating menus in most cases, and the folder
    ‘Content’ which in this case is the place where the content of
    within the game.

![](.//media/image4.png)

6.  In this example we find several files, each responsible for
    something, let's use JokeBoatAnimal.jet for this example:

![](.//media/image5.png)

7.  Some files are found on only one line in a way that
    it’s difficult to translate, for this file we’ll have to do some
    additional steps, otherwise we could proceed to the next steps.
    We continue copying the entire content using the Ctrl + A keys (
    select all text) and Ctrl + C, or we can do 2 clicks on the line and
    then CTRL + C.

![](.//media/image6.png)

8.  We started by copying all content to the site
    <https://jsonformatter.curiousconcept.com> and click on process, to
    let it leave the file with a more pleasant formatting.

![](.//media/image7.png)

9.  We click on the copy icon, to copy the formatted text

![](.//media/image8.png)
10.  We go back to github and click on the edit button

![](.//media/image9.png)

11.  Use the command Ctrl + A and 'delete' to delete all text, and then
    paste the new formatted text in place of the old text.

![](.//media/image10.png)

12.  Now with the better formatted text, we can perform the translation.

![](.//media/image11.png)

13. To perform the translation, just replace the words of the game that
    are in English, and for that it is necessary to have an initial care
    to understand which words are related to the game and which
    are “keys” of the file, usually the file is in the following
    Format:\
    “Key”: ”word to be translated” \
    we must not use any keys, just the words of the game,
    to illustrate in red the keys and words that should not be
    translated- and in blue the word of the game that was translated.

![](.//media/image12.png)

14. After performing the translation (note that it is not necessary to translate everything
    at once, you can do this gradually), you can write a
    description of what was done and send.

![](.//media/image13.png)

15.  After clicking on the submit button, you will be able to see what
    has been removed, modified and changed according to the colors. In
    sequence we click on the “Create pull request” button



![](.//media/image14.png)

16\. Here we have the same screen as in step 14, for you to put information
of what was done. \
we click on the button “Create pull request” to send the request.

![](.//media/image15.png)

17. Okay, we sent our first translation, now we have to wait
    that it is accepted and the original file will be modified,
    thank you!

![](.//media/image16.png)

18. **if you find any problem please contact us.**


