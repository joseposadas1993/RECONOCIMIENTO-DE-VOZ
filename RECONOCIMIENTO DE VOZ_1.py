
import speech_recognition as sr

def reconocer_voz():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("por favor, hable ahora...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        texto = recognizer.recognize_google(audio, language='es-MX') 
        print("has dicho:" + texto)
    
    except sr.UnknownValueError:
      print("No se pudo entender el audio")
    except sr.RequestError as e:
        print("Error al solicitar resultados; {0}".format(e))

if __name__ == "__main__":
    reconocer_voz()      
