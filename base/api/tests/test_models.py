from django.test import TestCase
from api.models import (
    Level,
    ProgrammingLang,
    Category,
    Question,
    Favourite,
    Comment
)
from django.contrib.auth.models import User 

class ModelsValidDataTestCase(TestCase):
    def setUp(self) -> None:
        self.user = User(
            username = "test",
            email = "test@example.com",
            password = "test1234"
        )
        self.level = Level(
            name = "Junior",
            short_desc = "Person who copy code from chatgpt"
        )
        self.language = ProgrammingLang(
            name = "Python",
            short_desc = "I am using it now"
        )
        self.category = Category(
            name = "Web dev"
        )
        self.question = Question(
            name = "Python slow or fast",
            content = "Python is slower than other static typed langs",
            content_code = "<h1> Hello World </h1>",
            programming_lang = self.language,
            category = self.category,
            level = self.level,
            author = self.user
        )
        self.comment = Comment(
            name = "You are right",
            content = "That's true", 
            content_code = "<p> Hello world </p>",
            question = self.question,
            author = self.user
        )
        self.favourite = Favourite(
            user = self.user,
            question = self.question,
        )
    
    def test_level_model_valid_data(self) -> None:
        self.assertEqual(self.level.name, "Junior")
        
    def test_programming_language_model_valid_data(self) -> None:
        self.assertEqual(self.language.name, "Python")

    def test_category_model_valid_data(self) -> None:
        self.assertEqual(self.category.name, "Web dev")

    def test_question_model_valid_data(self) -> None:
        self.assertEqual(self.question.name, "Python slow or fast")
        self.assertEqual(self.question.programming_lang, self.language)
        self.assertEqual(self.question.category, self.category)
        self.assertEqual(self.question.level, self.level)
        self.assertEqual(self.question.author, self.user)

    def test_comment_model_valid_data(self) -> None:
        self.assertEqual(self.comment.name, "You are right")
        self.assertEqual(self.comment.question, self.question)
        self.assertEqual(self.comment.author, self.user)
        