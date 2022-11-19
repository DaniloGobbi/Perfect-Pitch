# PERFECT PITCH
#### Video Demo:  <https://youtu.be/vNdThboIWBE>
#### Description:
- The objective of this project is to be able to practice your listening sense of musical notes and chords
- The program will give you options of what you want to practice: notes or chords
- The program will play a note or a chord randomly selected and will prompt the user a input to guess what note or chord was played
- Notes: C, D, E, F, G, A and B 
- Chords: major and minor triads of the C scale
- The total of sounds to guess is 28
### Functions:
The first function is main(), where contain 4 more functions. The first one of then is menu() and its porpouse is to create a menu interface using only de print() function, showing the options to practice. The second function is validar_opcao(), this one is for reading the input, it wil return 1 if the note option was selected or 2 if the chords option was selected. If the note was selected the nota() function is called and it will start a countdown until a random note from the lista_notas list is played, after that you can hear the note again or you can try to guess, if your guess is correct the nota() function will return a string: "Correct!" or if it's wrong: f"No! That's {note}". The same logic is apllied to the the acorde() function. And so, the porpouse of this program is to practice your sense of musicals sounds and help you get the perfect pitch
### Libraries:
The libraries used in this program are: 
- playsound, to play the notes and chords that were recorded in the piano
- time, to create a countdown with sleep() function
- random, to be able to choose using the choice() function a random note or chord from the lists
### Lists and Dicts:
In this program was used a list of all the notes used and a list of all the chords used. These lists were used to have a way to get a random note or chord.
The dicts were used for create a relation between keys and values to be able to compare your guess with the correct answer
