import speech_recognition as sr
import pyttsx3
import datetime
import time
import webbrowser
import random
from urllib.parse import quote
import pyautogui

class VoiceAssistant:
    def __init__(self):
        # Initialize text-to-speech engine
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)
        self.engine.setProperty('volume', 1.0)
        
        # Initialize speech recognizer
        self.recognizer = sr.Recognizer()
        self.recognizer.dynamic_energy_threshold = True
        self.recognizer.pause_threshold = 0.8
        
        # Initialize task list
        self.tasks = []
        self.listening_for_task = False
        
        # Define command keywords
        self.commands = {
            'greeting': ['hello', 'hi', 'hey', 'good morning', 'good afternoon', 'good evening'],
            'farewell': ['bye', 'stop', 'exit', 'quit', 'goodbye'],
            'time': ['time', "what's the time", 'tell me the time'],
            'date': ['date', "what's the date", 'tell me the date'],
            'search': ['search', 'google', 'look up', 'find', 'search for'],
            'task': ['add task', 'add a task', 'new task', 'list tasks', 'show tasks', 'what are my tasks'],
            'screenshot': ['take a screenshot', 'capture screen', 'screenshot'],
            'browser': ['open chrome', 'launch chrome', 'open browser'],
            'joke': ['tell me a joke', 'joke', 'make me laugh'],
            'thank': ['thank you', 'thanks']
        }

    def speak(self, audio):
        """Convert text to speech"""
        try:
            print(audio)  # Print the response for visual feedback
            self.engine.say(audio)
            self.engine.runAndWait()
        except Exception as e:
            print(f"Error in speech synthesis: {str(e)}")
            
    def take_command(self):
        """Listen to user input and convert to text"""
        with sr.Microphone() as source:
            print("Listening...")
            self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
            
            try:
                audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=5)
                print("Recognizing...")
                
                query = self.recognizer.recognize_google(audio, language="en-in")
                print(f"You said: {query}")
                return query.lower()
                
            except sr.WaitTimeoutError:
                print("Listening timed out. Please try again.")
                return None
            except sr.UnknownValueError:
                print("Sorry, I couldn't understand that.")
                return None
            except sr.RequestError:
                print("Sorry, there was an error with the speech recognition service.")
                return None
            except Exception as e:
                print(f"An error occurred: {str(e)}")
                return None

    def greet_user(self):
        """Greet the user based on time of day"""
        hour = datetime.datetime.now().hour
        if hour < 12:
            self.speak("Good Morning!")
        elif 12 <= hour < 18:
            self.speak("Good Afternoon!")
        else:
            self.speak("Good Evening!")
        self.speak("I'm your voice assistant. How can I help you today?")

    def find_command_type(self, query):
        """Determine the type of command from user input"""
        for command_type, phrases in self.commands.items():
            if any(phrase in query for phrase in phrases):
                return command_type
        return None

    def google_search(self, query):
        """Perform a Google search"""
        search_terms = query
        for phrase in self.commands['search']:
            search_terms = search_terms.replace(phrase, "").strip()
        
        if search_terms:
            self.speak(f"Searching Google for {search_terms}")
            search_url = f"https://www.google.com/search?q={quote(search_terms)}"
            webbrowser.open(search_url)
            return True
        return False

    def manage_tasks(self, query):
        """Handle task-related commands"""
        if self.listening_for_task:
            self.tasks.append(query)
            self.listening_for_task = False
            self.speak(f"Adding {query} to your task list. You now have {len(self.tasks)} tasks.")
        elif any(phrase in query for phrase in ['add task', 'add a task', 'new task']):
            self.listening_for_task = True
            self.speak("Sure, what is the task?")
        elif any(phrase in query for phrase in ['list tasks', 'show tasks', 'what are my tasks']):
            if not self.tasks:
                self.speak("You don't have any tasks in your list.")
            else:
                self.speak("Here are your tasks:")
                for i, task in enumerate(self.tasks, 1):
                    self.speak(f"Task {i}: {task}")

    def take_screenshot(self):
        """Capture a screenshot"""
        try:
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            screenshot_path = f"screenshot_{timestamp}.png"
            pyautogui.screenshot(screenshot_path)
            self.speak(f"I've taken a screenshot and saved it as {screenshot_path}")
        except Exception as e:
            self.speak("Sorry, I couldn't take the screenshot.")
            print(f"Screenshot error: {str(e)}")

    def process_command(self, query):
        """Process and respond to user commands"""
        try:
            command_type = self.find_command_type(query)
            
            if command_type == 'greeting':
                responses = ["Hello! How can I help you?", "Hi there! What can I do for you?", 
                           "Hey! How may I assist you?"]
                self.speak(random.choice(responses))
                
            elif command_type == 'farewell':
                self.speak("Goodbye! Have a great day!")
                return False
                
            elif command_type == 'time':
                current_time = datetime.datetime.now().strftime("%I:%M %p")
                self.speak(f"The current time is {current_time}")
                
            elif command_type == 'date':
                current_date = datetime.datetime.now().strftime("%B %d, %Y")
                self.speak(f"Today's date is {current_date}")
                
            elif command_type == 'search':
                if not self.google_search(query):
                    self.speak("What would you like me to search for?")
                    
            elif command_type == 'task':
                self.manage_tasks(query)
                
            elif command_type == 'screenshot':
                self.take_screenshot()
                
            elif command_type == 'browser':
                self.speak("Opening Chrome")
                webbrowser.open("https://www.google.com")
                
            elif command_type == 'joke':
                jokes = [
                    "Why don't scientists trust atoms? Because they make up everything!",
                    "What did the ocean say to the shore? Nothing, it just waved!",
                    "Why did the scarecrow win an award? Because he was outstanding in his field!"
                ]
                self.speak(random.choice(jokes))
                
            elif command_type == 'thank':
                responses = ["You're welcome!", "My pleasure!", "Glad I could help!"]
                self.speak(random.choice(responses))
                
            else:
                self.speak("I heard you say: " + query)
                self.speak("Sorry, I can only help you with Add and manage your tasks, take screenshots, tell time and date, search Google, tell jokes and more.")
                
            return True
            
        except Exception as e:
            print(f"Error processing command: {str(e)}")
            self.speak("Sorry, I encountered an error while processing your request.")
            return True

    def run(self):
        """Main loop of the voice assistant"""
        self.greet_user()
        running = True
        
        while running:
            query = self.take_command()
            if query:
                running = self.process_command(query)
            else:
                time.sleep(1)

def main():
    assistant = VoiceAssistant()
    assistant.run()

if __name__ == "__main__":
    main()