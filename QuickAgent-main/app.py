import gradio as gr

# Import the LanguageModelProcessor, TextToSpeech, and TranscriptCollector classes
from QuickAgent import LanguageModelProcessor, TextToSpeech, TranscriptCollector

# Initialize the language model processor
llm_processor = LanguageModelProcessor()

# Initialize the text-to-speech component
tts = TextToSpeech()

# Initialize the transcript collector
transcript_collector = TranscriptCollector()


# Define a function to process voice input and return AI response
def chatbot(message, history):
    output = llm_processor.process(message)
    
    return output

gr.ChatInterface(chatbot, title="AI Customer ChatBot").launch(share=True)