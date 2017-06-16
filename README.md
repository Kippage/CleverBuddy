CleverBuddy is a small example of a CleverBot structure made in Python 3.6.1.
*If you use it in your work, be sure to mention this link or this project.*


IT REQUIRES `random_words` MODULE! If you don't have it, simply `pip install random_words`


Changing the Bot Name?

```python
>>> CleverBuddy.Settings.Name('ABCD')
>>> CleverBuddy.Bot.Talk('Hi!')
Hello! I'm ABCD.
>>> CleverBuddy.Settings.Name('DEFG')
>>> CleverBuddy.Bot.Talk('Hi!')
Hello! I'm DEFG.
```

`Bot.Talk()` and `Bot.TalkReturn()`? `Bot.TalkReturn()` will return the response and `Bot.Talk()` will print your response.

```python
>>> CleverBuddy.Bot.TalkReturn('dab')
"Let's dab."
>>> CleverBuddy.Bot.Talk('dab')
Let's dab.
>>> print(CleverBuddy.Bot.TalkReturn('dab'))
Let's dab.
```
