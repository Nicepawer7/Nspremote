# Nspremote
This repository represent my development of a spike 2 controll app, the app is forked on [Spremote  library for spike 3 comunication](https://github.com/jeflem/spremote) by jeflem, the library has been majorly rewritten to controll a spike 2 Robot built by (Gome Neve robotics team)[https://sites.google.com/scuolaladina.com/gome-neve/] to compete in FIRST Lego League.
The desktop app is written in python using the graphical Tkinter framework using the Nspremote and serial library (once finished will become a separate repository) to handle the Computer-Brick bluetooth comunication (wired connection is also avaible)
## Usage
The app requires python (aggiungere versione) and the serial library (installed in the virtual envivorment)
## TODO:
- [ ] Controllare per riconnessione pad
- [X] aggiungere barra con scelta pad (sarebbe bello testarli)
- [X] aggiungere scelta seriale
- [ ] riiorganizzare a frame TUTTO
- [ ] se fattibile documentare la lettura dell'id (print(hub.port.A.info()['type']))
- [ ] aggiungere tutti gli id  https://github.com/pybricks/technical-info/blob/master/assigned-numbers.md con lo stesso connettore
